# -*- coding: utf-8 -*-
"""Mega Wave 46 — ~600 pages (500 cities + regional hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave46_cities_data import WAVE46_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_46(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "orange-county-coast-ca-mahjong-hub.html",
            "Orange County Coast CA Mahjong | Irvine, Newport & Laguna",
            "Orange County Coast CA mahjong — Irvine, Newport Beach, Laguna private lessons.",
            "orange county coast california mahjong hub, newport beach mah jongg",
            "Orange County Coast CA Mahjong Guide",
            """<p><strong>OC Coast mahjong</strong> — South Coast private lessons:</p>
<p><a href="irvine-ca-3-mahjong.html">Irvine</a> · <a href="newport-beach-ca-6-mahjong.html">Newport Beach</a> · <a href="laguna-beach-ca-2-mahjong.html">Laguna Beach</a></p>
<p><a href="southern-california-mahjong-hub.html">SoCal hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "westchester-ny-mahjong-hub.html",
            "Westchester NY Mahjong | Scarsdale, Rye & Greenwich Area",
            "Westchester NY mahjong — Scarsdale, Rye, Westchester County private lessons.",
            "westchester new york mahjong hub, scarsdale mah jongg",
            "Westchester NY Mahjong Guide",
            """<p><strong>Westchester mahjong</strong> — NYC suburb private events:</p>
<p><a href="scarsdale-ny-2-mahjong.html">Scarsdale</a> · <a href="rye-ny-2-mahjong.html">Rye</a> · <a href="new-york-mahjong.html">New York</a></p>
<p><a href="gold-coast-ct-mahjong-hub.html">CT Gold Coast</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "san-antonio-hill-country-tx-mahjong-hub.html",
            "San Antonio Hill Country TX Mahjong | Kerrville, New Braunfels & Kyle",
            "San Antonio Hill Country TX mahjong — Kerrville, Seguin, Kyle private lessons.",
            "san antonio hill country texas mahjong hub, kerrville mah jongg",
            "San Antonio Hill Country TX Mahjong Guide",
            """<p><strong>SA Hill Country mahjong</strong> — Texas Hill Country private events:</p>
<p><a href="kerrville-tx-2-mahjong.html">Kerrville</a> · <a href="seguin-tx-2-mahjong.html">Seguin</a> · <a href="kyle-tx-2-mahjong.html">Kyle</a> · <a href="san-antonio-mahjong.html">San Antonio</a></p>
<p><a href="texas-hill-country-mahjong-hub.html">TX Hill Country</a></p>""",
        ),
        (
            "tulsa-metro-ok-mahjong-hub.html",
            "Tulsa Metro OK Mahjong | Broken Arrow, Edmond & Claremore",
            "Tulsa metro OK mahjong — Broken Arrow, Edmond, Claremore private lessons.",
            "tulsa metro oklahoma mahjong hub, broken arrow mah jongg",
            "Tulsa Metro OK Mahjong Guide",
            """<p><strong>Tulsa metro mahjong</strong> — northeast Oklahoma private events:</p>
<p><a href="broken-arrow-ok-9-mahjong.html">Broken Arrow</a> · <a href="edmond-ok-3-mahjong.html">Edmond</a> · <a href="claremore-ok-2-mahjong.html">Claremore</a></p>
<p><a href="oklahoma-mahjong-hub.html">Oklahoma hub</a></p>""",
        ),
        (
            "nebraska-statewide-mahjong-hub.html",
            "Nebraska Mahjong Cities | Omaha, Lincoln & Panhandle",
            "Nebraska mahjong cities — Omaha, Lincoln, Grand Island, panhandle towns.",
            "nebraska cities mahjong hub, omaha mah jongg suburbs",
            "Nebraska Cities Mahjong Guide",
            """<p><strong>Nebraska mahjong</strong> — statewide private lessons:</p>
