# -*- coding: utf-8 -*-
"""Mega Wave 44 — ~600 pages (500 cities + regional hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave44_cities_data import WAVE44_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_44(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "middle-tennessee-suburbs-mahjong-hub.html",
            "Middle Tennessee Suburbs Mahjong | Brentwood, Spring Hill & Mt Juliet",
            "Middle Tennessee suburbs mahjong — Williamson & Rutherford county private lessons.",
            "middle tennessee suburbs mahjong hub, brentwood mah jongg",
            "Middle Tennessee Suburbs Mahjong Guide",
            """<p><strong>Middle TN suburbs mahjong</strong> — book private teachers:</p>
<p><a href="brentwood-tn-2-mahjong.html">Brentwood</a> · <a href="spring-hill-tn-2-mahjong.html">Spring Hill</a> · <a href="mount-juliet-tn-tn-mahjong.html">Mount Juliet</a> · <a href="nashville-mahjong.html">Nashville</a></p>
<p><a href="nashville-suburbs-mahjong-hub.html">Nashville suburbs</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "triangle-nc-suburbs-mahjong-hub.html",
            "Triangle NC Suburbs Mahjong | Apex, Cary & Wake Forest",
            "Triangle NC suburbs mahjong — Wake County private lessons and events.",
            "triangle nc suburbs mahjong hub, apex nc mah jongg",
            "Triangle NC Suburbs Mahjong Guide",
            """<p><strong>Triangle suburbs mahjong</strong> — Raleigh-Durham corridor:</p>
<p><a href="apex-nc-7-mahjong.html">Apex</a> · <a href="holly-springs-nc-2-mahjong.html">Holly Springs</a> · <a href="wake-forest-nc-2-mahjong.html">Wake Forest</a></p>
<p><a href="raleigh-suburbs-mahjong-hub.html">Raleigh suburbs</a> · <a href="raleigh-durham-mahjong-hub.html">Raleigh-Durham</a></p>""",
        ),
        (
            "denver-south-metro-mahjong-hub.html",
            "Denver South Metro Mahjong | Highlands Ranch, Parker & Castle Rock",
            "Denver south metro mahjong — Douglas & Arapahoe county private lessons.",
            "denver south metro mahjong hub, highlands ranch mah jongg",
            "Denver South Metro Mahjong Guide",
            """<p><strong>Denver south metro mahjong</strong> — south Denver suburbs:</p>
<p><a href="highlands-ranch-co-co-mahjong.html">Highlands Ranch</a> · <a href="castle-rock-co-co-mahjong.html">Castle Rock</a> · <a href="parker-co-7-mahjong.html">Parker</a></p>
<p><a href="front-range-co-mahjong-hub.html">Front Range</a> · <a href="denver-mahjong.html">Denver</a></p>""",
        ),
        (
            "phoenix-metro-mahjong-hub.html",
            "Phoenix Metro Mahjong | Scottsdale, Mesa & Tempe",
            "Phoenix metro mahjong — Scottsdale, Mesa, Tempe, East Valley private lessons.",
            "phoenix metro mahjong hub, scottsdale mah jongg",
            "Phoenix Metro Mahjong Guide",
            """<p><strong>Phoenix metro mahjong</strong> — Valley of the Sun private events:</p>
<p><a href="scottsdale-az-7-mahjong.html">Scottsdale</a> · <a href="mesa-az-8-mahjong.html">Mesa</a> · <a href="tempe-az-6-mahjong.html">Tempe</a></p>
<p><a href="phoenix-east-valley-mahjong-hub.html">East Valley</a> · <a href="phoenix-mahjong.html">Phoenix</a></p>""",
        ),
        (
            "northwest-arkansas-mahjong-hub.html",
            "Northwest Arkansas Mahjong | Bentonville, Rogers & Fayetteville",
            "Northwest Arkansas mahjong — Bentonville, Rogers, Fayetteville private lessons.",
            "northwest arkansas mahjong hub, bentonville mah jongg",
            "Northwest Arkansas Mahjong Guide",
            """<p><strong>NW Arkansas mahjong</strong> — Ozarks corporate &amp; suburb private lessons:</p>
<p><a href="bentonville-ar-2-mahjong.html">Bentonville</a> · <a href="rogers-ar-8-mahjong.html">Rogers</a> · <a href="fayetteville-ar-2-mahjong.html">Fayetteville</a></p>
<p><a href="arkansas-mahjong-hub.html">Arkansas hub</a> · <a href="ozarks-mahjong-hub.html">Ozarks</a></p>""",
        ),
        (
            "north-georgia-foothills-mahjong-hub.html",
            "North Georgia Foothills Mahjong | Cartersville, Calhoun & Toccoa",
            "North Georgia foothills mahjong — I-75 corridor north of Atlanta.",
            "north georgia foothills mahjong hub, cartersville mah jongg",
            "North Georgia Foothills Mahjong Guide",
            """<p><strong>North GA foothills mahjong</strong> — between Atlanta &amp; mountains:</p>
<p><a href="cartersville-ga-2-mahjong.html">Cartersville</a> · <a href="calhoun-ga-2-mahjong.html">Calhoun</a> · <a href="toccoa-ga-2-mahjong.html">Toccoa</a></p>
<p><a href="north-georgia-mahjong-hub.html">North Georgia</a> · <a href="southeast-mahjong-hub.html">Southeast</a></p>""",
        ),
        (
            "oklahoma-city-metro-mahjong-hub.html",
            "Oklahoma City Metro Mahjong | Edmond, Norman & Moore",
            "OKC metro mahjong — Edmond, Norman, Moore private lessons.",
            "oklahoma city metro mahjong hub, edmond ok mah jongg",
            "Oklahoma City Metro Mahjong Guide",
            """<p><strong>OKC metro mahjong</strong> — central Oklahoma private events:</p>
<p><a href="oklahoma-city-mahjong.html">Oklahoma City</a> · <a href="norman-ok-mahjong.html">Norman</a></p>
<p><a href="oklahoma-mahjong-hub.html">Oklahoma hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "southern-illinois-mahjong-hub.html",
            "Southern Illinois Mahjong | Carbondale, Marion & Mt Vernon",
            "Southern Illinois mahjong — Carbondale, Shawnee region private lessons.",
            "southern illinois mahjong hub, carbondale mah jongg",
            "Southern Illinois Mahjong Guide",
            """<p><strong>Southern Illinois mahjong</strong> — downstate private events:</p>
<p><a href="carbondale-il-2-mahjong.html">Carbondale</a> · <a href="springfield-il-8-mahjong.html">Springfield IL</a></p>
<p><a href="illinois-mahjong-hub.html">Illinois hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "sedona-flagstaff-mahjong-hub.html",
            "Sedona & Flagstaff Mahjong | Northern Arizona",
            "Sedona Flagstaff mahjong — northern Arizona resort & mountain towns.",
            "sedona flagstaff mahjong hub, sedona arizona mah jongg",
            "Sedona & Flagstaff Mahjong Guide",
            """<p><strong>Northern AZ mahjong</strong> — resort &amp; vacation private lessons:</p>
<p><a href="sedona-az-2-mahjong.html">Sedona</a> · <a href="flagstaff-az-8-mahjong.html">Flagstaff</a></p>
<p><a href="arizona-mahjong-hub.html">Arizona hub</a> · <a href="vacation-mahjong.html">Vacation</a></p>""",
        ),
        (
            "wave-44-mahjong-hub.html",
            "Wave 44 City Guide | Latest Metro Additions",
            "Wave 44 mahjong cities — latest Lookout Mountain Mahjong metro additions nationwide.",
            "wave 44 mahjong cities, latest mahjong cities",
            "Wave 44 — Latest Cities",
            """<p><strong>Wave 44</strong> adds hundreds of metro &amp; suburb pages — each links to booking:</p>
<p><a href="mahjong-booking-near-me-hub.html">Book near me</a> · <a href="cities-mahjong-hub.html">All cities</a> · <a href="book-mahjong-by-region-hub.html">Book by region</a> · <a href="book-mahjong-lesson.html">Book now</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.88"))

    for tup in WAVE44_CITIES:
        out.append(_city_from_tuple(city, tup))

    for i in range(1, 19):
        out.append(_greek_fr(mahjong_kw, f"w44-fraternity-{i}", f"Fraternity Group {i}", f"F{i}"))
        out.append(_greek_sor(mahjong_kw, f"w44-sorority-{i}", f"Sorority Group {i}", f"S{i}"))

    occasions = [
        (f"w44-social-{i}", f"Social Event {i}", f"w44 social event {i} mahjong", f'<p><strong>Social event {i}</strong> — <a href="mahjong-booking-near-me-hub.html">Book</a> · <a href="/book-mahjong-lesson.html">Schedule</a>.</p>')
        for i in range(1, 31)
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("w44-four-player-table.html", "Four Player Table", "four player mahjong table booking — standard lesson size", '<p>Book a <strong>four-player</strong> table — <a href="mahjong-101.html">Mahjong 101</a>.</p>'),
        ("w44-bring-friends-booking.html", "Bring Friends", "bring friends mahjong booking — group of 4-8", '<p><strong>Bring friends</strong> — ideal 4–8 for 101 — <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("w44-corporate-booking-quote.html", "Corporate Quote", "corporate mahjong booking quote — email for events", '<p>Corporate quotes — lookoutmountainmahjong@gmail.com · <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("w44-resort-booking.html", "Resort Booking", "resort mahjong booking — hotel event scheduling", '<p><strong>Resort booking</strong> — <a href="book-mahjong-resort.html">Resort</a>.</p>'),
        ("w44-tournament-prep-book.html", "Tournament Prep Book", "tournament prep booking mahjong — before your event", '<p><strong>Tournament prep</strong> — <a href="book-mahjong-tournament-hub.html">Tournament hub</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
