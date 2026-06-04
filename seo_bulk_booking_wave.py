# -*- coding: utf-8 -*-
"""Generate near-me / book / hire pages for a city tuple list."""
from __future__ import annotations

from generate_bulk_city_data import STATE_META
from seo_bulk_booking_city import booking_page_book, booking_page_hire, booking_page_near_me


def _state_near(st: str) -> str:
    st_page = STATE_META.get(st, (f"{st.lower()}-mahjong.html", ""))[0]
    return f"mahjong-lessons-near-me-{st_page.replace('-mahjong.html', '')}.html"


def bulk_booking_pages_for_cities(
    mahjong_kw,
    cities: list[tuple],
) -> list[dict]:
    out: list[dict] = []
    for city_slug, label, st, state_page, _hub in cities:
        stem = city_slug.replace("-mahjong.html", "")
        state_near = _state_near(st)
        out.append(
            booking_page_near_me(
                mahjong_kw,
                (f"{stem}-lessons-near-me.html", label, st, state_page, city_slug, state_near),
            )
        )
        out.append(
            booking_page_book(
                mahjong_kw,
                (f"book-mahjong-{stem}.html", label, st, state_page, city_slug, state_near),
            )
        )
        out.append(
            booking_page_hire(
                mahjong_kw,
                (
                    f"hire-mahjong-instructor-{stem}.html",
                    label,
                    st,
                    state_page,
                    city_slug,
                    state_near,
                ),
            )
        )
    return out
