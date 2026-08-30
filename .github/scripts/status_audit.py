#!/usr/bin/env python3
"""Quarterly project-status audit for the live entries in README.md.

Beyond HTTP liveness (the weekly lychee run covers that), this checks:
- Source repositories: archived flag, last push, latest release age.
  The repository comes from the entry URL when it points at GitHub,
  otherwise from the .github/data/repos.json record.
- Non-GitHub homepages: DNS/HTTP failures and cross-domain redirects
  (a redirect to an unrelated domain is how hijacked projects present).

repos.json record formats (validated by validate_metadata.py):
  "Name": "owner/repo"                      monitored
  "Name": {"repo": "owner/repo",
           "stable": true, "note": "..."}   monitored; inactivity is
                                            expected (finished standard),
                                            only archival is reported
  "Name": {"exempt": "reason"}              intentionally unmonitored
                                            (other forge, no repo)

Inactivity findings are also suppressed for entries the README already
tags **Dormant** — they are known-quiet, not news.

The script never raises out of the per-entry loop: API errors become
report findings, and status-report.md is always written. Exit code 1
when there are findings, 0 when everything monitored is healthy.
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
REPO_MAP_FILE = ".github/data/repos.json"
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
entries = re.findall(r"^- \[([^\]]+)\]\((https?://[^)]+)\).*?$", live, re.M)
entry_lines = {m.group(1): m.group(0) for m in
               re.finditer(r"^- \[([^\]]+)\]\(https?://[^)]+\).*$", live, re.M)}
try:
    repo_map = json.load(open(REPO_MAP_FILE))
except Exception:
    repo_map = {}

archived, stale, failures, redirects, no_release, api_errors, unmapped = \
    [], [], [], [], [], [], []
exempt_names = []

for name, url in entries:
    m = re.match(r"https://github\.com/([\w.-]+)/([\w.-]+)", url)
    rec = repo_map.get(name)
    stable = isinstance(rec, dict) and rec.get("stable", False)
    exempt = isinstance(rec, dict) and "exempt" in rec
    if m:
        repo = f"{m.group(1)}/{m.group(2)}"
    elif isinstance(rec, str):
        repo = rec
    elif isinstance(rec, dict):
        repo = rec.get("repo")
    else:
        repo = None
    dormant_tagged = "**Dormant**" in entry_lines.get(name, "")
    quiet_ok = stable or dormant_tagged  # inactivity is not news here

    if exempt:
        exempt_names.append(name)
    elif repo is None:
        unmapped.append(name)

    # repository health (archival, pushes, releases)
    if repo:
        try:
            d = gh(f"/repos/{repo}")
            if d.get("archived"):
                archived.append((name, url))
            age = months_ago(d["pushed_at"])
            if age > STALE_MONTHS and not quiet_ok:
                stale.append((name, url, f"last push {d['pushed_at'][:10]} ({age:.0f} months)"))
            if not quiet_ok:
                try:
                    rel = gh(f"/repos/{repo}/releases/latest")
                    if months_ago(rel["published_at"]) > STALE_MONTHS:
                        no_release.append((name, url, f"latest release {rel['tag_name']} on {rel['published_at'][:10]}"))
                except HTTPError as e:
                    if e.code != 404:  # 404 = repo simply doesn't use releases
                        api_errors.append((name, repo, f"releases: HTTP {e.code}"))
                except Exception as e:
                    api_errors.append((name, repo, f"releases: {type(e).__name__}"))
        except Exception as e:
            api_errors.append((name, repo, f"repo: {type(e).__name__}: {e}"))

    # homepage health (only for non-GitHub entry URLs)
    if not m:
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
    ("🚨 Unreachable homepages (DNS or HTTP failure)",
     [f"- **{n}** — {u} — {msg}" for n, u, msg in failures]),
    ("⚠️ Cross-domain redirects (possible rebrand or hijack — inspect!)",
     [f"- **{n}** — {u} — {msg}" for n, u, msg in redirects]),
    (f"⚠️ No push in {STALE_MONTHS}+ months (Dormant candidates)",
     [f"- **{n}** — {u} — {msg}" for n, u, msg in stale]),
    (f"ℹ️ No release in {STALE_MONTHS}+ months (repo may still be active)",
     [f"- **{n}** — {u} — {msg}" for n, u, msg in no_release]),
    ("ℹ️ API errors during this run (retry or investigate)",
     [f"- **{n}** ({r}) — {msg}" for n, r, msg in api_errors]),
    (f"⚠️ Entries with no repository mapping or exemption (add to `{REPO_MAP_FILE}`)",
     [f"- **{n}**" for n in unmapped]),
]

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
monitored = len(entries) - len(exempt_names) - len(unmapped)
coverage = (f"Coverage: {len(entries)} live entries — {monitored} repository-monitored, "
            f"{len(exempt_names)} exempt with a documented reason, {len(unmapped)} unmapped.")
lines = [f"# Quarterly status audit — {today}", "", coverage, ""]
findings = 0
for title, items in sections:
    if items:
        findings += len(items)
        lines += [f"## {title}", ""] + items + [""]
if exempt_names:
    lines += ["## ℹ️ Exempt entries (homepage checks only; reasons in repos.json)", "",
              ", ".join(sorted(exempt_names)), ""]
if findings == 0:
    lines.append(f"All monitored checks passed. {coverage}")
open(REPORT, "w").write("\n".join(lines) + "\n")
print(f"{findings} findings; {coverage}")
sys.exit(1 if findings else 0)
