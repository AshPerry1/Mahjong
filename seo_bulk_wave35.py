# -*- coding: utf-8 -*-
"""Mega Wave 35 — ~600+ pages (500 cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave35_cities_data import WAVE35_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_35(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "yuma-mohave-az-mahjong-hub.html",
            "Yuma & Mohave AZ Mahjong | Yuma, Lake Havasu & Kingman",
            "Yuma Mohave AZ mahjong — Yuma, Lake Havasu City, Kingman desert private events.",
            "yuma mohave arizona mahjong hub, lake havasu mah jongg",
            "Yuma & Mohave AZ Mahjong Guide",
            """<p><strong>Yuma & Mohave mahjong</strong> — desert private lessons:</p>
<p><a href="yuma-az-mahjong.html">Yuma</a> · <a href="phoenix-mahjong.html">Phoenix</a> · <a href="sedona-az-mahjong.html">Sedona</a></p>
<p><a href="arizona-mahjong-hub.html">Arizona hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "southern-oregon-mahjong-hub.html",
            "Southern Oregon Mahjong | Medford, Ashland & Grants Pass",
            "Southern Oregon mahjong — Medford, Ashland, Grants Pass Rogue Valley events.",
            "southern oregon mahjong hub, medford mah jongg",
            "Southern Oregon Mahjong Guide",
            """<p><strong>Southern Oregon mahjong</strong> — Rogue Valley private lessons:</p>
<p><a href="medford-or-mahjong.html">Medford</a> · <a href="ashland-or-mahjong.html">Ashland</a> · <a href="eugene-or-mahjong.html">Eugene</a></p>
<p><a href="oregon-mahjong-hub.html">Oregon hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "nebraska-sandhills-mahjong-hub.html",
            "Nebraska Sandhills Mahjong | North Platte & Valentine",
            "Nebraska Sandhills mahjong — North Platte, Valentine sandhills ranch country.",
            "nebraska sandhills mahjong hub, north platte mah jongg",
            "Nebraska Sandhills Mahjong Guide",
            """<p><strong>Nebraska Sandhills mahjong</strong> — High Plains private lessons:</p>
<p><a href="north-platte-ne-mahjong.html">North Platte</a> · <a href="omaha-ne-mahjong.html">Omaha</a> · <a href="lincoln-ne-mahjong.html">Lincoln</a></p>
<p><a href="nebraska-mahjong-hub.html">Nebraska hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "blue-ridge-parkway-va-mahjong-hub.html",
            "Blue Ridge Parkway VA Mahjong | Roanoke, Lexington & Staunton",
            "Blue Ridge Parkway VA mahjong — Roanoke, Lexington, Staunton mountain corridor.",
            "blue ridge parkway virginia mahjong hub, roanoke mah jongg",
            "Blue Ridge Parkway VA Mahjong Guide",
            """<p><strong>Blue Ridge Parkway mahjong</strong> — mountain corridor private lessons:</p>
<p><a href="roanoke-va-mahjong.html">Roanoke</a> · <a href="charlottesville-va-mahjong.html">Charlottesville</a> · <a href="richmond-mahjong.html">Richmond</a></p>
<p><a href="virginia-mahjong-hub.html">Virginia hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "southeast-missouri-mahjong-hub.html",
            "Southeast Missouri Mahjong | Cape Girardeau & Poplar Bluff",
            "Southeast Missouri mahjong — Cape Girardeau, Poplar Bluff, Ozark foothills.",
            "southeast missouri mahjong hub, cape girardeau mah jongg",
            "Southeast Missouri Mahjong Guide",
            """<p><strong>Southeast Missouri mahjong</strong> — Bootheel region private lessons:</p>
<p><a href="st-louis-mahjong.html">St. Louis</a> · <a href="springfield-mo-mahjong.html">Springfield MO</a></p>
<p><a href="missouri-mahjong-hub.html">Missouri hub</a> · <a href="ozarks-mahjong-hub.html">Ozarks</a></p>""",
        ),
        (
            "northwest-arkansas-mahjong-hub.html",
            "Northwest Arkansas Mahjong | Fayetteville, Bentonville & Rogers",
            "Northwest Arkansas mahjong — Fayetteville, Bentonville, Rogers Ozarks metro.",
            "northwest arkansas mahjong hub, bentonville mah jongg",
            "Northwest Arkansas Mahjong Guide",
            """<p><strong>NW Arkansas mahjong</strong> — Ozarks metro private lessons:</p>
