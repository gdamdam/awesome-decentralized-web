#!/usr/bin/env python3
"""Quarterly project-status audit for the live entries in README.md.

Beyond HTTP liveness (the weekly lychee run covers that), this checks:
- GitHub repositories: archived flag, last push, latest release age
- Non-GitHub sites: DNS/HTTP failures and cross-domain redirects
  (a redirect to an unrelated domain is how hijacked projects present)

Writes a markdown report to status-report.md. Exit code 1 when there
are findings, 0 when everything is healthy.
"""
import json
import os
import re
import ssl
import sys
import urllib.request
from datetime import datetime, timezone
from urllib.error import HTTPError

STALE_MONTHS = 24
README = "README.md"
REPORT = "status-report.md"
TOKEN = os.environ.get("GH_TOKEN", "")
UA = {"User-Agent": "awesome-decentralized-web status audit"}

ctx = ssl.create_default_context()


def gh(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={**UA, "Authorization": f"Bearer {TOKEN}",
                 "Accept": "application/vnd.github+json"})
    return json.loads(urllib.request.urlopen(req, timeout=30, context=ctx).read())


def months_ago(iso):
    d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return (datetime.now(timezone.utc) - d).days / 30.4


live = open(README).read().split("## Graveyard")[0]
entries = re.findall(r"^- \[([^\]]+)\]\((https?://[^)]+)\)", live, re.M)

archived, stale, failures, redirects, no_release = [], [], [], [], []

for name, url in entries:
    m = re.match(r"https://github\.com/([\w.-]+)/([\w.-]+)", url)
    if m:
        owner, repo = m.group(1), m.group(2)
        try:
            d = gh(f"/repos/{owner}/{repo}")
        except Exception as e:
            failures.append((name, url, f"GitHub API: {e}"))
            continue
        if d.get("archived"):
            archived.append((name, url))
        age = months_ago(d["pushed_at"])
        if age > STALE_MONTHS:
            stale.append((name, url, f"last push {d['pushed_at'][:10]} ({age:.0f} months)"))
        try:
            rel = gh(f"/repos/{owner}/{repo}/releases/latest")
            rel_age = months_ago(rel["published_at"])
            if rel_age > STALE_MONTHS:
                no_release.append((name, url, f"latest release {rel['tag_name']} on {rel['published_at'][:10]}"))
        except HTTPError as e:
            if e.code != 404:  # 404 = repo simply doesn't use releases
                raise
        except Exception:
            pass
    else:
        try:
            r = urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=30, context=ctx)
            src = url.split("/")[2].removeprefix("www.")
            dst = r.geturl().split("/")[2].removeprefix("www.")
            if src != dst and not dst.endswith("." + src) and not src.endswith("." + dst):
                redirects.append((name, url, f"now lands on {dst}"))
        except Exception as e:
            failures.append((name, url, f"{type(e).__name__}: {e}"))

sections = [
    ("🚨 Archived repositories (move to Graveyard?)",
     [f"- **{n}** — {u}" for n, u in archived]),
    ("🚨 Unreachable (DNS or HTTP failure)",
     [f"- **{n}** — {u} — {msg}" for n, u, msg in failures]),
    ("⚠️ Cross-domain redirects (possible rebrand or hijack — inspect!)",
     [f"- **{n}** — {u} — {msg}" for n, u, msg in redirects]),
    (f"⚠️ No push in {STALE_MONTHS}+ months (Dormant candidates)",
     [f"- **{n}** — {u} — {msg}" for n, u, msg in stale]),
    (f"ℹ️ No release in {STALE_MONTHS}+ months (repo may still be active)",
     [f"- **{n}** — {u} — {msg}" for n, u, msg in no_release]),
]

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
lines = [f"# Quarterly status audit — {today}", "",
         f"Checked {len(entries)} live entries.", ""]
findings = 0
for title, items in sections:
    if items:
        findings += len(items)
        lines += [f"## {title}", ""] + items + [""]
if findings == 0:
    lines.append("All checks passed — nothing to review this quarter. 🎉")
open(REPORT, "w").write("\n".join(lines) + "\n")
print(f"{findings} findings across {len(entries)} entries; report in {REPORT}")
sys.exit(1 if findings else 0)
