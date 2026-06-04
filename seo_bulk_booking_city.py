# -*- coding: utf-8 -*-
"""Shared builders for city-level booking / near-me SEO pages."""
from __future__ import annotations

BOOKING_HUB = "mahjong-booking-near-me-hub.html"


def _stem_from_city(city_page: str) -> str:
    return city_page.replace("-mahjong.html", "")


def booking_page_near_me(mahjong_kw, row: tuple) -> dict:
    slug, label, st, state_page, city_page, state_near = row
    stem = _stem_from_city(city_page)
    desc = (
        f"Book mahjong lessons near {label} — private teacher comes to you. "
        "Mahjong 101 $125 · nationwide travel · Lookout Mountain Mahjong."
    )
    body = (
        f"<p><strong>Mahjong lessons near {label}</strong> — certified TML Ambassadors "
        f'<a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a> travel to your home, '
        "club, resort, or tournament. We bring tiles, tables, and NMJL cards.</p>"
        f'<p><a href="{city_page}">{label} mahjong</a> · '
        f'<a href="book-mahjong-{stem}.html">Book in {label}</a> · '
        f'<a href="{state_near}">Near me in {st}</a></p>'
        f'<p class="seo-inline-cta"><strong>Book now:</strong> '
        f'<a href="/book-mahjong-lesson.html">Schedule Mahjong 101</a> · '
        f'<a href="hire-mahjong-instructor-{stem}.html">Hire instructor</a> · '
        f'<a href="{BOOKING_HUB}">Booking hub</a></p>'
    )
    return mahjong_kw(
        slug,
        f"Mahjong Lessons Near {label} | Book Now",
        desc,
        f"mahjong lessons near me {stem}, book mahjong lessons {label.lower()}, mahjong teacher {stem}",
        f"Mahjong Lessons Near {label}",
        body,
    )


def booking_page_book(mahjong_kw, row: tuple) -> dict:
    slug, label, st, state_page, city_page, state_near = row
    stem = _stem_from_city(city_page)
    near_slug = f"{stem}-lessons-near-me.html"
    desc = (
        f"Book mahjong in {label} — schedule private Mahjong 101 with a certified instructor. "
        "We travel to your home, club, or event."
    )
    body = (
        f"<p><strong>Book mahjong in {label}</strong> — "
        f'<a href="/book-mahjong-lesson.html">Mahjong 101</a> $125/person · tiles &amp; tables included. '
        "Private teachers travel nationwide.</p>"
        f'<p><a href="{near_slug}">Lessons near me in {label}</a> · '
        f'<a href="{city_page}">{label} guide</a> · '
        f'<a href="{state_near}">{st} near me</a></p>'
        f'<p class="seo-inline-cta"><strong>Schedule:</strong> '
        f'<a href="/book-mahjong-lesson.html">Book now</a> · '
        f'<a href="hire-mahjong-instructor-{stem}.html">Hire instructor</a> · '
        f'<a href="book-mahjong-tournament-coach.html">Tournament coach</a> · '
        f'<a href="{BOOKING_HUB}">Near me hub</a></p>'
    )
    return mahjong_kw(
        slug,
        f"Book Mahjong Lessons in {label}",
        desc,
        f"book mahjong {stem}, book mahjong lessons {label.lower()}, schedule mahjong {stem}",
        f"Book Mahjong in {label}",
        body,
    )


def booking_page_hire(mahjong_kw, row: tuple) -> dict:
    slug, label, st, state_page, city_page, state_near = row
    stem = _stem_from_city(city_page)
    desc = (
        f"Hire a mahjong instructor in {label} — private teacher for home, club, resort, or tournament."
    )
    body = (
        f"<p><strong>Hire a mahjong instructor in {label}</strong> — "
        "corporate events, country clubs, bachelorettes, and private homes. "
        "Certified TML Ambassadors Mahj Jen &amp; Mahj Hen.</p>"
        f'<p><a href="book-mahjong-{stem}.html">Book lessons</a> · '
        f'<a href="{stem}-lessons-near-me.html">Near me</a> · '
        f'<a href="{city_page}">{label}</a></p>'
        f'<p class="seo-inline-cta"><strong>Hire now:</strong> '
        f'<a href="hire-mahjong-instructor.html">Hire guide</a> · '
        f'<a href="/book-mahjong-lesson.html">Book Mahjong 101</a> · '
        f'<a href="private-mahjong-teacher-home-visit.html">Home visit</a></p>'
    )
    return mahjong_kw(
        slug,
        f"Hire Mahjong Instructor {label}",
        desc,
        f"hire mahjong instructor {stem}, mahjong teacher for hire {label.lower()}, private mahjong teacher {stem}",
        f"Hire Mahjong Instructor — {label}",
        body,
    )