<p><a href="fayetteville-ar-mahjong.html">Fayetteville</a> · <a href="bentonville-ar-mahjong.html">Bentonville</a> · <a href="rogers-ar-mahjong.html">Rogers</a></p>
<p><a href="arkansas-mahjong-hub.html">Arkansas hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "central-valley-ca-mahjong-hub.html",
            "Central Valley CA Mahjong | Fresno, Bakersfield & Modesto",
            "Central Valley California mahjong — Fresno, Bakersfield, Modesto agricultural valley.",
            "central valley california mahjong hub, fresno mah jongg",
            "Central Valley CA Mahjong Guide",
            """<p><strong>Central Valley mahjong</strong> — valley private lessons:</p>
<p><a href="fresno-ca-mahjong.html">Fresno</a> · <a href="bakersfield-ca-mahjong.html">Bakersfield</a> · <a href="modesto-ca-mahjong.html">Modesto</a></p>
<p><a href="california-mahjong-hub.html">California hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "long-island-sound-ct-mahjong-hub.html",
            "Long Island Sound CT Mahjong | New Haven, Milford & Guilford",
            "Long Island Sound CT mahjong — New Haven, Milford, Guilford shoreline events.",
            "long island sound connecticut mahjong hub, new haven mah jongg",
            "Long Island Sound CT Mahjong Guide",
            """<p><strong>Long Island Sound CT mahjong</strong> — shoreline private lessons:</p>
