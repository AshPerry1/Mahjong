# -*- coding: utf-8 -*-
"""Mega Wave 41 — ~600 pages (500 cities + hubs + booking keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave41_cities_data import WAVE41_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_41(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "north-atlanta-suburbs-mahjong-hub.html",
            "North Atlanta Suburbs Mahjong | Dunwoody, Alpharetta & Johns Creek",
            "North Atlanta suburbs mahjong — Dunwoody, Sandy Springs, Johns Creek private lessons.",
            "north atlanta suburbs mahjong hub, dunwoody mah jongg",
            "North Atlanta Suburbs Mahjong Guide",
            """<p><strong>North Atlanta suburbs mahjong</strong> — book private teachers:</p>
<p><a href="dunwoody-ga-ga-mahjong.html">Dunwoody</a> · <a href="alpharetta-mahjong.html">Alpharetta</a> · <a href="atlanta-mahjong.html">Atlanta</a></p>
<p><a href="atlanta-metro-mahjong-hub.html">Atlanta metro</a> · <a href="book-mahjong-lesson.html">Book</a> · <a href="mahjong-booking-near-me-hub.html">Near me</a></p>""",
        ),
        (
            "south-atlanta-suburbs-mahjong-hub.html",
            "South Atlanta Suburbs Mahjong | McDonough, Stockbridge & Conyers",
            "South Atlanta suburbs mahjong — Henry & Rockdale county private events.",
            "south atlanta suburbs mahjong hub, mcdonough mah jongg",
            "South Atlanta Suburbs Mahjong Guide",
            """<p><strong>South Atlanta suburbs mahjong</strong> — private lessons south of the city:</p>
<p><a href="mcdonough-ga-ga-mahjong.html">McDonough</a> · <a href="stockbridge-ga-ga-mahjong.html">Stockbridge</a> · <a href="conyers-ga-ga-mahjong.html">Conyers</a></p>
<p><a href="georgia-mahjong-hub.html">Georgia hub</a> · <a href="atlanta-lessons-near-me.html">Atlanta near me</a></p>""",
        ),
        (
            "north-dallas-suburbs-mahjong-hub.html",
            "North Dallas Suburbs Mahjong | Plano, Frisco & McKinney",
            "North Dallas suburbs mahjong — Collin County private lessons.",
            "north dallas suburbs mahjong hub, frisco mah jongg",
            "North Dallas Suburbs Mahjong Guide",
            """<p><strong>North Dallas suburbs mahjong</strong> — DFW north metro:</p>
<p><a href="plano-mahjong.html">Plano</a> · <a href="frisco-tx-mahjong.html">Frisco</a> · <a href="dallas-mahjong.html">Dallas</a></p>
<p><a href="book-mahjong-dallas.html">Book Dallas</a> · <a href="texas-mahjong-hub.html">Texas hub</a></p>""",
        ),
        (
            "houston-suburbs-mahjong-hub.html",
            "Houston Suburbs Mahjong | Katy, Sugar Land & The Woodlands",
            "Houston suburbs mahjong — Katy, Sugar Land, Woodlands private events.",
            "houston suburbs mahjong hub, katy mah jongg",
            "Houston Suburbs Mahjong Guide",
            """<p><strong>Houston suburbs mahjong</strong> — west &amp; north Houston metro:</p>
