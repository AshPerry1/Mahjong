#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tell search engines about new/updated URLs (IndexNow).

This is NOT a traffic bot. Simulated visits do not improve Google rankings and can
hurt trust signals. Use this script plus Google Search Console instead.

IndexNow: Bing, Yandex, Seznam, Naver, and partners.
Google: submit https://lookoutmountainmahjong.com/sitemap.xml in Search Console once,
then rely on sitemap + natural crawls (optional Search Console API for power users).

Usage:
  python3 notify-search-engines.py              # ping all sitemap URLs (batched)
  python3 notify-search-engines.py --limit 200  # newest N URLs only (after big waves)
  python3 notify-search-engines.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

BASE = "https://lookoutmountainmahjong.com"
HOST = "lookoutmountainmahjong.com"
INDEXNOW_KEY = "lmmahjongindex2026"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
BATCH_SIZE = 500
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def load_sitemap_urls(root: Path) -> list[str]:
    path = root / "sitemap.xml"
    if not path.is_file():
        raise FileNotFoundError(f"Missing {path} — run: python3 generate-seo-pages.py")
    tree = ET.parse(path)
    urls: list[str] = []
    for loc in tree.findall(".//sm:loc", NS):
        if loc.text:
            urls.append(loc.text.strip())
    if not urls:
        for loc in tree.findall(".//{*}loc"):
            if loc.text:
                urls.append(loc.text.strip())
    return urls


def indexnow_batch(urls: list[str], *, dry_run: bool) -> bool:
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    if dry_run:
        print(f"[dry-run] IndexNow batch of {len(urls)} URLs (sample: {urls[0]})")
        return True
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            code = resp.getcode()
            print(f"IndexNow OK (HTTP {code}) — {len(urls)} URLs")
            return 200 <= code < 300
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:500]
        print(f"IndexNow HTTP {e.code}: {body}", file=sys.stderr)
        return False
    except urllib.error.URLError as e:
        print(f"IndexNow network error: {e}", file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Notify search engines via IndexNow (legitimate indexing).")
    parser.add_argument("--limit", type=int, default=0, help="Max URLs to send (0 = all in sitemap)")
    parser.add_argument("--dry-run", action="store_true", help="Print batches without calling IndexNow")
    args = parser.parse_args()

    root = Path(__file__).parent
    key_file = root / f"{INDEXNOW_KEY}.txt"
    if not key_file.is_file():
        print(f"Missing verification file: {key_file.name}", file=sys.stderr)
        return 1

    urls = load_sitemap_urls(root)
    if args.limit > 0:
        urls = urls[-args.limit :]
    if not urls:
        print("No URLs in sitemap.", file=sys.stderr)
        return 1

    print(f"Sitemap: {len(urls)} URL(s) to notify")
    ok = True
    for i in range(0, len(urls), BATCH_SIZE):
        batch = urls[i : i + BATCH_SIZE]
        if not indexnow_batch(batch, dry_run=args.dry_run):
            ok = False
    if ok and not args.dry_run:
        print(
            "\nGoogle: add the property in Search Console and submit the sitemap once:\n"
            f"  {BASE}/sitemap.xml\n"
            "  https://search.google.com/search-console"
        )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
