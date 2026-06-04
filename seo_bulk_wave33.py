# -*- coding: utf-8 -*-
"""Mega Wave 33 — ~600+ pages (500 cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave33_cities_data import WAVE33_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_33(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "skagit-valley-wa-mahjong-hub.html",
            "Skagit Valley WA Mahjong | Mount Vernon & Anacortes",
            "Skagit Valley WA mahjong — Mount Vernon, Anacortes, tulip country private events.",
            "skagit valley washington mahjong hub, mount vernon mah jongg",
            "Skagit Valley WA Mahjong Guide",
            """<p><strong>Skagit Valley mahjong</strong> — farmland and islands private lessons:</p>
<p><a href="mount-vernon-wa-mahjong.html">Mount Vernon</a> · <a href="anacortes-wa-mahjong.html">Anacortes</a> · <a href="bellingham-wa-mahjong.html">Bellingham</a> · <a href="everett-wa-mahjong.html">Everett</a></p>
<p><a href="washington-mahjong-hub.html">Washington hub</a> · <a href="/book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "red-river-valley-mahjong-hub.html",
            "Red River Valley Mahjong | Fargo, Grand Forks & Moorhead",
            "Red River Valley mahjong — Fargo, Grand Forks, Moorhead border region private events.",
            "red river valley mahjong hub, fargo mah jongg",
            "Red River Valley Mahjong Guide",
            """<p><strong>Red River Valley mahjong</strong> — prairie metro private lessons:</p>
<p><a href="fargo-nd-mahjong.html">Fargo</a> · <a href="grand-forks-nd-mahjong.html">Grand Forks</a> · <a href="moorhead-mn-mahjong.html">Moorhead</a> · <a href="bismarck-nd-mahjong.html">Bismarck</a></p>
<p><a href="north-dakota-mahjong-hub.html">ND hub</a> · <a href="minnesota-mahjong-hub.html">Minnesota hub</a></p>""",
        ),
        (
            "wiregrass-al-mahjong-hub.html",
            "Wiregrass AL Mahjong | Dothan & Enterprise",
            "Wiregrass Alabama mahjong — Dothan, Enterprise, southeast AL private events.",
            "wiregrass alabama mahjong hub, dothan mah jongg",
            "Wiregrass AL Mahjong Guide",
            """<p><strong>Wiregrass mahjong</strong> — southeast Alabama private lessons:</p>
<p><a href="dothan-al-mahjong.html">Dothan</a> · <a href="enterprise-al-mahjong.html">Enterprise</a> · <a href="ozark-al-mahjong.html">Ozark AL</a> · <a href="mobile-mahjong.html">Mobile</a></p>
<p><a href="alabama-mahjong-hub.html">Alabama hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "michigan-thumb-mahjong-hub.html",
            "Michigan Thumb Mahjong | Port Huron & Bad Axe",
            "Michigan Thumb mahjong — Port Huron, Bad Axe, Lake Huron shore private events.",
            "michigan thumb mahjong hub, port huron mah jongg",
            "Michigan Thumb Mahjong Guide",
            """<p><strong>Michigan Thumb mahjong</strong> — Lake Huron shore private lessons:</p>
<p><a href="port-huron-mi-mahjong.html">Port Huron</a> · <a href="bad-axe-mi-mahjong.html">Bad Axe</a> · <a href="flint-mi-mahjong.html">Flint</a> · <a href="detroit-mahjong.html">Detroit</a></p>
<p><a href="michigan-mahjong-hub.html">Michigan hub</a> · <a href="great-lakes-mahjong-hub.html">Great Lakes</a></p>""",
        ),
        (
            "leelanau-peninsula-mi-mahjong-hub.html",
            "Leelanau Peninsula MI Mahjong | Traverse City & Glen Arbor",
            "Leelanau Peninsula MI mahjong — Traverse City, Glen Arbor, cherry country events.",
            "leelanau peninsula michigan mahjong hub, traverse city mah jongg",
            "Leelanau Peninsula MI Mahjong Guide",
            """<p><strong>Leelanau Peninsula mahjong</strong> — wine and cherry country private lessons:</p>
<p><a href="traverse-city-mi-mahjong.html">Traverse City</a> · <a href="glen-arbor-mi-mahjong.html">Glen Arbor</a> · <a href="petoskey-mi-mahjong.html">Petoskey</a> · <a href="charlevoix-mi-mahjong.html">Charlevoix</a></p>
<p><a href="michigan-mahjong-hub.html">Michigan hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "buffalo-niagara-ny-mahjong-hub.html",
            "Buffalo Niagara NY Mahjong | Buffalo, Niagara Falls & Lewiston",
            "Buffalo Niagara NY mahjong — Buffalo, Niagara Falls, Lewiston private events.",
            "buffalo niagara new york mahjong hub, buffalo mah jongg",
            "Buffalo Niagara NY Mahjong Guide",
            """<p><strong>Buffalo Niagara mahjong</strong> — western NY private lessons:</p>
<p><a href="buffalo-ny-mahjong.html">Buffalo</a> · <a href="niagara-falls-ny-mahjong.html">Niagara Falls</a> · <a href="lewiston-ny-mahjong.html">Lewiston NY</a> · <a href="rochester-ny-mahjong.html">Rochester</a></p>
<p><a href="new-york-mahjong-hub.html">New York hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "southern-indiana-mahjong-hub.html",
            "Southern Indiana Mahjong | Bloomington, Evansville & Columbus IN",
            "Southern Indiana mahjong — Bloomington, Evansville, Columbus IN private events.",
            "southern indiana mahjong hub, bloomington in mah jongg",
            "Southern Indiana Mahjong Guide",
            """<p><strong>Southern Indiana mahjong</strong> — Hoosier south private lessons:</p>
<p><a href="bloomington-in-mahjong.html">Bloomington IN</a> · <a href="evansville-in-mahjong.html">Evansville</a> · <a href="columbus-in-mahjong.html">Columbus IN</a> · <a href="indianapolis-mahjong.html">Indianapolis</a></p>
<p><a href="indiana-mahjong-hub.html">Indiana hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "land-between-lakes-mahjong-hub.html",
            "Land Between the Lakes Mahjong | Murray & Clarksville TN",
            "Land Between the Lakes mahjong — Murray KY, Clarksville, lake country private events.",
            "land between the lakes mahjong hub, murray ky mah jongg",
            "Land Between the Lakes Mahjong Guide",
            """<p><strong>Land Between the Lakes mahjong</strong> — lake peninsula private lessons:</p>
<p><a href="murray-ky-mahjong.html">Murray KY</a> · <a href="clarksville-tn-mahjong.html">Clarksville</a> · <a href="paducah-ky-mahjong.html">Paducah</a> · <a href="nashville-mahjong.html">Nashville</a></p>
<p><a href="kentucky-mahjong-hub.html">Kentucky hub</a> · <a href="tennessee-mahjong-hub.html">Tennessee hub</a></p>""",
        ),
        (
            "caprock-tx-mahjong-hub.html",
            "Caprock TX Mahjong | Lubbock, Amarillo & Plainview",
            "Caprock Texas mahjong — Lubbock, Amarillo, Plainview High Plains private events.",
            "caprock texas mahjong hub, lubbock mah jongg",
            "Caprock TX Mahjong Guide",
            """<p><strong>Caprock mahjong</strong> — High Plains private lessons:</p>
<p><a href="lubbock-tx-mahjong.html">Lubbock</a> · <a href="amarillo-tx-mahjong.html">Amarillo</a> · <a href="plainview-tx-mahjong.html">Plainview</a> · <a href="midland-tx-mahjong.html">Midland</a></p>
<p><a href="texas-mahjong-hub.html">Texas hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "high-country-nc-mahjong-hub.html",
            "High Country NC Mahjong | Boone, Blowing Rock & Banner Elk",
            "High Country NC mahjong — Boone, Blowing Rock, Banner Elk mountain private events.",
            "high country north carolina mahjong hub, boone mah jongg",
            "High Country NC Mahjong Guide",
            """<p><strong>High Country mahjong</strong> — Blue Ridge high elevation private lessons:</p>
<p><a href="boone-nc-mahjong.html">Boone</a> · <a href="blowing-rock-nc-mahjong.html">Blowing Rock</a> · <a href="banner-elk-nc-mahjong.html">Banner Elk</a> · <a href="asheville-mahjong.html">Asheville</a></p>
<p><a href="north-carolina-mountains-mahjong-hub.html">NC mountains</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "mississippi-delta-mahjong-hub.html",
            "Mississippi Delta Mahjong | Greenville MS & Clarksdale",
            "Mississippi Delta mahjong — Greenville, Clarksdale, Delta blues country private events.",
            "mississippi delta mahjong hub, greenville ms mah jongg",
            "Mississippi Delta Mahjong Guide",
            """<p><strong>Mississippi Delta mahjong</strong> — Delta private lessons:</p>
<p><a href="greenville-ms-mahjong.html">Greenville MS</a> · <a href="clarksdale-ms-mahjong.html">Clarksdale</a> · <a href="tupelo-ms-mahjong.html">Tupelo</a> · <a href="jackson-ms-mahjong.html">Jackson MS</a></p>
<p><a href="mississippi-mahjong-hub.html">Mississippi hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "coastal-maine-mahjong-hub.html",
            "Coastal Maine Mahjong | Camden, Rockport & Boothbay",
            "Coastal Maine mahjong — Camden, Rockport, Boothbay Harbor private events.",
            "coastal maine mahjong hub, camden maine mah jongg",
            "Coastal Maine Mahjong Guide",
            """<p><strong>Coastal Maine mahjong</strong> — midcoast private lessons:</p>
<p><a href="camden-me-mahjong.html">Camden</a> · <a href="rockport-me-mahjong.html">Rockport ME</a> · <a href="boothbay-harbor-me-mahjong.html">Boothbay Harbor</a> · <a href="portland-me-mahjong.html">Portland ME</a></p>
<p><a href="maine-mahjong-hub.html">Maine hub</a> · <a href="new-england-mahjong-hub.html">New England</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE33_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("alpha-phi-omega", "Alpha Phi Omega", "APO"),
        ("beta-kappa-gamma", "Beta Kappa Gamma", "BKG"),
        ("chi-phi-sigma", "Chi Phi Sigma", "Chi Phi Sigma"),
        ("delta-psi", "Delta Psi", "Delta Psi"),
        ("kappa-psi", "Kappa Psi", "Kappa Psi"),
        ("lambda-theta-phi", "Lambda Theta Phi", "Lambda Theta"),
        ("nu-alpha-phi", "Nu Alpha Phi", "Nu Alpha Phi"),
        ("omega-hi-phi", "Omega Hi Phi", "Omega Hi Phi"),
        ("phi-beta-lambda", "Phi Beta Lambda", "Phi Beta Lambda"),
        ("phi-eta-mu", "Phi Eta Mu", "Phi Eta Mu"),
        ("sigma-pi", "Sigma Pi", "Sigma Pi"),
        ("theta-delta-chi", "Theta Delta Chi", "TDC"),
        ("triangle-fraternity", "Triangle", "Triangle"),
        ("zeta-beta-tau", "Zeta Beta Tau", "ZBT"),
        ("iota-phi-theta", "Iota Phi Theta", "Iota Phi"),
        ("kappa-alpha-society", "Kappa Alpha Society", "Kappa Alpha Soc"),
        ("phi-sigma-pi", "Phi Sigma Pi", "Phi Sigma Pi"),
        ("sigma-nu-alumni", "Sigma Nu Alumni", "Sigma Nu"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("alpha-chi-sigma", "Alpha Chi Sigma", "Alpha Chi Sigma"),
        ("alpha-kappa-phi", "Alpha Kappa Phi", "AKPhi"),
        ("beta-sigma-phi", "Beta Sigma Phi", "Beta Sigma Phi"),
        ("delta-chi", "Delta Chi", "Delta Chi"),
        ("gamma-eta", "Gamma Eta", "Gamma Eta"),
        ("kappa-alpha-sigma", "Kappa Alpha Sigma", "KAS"),
        ("phi-alpha", "Phi Alpha", "Phi Alpha"),
        ("sigma-alpha", "Sigma Alpha", "Sigma Alpha"),
        ("zeta-eta-eta", "Zeta Eta Eta", "Zeta Eta Eta"),
        ("alpha-sigma-phi-sorority", "Alpha Sigma Phi", "Alpha Sig"),
        ("chi-delta-theta", "Chi Delta Theta", "Chi Delta Theta"),
        ("delta-kappa-sorority", "Delta Kappa", "Delta Kappa"),
        ("kappa-phi-iota", "Kappa Phi Iota", "Kappa Phi Iota"),
        ("lambda-psi-delta", "Lambda Psi Delta", "LPD"),
        ("mu-sigma-uu", "Mu Sigma Upsilon", "MSU"),
        ("phi-sigma-rho", "Phi Sigma Rho", "Phi Sigma Rho"),
        ("sigma-phi-omega", "Sigma Phi Omega", "SPO"),
        ("tau-alpha-pi", "Tau Alpha Pi", "TAP"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ('w33-occasion-1', 'Event Style 1', 'w33 occasion 1 mahjong event', '<p><strong>Event Style 1</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-2', 'Event Style 2', 'w33 occasion 2 mahjong event', '<p><strong>Event Style 2</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-3', 'Event Style 3', 'w33 occasion 3 mahjong event', '<p><strong>Event Style 3</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-4', 'Event Style 4', 'w33 occasion 4 mahjong event', '<p><strong>Event Style 4</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-5', 'Event Style 5', 'w33 occasion 5 mahjong event', '<p><strong>Event Style 5</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-6', 'Event Style 6', 'w33 occasion 6 mahjong event', '<p><strong>Event Style 6</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-7', 'Event Style 7', 'w33 occasion 7 mahjong event', '<p><strong>Event Style 7</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-8', 'Event Style 8', 'w33 occasion 8 mahjong event', '<p><strong>Event Style 8</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-9', 'Event Style 9', 'w33 occasion 9 mahjong event', '<p><strong>Event Style 9</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-10', 'Event Style 10', 'w33 occasion 10 mahjong event', '<p><strong>Event Style 10</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-11', 'Event Style 11', 'w33 occasion 11 mahjong event', '<p><strong>Event Style 11</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-12', 'Event Style 12', 'w33 occasion 12 mahjong event', '<p><strong>Event Style 12</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-13', 'Event Style 13', 'w33 occasion 13 mahjong event', '<p><strong>Event Style 13</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-14', 'Event Style 14', 'w33 occasion 14 mahjong event', '<p><strong>Event Style 14</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-15', 'Event Style 15', 'w33 occasion 15 mahjong event', '<p><strong>Event Style 15</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-16', 'Event Style 16', 'w33 occasion 16 mahjong event', '<p><strong>Event Style 16</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-17', 'Event Style 17', 'w33 occasion 17 mahjong event', '<p><strong>Event Style 17</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-18', 'Event Style 18', 'w33 occasion 18 mahjong event', '<p><strong>Event Style 18</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-19', 'Event Style 19', 'w33 occasion 19 mahjong event', '<p><strong>Event Style 19</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-20', 'Event Style 20', 'w33 occasion 20 mahjong event', '<p><strong>Event Style 20</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-21', 'Event Style 21', 'w33 occasion 21 mahjong event', '<p><strong>Event Style 21</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-22', 'Event Style 22', 'w33 occasion 22 mahjong event', '<p><strong>Event Style 22</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-23', 'Event Style 23', 'w33 occasion 23 mahjong event', '<p><strong>Event Style 23</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-24', 'Event Style 24', 'w33 occasion 24 mahjong event', '<p><strong>Event Style 24</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-25', 'Event Style 25', 'w33 occasion 25 mahjong event', '<p><strong>Event Style 25</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-26', 'Event Style 26', 'w33 occasion 26 mahjong event', '<p><strong>Event Style 26</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-27', 'Event Style 27', 'w33 occasion 27 mahjong event', '<p><strong>Event Style 27</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-28', 'Event Style 28', 'w33 occasion 28 mahjong event', '<p><strong>Event Style 28</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-29', 'Event Style 29', 'w33 occasion 29 mahjong event', '<p><strong>Event Style 29</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-30', 'Event Style 30', 'w33 occasion 30 mahjong event', '<p><strong>Event Style 30</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-31', 'Event Style 31', 'w33 occasion 31 mahjong event', '<p><strong>Event Style 31</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-32', 'Event Style 32', 'w33 occasion 32 mahjong event', '<p><strong>Event Style 32</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-33', 'Event Style 33', 'w33 occasion 33 mahjong event', '<p><strong>Event Style 33</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-34', 'Event Style 34', 'w33 occasion 34 mahjong event', '<p><strong>Event Style 34</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-35', 'Event Style 35', 'w33 occasion 35 mahjong event', '<p><strong>Event Style 35</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-36', 'Event Style 36', 'w33 occasion 36 mahjong event', '<p><strong>Event Style 36</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-37', 'Event Style 37', 'w33 occasion 37 mahjong event', '<p><strong>Event Style 37</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-38', 'Event Style 38', 'w33 occasion 38 mahjong event', '<p><strong>Event Style 38</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-39', 'Event Style 39', 'w33 occasion 39 mahjong event', '<p><strong>Event Style 39</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w33-occasion-40', 'Event Style 40', 'w33 occasion 40 mahjong event', '<p><strong>Event Style 40</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ('mahjong-w33-rule-1.html', 'Rule Topic 1', 'rule topic 1 in mahjong', '<p><strong>Rule Topic 1</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-2.html', 'Rule Topic 2', 'rule topic 2 in mahjong', '<p><strong>Rule Topic 2</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-3.html', 'Rule Topic 3', 'rule topic 3 in mahjong', '<p><strong>Rule Topic 3</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-4.html', 'Rule Topic 4', 'rule topic 4 in mahjong', '<p><strong>Rule Topic 4</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-5.html', 'Rule Topic 5', 'rule topic 5 in mahjong', '<p><strong>Rule Topic 5</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-6.html', 'Rule Topic 6', 'rule topic 6 in mahjong', '<p><strong>Rule Topic 6</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-7.html', 'Rule Topic 7', 'rule topic 7 in mahjong', '<p><strong>Rule Topic 7</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-8.html', 'Rule Topic 8', 'rule topic 8 in mahjong', '<p><strong>Rule Topic 8</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-9.html', 'Rule Topic 9', 'rule topic 9 in mahjong', '<p><strong>Rule Topic 9</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-10.html', 'Rule Topic 10', 'rule topic 10 in mahjong', '<p><strong>Rule Topic 10</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-11.html', 'Rule Topic 11', 'rule topic 11 in mahjong', '<p><strong>Rule Topic 11</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-12.html', 'Rule Topic 12', 'rule topic 12 in mahjong', '<p><strong>Rule Topic 12</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-13.html', 'Rule Topic 13', 'rule topic 13 in mahjong', '<p><strong>Rule Topic 13</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-14.html', 'Rule Topic 14', 'rule topic 14 in mahjong', '<p><strong>Rule Topic 14</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-15.html', 'Rule Topic 15', 'rule topic 15 in mahjong', '<p><strong>Rule Topic 15</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-16.html', 'Rule Topic 16', 'rule topic 16 in mahjong', '<p><strong>Rule Topic 16</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-17.html', 'Rule Topic 17', 'rule topic 17 in mahjong', '<p><strong>Rule Topic 17</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-18.html', 'Rule Topic 18', 'rule topic 18 in mahjong', '<p><strong>Rule Topic 18</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-19.html', 'Rule Topic 19', 'rule topic 19 in mahjong', '<p><strong>Rule Topic 19</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-20.html', 'Rule Topic 20', 'rule topic 20 in mahjong', '<p><strong>Rule Topic 20</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-21.html', 'Rule Topic 21', 'rule topic 21 in mahjong', '<p><strong>Rule Topic 21</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-22.html', 'Rule Topic 22', 'rule topic 22 in mahjong', '<p><strong>Rule Topic 22</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-23.html', 'Rule Topic 23', 'rule topic 23 in mahjong', '<p><strong>Rule Topic 23</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-24.html', 'Rule Topic 24', 'rule topic 24 in mahjong', '<p><strong>Rule Topic 24</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-25.html', 'Rule Topic 25', 'rule topic 25 in mahjong', '<p><strong>Rule Topic 25</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-26.html', 'Rule Topic 26', 'rule topic 26 in mahjong', '<p><strong>Rule Topic 26</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-27.html', 'Rule Topic 27', 'rule topic 27 in mahjong', '<p><strong>Rule Topic 27</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-28.html', 'Rule Topic 28', 'rule topic 28 in mahjong', '<p><strong>Rule Topic 28</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-29.html', 'Rule Topic 29', 'rule topic 29 in mahjong', '<p><strong>Rule Topic 29</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-30.html', 'Rule Topic 30', 'rule topic 30 in mahjong', '<p><strong>Rule Topic 30</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-31.html', 'Rule Topic 31', 'rule topic 31 in mahjong', '<p><strong>Rule Topic 31</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-32.html', 'Rule Topic 32', 'rule topic 32 in mahjong', '<p><strong>Rule Topic 32</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-33.html', 'Rule Topic 33', 'rule topic 33 in mahjong', '<p><strong>Rule Topic 33</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-34.html', 'Rule Topic 34', 'rule topic 34 in mahjong', '<p><strong>Rule Topic 34</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w33-rule-35.html', 'Rule Topic 35', 'rule topic 35 in mahjong', '<p><strong>Rule Topic 35</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
