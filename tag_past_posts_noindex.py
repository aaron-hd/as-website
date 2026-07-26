#!/usr/bin/env python3
"""
One-time migration script: adds `robots: "noindex, nofollow"` and `sitemap: false`
to the YAML front matter of every post in _posts/ that is NOT currently tagged
`category: "future"`.

Usage:
    python3 tag_past_posts_noindex.py            # dry run, shows what would change
    python3 tag_past_posts_noindex.py --apply    # actually writes the changes

Run this from the root of your Jekyll repo (the directory that contains _posts/).
Commit or otherwise back up your repo before running with --apply.
"""

import re
import sys
from pathlib import Path

POSTS_DIR = Path("_posts")
DRY_RUN = "--apply" not in sys.argv

FRONT_MATTER_RE = re.compile(r"^---\n(.*?\n)---\n", re.DOTALL)


def is_future(front_matter_text: str) -> bool:
    """Crude but effective: looks for a category/categories field mentioning 'future'."""
    return bool(re.search(r'categor(y|ies)\s*:\s*.*future', front_matter_text, re.IGNORECASE))


def already_tagged(front_matter_text: str) -> bool:
    return "robots:" in front_matter_text or re.search(r"sitemap\s*:\s*false", front_matter_text) is not None


def main():
    if not POSTS_DIR.is_dir():
        print(f"ERROR: {POSTS_DIR} not found. Run this from your Jekyll repo root.")
        sys.exit(1)

    changed, skipped_future, skipped_already, no_front_matter = [], [], [], []

    for path in sorted(POSTS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = FRONT_MATTER_RE.match(text)
        if not m:
            no_front_matter.append(path)
            continue

        fm = m.group(1)

        if is_future(fm):
            skipped_future.append(path)
            continue

        if already_tagged(fm):
            skipped_already.append(path)
            continue

        new_fm = fm + 'robots: "noindex, nofollow"\nsitemap: false\n'
        new_text = text[: m.start(1)] + new_fm + text[m.end(1) :]

        changed.append(path)
        if not DRY_RUN:
            path.write_text(new_text, encoding="utf-8")

    verb = "Would tag" if DRY_RUN else "Tagged"
    print(f"{verb} {len(changed)} post(s) as noindex / sitemap:false")
    for p in changed:
        print(f"  - {p}")

    print(f"\nSkipped {len(skipped_future)} post(s) with category: future (left indexable)")
    print(f"Skipped {len(skipped_already)} post(s) that already had robots/sitemap set")

    if no_front_matter:
        print(f"\nWARNING: {len(no_front_matter)} file(s) had no parsable front matter, left untouched:")
        for p in no_front_matter:
            print(f"  - {p}")

    if DRY_RUN:
        print("\nThis was a dry run. Re-run with --apply to write these changes.")


if __name__ == "__main__":
    main()
