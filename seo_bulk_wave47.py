# -*- coding: utf-8 -*-
"""Booking Wave 47 — near-me, book, and hire pages for Wave 46 cities."""
from __future__ import annotations

from seo_bulk_booking_wave import bulk_booking_pages_for_cities
from seo_bulk_wave46_cities_data import WAVE46_CITIES


def bulk_pages_wave_46_booking(city, page, mahjong_kw) -> list:
    del city, page
    return bulk_booking_pages_for_cities(mahjong_kw, WAVE46_CITIES)
