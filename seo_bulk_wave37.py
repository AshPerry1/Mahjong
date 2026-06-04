# -*- coding: utf-8 -*-
"""Mega Wave 37 — ~600+ pages (500 cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave37_cities_data import WAVE37_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_37(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "snake-river-id-mahjong-hub.html",
            "Snake River ID Mahjong | Twin Falls, Idaho Falls & Pocatello",
            "Snake River Idaho mahjong — Twin Falls, Idaho Falls, Pocatello corridor.",
            "snake river idaho mahjong hub, twin falls mah jongg",
            "Snake River ID Mahjong Guide",
            """<p><strong>Snake River mahjong</strong> — southern Idaho private lessons:</p>
<p><a href="twin-falls-id-mahjong.html">Twin Falls</a> · <a href="pocatello-id-mahjong.html">Pocatello</a> · <a href="boise-city-id-mahjong.html">Boise</a></p>
<p><a href="idaho-mahjong-hub.html">Idaho hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "bighorn-basin-wy-mahjong-hub.html",
            "Bighorn Basin WY Mahjong | Cody, Sheridan & Buffalo",
            "Bighorn Basin Wyoming mahjong — Cody, Sheridan, Buffalo mountain basin.",
            "bighorn basin wyoming mahjong hub, cody wy mah jongg",
            "Bighorn Basin WY Mahjong Guide",
            """<p><strong>Bighorn Basin mahjong</strong> — Wyoming basin private lessons:</p>
<p><a href="cody-wy-mahjong.html">Cody</a> · <a href="sheridan-wy-mahjong.html">Sheridan</a> · <a href="cheyenne-wy-mahjong.html">Cheyenne</a></p>
<p><a href="wyoming-mahjong-hub.html">Wyoming hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "badlands-sd-mahjong-hub.html",
            "Badlands SD Mahjong | Rapid City, Spearfish & Deadwood",
            "Badlands SD mahjong — Rapid City, Spearfish, Deadwood Black Hills region.",
            "badlands south dakota mahjong hub, rapid city mah jongg",
            "Badlands SD Mahjong Guide",
            """<p><strong>Badlands SD mahjong</strong> — Black Hills gateway private lessons:</p>
<p><a href="rapid-city-sd-mahjong.html">Rapid City</a> · <a href="sioux-falls-sd-mahjong.html">Sioux Falls</a></p>
<p><a href="south-dakota-mahjong-hub.html">SD hub</a> · <a href="black-hills-mahjong-hub.html">Black Hills</a></p>""",
        ),
        (
            "tri-state-oh-ky-wv-mahjong-hub.html",
            "Tri-State OH KY WV Mahjong | Cincinnati, Covington & Huntington",
            "Tri-State OH KY WV mahjong — Cincinnati, Covington, Huntington river metro.",
            "tri state oh ky wv mahjong hub, cincinnati mah jongg",
            "Tri-State OH KY WV Mahjong Guide",
            """<p><strong>Tri-State mahjong</strong> — Ohio River metro private lessons:</p>
<p><a href="cincinnati-oh-mahjong.html">Cincinnati</a> · <a href="lexington-ky-mahjong.html">Lexington</a> · <a href="louisville-mahjong.html">Louisville</a></p>
<p><a href="ohio-mahjong-hub.html">Ohio hub</a> · <a href="kentucky-mahjong-hub.html">Kentucky hub</a></p>""",
        ),
        (
            "pine-barrens-nj-mahjong-hub.html",
            "Pine Barrens NJ Mahjong | Toms River, Hammonton & Vineland",
            "Pine Barrens NJ mahjong — Toms River, Hammonton, Vineland South Jersey interior.",
            "pine barrens new jersey mahjong hub, toms river mah jongg",
            "Pine Barrens NJ Mahjong Guide",
            """<p><strong>Pine Barrens mahjong</strong> — South Jersey private lessons:</p>