<p><a href="omaha-mahjong.html">Omaha</a> · <a href="lincoln-ne-mahjong.html">Lincoln</a> · <a href="grand-island-ne-mahjong.html">Grand Island</a></p>
<p><a href="nebraska-mahjong-hub.html">Nebraska hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "hudson-valley-ny-mahjong-hub.html",
            "Hudson Valley NY Mahjong | Beacon, Kingston & Saratoga",
            "Hudson Valley NY mahjong — Beacon, Kingston, Saratoga Springs private lessons.",
            "hudson valley new york mahjong hub, saratoga springs mah jongg",
            "Hudson Valley NY Mahjong Guide",
            """<p><strong>Hudson Valley mahjong</strong> — upstate NY private events:</p>
<p><a href="beacon-ny-2-mahjong.html">Beacon</a> · <a href="kingston-ny-3-mahjong.html">Kingston</a> · <a href="saratoga-springs-ny-3-mahjong.html">Saratoga Springs</a></p>
<p><a href="hudson-valley-mahjong-hub.html">Hudson Valley hub</a></p>""",
        ),
        (
            "austin-satellite-cities-mahjong-hub.html",
            "Austin Satellite Cities Mahjong | Pflugerville, Buda & Round Rock",
            "Austin satellite cities mahjong — Pflugerville, Buda, Kyle Austin metro private lessons.",
            "austin satellite cities mahjong hub, pflugerville mah jongg",
            "Austin Satellite Cities Mahjong Guide",
            """<p><strong>Austin metro satellites mahjong</strong> — suburb private lessons:</p>
<p><a href="pflugerville-tx-2-mahjong.html">Pflugerville</a> · <a href="buda-tx-2-mahjong.html">Buda</a> · <a href="austin-mahjong.html">Austin</a></p>
<p><a href="book-mahjong-austin.html">Book Austin</a></p>""",
        ),
        (
            "south-bay-ca-mahjong-hub.html",
            "South Bay CA Mahjong | Torrance, Manhattan Beach & Redondo",
            "South Bay California mahjong — Torrance, Manhattan Beach, Redondo Beach.",
            "south bay california mahjong hub, manhattan beach mah jongg",
            "South Bay CA Mahjong Guide",
            """<p><strong>South Bay mahjong</strong> — LA South Bay private lessons:</p>
<p><a href="torrance-ca-2-mahjong.html">Torrance</a> · <a href="manhattan-beach-ca-2-mahjong.html">Manhattan Beach</a> · <a href="redondo-beach-ca-2-mahjong.html">Redondo Beach</a></p>
<p><a href="los-angeles-mahjong.html">Los Angeles</a></p>""",
        ),
        (
            "arkansas-ozarks-mahjong-hub.html",
            "Arkansas Ozarks Mahjong | Fayetteville, Rogers & Hot Springs",
            "Arkansas Ozarks mahjong — NW Arkansas & Hot Springs private lessons.",
            "arkansas ozarks mahjong hub, hot springs ar mah jongg",
            "Arkansas Ozarks Mahjong Guide",
            """<p><strong>AR Ozarks mahjong</strong> — mountains &amp; corporate corridor:</p>
<p><a href="fayetteville-ar-4-mahjong.html">Fayetteville</a> · <a href="rogers-ar-10-mahjong.html">Rogers</a> · <a href="hot-springs-ar-4-mahjong.html">Hot Springs</a></p>
<p><a href="northwest-arkansas-mahjong-hub.html">NW Arkansas</a> · <a href="ozarks-mahjong-hub.html">Ozarks</a></p>""",
        ),
        (
            "wave-46-mahjong-hub.html",
            "Wave 46 City Guide | Latest Metro Additions",
            "Wave 46 mahjong cities — OC coast, Westchester, NE, OK metro, AR Ozarks.",
            "wave 46 mahjong cities, latest mahjong booking cities",
            "Wave 46 — Latest Cities",
            """<p><strong>Wave 46</strong> — hundreds of new bookable cities:</p>
<p><a href="mahjong-booking-near-me-hub.html">Book near me</a> · <a href="orange-county-coast-ca-mahjong-hub.html">OC Coast</a> · <a href="westchester-ny-mahjong-hub.html">Westchester</a> · <a href="cities-mahjong-hub.html">All cities</a> · <a href="book-mahjong-lesson.html">Book now</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.88"))

    for tup in WAVE46_CITIES:
        out.append(_city_from_tuple(city, tup))

    for i in range(1, 19):
        out.append(_greek_fr(mahjong_kw, f"w46-fraternity-{i}", f"Fraternity Group {i}", f"F{i}"))
        out.append(_greek_sor(mahjong_kw, f"w46-sorority-{i}", f"Sorority Group {i}", f"S{i}"))

    occasions = [
        (f"w46-event-{i}", f"Event Style {i}", f"w46 mahjong event {i} booking", f'<p><strong>Event {i}</strong> — <a href="mahjong-booking-near-me-hub.html">Book</a> · <a href="/book-mahjong-lesson.html">Schedule</a>.</p>')
        for i in range(1, 31)
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("w46-instructor-travel.html", "Instructor Travel", "mahjong instructor travel to your city — nationwide", '<p>We <strong>travel</strong> — <a href="travel-to-you-mahjong.html">Travel</a> · <a href="hire-mahjong-instructor.html">Hire</a>.</p>'),
        ("w46-lesson-gift-booking.html", "Lesson Gift Booking", "mahjong lesson gift booking — gift a class", '<p><strong>Gift a lesson</strong> — <a href="mahjong-gift-experience.html">Gift experience</a>.</p>'),
        ("w46-club-league-booking.html", "Club League Booking", "mahjong club league booking — pro instructor night", '<p><strong>Club league booking</strong> — <a href="mahjong-league.html">League</a>.</p>'),
        ("w46-snowbird-booking-fl.html", "Snowbird FL Booking", "snowbird florida mahjong booking — winter season", '<p><strong>Snowbird booking</strong> — <a href="snowbird-mahjong.html">Snowbird</a> · <a href="florida-mahjong-hub.html">Florida</a>.</p>'),
        ("w46-greenbrier-trip-booking.html", "Greenbrier Trip Booking", "greenbrier trip mahjong booking — tournament weekend", '<p><strong>Greenbrier trip</strong> — <a href="greenbrier-tournament-booking.html">Tournament booking</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
