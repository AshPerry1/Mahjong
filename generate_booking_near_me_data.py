#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build seo_bulk_wave40_booking_cities_data.py from bulk wave city seeds."""
from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path

from generate_bulk_city_data import STATE_META

ROOT = Path(__file__).resolve().parent


def _load_wave_cities(wave: int) -> list[tuple]:
    path = ROOT / f"seo_bulk_wave{wave}_cities_data.py"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    m = re.search(r"WAVE\d+_CITIES\s*=\s*(\[.*?\])\s*(?:\n\n|\Z)", text, re.S)
    if not m:
        return []
    return ast.literal_eval(m.group(1))


def _stem(city_slug: str) -> str:
    return city_slug.replace("-mahjong.html", "")


def _slug_for_variant(stem: str, variant: str) -> str:
    if variant == "book-mahjong":
        return f"book-mahjong-{stem}.html"
    if variant == "hire-instructor":
        return f"hire-mahjong-instructor-{stem}.html"
    return f"{stem}-lessons-near-me.html"


def iter_booking_cities(
    limit: int = 500,
    *,
    variant: str = "lessons-near-me",
    wave_start: int = 27,
    wave_end: int = 41,
) -> list[tuple]:
    """(booking_slug, label, st, state_page, city_page, state_near_me_slug)."""
    seen: set[str] = set()
    out: list[tuple] = []
    for wave in range(wave_start, wave_end + 1):
        for tup in _load_wave_cities(wave):
            city_slug, label, st, state_page, _hub = tup
            stem = _stem(city_slug)
            booking_slug = _slug_for_variant(stem, variant)
            if booking_slug in seen:
                continue
            seen.add(booking_slug)
            st_slug = STATE_META.get(st, (f"{st.lower()}-mahjong.html", ""))[0]
            st_name = st_slug.replace("-mahjong.html", "").replace("-", " ")
            state_near = f"mahjong-lessons-near-me-{st_name}.html"
            out.append((booking_slug, label, st, state_page, city_slug, state_near))
            if len(out) >= limit:
                return out
    return out


def write_module(cities: list[tuple], out_path: Path, const_name: str) -> None:
    lines = [f"# auto-generated booking city tuples — {const_name}", f"{const_name} = ["]
    for row in cities:
        lines.append(f"    {row!r},")
    lines.append("]")
    lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=500)
    ap.add_argument(
        "--variant",
        choices=("lessons-near-me", "book-mahjong", "hire-instructor"),
        default="lessons-near-me",
    )
    ap.add_argument("--wave-end", type=int, default=41)
    ap.add_argument("--out", type=str, default="")
    args = ap.parse_args()
    cities = iter_booking_cities(
        args.limit, variant=args.variant, wave_end=args.wave_end
    )
    if args.out:
        out = ROOT / args.out
        const = out.stem.upper().replace("-", "_")
    elif args.variant == "book-mahjong":
        out = ROOT / "seo_bulk_wave42_book_cities_data.py"
        const = "WAVE42_BOOK_CITIES"
    elif args.variant == "hire-instructor":
        out = ROOT / "seo_bulk_wave43_hire_cities_data.py"
        const = "WAVE43_HIRE_CITIES"
    else:
        out = ROOT / "seo_bulk_wave40_booking_cities_data.py"
        const = "WAVE40_BOOKING_CITIES"
    write_module(cities, out, const)
    print(f"Wrote {len(cities)} {args.variant} cities to {out.name}")


if __name__ == "__main__":
    main()