<p><a href="atlantic-city-nj-mahjong.html">Atlantic City</a> · <a href="trenton-nj-mahjong.html">Trenton</a></p>
<p><a href="new-jersey-mahjong-hub.html">NJ hub</a> · <a href="south-jersey-mahjong-hub.html">South Jersey</a></p>""",
        ),
        (
            "savannah-river-region-mahjong-hub.html",
            "Savannah River Region Mahjong | Augusta & Aiken",
            "Savannah River region mahjong — Augusta, Aiken GA-SC border events.",
            "savannah river region mahjong hub, augusta mah jongg",
            "Savannah River Region Mahjong Guide",
            """<p><strong>Savannah River region mahjong</strong> — border private lessons:</p>
<p><a href="augusta-ga-mahjong.html">Augusta</a> · <a href="aiken-sc-mahjong.html">Aiken</a> · <a href="savannah-mahjong.html">Savannah</a></p>
<p><a href="georgia-mahjong-hub.html">Georgia hub</a> · <a href="south-carolina-mahjong-hub.html">SC hub</a></p>""",
        ),
        (
            "arrowhead-mn-mahjong-hub.html",
            "Arrowhead MN Mahjong | Duluth, Grand Marais & Ely",
            "Arrowhead Minnesota mahjong — Duluth, Grand Marais, Ely North Shore lake.",
            "arrowhead minnesota mahjong hub, duluth mah jongg",
            "Arrowhead MN Mahjong Guide",
            """<p><strong>Arrowhead MN mahjong</strong> — North Shore private lessons:</p>
<p><a href="duluth-mn-mahjong.html">Duluth</a> · <a href="minneapolis-mahjong.html">Minneapolis</a></p>
<p><a href="minnesota-mahjong-hub.html">Minnesota hub</a> · <a href="great-lakes-mahjong-hub.html">Great Lakes</a></p>""",
        ),
        (
            "florida-heartland-mahjong-hub.html",
            "Florida Heartland Mahjong | Sebring, Lake Placid & Arcadia",
            "Florida Heartland mahjong — Sebring, Lake Placid, Arcadia central FL inland.",
            "florida heartland mahjong hub, sebring mah jongg",
            "Florida Heartland Mahjong Guide",
            """<p><strong>FL Heartland mahjong</strong> — inland Florida private lessons:</p>
<p><a href="lakeland-fl-mahjong.html">Lakeland</a> · <a href="orlando-mahjong.html">Orlando</a></p>
<p><a href="florida-mahjong-hub.html">Florida hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "pennsylvania-dutch-mahjong-hub.html",
            "Pennsylvania Dutch Mahjong | Lancaster, Hershey & York",
            "Pennsylvania Dutch mahjong — Lancaster, Hershey, York Amish country events.",
            "pennsylvania dutch mahjong hub, lancaster mah jongg",
            "Pennsylvania Dutch Mahjong Guide",
            """<p><strong>PA Dutch country mahjong</strong> — Lancaster corridor private lessons:</p>
<p><a href="harrisburg-pa-mahjong.html">Harrisburg</a> · <a href="philadelphia-mahjong.html">Philadelphia</a></p>
<p><a href="pennsylvania-mahjong-hub.html">Pennsylvania hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "ozark-plateau-ar-mahjong-hub.html",
            "Ozark Plateau AR Mahjong | Harrison & Mountain Home",
            "Ozark Plateau Arkansas mahjong — Harrison, Mountain Home, Batesville hills.",
            "ozark plateau arkansas mahjong hub, harrison ar mah jongg",
            "Ozark Plateau AR Mahjong Guide",
            """<p><strong>Ozark Plateau mahjong</strong> — AR hills private lessons:</p>
<p><a href="fayetteville-ar-mahjong.html">Fayetteville</a> · <a href="little-rock-ar-mahjong.html">Little Rock</a></p>
<p><a href="arkansas-mahjong-hub.html">Arkansas hub</a> · <a href="ozarks-mahjong-hub.html">Ozarks</a></p>""",
        ),
        (
            "columbia-gorge-east-mahjong-hub.html",
            "Columbia Gorge East Mahjong | Hood River & The Dalles",
            "Columbia Gorge East mahjong — Hood River, The Dalles windsurfing gorge.",
            "columbia gorge east mahjong hub, hood river mah jongg",
            "Columbia Gorge East Mahjong Guide",
            """<p><strong>Columbia Gorge East mahjong</strong> — gorge private lessons:</p>