<p><a href="katy-tx-mahjong.html">Katy</a> · <a href="sugar-land-tx-mahjong.html">Sugar Land</a> · <a href="the-woodlands-mahjong.html">The Woodlands</a></p>
<p><a href="houston-lessons-near-me.html">Houston near me</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "charlotte-suburbs-mahjong-hub.html",
            "Charlotte Suburbs Mahjong | Matthews, Huntersville & Cornelius",
            "Charlotte suburbs mahjong — Mecklenburg &amp; lake Norman private lessons.",
            "charlotte suburbs mahjong hub, matthews mah jongg",
            "Charlotte Suburbs Mahjong Guide",
            """<p><strong>Charlotte suburbs mahjong</strong> — south &amp; north metro:</p>
<p><a href="matthews-nc-mahjong.html">Matthews</a> · <a href="lake-norman-mahjong.html">Lake Norman</a> · <a href="charlotte-mahjong.html">Charlotte</a></p>
<p><a href="charlotte-lessons-near-me.html">Charlotte near me</a></p>""",
        ),
        (
            "raleigh-suburbs-mahjong-hub.html",
            "Raleigh Suburbs Mahjong | Cary, Apex & Wake Forest",
            "Raleigh suburbs mahjong — Triangle suburbs private lessons.",
            "raleigh suburbs mahjong hub, cary mah jongg",
            "Raleigh Suburbs Mahjong Guide",
            """<p><strong>Raleigh suburbs mahjong</strong> — Wake County private events:</p>
<p><a href="cary-nc-mahjong.html">Cary</a> · <a href="apex-nc-mahjong.html">Apex</a> · <a href="raleigh-mahjong.html">Raleigh</a></p>
<p><a href="raleigh-durham-mahjong-hub.html">Raleigh-Durham hub</a></p>""",
        ),
        (
            "nashville-suburbs-mahjong-hub.html",
            "Nashville Suburbs Mahjong | Franklin, Brentwood & Murfreesboro",
            "Nashville suburbs mahjong — Williamson &amp; Rutherford county events.",
            "nashville suburbs mahjong hub, franklin tn mah jongg",
            "Nashville Suburbs Mahjong Guide",
            """<p><strong>Nashville suburbs mahjong</strong> — Music City suburbs:</p>
<p><a href="franklin-tn-mahjong.html">Franklin</a> · <a href="brentwood-tn-mahjong.html">Brentwood</a> · <a href="nashville-mahjong.html">Nashville</a></p>
<p><a href="nashville-lessons-near-me.html">Nashville near me</a></p>""",
        ),
        (
            "phoenix-east-valley-mahjong-hub.html",
            "Phoenix East Valley Mahjong | Mesa, Gilbert & Chandler",
            "Phoenix East Valley mahjong — Mesa, Gilbert, Chandler private lessons.",
            "phoenix east valley mahjong hub, mesa mah jongg",
            "Phoenix East Valley Mahjong Guide",
            """<p><strong>East Valley mahjong</strong> — greater Phoenix suburbs:</p>
<p><a href="chandler-az-mahjong.html">Chandler</a> · <a href="gilbert-az-mahjong.html">Gilbert</a> · <a href="phoenix-mahjong.html">Phoenix</a></p>
<p><a href="phoenix-metro-mahjong-hub.html">Phoenix metro</a></p>""",
        ),
        (
            "chicago-suburbs-mahjong-hub.html",
            "Chicago Suburbs Mahjong | Naperville, Evanston & Oak Park",
            "Chicago suburbs mahjong — collar counties private lessons.",
            "chicago suburbs mahjong hub, naperville mah jongg",
            "Chicago Suburbs Mahjong Guide",
            """<p><strong>Chicago suburbs mahjong</strong> — north &amp; west metro:</p>
<p><a href="naperville-il-mahjong.html">Naperville</a> · <a href="evanston-il-mahjong.html">Evanston</a> · <a href="chicago-mahjong.html">Chicago</a></p>
<p><a href="illinois-mahjong-hub.html">Illinois hub</a></p>""",
        ),
        (
            "book-mahjong-by-region-hub.html",
            "Book Mahjong by Region | Nationwide City Booking",
            "Book mahjong by region — find your city, hire instructor, schedule Mahjong 101.",
            "book mahjong by region, mahjong booking cities",
            "Book Mahjong by Region",
            """<p><strong>Book mahjong by region</strong> — every metro we travel:</p>
<p><a href="mahjong-booking-near-me-hub.html">★ Booking near me hub</a> · <a href="mahjong-lessons-near-me-hub.html">Lessons near me</a> · <a href="book-private-mahjong-teacher-hub.html">Private teacher</a></p>
<p><a href="southeast-mahjong-hub.html">Southeast</a> · <a href="cities-mahjong-hub.html">All cities</a> · <a href="book-mahjong-lesson.html">Book now</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.89"))

    for tup in WAVE41_CITIES:
        out.append(_city_from_tuple(city, tup))

    for i in range(1, 19):
        out.append(_greek_fr(mahjong_kw, f"w41-fraternity-{i}", f"Fraternity Group {i}", f"F{i}"))
        out.append(_greek_sor(mahjong_kw, f"w41-sorority-{i}", f"Sorority Group {i}", f"S{i}"))

    occasions = [
        (f"w41-booking-{i}", f"Booking Event {i}", f"w41 booking event {i} mahjong", f'<p><strong>Booking event {i}</strong> — <a href="mahjong-booking-near-me-hub.html">Book near me</a> · <a href="/book-mahjong-lesson.html">Schedule</a>.</p>')
        for i in range(1, 31)
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("w41-book-online-mahjong.html", "Book Online", "book online mahjong lesson — email schedule", '<p>Book online via <a href="book-mahjong-lesson.html">book page</a> or lookoutmountainmahjong@gmail.com.</p>'),
        ("w41-same-week-mahjong-booking.html", "Same Week Booking", "same week mahjong booking — ask availability", '<p>Ask about <strong>same-week</strong> dates — <a href="book-mahjong-lesson-today.html">Book today</a>.</p>'),
        ("w41-weekend-mahjong-booking.html", "Weekend Booking", "weekend mahjong booking — Saturday Sunday lessons", '<p><strong>Weekend booking</strong> popular for showers &amp; girls night — <a href="book-mahjong-this-weekend.html">This weekend</a>.</p>'),
        ("w41-travel-mahjong-booking.html", "Travel Booking", "travel mahjong booking — instructor flies or drives", '<p>We <strong>travel</strong> for lessons — <a href="travel-to-you-mahjong.html">Travel policy</a>.</p>'),
        ("w41-tournament-travel-booking.html", "Tournament Travel", "tournament travel mahjong booking — Greenbrier prep trips", '<p><strong>Tournament travel</strong> — <a href="book-mahjong-tournament-hub.html">Tournament hub</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
