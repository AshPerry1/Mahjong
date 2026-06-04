# -*- coding: utf-8 -*-
"""Booking Wave 42 — book-mahjong-{city} pages (1500 cities)."""
from __future__ import annotations

from generate_bulk_city_data import STATE_META
from seo_bulk_booking_city import booking_page_book
from seo_bulk_wave42_book_cities_data import WAVE42_BOOK_CITIES


def _state_near(st: str) -> str:
    st_page = STATE_META.get(st, (f"{st.lower()}-mahjong.html", ""))[0]
    name = st_page.replace("-mahjong.html", "")
    return f"mahjong-lessons-near-me-{name}.html"


PRIORITY_BOOK = [
    ("book-mahjong-atlanta.html", "Atlanta", "GA", "georgia-mahjong.html", "atlanta-mahjong.html"),
    ("book-mahjong-chattanooga.html", "Chattanooga", "TN", "tennessee-mahjong.html", "chattanooga-mahjong.html"),
    ("book-mahjong-nashville.html", "Nashville", "TN", "tennessee-mahjong.html", "nashville-mahjong.html"),
    ("book-mahjong-charlotte.html", "Charlotte", "NC", "north-carolina-mahjong.html", "charlotte-mahjong.html"),
    ("book-mahjong-raleigh.html", "Raleigh", "NC", "north-carolina-mahjong.html", "raleigh-mahjong.html"),
    ("book-mahjong-dallas.html", "Dallas", "TX", "texas-mahjong.html", "dallas-mahjong.html"),
    ("book-mahjong-houston.html", "Houston", "TX", "texas-mahjong.html", "houston-mahjong.html"),
    ("book-mahjong-miami.html", "Miami", "FL", "florida-mahjong.html", "miami-mahjong.html"),
    ("book-mahjong-denver.html", "Denver", "CO", "colorado-mahjong.html", "denver-mahjong.html"),
    ("book-mahjong-chicago.html", "Chicago", "IL", "illinois-mahjong.html", "chicago-mahjong.html"),
]


def bulk_pages_book_mahjong_wave(city, page, mahjong_kw) -> list:
    del city, page
    out = []
    seen = {r[0] for r in WAVE42_BOOK_CITIES}
    for slug, label, st, state_page, city_page in PRIORITY_BOOK:
        if slug not in seen:
            out.append(
                booking_page_book(
                    mahjong_kw,
                    (slug, label, st, state_page, city_page, _state_near(st)),
                )
            )
            seen.add(slug)
    for row in WAVE42_BOOK_CITIES:
        out.append(booking_page_book(mahjong_kw, row))
    return out
