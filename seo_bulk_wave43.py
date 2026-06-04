# -*- coding: utf-8 -*-
"""Booking Wave 43 — hire-mahjong-instructor-{city} pages (1500 cities)."""
from __future__ import annotations

from generate_bulk_city_data import STATE_META
from seo_bulk_booking_city import booking_page_hire
from seo_bulk_wave43_hire_cities_data import WAVE43_HIRE_CITIES

PRIORITY_HIRE = [
    ("hire-mahjong-instructor-atlanta.html", "Atlanta", "GA", "georgia-mahjong.html", "atlanta-mahjong.html"),
    ("hire-mahjong-instructor-chattanooga.html", "Chattanooga", "TN", "tennessee-mahjong.html", "chattanooga-mahjong.html"),
    ("hire-mahjong-instructor-nashville.html", "Nashville", "TN", "tennessee-mahjong.html", "nashville-mahjong.html"),
    ("hire-mahjong-instructor-charlotte.html", "Charlotte", "NC", "north-carolina-mahjong.html", "charlotte-mahjong.html"),
    ("hire-mahjong-instructor-dallas.html", "Dallas", "TX", "texas-mahjong.html", "dallas-mahjong.html"),
    ("hire-mahjong-instructor-houston.html", "Houston", "TX", "texas-mahjong.html", "houston-mahjong.html"),
]


def _state_near(st: str) -> str:
    st_page = STATE_META.get(st, (f"{st.lower()}-mahjong.html", ""))[0]
    name = st_page.replace("-mahjong.html", "")
    return f"mahjong-lessons-near-me-{name}.html"


def bulk_pages_hire_instructor_wave(city, page, mahjong_kw) -> list:
    del city, page
    out = []
    seen = {r[0] for r in WAVE43_HIRE_CITIES}
    for slug, label, st, state_page, city_page in PRIORITY_HIRE:
        if slug not in seen:
            out.append(
                booking_page_hire(
                    mahjong_kw,
                    (slug, label, st, state_page, city_page, _state_near(st)),
                )
            )
            seen.add(slug)
    for row in WAVE43_HIRE_CITIES:
        out.append(booking_page_hire(mahjong_kw, row))
    return out