<p><a href="hood-river-or-mahjong.html">Hood River</a> · <a href="portland-mahjong.html">Portland</a></p>
<p><a href="columbia-river-gorge-mahjong-hub.html">Gorge hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "sun-coast-al-mahjong-hub.html",
            "Sun Coast AL Mahjong | Fairhope, Daphne & Gulf Shores",
            "Sun Coast Alabama mahjong — Fairhope, Daphne, Gulf Shores eastern shore.",
            "sun coast alabama mahjong hub, fairhope mah jongg",
            "Sun Coast AL Mahjong Guide",
            """<p><strong>Sun Coast AL mahjong</strong> — eastern shore private lessons:</p>
<p><a href="gulf-shores-al-mahjong.html">Gulf Shores</a> · <a href="mobile-mahjong.html">Mobile</a></p>
<p><a href="alabama-gulf-coast-mahjong-hub.html">AL Gulf Coast</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE37_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("w37-fraternity-1", "Fraternity Group 1", "FG1"),
        ("w37-fraternity-2", "Fraternity Group 2", "FG2"),
        ("w37-fraternity-3", "Fraternity Group 3", "FG3"),
        ("w37-fraternity-4", "Fraternity Group 4", "FG4"),
        ("w37-fraternity-5", "Fraternity Group 5", "FG5"),
        ("w37-fraternity-6", "Fraternity Group 6", "FG6"),
        ("w37-fraternity-7", "Fraternity Group 7", "FG7"),
        ("w37-fraternity-8", "Fraternity Group 8", "FG8"),
        ("w37-fraternity-9", "Fraternity Group 9", "FG9"),
        ("w37-fraternity-10", "Fraternity Group 10", "FG10"),
        ("w37-fraternity-11", "Fraternity Group 11", "FG11"),
        ("w37-fraternity-12", "Fraternity Group 12", "FG12"),
        ("w37-fraternity-13", "Fraternity Group 13", "FG13"),
        ("w37-fraternity-14", "Fraternity Group 14", "FG14"),
        ("w37-fraternity-15", "Fraternity Group 15", "FG15"),
        ("w37-fraternity-16", "Fraternity Group 16", "FG16"),
        ("w37-fraternity-17", "Fraternity Group 17", "FG17"),
        ("w37-fraternity-18", "Fraternity Group 18", "FG18"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("w37-sorority-1", "Sorority Group 1", "SG1"),
        ("w37-sorority-2", "Sorority Group 2", "SG2"),
        ("w37-sorority-3", "Sorority Group 3", "SG3"),
        ("w37-sorority-4", "Sorority Group 4", "SG4"),
        ("w37-sorority-5", "Sorority Group 5", "SG5"),
        ("w37-sorority-6", "Sorority Group 6", "SG6"),
        ("w37-sorority-7", "Sorority Group 7", "SG7"),
        ("w37-sorority-8", "Sorority Group 8", "SG8"),
        ("w37-sorority-9", "Sorority Group 9", "SG9"),
        ("w37-sorority-10", "Sorority Group 10", "SG10"),
        ("w37-sorority-11", "Sorority Group 11", "SG11"),
        ("w37-sorority-12", "Sorority Group 12", "SG12"),
        ("w37-sorority-13", "Sorority Group 13", "SG13"),
        ("w37-sorority-14", "Sorority Group 14", "SG14"),
        ("w37-sorority-15", "Sorority Group 15", "SG15"),
        ("w37-sorority-16", "Sorority Group 16", "SG16"),
        ("w37-sorority-17", "Sorority Group 17", "SG17"),
        ("w37-sorority-18", "Sorority Group 18", "SG18"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ('w37-social-1', 'Social Event 1', 'w37-social-1 mahjong gathering', '<p><strong>Social Event 1</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-2', 'Social Event 2', 'w37-social-2 mahjong gathering', '<p><strong>Social Event 2</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-3', 'Social Event 3', 'w37-social-3 mahjong gathering', '<p><strong>Social Event 3</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-4', 'Social Event 4', 'w37-social-4 mahjong gathering', '<p><strong>Social Event 4</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-5', 'Social Event 5', 'w37-social-5 mahjong gathering', '<p><strong>Social Event 5</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-6', 'Social Event 6', 'w37-social-6 mahjong gathering', '<p><strong>Social Event 6</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-7', 'Social Event 7', 'w37-social-7 mahjong gathering', '<p><strong>Social Event 7</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-8', 'Social Event 8', 'w37-social-8 mahjong gathering', '<p><strong>Social Event 8</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-9', 'Social Event 9', 'w37-social-9 mahjong gathering', '<p><strong>Social Event 9</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-10', 'Social Event 10', 'w37-social-10 mahjong gathering', '<p><strong>Social Event 10</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-11', 'Social Event 11', 'w37-social-11 mahjong gathering', '<p><strong>Social Event 11</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-12', 'Social Event 12', 'w37-social-12 mahjong gathering', '<p><strong>Social Event 12</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-13', 'Social Event 13', 'w37-social-13 mahjong gathering', '<p><strong>Social Event 13</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-14', 'Social Event 14', 'w37-social-14 mahjong gathering', '<p><strong>Social Event 14</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-15', 'Social Event 15', 'w37-social-15 mahjong gathering', '<p><strong>Social Event 15</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-16', 'Social Event 16', 'w37-social-16 mahjong gathering', '<p><strong>Social Event 16</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-17', 'Social Event 17', 'w37-social-17 mahjong gathering', '<p><strong>Social Event 17</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-18', 'Social Event 18', 'w37-social-18 mahjong gathering', '<p><strong>Social Event 18</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-19', 'Social Event 19', 'w37-social-19 mahjong gathering', '<p><strong>Social Event 19</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-20', 'Social Event 20', 'w37-social-20 mahjong gathering', '<p><strong>Social Event 20</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-21', 'Social Event 21', 'w37-social-21 mahjong gathering', '<p><strong>Social Event 21</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-22', 'Social Event 22', 'w37-social-22 mahjong gathering', '<p><strong>Social Event 22</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-23', 'Social Event 23', 'w37-social-23 mahjong gathering', '<p><strong>Social Event 23</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-24', 'Social Event 24', 'w37-social-24 mahjong gathering', '<p><strong>Social Event 24</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-25', 'Social Event 25', 'w37-social-25 mahjong gathering', '<p><strong>Social Event 25</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-26', 'Social Event 26', 'w37-social-26 mahjong gathering', '<p><strong>Social Event 26</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-27', 'Social Event 27', 'w37-social-27 mahjong gathering', '<p><strong>Social Event 27</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-28', 'Social Event 28', 'w37-social-28 mahjong gathering', '<p><strong>Social Event 28</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-29', 'Social Event 29', 'w37-social-29 mahjong gathering', '<p><strong>Social Event 29</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-30', 'Social Event 30', 'w37-social-30 mahjong gathering', '<p><strong>Social Event 30</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-31', 'Social Event 31', 'w37-social-31 mahjong gathering', '<p><strong>Social Event 31</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-32', 'Social Event 32', 'w37-social-32 mahjong gathering', '<p><strong>Social Event 32</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-33', 'Social Event 33', 'w37-social-33 mahjong gathering', '<p><strong>Social Event 33</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-34', 'Social Event 34', 'w37-social-34 mahjong gathering', '<p><strong>Social Event 34</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-35', 'Social Event 35', 'w37-social-35 mahjong gathering', '<p><strong>Social Event 35</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-36', 'Social Event 36', 'w37-social-36 mahjong gathering', '<p><strong>Social Event 36</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-37', 'Social Event 37', 'w37-social-37 mahjong gathering', '<p><strong>Social Event 37</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-38', 'Social Event 38', 'w37-social-38 mahjong gathering', '<p><strong>Social Event 38</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-39', 'Social Event 39', 'w37-social-39 mahjong gathering', '<p><strong>Social Event 39</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-40', 'Social Event 40', 'w37-social-40 mahjong gathering', '<p><strong>Social Event 40</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-41', 'Social Event 41', 'w37-social-41 mahjong gathering', '<p><strong>Social Event 41</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-42', 'Social Event 42', 'w37-social-42 mahjong gathering', '<p><strong>Social Event 42</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-43', 'Social Event 43', 'w37-social-43 mahjong gathering', '<p><strong>Social Event 43</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-44', 'Social Event 44', 'w37-social-44 mahjong gathering', '<p><strong>Social Event 44</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w37-social-45', 'Social Event 45', 'w37-social-45 mahjong gathering', '<p><strong>Social Event 45</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ('mahjong-w37-guide-1.html', 'Guide Topic 1', 'mahjong guide topic 1', '<p><strong>Guide 1</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-2.html', 'Guide Topic 2', 'mahjong guide topic 2', '<p><strong>Guide 2</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-3.html', 'Guide Topic 3', 'mahjong guide topic 3', '<p><strong>Guide 3</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-4.html', 'Guide Topic 4', 'mahjong guide topic 4', '<p><strong>Guide 4</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-5.html', 'Guide Topic 5', 'mahjong guide topic 5', '<p><strong>Guide 5</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-6.html', 'Guide Topic 6', 'mahjong guide topic 6', '<p><strong>Guide 6</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-7.html', 'Guide Topic 7', 'mahjong guide topic 7', '<p><strong>Guide 7</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-8.html', 'Guide Topic 8', 'mahjong guide topic 8', '<p><strong>Guide 8</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-9.html', 'Guide Topic 9', 'mahjong guide topic 9', '<p><strong>Guide 9</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-10.html', 'Guide Topic 10', 'mahjong guide topic 10', '<p><strong>Guide 10</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-11.html', 'Guide Topic 11', 'mahjong guide topic 11', '<p><strong>Guide 11</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-12.html', 'Guide Topic 12', 'mahjong guide topic 12', '<p><strong>Guide 12</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-13.html', 'Guide Topic 13', 'mahjong guide topic 13', '<p><strong>Guide 13</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-14.html', 'Guide Topic 14', 'mahjong guide topic 14', '<p><strong>Guide 14</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-15.html', 'Guide Topic 15', 'mahjong guide topic 15', '<p><strong>Guide 15</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-16.html', 'Guide Topic 16', 'mahjong guide topic 16', '<p><strong>Guide 16</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-17.html', 'Guide Topic 17', 'mahjong guide topic 17', '<p><strong>Guide 17</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-18.html', 'Guide Topic 18', 'mahjong guide topic 18', '<p><strong>Guide 18</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-19.html', 'Guide Topic 19', 'mahjong guide topic 19', '<p><strong>Guide 19</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-20.html', 'Guide Topic 20', 'mahjong guide topic 20', '<p><strong>Guide 20</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-21.html', 'Guide Topic 21', 'mahjong guide topic 21', '<p><strong>Guide 21</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-22.html', 'Guide Topic 22', 'mahjong guide topic 22', '<p><strong>Guide 22</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-23.html', 'Guide Topic 23', 'mahjong guide topic 23', '<p><strong>Guide 23</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-24.html', 'Guide Topic 24', 'mahjong guide topic 24', '<p><strong>Guide 24</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-25.html', 'Guide Topic 25', 'mahjong guide topic 25', '<p><strong>Guide 25</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-26.html', 'Guide Topic 26', 'mahjong guide topic 26', '<p><strong>Guide 26</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-27.html', 'Guide Topic 27', 'mahjong guide topic 27', '<p><strong>Guide 27</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-28.html', 'Guide Topic 28', 'mahjong guide topic 28', '<p><strong>Guide 28</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-29.html', 'Guide Topic 29', 'mahjong guide topic 29', '<p><strong>Guide 29</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-30.html', 'Guide Topic 30', 'mahjong guide topic 30', '<p><strong>Guide 30</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-31.html', 'Guide Topic 31', 'mahjong guide topic 31', '<p><strong>Guide 31</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-32.html', 'Guide Topic 32', 'mahjong guide topic 32', '<p><strong>Guide 32</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-33.html', 'Guide Topic 33', 'mahjong guide topic 33', '<p><strong>Guide 33</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-34.html', 'Guide Topic 34', 'mahjong guide topic 34', '<p><strong>Guide 34</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w37-guide-35.html', 'Guide Topic 35', 'mahjong guide topic 35', '<p><strong>Guide 35</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
