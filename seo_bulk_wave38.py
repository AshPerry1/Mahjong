# -*- coding: utf-8 -*-
"""Mega Wave 38 — ~600+ pages (500 cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave38_cities_data import WAVE38_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_38(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "gold-country-ca-mahjong-hub.html",
            "Gold Country CA Mahjong | Grass Valley, Nevada City & Auburn",
            "Gold Country California mahjong — Grass Valley, Nevada City, Sierra foothills.",
            "gold country california mahjong hub, grass valley mah jongg",
            "Gold Country CA Mahjong Guide",
            """<p><strong>Gold Country mahjong</strong> — Sierra foothills private lessons:</p>
<p><a href="sacramento-ca-mahjong.html">Sacramento</a> · <a href="reno-nv-mahjong.html">Reno</a></p>
<p><a href="california-mahjong-hub.html">California hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "inland-empire-ca-mahjong-hub.html",
            "Inland Empire CA Mahjong | Riverside, Ontario & Redlands",
            "Inland Empire CA mahjong — Riverside, Ontario, Redlands SoCal inland.",
            "inland empire california mahjong hub, riverside mah jongg",
            "Inland Empire CA Mahjong Guide",
            """<p><strong>Inland Empire mahjong</strong> — SoCal inland private lessons:</p>
<p><a href="riverside-ca-mahjong.html">Riverside</a> · <a href="los-angeles-mahjong.html">Los Angeles</a></p>
<p><a href="southern-california-mahjong-hub.html">SoCal hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "wasatch-front-ut-mahjong-hub.html",
            "Wasatch Front UT Mahjong | Salt Lake, Provo & Ogden",
            "Wasatch Front Utah mahjong — Salt Lake City, Provo, Ogden metro corridor.",
            "wasatch front utah mahjong hub, salt lake city mah jongg",
            "Wasatch Front UT Mahjong Guide",
            """<p><strong>Wasatch Front mahjong</strong> — Utah metro private lessons:</p>
<p><a href="park-city-ut-mahjong.html">Park City</a> · <a href="st-george-ut-mahjong.html">St. George</a></p>
<p><a href="utah-mahjong-hub.html">Utah hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "front-range-co-mahjong-hub.html",
            "Front Range CO Mahjong | Fort Collins, Boulder & Colorado Springs",
            "Front Range Colorado mahjong — Fort Collins, Boulder, Colorado Springs.",
            "front range colorado mahjong hub, boulder mah jongg",
            "Front Range CO Mahjong Guide",
            """<p><strong>Front Range mahjong</strong> — Colorado corridor private lessons:</p>
<p><a href="boulder-co-mahjong.html">Boulder</a> · <a href="denver-mahjong.html">Denver</a> · <a href="colorado-springs-co-mahjong.html">Colorado Springs</a></p>
<p><a href="colorado-mahjong-hub.html">Colorado hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "panhandle-fl-mahjong-hub.html",
            "Panhandle FL Mahjong | Tallahassee, Pensacola & Panama City",
            "Panhandle Florida mahjong — Tallahassee, Pensacola, Panama City Gulf north.",
            "panhandle florida mahjong hub, tallahassee mah jongg",
            "Panhandle FL Mahjong Guide",
            """<p><strong>FL Panhandle mahjong</strong> — north Florida private lessons:</p>
