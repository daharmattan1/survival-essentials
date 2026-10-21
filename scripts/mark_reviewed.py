#!/usr/bin/env python3
"""Mark one domain's entries as human safety-read reviewed.

Only a human reviewer runs this. AI agents must never run it.

A human runs this after finishing the CONVENTIONS.md section 10 safety read
of ONE domain. For every entry in that domain's entries/ folder it sets
`review_status: reviewed` and `last_reviewed: <today, ISO>` in the front
matter, and it updates the `review_status` column of the matching rows in the
domain's _index.md manifest.

Usage:
    python scripts/mark_reviewed.py --domain regional/mid-atlantic-appalachian/mushrooms \\
        --reviewer "Full Name"
    python scripts/mark_reviewed.py --domain <domain> --reviewer "Full Name" --dry-run

Safeguards:
  * A real run lists the entries, then makes you type an exact phrase.
  * It refuses to run unless stdin is an interactive terminal.
  * It refuses an empty or missing --reviewer.
  * It accepts no flag that skips the prompt (no --yes, --force, and so on).
  * --dry-run shows the changes and writes nothing. It asks no question.

After a real run, add a sign-off line to CHANGELOG.md (the script reminds you).
"""

import argparse
import datetime
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ALLOWED_TOP = ("regional", "substrate")

LINE_RE = re.compile(r"[^\r\n]*(?:\r\n|\n|\r)|[^\r\n]+")
KEY_RE = re.compile(r"^(last_reviewed|review_status):(.*?)(\r\n|\n|\r)?$", re.S)


def die(msg, code=2):
    print("REFUSED: " + msg, file=sys.stderr)
    sys.exit(code)


def split_lines(text):
    return LINE_RE.findall(text)


def eol_of(line):
    for e in ("\r\n", "\n", "\r"):
        if line.endswith(e):
            return e
    return ""


