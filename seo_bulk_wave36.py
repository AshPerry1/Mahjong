# -*- coding: utf-8 -*-
"""Mega Wave 36 — ~600+ pages (500 cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave36_cities_data import WAVE36_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_36(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "big-bend-tx-mahjong-hub.html",
            "Big Bend TX Mahjong | Alpine, Marfa & Terlingua",
            "Big Bend Texas mahjong — Alpine, Marfa, Terlingua desert mountain private events.",
            "big bend texas mahjong hub, marfa mah jongg",
            "Big Bend TX Mahjong Guide",
            """<p><strong>Big Bend mahjong</strong> — desert mountain private lessons:</p>
<p><a href="el-paso-tx-mahjong.html">El Paso</a> · <a href="austin-mahjong.html">Austin</a></p>
<p><a href="texas-mahjong-hub.html">Texas hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "permian-basin-tx-mahjong-hub.html",
            "Permian Basin TX Mahjong | Midland, Odessa & Pecos",
            "Permian Basin TX mahjong — Midland, Odessa, Pecos West Texas oil country.",
            "permian basin texas mahjong hub, midland mah jongg",
            "Permian Basin TX Mahjong Guide",
            """<p><strong>Permian Basin mahjong</strong> — West Texas private lessons:</p>
<p><a href="midland-tx-mahjong.html">Midland</a> · <a href="odessa-tx-mahjong.html">Odessa</a> · <a href="lubbock-tx-mahjong.html">Lubbock</a></p>
<p><a href="texas-mahjong-hub.html">Texas hub</a> · <a href="caprock-tx-mahjong-hub.html">Caprock</a></p>""",
        ),
        (
            "florida-panhandle-mahjong-hub.html",
            "Florida Panhandle Mahjong | Pensacola, Destin & Panama City",
            "Florida Panhandle mahjong — Pensacola, Destin, Panama City Gulf Coast.",
            "florida panhandle mahjong hub, pensacola mah jongg",
            "Florida Panhandle Mahjong Guide",
            """<p><strong>FL Panhandle mahjong</strong> — Gulf Coast private lessons:</p>
<p><a href="pensacola-fl-mahjong.html">Pensacola</a> · <a href="destin-florida-mahjong.html">Destin</a> · <a href="tallahassee-mahjong.html">Tallahassee</a></p>
<p><a href="florida-mahjong-hub.html">Florida hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "south-jersey-mahjong-hub.html",
            "South Jersey Mahjong | Cherry Hill, Cape May & Atlantic City",
            "South Jersey mahjong — Cherry Hill, Cape May, Atlantic City shore events.",
            "south jersey mahjong hub, cherry hill mah jongg",
            "South Jersey Mahjong Guide",
            """<p><strong>South Jersey mahjong</strong> — shore private lessons:</p>
<p><a href="cape-may-nj-mahjong.html">Cape May</a> · <a href="philadelphia-mahjong.html">Philadelphia</a></p>
<p><a href="new-jersey-mahjong-hub.html">NJ hub</a> · <a href="jersey-shore-mahjong-hub.html">Jersey Shore</a></p>""",
        ),
        (
            "green-mountains-vt-mahjong-hub.html",
            "Green Mountains VT Mahjong | Killington, Stowe & Manchester",
            "Green Mountains VT mahjong — Killington, Stowe, Manchester ski country.",
            "green mountains vermont mahjong hub, killington mah jongg",
            "Green Mountains VT Mahjong Guide",
            """<p><strong>Green Mountains mahjong</strong> — VT ski country private lessons:</p>
<p><a href="stowe-vt-mahjong.html">Stowe</a> · <a href="burlington-vt-mahjong.html">Burlington</a></p>
<p><a href="vermont-mahjong-hub.html">Vermont hub</a> · <a href="new-england-mahjong-hub.html">New England</a></p>""",
        ),
        (
            "santa-fe-taos-nm-mahjong-hub.html",
            "Santa Fe & Taos NM Mahjong | Art Country Private Events",
            "Santa Fe Taos NM mahjong — Santa Fe, Taos, Los Alamos art and mountain events.",
            "santa fe taos new mexico mahjong hub, santa fe mah jongg",
            "Santa Fe & Taos NM Mahjong Guide",
            """<p><strong>Santa Fe & Taos mahjong</strong> — art country private lessons:</p>
<p><a href="taos-nm-mahjong.html">Taos</a> · <a href="albuquerque-mahjong.html">Albuquerque</a></p>
<p><a href="new-mexico-mahjong-hub.html">New Mexico hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "wichita-falls-tx-mahjong-hub.html",
            "Wichita Falls TX Mahjong | Wichita Falls & Vernon",
            "Wichita Falls TX mahjong — Wichita Falls, Vernon, North Texas plains.",
            "wichita falls texas mahjong hub, wichita falls mah jongg",
            "Wichita Falls TX Mahjong Guide",
            """<p><strong>Wichita Falls mahjong</strong> — North Texas private lessons:</p>
<p><a href="wichita-falls-tx-mahjong.html">Wichita Falls</a> · <a href="dallas-mahjong.html">Dallas</a></p>
<p><a href="texas-mahjong-hub.html">Texas hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "mississippi-coast-mahjong-hub.html",
            "Mississippi Coast Mahjong | Biloxi, Gulfport & Ocean Springs",
            "Mississippi Coast mahjong — Biloxi, Gulfport, Ocean Springs Gulf private events.",
            "mississippi coast mahjong hub, biloxi mah jongg",
            "Mississippi Coast Mahjong Guide",
            """<p><strong>MS Coast mahjong</strong> — Gulf Coast private lessons:</p>
<p><a href="mobile-mahjong.html">Mobile</a> · <a href="new-orleans-mahjong.html">New Orleans</a></p>
<p><a href="mississippi-mahjong-hub.html">Mississippi hub</a> · <a href="gulf-coast-mahjong-hub.html">Gulf Coast</a></p>""",
        ),
        (
            "tri-cities-wa-mahjong-hub.html",
            "Tri-Cities WA Mahjong | Kennewick, Pasco & Richland",
            "Tri-Cities WA mahjong — Kennewick, Pasco, Richland Columbia River events.",
            "tri cities washington mahjong hub, kennewick mah jongg",
            "Tri-Cities WA Mahjong Guide",
            """<p><strong>Tri-Cities mahjong</strong> — Columbia Basin private lessons:</p>
<p><a href="spokane-wa-mahjong.html">Spokane</a> · <a href="seattle-mahjong.html">Seattle</a></p>
<p><a href="washington-mahjong-hub.html">Washington hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "heartland-ia-mahjong-hub.html",
            "Heartland IA Mahjong | Des Moines, Ames & Cedar Rapids",
            "Heartland Iowa mahjong — Des Moines, Ames, Cedar Rapids central Iowa events.",
            "heartland iowa mahjong hub, des moines mah jongg",
            "Heartland IA Mahjong Guide",
            """<p><strong>Heartland Iowa mahjong</strong> — central Iowa private lessons:</p>
<p><a href="des-moines-mahjong.html">Des Moines</a> · <a href="iowa-mahjong.html">Iowa</a></p>
<p><a href="iowa-mahjong-hub.html">Iowa hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "charleston-sc-lowcountry-mahjong-hub.html",
            "Charleston Lowcountry SC Mahjong | Mount Pleasant & Summerville",
            "Charleston Lowcountry SC mahjong — Mount Pleasant, Summerville, Daniel Island.",
            "charleston lowcountry sc mahjong hub, mount pleasant mah jongg",
            "Charleston Lowcountry SC Mahjong Guide",
            """<p><strong>Charleston Lowcountry mahjong</strong> — coastal SC private lessons:</p>
<p><a href="charleston-sc-mahjong.html">Charleston</a> · <a href="hilton-head-mahjong.html">Hilton Head</a></p>
<p><a href="lowcountry-sc-mahjong-hub.html">Lowcountry hub</a> · <a href="south-carolina-mahjong-hub.html">SC hub</a></p>""",
        ),
        (
            "peninsula-michigan-mahjong-hub.html",
            "Michigan Peninsula Mahjong | Petoskey, Charlevoix & Harbor Springs",
            "Michigan Peninsula mahjong — Petoskey, Charlevoix, Harbor Springs lake Michigan.",
            "michigan peninsula mahjong hub, harbor springs mah jongg",
            "Michigan Peninsula Mahjong Guide",
            """<p><strong>Michigan Peninsula mahjong</strong> — lake Michigan shore private lessons:</p>
<p><a href="traverse-city-mi-mahjong.html">Traverse City</a> · <a href="grand-rapids-mi-mahjong.html">Grand Rapids</a></p>
<p><a href="michigan-mahjong-hub.html">Michigan hub</a> · <a href="leelanau-peninsula-mi-mahjong-hub.html">Leelanau</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE36_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("w36-fraternity-1", "Fraternity Group 1", "FG1"),
        ("w36-fraternity-2", "Fraternity Group 2", "FG2"),
        ("w36-fraternity-3", "Fraternity Group 3", "FG3"),
        ("w36-fraternity-4", "Fraternity Group 4", "FG4"),
        ("w36-fraternity-5", "Fraternity Group 5", "FG5"),
        ("w36-fraternity-6", "Fraternity Group 6", "FG6"),
        ("w36-fraternity-7", "Fraternity Group 7", "FG7"),
        ("w36-fraternity-8", "Fraternity Group 8", "FG8"),
        ("w36-fraternity-9", "Fraternity Group 9", "FG9"),
        ("w36-fraternity-10", "Fraternity Group 10", "FG10"),
        ("w36-fraternity-11", "Fraternity Group 11", "FG11"),
        ("w36-fraternity-12", "Fraternity Group 12", "FG12"),
        ("w36-fraternity-13", "Fraternity Group 13", "FG13"),
        ("w36-fraternity-14", "Fraternity Group 14", "FG14"),
        ("w36-fraternity-15", "Fraternity Group 15", "FG15"),
        ("w36-fraternity-16", "Fraternity Group 16", "FG16"),
        ("w36-fraternity-17", "Fraternity Group 17", "FG17"),
        ("w36-fraternity-18", "Fraternity Group 18", "FG18"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("w36-sorority-1", "Sorority Group 1", "SG1"),
        ("w36-sorority-2", "Sorority Group 2", "SG2"),
        ("w36-sorority-3", "Sorority Group 3", "SG3"),
        ("w36-sorority-4", "Sorority Group 4", "SG4"),
        ("w36-sorority-5", "Sorority Group 5", "SG5"),
        ("w36-sorority-6", "Sorority Group 6", "SG6"),
        ("w36-sorority-7", "Sorority Group 7", "SG7"),
        ("w36-sorority-8", "Sorority Group 8", "SG8"),
        ("w36-sorority-9", "Sorority Group 9", "SG9"),
        ("w36-sorority-10", "Sorority Group 10", "SG10"),
        ("w36-sorority-11", "Sorority Group 11", "SG11"),
        ("w36-sorority-12", "Sorority Group 12", "SG12"),
        ("w36-sorority-13", "Sorority Group 13", "SG13"),
        ("w36-sorority-14", "Sorority Group 14", "SG14"),
        ("w36-sorority-15", "Sorority Group 15", "SG15"),
        ("w36-sorority-16", "Sorority Group 16", "SG16"),
        ("w36-sorority-17", "Sorority Group 17", "SG17"),
        ("w36-sorority-18", "Sorority Group 18", "SG18"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ('w36-social-1', 'Social Event 1', 'w36-social-1 mahjong gathering', '<p><strong>Social Event 1</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-2', 'Social Event 2', 'w36-social-2 mahjong gathering', '<p><strong>Social Event 2</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-3', 'Social Event 3', 'w36-social-3 mahjong gathering', '<p><strong>Social Event 3</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-4', 'Social Event 4', 'w36-social-4 mahjong gathering', '<p><strong>Social Event 4</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-5', 'Social Event 5', 'w36-social-5 mahjong gathering', '<p><strong>Social Event 5</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-6', 'Social Event 6', 'w36-social-6 mahjong gathering', '<p><strong>Social Event 6</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-7', 'Social Event 7', 'w36-social-7 mahjong gathering', '<p><strong>Social Event 7</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-8', 'Social Event 8', 'w36-social-8 mahjong gathering', '<p><strong>Social Event 8</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-9', 'Social Event 9', 'w36-social-9 mahjong gathering', '<p><strong>Social Event 9</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-10', 'Social Event 10', 'w36-social-10 mahjong gathering', '<p><strong>Social Event 10</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-11', 'Social Event 11', 'w36-social-11 mahjong gathering', '<p><strong>Social Event 11</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-12', 'Social Event 12', 'w36-social-12 mahjong gathering', '<p><strong>Social Event 12</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-13', 'Social Event 13', 'w36-social-13 mahjong gathering', '<p><strong>Social Event 13</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-14', 'Social Event 14', 'w36-social-14 mahjong gathering', '<p><strong>Social Event 14</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-15', 'Social Event 15', 'w36-social-15 mahjong gathering', '<p><strong>Social Event 15</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-16', 'Social Event 16', 'w36-social-16 mahjong gathering', '<p><strong>Social Event 16</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-17', 'Social Event 17', 'w36-social-17 mahjong gathering', '<p><strong>Social Event 17</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-18', 'Social Event 18', 'w36-social-18 mahjong gathering', '<p><strong>Social Event 18</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-19', 'Social Event 19', 'w36-social-19 mahjong gathering', '<p><strong>Social Event 19</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-20', 'Social Event 20', 'w36-social-20 mahjong gathering', '<p><strong>Social Event 20</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-21', 'Social Event 21', 'w36-social-21 mahjong gathering', '<p><strong>Social Event 21</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-22', 'Social Event 22', 'w36-social-22 mahjong gathering', '<p><strong>Social Event 22</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-23', 'Social Event 23', 'w36-social-23 mahjong gathering', '<p><strong>Social Event 23</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-24', 'Social Event 24', 'w36-social-24 mahjong gathering', '<p><strong>Social Event 24</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-25', 'Social Event 25', 'w36-social-25 mahjong gathering', '<p><strong>Social Event 25</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-26', 'Social Event 26', 'w36-social-26 mahjong gathering', '<p><strong>Social Event 26</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-27', 'Social Event 27', 'w36-social-27 mahjong gathering', '<p><strong>Social Event 27</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-28', 'Social Event 28', 'w36-social-28 mahjong gathering', '<p><strong>Social Event 28</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-29', 'Social Event 29', 'w36-social-29 mahjong gathering', '<p><strong>Social Event 29</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-30', 'Social Event 30', 'w36-social-30 mahjong gathering', '<p><strong>Social Event 30</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-31', 'Social Event 31', 'w36-social-31 mahjong gathering', '<p><strong>Social Event 31</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-32', 'Social Event 32', 'w36-social-32 mahjong gathering', '<p><strong>Social Event 32</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-33', 'Social Event 33', 'w36-social-33 mahjong gathering', '<p><strong>Social Event 33</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-34', 'Social Event 34', 'w36-social-34 mahjong gathering', '<p><strong>Social Event 34</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-35', 'Social Event 35', 'w36-social-35 mahjong gathering', '<p><strong>Social Event 35</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-36', 'Social Event 36', 'w36-social-36 mahjong gathering', '<p><strong>Social Event 36</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-37', 'Social Event 37', 'w36-social-37 mahjong gathering', '<p><strong>Social Event 37</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-38', 'Social Event 38', 'w36-social-38 mahjong gathering', '<p><strong>Social Event 38</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-39', 'Social Event 39', 'w36-social-39 mahjong gathering', '<p><strong>Social Event 39</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-40', 'Social Event 40', 'w36-social-40 mahjong gathering', '<p><strong>Social Event 40</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-41', 'Social Event 41', 'w36-social-41 mahjong gathering', '<p><strong>Social Event 41</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-42', 'Social Event 42', 'w36-social-42 mahjong gathering', '<p><strong>Social Event 42</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-43', 'Social Event 43', 'w36-social-43 mahjong gathering', '<p><strong>Social Event 43</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-44', 'Social Event 44', 'w36-social-44 mahjong gathering', '<p><strong>Social Event 44</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w36-social-45', 'Social Event 45', 'w36-social-45 mahjong gathering', '<p><strong>Social Event 45</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ('mahjong-w36-guide-1.html', 'Guide Topic 1', 'mahjong guide topic 1', '<p><strong>Guide 1</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-2.html', 'Guide Topic 2', 'mahjong guide topic 2', '<p><strong>Guide 2</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-3.html', 'Guide Topic 3', 'mahjong guide topic 3', '<p><strong>Guide 3</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-4.html', 'Guide Topic 4', 'mahjong guide topic 4', '<p><strong>Guide 4</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-5.html', 'Guide Topic 5', 'mahjong guide topic 5', '<p><strong>Guide 5</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-6.html', 'Guide Topic 6', 'mahjong guide topic 6', '<p><strong>Guide 6</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-7.html', 'Guide Topic 7', 'mahjong guide topic 7', '<p><strong>Guide 7</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-8.html', 'Guide Topic 8', 'mahjong guide topic 8', '<p><strong>Guide 8</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-9.html', 'Guide Topic 9', 'mahjong guide topic 9', '<p><strong>Guide 9</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-10.html', 'Guide Topic 10', 'mahjong guide topic 10', '<p><strong>Guide 10</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-11.html', 'Guide Topic 11', 'mahjong guide topic 11', '<p><strong>Guide 11</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-12.html', 'Guide Topic 12', 'mahjong guide topic 12', '<p><strong>Guide 12</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-13.html', 'Guide Topic 13', 'mahjong guide topic 13', '<p><strong>Guide 13</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-14.html', 'Guide Topic 14', 'mahjong guide topic 14', '<p><strong>Guide 14</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-15.html', 'Guide Topic 15', 'mahjong guide topic 15', '<p><strong>Guide 15</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-16.html', 'Guide Topic 16', 'mahjong guide topic 16', '<p><strong>Guide 16</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-17.html', 'Guide Topic 17', 'mahjong guide topic 17', '<p><strong>Guide 17</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-18.html', 'Guide Topic 18', 'mahjong guide topic 18', '<p><strong>Guide 18</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-19.html', 'Guide Topic 19', 'mahjong guide topic 19', '<p><strong>Guide 19</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-20.html', 'Guide Topic 20', 'mahjong guide topic 20', '<p><strong>Guide 20</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-21.html', 'Guide Topic 21', 'mahjong guide topic 21', '<p><strong>Guide 21</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-22.html', 'Guide Topic 22', 'mahjong guide topic 22', '<p><strong>Guide 22</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-23.html', 'Guide Topic 23', 'mahjong guide topic 23', '<p><strong>Guide 23</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-24.html', 'Guide Topic 24', 'mahjong guide topic 24', '<p><strong>Guide 24</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-25.html', 'Guide Topic 25', 'mahjong guide topic 25', '<p><strong>Guide 25</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-26.html', 'Guide Topic 26', 'mahjong guide topic 26', '<p><strong>Guide 26</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-27.html', 'Guide Topic 27', 'mahjong guide topic 27', '<p><strong>Guide 27</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-28.html', 'Guide Topic 28', 'mahjong guide topic 28', '<p><strong>Guide 28</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-29.html', 'Guide Topic 29', 'mahjong guide topic 29', '<p><strong>Guide 29</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-30.html', 'Guide Topic 30', 'mahjong guide topic 30', '<p><strong>Guide 30</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-31.html', 'Guide Topic 31', 'mahjong guide topic 31', '<p><strong>Guide 31</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-32.html', 'Guide Topic 32', 'mahjong guide topic 32', '<p><strong>Guide 32</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-33.html', 'Guide Topic 33', 'mahjong guide topic 33', '<p><strong>Guide 33</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-34.html', 'Guide Topic 34', 'mahjong guide topic 34', '<p><strong>Guide 34</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w36-guide-35.html', 'Guide Topic 35', 'mahjong guide topic 35', '<p><strong>Guide 35</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