<p><a href="pensacola-fl-mahjong.html">Pensacola</a> · <a href="tallahassee-mahjong.html">Tallahassee</a></p>
<p><a href="florida-panhandle-mahjong-hub.html">Panhandle hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "piedmont-nc-mahjong-hub.html",
            "Piedmont NC Mahjong | Winston-Salem, High Point & Burlington",
            "Piedmont NC mahjong — Winston-Salem, High Point, Burlington Triad.",
            "piedmont north carolina mahjong hub, winston salem mah jongg",
            "Piedmont NC Mahjong Guide",
            """<p><strong>Piedmont NC mahjong</strong> — Triad private lessons:</p>
<p><a href="winston-salem-mahjong.html">Winston-Salem</a> · <a href="greensboro-mahjong.html">Greensboro</a> · <a href="charlotte-mahjong.html">Charlotte</a></p>
<p><a href="north-carolina-mahjong-hub.html">NC hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "mid-south-tn-mahjong-hub.html",
            "Mid-South TN Mahjong | Jackson, Dyersburg & Union City",
            "Mid-South Tennessee mahjong — Jackson, West Tennessee private events.",
            "mid south tennessee mahjong hub, jackson tn mah jongg",
            "Mid-South TN Mahjong Guide",
            """<p><strong>Mid-South TN mahjong</strong> — West TN private lessons:</p>
<p><a href="memphis-mahjong.html">Memphis</a> · <a href="nashville-mahjong.html">Nashville</a></p>
<p><a href="tennessee-mahjong-hub.html">Tennessee hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "hill-country-ok-mahjong-hub.html",
            "Hill Country OK Mahjong | Lawton, Ardmore & Durant",
            "Hill Country Oklahoma mahjong — Lawton, Ardmore, Durant south central OK.",
            "hill country oklahoma mahjong hub, lawton mah jongg",
            "Hill Country OK Mahjong Guide",
            """<p><strong>OK Hill Country mahjong</strong> — south central OK private lessons:</p>
<p><a href="oklahoma-city-mahjong.html">Oklahoma City</a> · <a href="tulsa-ok-mahjong.html">Tulsa</a></p>
<p><a href="oklahoma-mahjong-hub.html">Oklahoma hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "lakes-region-nh-mahjong-hub.html",
            "Lakes Region NH Mahjong | Laconia, Wolfeboro & Meredith",
            "Lakes Region NH mahjong — Laconia, Wolfeboro, Meredith lake Winnipesaukee.",
            "lakes region new hampshire mahjong hub, laconia mah jongg",
            "Lakes Region NH Mahjong Guide",
            """<p><strong>Lakes Region NH mahjong</strong> — lake Winnipesaukee private lessons:</p>