def read_text(path):
    with open(path, "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def update_entry(text, today):
    """Return (new_text, old_status). Raises ValueError if front matter is off."""
    lines = split_lines(text)
    if not lines or lines[0].lstrip("﻿").rstrip("\r\n") != "---":
        raise ValueError("no front matter at top of file")
    end = None
    for i in range(1, len(lines)):
        if lines[i].rstrip("\r\n") == "---":
            end = i
            break
    if end is None:
        raise ValueError("front matter is not closed with ---")
    seen = {}
    old_status = None
    for i in range(1, end):
        m = KEY_RE.match(lines[i])
        if not m:
            continue
        key, rest, eol = m.group(1), m.group(2), m.group(3) or ""
        if key in seen:
            raise ValueError("duplicate " + key)
        seen[key] = i
        if key == "review_status":
            old_status = rest.strip()
            lines[i] = "review_status: reviewed" + eol
        else:
            lines[i] = "last_reviewed: " + today + eol
    for key in ("last_reviewed", "review_status"):
        if key not in seen:
            raise ValueError("front matter has no " + key)
    return "".join(lines), old_status


def update_manifest(text, entry_ids):
    """Set review_status to reviewed for rows whose entry_id is in entry_ids.

    Returns (new_text, set_of_entry_ids_updated).
    """
    lines = split_lines(text)
    col = None
    ncols = 0
    updated = set()
    for i, line in enumerate(lines):
        body = line.rstrip("\r\n")
        if not body.lstrip().startswith("|"):
            col = None
            continue
        cells = [c.strip() for c in body.strip().strip("|").split("|")]
        if cells and cells[0] == "entry_id" and "review_status" in cells:
            col = cells.index("review_status")
            ncols = len(cells)
            continue
        if col is None or set(cells[0]) <= set("-: "):
            continue
        if cells[0] in entry_ids and len(cells) == ncols:
            raw = body.strip().strip("|").split("|")
            width = len(raw[col])
            lead = len(raw[col]) - len(raw[col].lstrip())
            raw[col] = " " * (lead or 1) + "reviewed" + " " * max(1, width - lead - 8)
            indent = body[: len(body) - len(body.lstrip())]
            lines[i] = indent + "|" + "|".join(raw) + "|" + eol_of(line)
            updated.add(cells[0])
    return "".join(lines), updated


def resolve_domain(arg):
    p = Path(arg)
    if not p.is_absolute():
        # Try the repo root first, then the current directory.
        for base in (REPO_ROOT, Path.cwd()):
            if (base / p).is_dir():
                p = base / p
                break
    try:
        p = p.resolve(strict=True)
        rel = p.relative_to(REPO_ROOT)
    except (OSError, ValueError):
        die("--domain must be an existing folder inside this repo: " + arg)
    if not rel.parts or rel.parts[0] not in ALLOWED_TOP or len(rel.parts) < 2:
        die("--domain must be a domain folder under regional/ or substrate/.")
    if not (p / "_index.md").is_file() or not (p / "entries").is_dir():
        die("that folder has no _index.md and entries/ (is it a domain folder?): " + rel.as_posix())
    return p, rel.as_posix()


def build_parser():
    ap = argparse.ArgumentParser(
        description="Human-only: mark a domain's entries reviewed after the section 10 safety read.",
        allow_abbrev=False,
    )
    ap.add_argument("--domain", required=True, help="path to ONE domain folder")
    ap.add_argument("--reviewer", default=None, help="full name of the human reviewer")
    ap.add_argument("--dry-run", action="store_true", help="show changes, write nothing")
    return ap


def main(argv=None):
    ap = build_parser()
    args, unknown = ap.parse_known_args(argv)
    if unknown:
        die("unrecognized argument(s): %s. This tool has no flag that skips the "
            "confirmation prompt, by design." % " ".join(unknown))
    if args.reviewer is None or not args.reviewer.strip():
        die('--reviewer "Full Name" is required and must not be empty.')
    reviewer = " ".join(args.reviewer.split())

    domain_path, domain = resolve_domain(args.domain)
    entry_files = sorted((domain_path / "entries").glob("*.md"))
    if not entry_files:
        die("no entries found in " + domain + "/entries/")

    today = datetime.date.today().isoformat()
    plan = []  # (path, new_text, old_status, entry_id)
    for f in entry_files:
        try:
            new_text, old = update_entry(read_text(f), today)
        except ValueError as exc:
            die("%s: %s. Nothing was changed." % (f.relative_to(REPO_ROOT).as_posix(), exc))
        plan.append((f, new_text, old, f.stem))

    ids = {p[3] for p in plan}
    index_path = domain_path / "_index.md"
    new_index, updated_ids = update_manifest(read_text(index_path), ids)

    mode = "DRY RUN (nothing will be written)" if args.dry_run else "REAL RUN"
    print("%s\nDomain:   %s\nReviewer: %s\nDate:     %s\n" % (mode, domain, reviewer, today))
    print("Entries that will be marked reviewed (%d):" % len(plan))
    for f, _, old, eid in plan:
        note = "" if eid in updated_ids else "   [no manifest row found]"
        print("  - %s   (%s -> reviewed)%s" % (f.relative_to(REPO_ROOT).as_posix(), old, note))
    print("\nManifest rows updated in %s: %d of %d"
          % (index_path.relative_to(REPO_ROOT).as_posix(), len(updated_ids), len(plan)))

    if args.dry_run:
        print("\nDry run complete. No files were written.")
        return 0

    if not sys.stdin.isatty():
        die("stdin is not an interactive terminal. A human must run this at a keyboard; "
            "piped or scripted input is refused.")

    phrase = "I have completed the safety read for " + domain
    print("\nOnly do this after you have finished the CONVENTIONS.md section 10 read of this domain.")
    print("To confirm, type this exact phrase:\n\n    " + phrase + "\n")
    try:
        typed = input("> ")
    except EOFError:
        die("no confirmation entered. Nothing was changed.")
    if typed.strip() != phrase:
        die("the phrase did not match. Nothing was changed.")

    writes = [(f, t) for f, t, _, _ in plan] + [(index_path, new_index)]
    for path, text in writes:
        tmp = path.with_name(path.name + ".tmp-mark-reviewed")
        with open(tmp, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
        os.replace(tmp, path)

    print("\nDone. Marked %d entries reviewed in %s and updated %d manifest rows."
          % (len(plan), domain, len(updated_ids)))
    print("\nNext: add a sign-off line to CHANGELOG.md, for example:")
    print("  SAFETY-READ-PASSED  %s  %s  reviewer: %s" % (today, domain, reviewer))
    return 0


if __name__ == "__main__":
    sys.exit(main())
