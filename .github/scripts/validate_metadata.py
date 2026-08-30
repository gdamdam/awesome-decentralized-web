#!/usr/bin/env python3
"""Offline consistency check between README.md and .github/data/repos.json.

Runs in CI on every PR and push (no network, no tokens). Fails when:
- a repos.json key does not exactly match a live README entry name
- a live entry has neither a GitHub link, a repository record, nor an
  explicit exemption
- an entry whose README URL already points at GitHub also has a record
  (redundant — the URL wins)
- a record is malformed (bad repo identifier, empty exemption reason,
  unknown keys)

Duplicate repository values across records are reported as warnings.
"""
import json
import re
import sys

README = "README.md"
REPO_MAP_FILE = ".github/data/repos.json"
REPO_RE = re.compile(r"^[\w.-]+/[\w.-]+$")
ALLOWED_KEYS = {"repo", "stable", "note", "exempt"}

live = open(README).read().split("## Graveyard")[0]
entries = dict(re.findall(r"^- \[([^\]]+)\]\((https?://[^)]+)\)", live, re.M))
repo_map = json.load(open(REPO_MAP_FILE))

errors, warnings = [], []

for key, rec in repo_map.items():
    if key not in entries:
        errors.append(f"orphan record: '{key}' matches no live README entry")
        continue
    if re.match(r"https://github\.com/[\w.-]+/[\w.-]+", entries[key]):
        errors.append(f"redundant record: '{key}' already links GitHub in the README")
    if isinstance(rec, str):
        if not REPO_RE.match(rec):
            errors.append(f"malformed repo id for '{key}': {rec!r}")
    elif isinstance(rec, dict):
        unknown = set(rec) - ALLOWED_KEYS
        if unknown:
            errors.append(f"unknown keys for '{key}': {sorted(unknown)}")
        if "exempt" in rec:
            if not (isinstance(rec["exempt"], str) and rec["exempt"].strip()):
                errors.append(f"empty exemption reason for '{key}'")
            if "repo" in rec:
                errors.append(f"'{key}' is both exempt and mapped — pick one")
        elif not (isinstance(rec.get("repo"), str) and REPO_RE.match(rec["repo"])):
            errors.append(f"malformed or missing repo id for '{key}': {rec.get('repo')!r}")
    else:
        errors.append(f"record for '{key}' must be a string or object, got {type(rec).__name__}")

for name, url in entries.items():
    if not re.match(r"https://github\.com/[\w.-]+/[\w.-]+", url) and name not in repo_map:
        errors.append(f"uncovered entry: '{name}' has no GitHub link, mapping, or exemption")

repos_seen = {}
for key, rec in repo_map.items():
    repo = rec if isinstance(rec, str) else rec.get("repo") if isinstance(rec, dict) else None
    if repo:
        if repo.lower() in repos_seen:
            warnings.append(f"duplicate repo {repo}: '{key}' and '{repos_seen[repo.lower()]}'")
        repos_seen[repo.lower()] = key

for w in warnings:
    print(f"WARNING: {w}")
for e in errors:
    print(f"ERROR: {e}")
print(f"{len(entries)} live entries, {len(repo_map)} records, "
      f"{len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