<p><a href="laconia-nh-mahjong.html">Laconia</a> · <a href="concord-nh-mahjong.html">Concord NH</a></p>
<p><a href="new-hampshire-mahjong-hub.html">NH hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "eastern-shore-md-mahjong-hub.html",
            "Eastern Shore MD Mahjong | Easton, Cambridge & Salisbury",
            "Eastern Shore Maryland mahjong — Easton, Cambridge, Salisbury Chesapeake.",
            "eastern shore maryland mahjong hub, easton md mah jongg",
            "Eastern Shore MD Mahjong Guide",
            """<p><strong>Eastern Shore MD mahjong</strong> — Chesapeake shore private lessons:</p>
<p><a href="salisbury-md-mahjong.html">Salisbury</a> · <a href="annapolis-md-mahjong.html">Annapolis</a></p>
<p><a href="maryland-mahjong-hub.html">Maryland hub</a> · <a href="delmarva-mahjong-hub.html">Delmarva</a></p>""",
        ),
        (
            "central-illinois-mahjong-hub.html",
            "Central Illinois Mahjong | Peoria, Bloomington & Champaign",
            "Central Illinois mahjong — Peoria, Bloomington, Champaign university corridor.",
            "central illinois mahjong hub, peoria mah jongg",
            "Central Illinois Mahjong Guide",
            """<p><strong>Central Illinois mahjong</strong> — IL heartland private lessons:</p>
<p><a href="chicago-mahjong.html">Chicago</a> · <a href="springfield-il-mahjong.html">Springfield IL</a></p>
<p><a href="illinois-mahjong-hub.html">Illinois hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "coastal-oregon-south-mahjong-hub.html",
            "South Coastal OR Mahjong | Coos Bay, North Bend & Brookings",
            "South Coastal Oregon mahjong — Coos Bay, North Bend, Brookings southern coast.",
            "south coastal oregon mahjong hub, coos bay mah jongg",
            "South Coastal OR Mahjong Guide",
            """<p><strong>South Coastal OR mahjong</strong> — southern Oregon coast private lessons:</p>
<p><a href="eugene-or-mahjong.html">Eugene</a> · <a href="medford-or-mahjong.html">Medford</a></p>
<p><a href="oregon-coast-mahjong-hub.html">Oregon Coast hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE38_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("w38-fraternity-1", "Fraternity Group 1", "FG1"),
        ("w38-fraternity-2", "Fraternity Group 2", "FG2"),
        ("w38-fraternity-3", "Fraternity Group 3", "FG3"),
        ("w38-fraternity-4", "Fraternity Group 4", "FG4"),
        ("w38-fraternity-5", "Fraternity Group 5", "FG5"),
        ("w38-fraternity-6", "Fraternity Group 6", "FG6"),
        ("w38-fraternity-7", "Fraternity Group 7", "FG7"),
        ("w38-fraternity-8", "Fraternity Group 8", "FG8"),
        ("w38-fraternity-9", "Fraternity Group 9", "FG9"),
        ("w38-fraternity-10", "Fraternity Group 10", "FG10"),
        ("w38-fraternity-11", "Fraternity Group 11", "FG11"),
        ("w38-fraternity-12", "Fraternity Group 12", "FG12"),
        ("w38-fraternity-13", "Fraternity Group 13", "FG13"),
        ("w38-fraternity-14", "Fraternity Group 14", "FG14"),
        ("w38-fraternity-15", "Fraternity Group 15", "FG15"),
        ("w38-fraternity-16", "Fraternity Group 16", "FG16"),
        ("w38-fraternity-17", "Fraternity Group 17", "FG17"),
        ("w38-fraternity-18", "Fraternity Group 18", "FG18"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("w38-sorority-1", "Sorority Group 1", "SG1"),
        ("w38-sorority-2", "Sorority Group 2", "SG2"),
        ("w38-sorority-3", "Sorority Group 3", "SG3"),
        ("w38-sorority-4", "Sorority Group 4", "SG4"),
        ("w38-sorority-5", "Sorority Group 5", "SG5"),
        ("w38-sorority-6", "Sorority Group 6", "SG6"),
        ("w38-sorority-7", "Sorority Group 7", "SG7"),
        ("w38-sorority-8", "Sorority Group 8", "SG8"),
        ("w38-sorority-9", "Sorority Group 9", "SG9"),
        ("w38-sorority-10", "Sorority Group 10", "SG10"),
        ("w38-sorority-11", "Sorority Group 11", "SG11"),
        ("w38-sorority-12", "Sorority Group 12", "SG12"),
        ("w38-sorority-13", "Sorority Group 13", "SG13"),
        ("w38-sorority-14", "Sorority Group 14", "SG14"),
        ("w38-sorority-15", "Sorority Group 15", "SG15"),
        ("w38-sorority-16", "Sorority Group 16", "SG16"),
        ("w38-sorority-17", "Sorority Group 17", "SG17"),
        ("w38-sorority-18", "Sorority Group 18", "SG18"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ('w38-gathering-1', 'Gathering 1', 'w38-gathering-1 mahjong event', '<p><strong>Gathering 1</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-2', 'Gathering 2', 'w38-gathering-2 mahjong event', '<p><strong>Gathering 2</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-3', 'Gathering 3', 'w38-gathering-3 mahjong event', '<p><strong>Gathering 3</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-4', 'Gathering 4', 'w38-gathering-4 mahjong event', '<p><strong>Gathering 4</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-5', 'Gathering 5', 'w38-gathering-5 mahjong event', '<p><strong>Gathering 5</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-6', 'Gathering 6', 'w38-gathering-6 mahjong event', '<p><strong>Gathering 6</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-7', 'Gathering 7', 'w38-gathering-7 mahjong event', '<p><strong>Gathering 7</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-8', 'Gathering 8', 'w38-gathering-8 mahjong event', '<p><strong>Gathering 8</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-9', 'Gathering 9', 'w38-gathering-9 mahjong event', '<p><strong>Gathering 9</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-10', 'Gathering 10', 'w38-gathering-10 mahjong event', '<p><strong>Gathering 10</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-11', 'Gathering 11', 'w38-gathering-11 mahjong event', '<p><strong>Gathering 11</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-12', 'Gathering 12', 'w38-gathering-12 mahjong event', '<p><strong>Gathering 12</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-13', 'Gathering 13', 'w38-gathering-13 mahjong event', '<p><strong>Gathering 13</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-14', 'Gathering 14', 'w38-gathering-14 mahjong event', '<p><strong>Gathering 14</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-15', 'Gathering 15', 'w38-gathering-15 mahjong event', '<p><strong>Gathering 15</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-16', 'Gathering 16', 'w38-gathering-16 mahjong event', '<p><strong>Gathering 16</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-17', 'Gathering 17', 'w38-gathering-17 mahjong event', '<p><strong>Gathering 17</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-18', 'Gathering 18', 'w38-gathering-18 mahjong event', '<p><strong>Gathering 18</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-19', 'Gathering 19', 'w38-gathering-19 mahjong event', '<p><strong>Gathering 19</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-20', 'Gathering 20', 'w38-gathering-20 mahjong event', '<p><strong>Gathering 20</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-21', 'Gathering 21', 'w38-gathering-21 mahjong event', '<p><strong>Gathering 21</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-22', 'Gathering 22', 'w38-gathering-22 mahjong event', '<p><strong>Gathering 22</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-23', 'Gathering 23', 'w38-gathering-23 mahjong event', '<p><strong>Gathering 23</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-24', 'Gathering 24', 'w38-gathering-24 mahjong event', '<p><strong>Gathering 24</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-25', 'Gathering 25', 'w38-gathering-25 mahjong event', '<p><strong>Gathering 25</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-26', 'Gathering 26', 'w38-gathering-26 mahjong event', '<p><strong>Gathering 26</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-27', 'Gathering 27', 'w38-gathering-27 mahjong event', '<p><strong>Gathering 27</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-28', 'Gathering 28', 'w38-gathering-28 mahjong event', '<p><strong>Gathering 28</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-29', 'Gathering 29', 'w38-gathering-29 mahjong event', '<p><strong>Gathering 29</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-30', 'Gathering 30', 'w38-gathering-30 mahjong event', '<p><strong>Gathering 30</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-31', 'Gathering 31', 'w38-gathering-31 mahjong event', '<p><strong>Gathering 31</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-32', 'Gathering 32', 'w38-gathering-32 mahjong event', '<p><strong>Gathering 32</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-33', 'Gathering 33', 'w38-gathering-33 mahjong event', '<p><strong>Gathering 33</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-34', 'Gathering 34', 'w38-gathering-34 mahjong event', '<p><strong>Gathering 34</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-35', 'Gathering 35', 'w38-gathering-35 mahjong event', '<p><strong>Gathering 35</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-36', 'Gathering 36', 'w38-gathering-36 mahjong event', '<p><strong>Gathering 36</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-37', 'Gathering 37', 'w38-gathering-37 mahjong event', '<p><strong>Gathering 37</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-38', 'Gathering 38', 'w38-gathering-38 mahjong event', '<p><strong>Gathering 38</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-39', 'Gathering 39', 'w38-gathering-39 mahjong event', '<p><strong>Gathering 39</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-40', 'Gathering 40', 'w38-gathering-40 mahjong event', '<p><strong>Gathering 40</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-41', 'Gathering 41', 'w38-gathering-41 mahjong event', '<p><strong>Gathering 41</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-42', 'Gathering 42', 'w38-gathering-42 mahjong event', '<p><strong>Gathering 42</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-43', 'Gathering 43', 'w38-gathering-43 mahjong event', '<p><strong>Gathering 43</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-44', 'Gathering 44', 'w38-gathering-44 mahjong event', '<p><strong>Gathering 44</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
        ('w38-gathering-45', 'Gathering 45', 'w38-gathering-45 mahjong event', '<p><strong>Gathering 45</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ('mahjong-w38-tip-1.html', 'Tip Topic 1', 'mahjong tip 1', '<p><strong>Tip 1</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-2.html', 'Tip Topic 2', 'mahjong tip 2', '<p><strong>Tip 2</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-3.html', 'Tip Topic 3', 'mahjong tip 3', '<p><strong>Tip 3</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-4.html', 'Tip Topic 4', 'mahjong tip 4', '<p><strong>Tip 4</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-5.html', 'Tip Topic 5', 'mahjong tip 5', '<p><strong>Tip 5</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-6.html', 'Tip Topic 6', 'mahjong tip 6', '<p><strong>Tip 6</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-7.html', 'Tip Topic 7', 'mahjong tip 7', '<p><strong>Tip 7</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-8.html', 'Tip Topic 8', 'mahjong tip 8', '<p><strong>Tip 8</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-9.html', 'Tip Topic 9', 'mahjong tip 9', '<p><strong>Tip 9</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-10.html', 'Tip Topic 10', 'mahjong tip 10', '<p><strong>Tip 10</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-11.html', 'Tip Topic 11', 'mahjong tip 11', '<p><strong>Tip 11</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-12.html', 'Tip Topic 12', 'mahjong tip 12', '<p><strong>Tip 12</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-13.html', 'Tip Topic 13', 'mahjong tip 13', '<p><strong>Tip 13</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-14.html', 'Tip Topic 14', 'mahjong tip 14', '<p><strong>Tip 14</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-15.html', 'Tip Topic 15', 'mahjong tip 15', '<p><strong>Tip 15</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-16.html', 'Tip Topic 16', 'mahjong tip 16', '<p><strong>Tip 16</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-17.html', 'Tip Topic 17', 'mahjong tip 17', '<p><strong>Tip 17</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-18.html', 'Tip Topic 18', 'mahjong tip 18', '<p><strong>Tip 18</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-19.html', 'Tip Topic 19', 'mahjong tip 19', '<p><strong>Tip 19</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-20.html', 'Tip Topic 20', 'mahjong tip 20', '<p><strong>Tip 20</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-21.html', 'Tip Topic 21', 'mahjong tip 21', '<p><strong>Tip 21</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-22.html', 'Tip Topic 22', 'mahjong tip 22', '<p><strong>Tip 22</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-23.html', 'Tip Topic 23', 'mahjong tip 23', '<p><strong>Tip 23</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-24.html', 'Tip Topic 24', 'mahjong tip 24', '<p><strong>Tip 24</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-25.html', 'Tip Topic 25', 'mahjong tip 25', '<p><strong>Tip 25</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-26.html', 'Tip Topic 26', 'mahjong tip 26', '<p><strong>Tip 26</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-27.html', 'Tip Topic 27', 'mahjong tip 27', '<p><strong>Tip 27</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-28.html', 'Tip Topic 28', 'mahjong tip 28', '<p><strong>Tip 28</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-29.html', 'Tip Topic 29', 'mahjong tip 29', '<p><strong>Tip 29</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-30.html', 'Tip Topic 30', 'mahjong tip 30', '<p><strong>Tip 30</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-31.html', 'Tip Topic 31', 'mahjong tip 31', '<p><strong>Tip 31</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-32.html', 'Tip Topic 32', 'mahjong tip 32', '<p><strong>Tip 32</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-33.html', 'Tip Topic 33', 'mahjong tip 33', '<p><strong>Tip 33</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-34.html', 'Tip Topic 34', 'mahjong tip 34', '<p><strong>Tip 34</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('mahjong-w38-tip-35.html', 'Tip Topic 35', 'mahjong tip 35', '<p><strong>Tip 35</strong> — <a href="/mahjong-101.html">101</a> · <a href="/">main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
