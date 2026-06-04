# -*- coding: utf-8 -*-
"""Booking Wave 45 — near-me, book, and hire pages for Wave 44 cities."""
from __future__ import annotations

from generate_bulk_city_data import STATE_META
from seo_bulk_booking_city import booking_page_book, booking_page_hire, booking_page_near_me
from seo_bulk_wave41_cities_data import WAVE41_CITIES
from seo_bulk_wave44_cities_data import WAVE44_CITIES


def _iter_wave_cities():
    seen: set[str] = set()
    for tup in WAVE41_CITIES + WAVE44_CITIES:
        if tup[0] not in seen:
            seen.add(tup[0])
            yield tup


def _state_near(st: str) -> str:
    st_page = STATE_META.get(st, (f"{st.lower()}-mahjong.html", ""))[0]
    return f"mahjong-lessons-near-me-{st_page.replace('-mahjong.html', '')}.html"


def _row(city_slug: str, label: str, st: str, state_page: str) -> tuple:
    stem = city_slug.replace("-mahjong.html", "")
    return (
        f"{stem}-lessons-near-me.html",
        label,
        st,
        state_page,
        city_slug,
        _state_near(st),
    )


def _book_row(city_slug: str, label: str, st: str, state_page: str) -> tuple:
    stem = city_slug.replace("-mahjong.html", "")
    return (
        f"book-mahjong-{stem}.html",
        label,
        st,
        state_page,
        city_slug,
        _state_near(st),
    )


def _hire_row(city_slug: str, label: str, st: str, state_page: str) -> tuple:
    stem = city_slug.replace("-mahjong.html", "")
    return (
        f"hire-mahjong-instructor-{stem}.html",
        label,
        st,
        state_page,
        city_slug,
        _state_near(st),
    )


def bulk_pages_wave_44_booking(city, page, mahjong_kw) -> list:
    del city, page
    out: list = []
    for city_slug, label, st, state_page, _hub in _iter_wave_cities():
        out.append(booking_page_near_me(mahjong_kw, _row(city_slug, label, st, state_page)))
        out.append(booking_page_book(mahjong_kw, _book_row(city_slug, label, st, state_page)))
        out.append(booking_page_hire(mahjong_kw, _hire_row(city_slug, label, st, state_page)))
    return out