<p><a href="hartford-ct-mahjong.html">Hartford</a> · <a href="greenwich-ct-mahjong.html">Greenwich</a></p>
<p><a href="connecticut-mahjong-hub.html">Connecticut hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "smoky-foothills-tn-mahjong-hub.html",
            "Smoky Foothills TN Mahjong | Maryville, Townsend & Sevierville",
            "Smoky Foothills TN mahjong — Maryville, Townsend, Sevierville gateway towns.",
            "smoky foothills tennessee mahjong hub, maryville mah jongg",
            "Smoky Foothills TN Mahjong Guide",
            """<p><strong>Smoky Foothills mahjong</strong> — gateway town private lessons:</p>
<p><a href="maryville-tn-mahjong.html">Maryville</a> · <a href="gatlinburg-tn-mahjong.html">Gatlinburg</a> · <a href="knoxville-mahjong.html">Knoxville</a></p>
<p><a href="smoky-mountains-mahjong-hub.html">Smokies hub</a> · <a href="tennessee-mahjong-hub.html">Tennessee hub</a></p>""",
        ),
        (
            "cape-fear-coast-nc-mahjong-hub.html",
            "Cape Fear Coast NC Mahjong | Wilmington & Carolina Beach",
            "Cape Fear Coast NC mahjong — Wilmington, Carolina Beach coast.",
            "cape fear coast north carolina mahjong hub, wilmington mah jongg",
            "Cape Fear Coast NC Mahjong Guide",
            """<p><strong>Cape Fear Coast mahjong</strong> — coastal NC private lessons:</p>
<p><a href="wilmington-nc-mahjong.html">Wilmington</a> · <a href="raleigh-mahjong.html">Raleigh</a></p>
<p><a href="north-carolina-mahjong-hub.html">NC hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "southwest-georgia-mahjong-hub.html",
            "Southwest Georgia Mahjong | Thomasville & Albany GA",
            "Southwest Georgia mahjong — Thomasville, Albany plantation country.",
            "southwest georgia mahjong hub, thomasville mah jongg",
            "Southwest Georgia Mahjong Guide",
            """<p><strong>SW Georgia mahjong</strong> — plantation country private lessons:</p>
<p><a href="albany-ga-mahjong.html">Albany GA</a> · <a href="atlanta-mahjong.html">Atlanta</a></p>
<p><a href="georgia-mahjong-hub.html">Georgia hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "northwoods-wi-mahjong-hub.html",
            "Northwoods WI Mahjong | Minocqua, Eagle River & Rhinelander",
            "Northwoods Wisconsin mahjong — Minocqua, Eagle River, Rhinelander lake country.",
            "northwoods wisconsin mahjong hub, minocqua mah jongg",
            "Northwoods WI Mahjong Guide",
            """<p><strong>Northwoods mahjong</strong> — lake country private lessons:</p>
<p><a href="madison-wi-mahjong.html">Madison</a> · <a href="milwaukee-wi-mahjong.html">Milwaukee</a></p>
<p><a href="wisconsin-mahjong-hub.html">Wisconsin hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE35_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("w35-fraternity-1", "Fraternity Group 1", "FG1"),
        ("w35-fraternity-2", "Fraternity Group 2", "FG2"),
        ("w35-fraternity-3", "Fraternity Group 3", "FG3"),
        ("w35-fraternity-4", "Fraternity Group 4", "FG4"),
        ("w35-fraternity-5", "Fraternity Group 5", "FG5"),
        ("w35-fraternity-6", "Fraternity Group 6", "FG6"),
        ("w35-fraternity-7", "Fraternity Group 7", "FG7"),
        ("w35-fraternity-8", "Fraternity Group 8", "FG8"),
        ("w35-fraternity-9", "Fraternity Group 9", "FG9"),
        ("w35-fraternity-10", "Fraternity Group 10", "FG10"),
        ("w35-fraternity-11", "Fraternity Group 11", "FG11"),
        ("w35-fraternity-12", "Fraternity Group 12", "FG12"),
        ("w35-fraternity-13", "Fraternity Group 13", "FG13"),
        ("w35-fraternity-14", "Fraternity Group 14", "FG14"),
        ("w35-fraternity-15", "Fraternity Group 15", "FG15"),
        ("w35-fraternity-16", "Fraternity Group 16", "FG16"),
        ("w35-fraternity-17", "Fraternity Group 17", "FG17"),
        ("w35-fraternity-18", "Fraternity Group 18", "FG18"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("w35-sorority-1", "Sorority Group 1", "SG1"),
        ("w35-sorority-2", "Sorority Group 2", "SG2"),
        ("w35-sorority-3", "Sorority Group 3", "SG3"),
        ("w35-sorority-4", "Sorority Group 4", "SG4"),
        ("w35-sorority-5", "Sorority Group 5", "SG5"),
        ("w35-sorority-6", "Sorority Group 6", "SG6"),
        ("w35-sorority-7", "Sorority Group 7", "SG7"),
        ("w35-sorority-8", "Sorority Group 8", "SG8"),
        ("w35-sorority-9", "Sorority Group 9", "SG9"),
        ("w35-sorority-10", "Sorority Group 10", "SG10"),
        ("w35-sorority-11", "Sorority Group 11", "SG11"),
        ("w35-sorority-12", "Sorority Group 12", "SG12"),
        ("w35-sorority-13", "Sorority Group 13", "SG13"),
        ("w35-sorority-14", "Sorority Group 14", "SG14"),
        ("w35-sorority-15", "Sorority Group 15", "SG15"),
        ("w35-sorority-16", "Sorority Group 16", "SG16"),
        ("w35-sorority-17", "Sorority Group 17", "SG17"),
        ("w35-sorority-18", "Sorority Group 18", "SG18"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ('w35-social-1', 'Social Event 1', 'w35-social-1 mahjong gathering', '<p><strong>Social Event 1</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-2', 'Social Event 2', 'w35-social-2 mahjong gathering', '<p><strong>Social Event 2</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-3', 'Social Event 3', 'w35-social-3 mahjong gathering', '<p><strong>Social Event 3</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-4', 'Social Event 4', 'w35-social-4 mahjong gathering', '<p><strong>Social Event 4</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-5', 'Social Event 5', 'w35-social-5 mahjong gathering', '<p><strong>Social Event 5</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-6', 'Social Event 6', 'w35-social-6 mahjong gathering', '<p><strong>Social Event 6</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-7', 'Social Event 7', 'w35-social-7 mahjong gathering', '<p><strong>Social Event 7</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-8', 'Social Event 8', 'w35-social-8 mahjong gathering', '<p><strong>Social Event 8</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-9', 'Social Event 9', 'w35-social-9 mahjong gathering', '<p><strong>Social Event 9</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-10', 'Social Event 10', 'w35-social-10 mahjong gathering', '<p><strong>Social Event 10</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-11', 'Social Event 11', 'w35-social-11 mahjong gathering', '<p><strong>Social Event 11</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-12', 'Social Event 12', 'w35-social-12 mahjong gathering', '<p><strong>Social Event 12</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-13', 'Social Event 13', 'w35-social-13 mahjong gathering', '<p><strong>Social Event 13</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-14', 'Social Event 14', 'w35-social-14 mahjong gathering', '<p><strong>Social Event 14</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-15', 'Social Event 15', 'w35-social-15 mahjong gathering', '<p><strong>Social Event 15</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-16', 'Social Event 16', 'w35-social-16 mahjong gathering', '<p><strong>Social Event 16</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-17', 'Social Event 17', 'w35-social-17 mahjong gathering', '<p><strong>Social Event 17</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-18', 'Social Event 18', 'w35-social-18 mahjong gathering', '<p><strong>Social Event 18</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-19', 'Social Event 19', 'w35-social-19 mahjong gathering', '<p><strong>Social Event 19</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-20', 'Social Event 20', 'w35-social-20 mahjong gathering', '<p><strong>Social Event 20</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-21', 'Social Event 21', 'w35-social-21 mahjong gathering', '<p><strong>Social Event 21</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-22', 'Social Event 22', 'w35-social-22 mahjong gathering', '<p><strong>Social Event 22</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-23', 'Social Event 23', 'w35-social-23 mahjong gathering', '<p><strong>Social Event 23</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-24', 'Social Event 24', 'w35-social-24 mahjong gathering', '<p><strong>Social Event 24</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-25', 'Social Event 25', 'w35-social-25 mahjong gathering', '<p><strong>Social Event 25</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-26', 'Social Event 26', 'w35-social-26 mahjong gathering', '<p><strong>Social Event 26</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-27', 'Social Event 27', 'w35-social-27 mahjong gathering', '<p><strong>Social Event 27</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-28', 'Social Event 28', 'w35-social-28 mahjong gathering', '<p><strong>Social Event 28</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-29', 'Social Event 29', 'w35-social-29 mahjong gathering', '<p><strong>Social Event 29</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-30', 'Social Event 30', 'w35-social-30 mahjong gathering', '<p><strong>Social Event 30</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-31', 'Social Event 31', 'w35-social-31 mahjong gathering', '<p><strong>Social Event 31</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-32', 'Social Event 32', 'w35-social-32 mahjong gathering', '<p><strong>Social Event 32</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-33', 'Social Event 33', 'w35-social-33 mahjong gathering', '<p><strong>Social Event 33</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-34', 'Social Event 34', 'w35-social-34 mahjong gathering', '<p><strong>Social Event 34</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-35', 'Social Event 35', 'w35-social-35 mahjong gathering', '<p><strong>Social Event 35</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-36', 'Social Event 36', 'w35-social-36 mahjong gathering', '<p><strong>Social Event 36</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-37', 'Social Event 37', 'w35-social-37 mahjong gathering', '<p><strong>Social Event 37</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-38', 'Social Event 38', 'w35-social-38 mahjong gathering', '<p><strong>Social Event 38</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-39', 'Social Event 39', 'w35-social-39 mahjong gathering', '<p><strong>Social Event 39</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-40', 'Social Event 40', 'w35-social-40 mahjong gathering', '<p><strong>Social Event 40</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-41', 'Social Event 41', 'w35-social-41 mahjong gathering', '<p><strong>Social Event 41</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-42', 'Social Event 42', 'w35-social-42 mahjong gathering', '<p><strong>Social Event 42</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-43', 'Social Event 43', 'w35-social-43 mahjong gathering', '<p><strong>Social Event 43</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-44', 'Social Event 44', 'w35-social-44 mahjong gathering', '<p><strong>Social Event 44</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w35-social-45', 'Social Event 45', 'w35-social-45 mahjong gathering', '<p><strong>Social Event 45</strong> — <a href="/">main site</a> · <a href="/mahjong.html">Mahjong</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ('mahjong-w35-guide-1.html', 'Guide Topic 1', 'mahjong guide topic 1', '<p><strong>Guide 1</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-2.html', 'Guide Topic 2', 'mahjong guide topic 2', '<p><strong>Guide 2</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-3.html', 'Guide Topic 3', 'mahjong guide topic 3', '<p><strong>Guide 3</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-4.html', 'Guide Topic 4', 'mahjong guide topic 4', '<p><strong>Guide 4</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-5.html', 'Guide Topic 5', 'mahjong guide topic 5', '<p><strong>Guide 5</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-6.html', 'Guide Topic 6', 'mahjong guide topic 6', '<p><strong>Guide 6</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-7.html', 'Guide Topic 7', 'mahjong guide topic 7', '<p><strong>Guide 7</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-8.html', 'Guide Topic 8', 'mahjong guide topic 8', '<p><strong>Guide 8</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-9.html', 'Guide Topic 9', 'mahjong guide topic 9', '<p><strong>Guide 9</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-10.html', 'Guide Topic 10', 'mahjong guide topic 10', '<p><strong>Guide 10</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-11.html', 'Guide Topic 11', 'mahjong guide topic 11', '<p><strong>Guide 11</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-12.html', 'Guide Topic 12', 'mahjong guide topic 12', '<p><strong>Guide 12</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-13.html', 'Guide Topic 13', 'mahjong guide topic 13', '<p><strong>Guide 13</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-14.html', 'Guide Topic 14', 'mahjong guide topic 14', '<p><strong>Guide 14</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-15.html', 'Guide Topic 15', 'mahjong guide topic 15', '<p><strong>Guide 15</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-16.html', 'Guide Topic 16', 'mahjong guide topic 16', '<p><strong>Guide 16</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-17.html', 'Guide Topic 17', 'mahjong guide topic 17', '<p><strong>Guide 17</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-18.html', 'Guide Topic 18', 'mahjong guide topic 18', '<p><strong>Guide 18</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-19.html', 'Guide Topic 19', 'mahjong guide topic 19', '<p><strong>Guide 19</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-20.html', 'Guide Topic 20', 'mahjong guide topic 20', '<p><strong>Guide 20</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-21.html', 'Guide Topic 21', 'mahjong guide topic 21', '<p><strong>Guide 21</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-22.html', 'Guide Topic 22', 'mahjong guide topic 22', '<p><strong>Guide 22</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-23.html', 'Guide Topic 23', 'mahjong guide topic 23', '<p><strong>Guide 23</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-24.html', 'Guide Topic 24', 'mahjong guide topic 24', '<p><strong>Guide 24</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-25.html', 'Guide Topic 25', 'mahjong guide topic 25', '<p><strong>Guide 25</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-26.html', 'Guide Topic 26', 'mahjong guide topic 26', '<p><strong>Guide 26</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-27.html', 'Guide Topic 27', 'mahjong guide topic 27', '<p><strong>Guide 27</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-28.html', 'Guide Topic 28', 'mahjong guide topic 28', '<p><strong>Guide 28</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-29.html', 'Guide Topic 29', 'mahjong guide topic 29', '<p><strong>Guide 29</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-30.html', 'Guide Topic 30', 'mahjong guide topic 30', '<p><strong>Guide 30</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-31.html', 'Guide Topic 31', 'mahjong guide topic 31', '<p><strong>Guide 31</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-32.html', 'Guide Topic 32', 'mahjong guide topic 32', '<p><strong>Guide 32</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-33.html', 'Guide Topic 33', 'mahjong guide topic 33', '<p><strong>Guide 33</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-34.html', 'Guide Topic 34', 'mahjong guide topic 34', '<p><strong>Guide 34</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
        ('mahjong-w35-guide-35.html', 'Guide Topic 35', 'mahjong guide topic 35', '<p><strong>Guide 35</strong> — <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/">main site</a> · <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
