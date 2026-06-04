# -*- coding: utf-8 -*-
"""Mega Wave 34 — ~600+ pages (500 cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave34_cities_data import WAVE34_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_34(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "sierra-nevada-ca-mahjong-hub.html",
            "Sierra Nevada CA Mahjong | Mammoth, Tahoe & Sonora Pass",
            "Sierra Nevada California mahjong — Mammoth Lakes, Tahoe corridor, mountain resort events.",
            "sierra nevada california mahjong hub, mammoth lakes mah jongg",
            "Sierra Nevada CA Mahjong Guide",
            """<p><strong>Sierra Nevada mahjong</strong> — mountain resort private lessons:</p>
<p><a href="mammoth-lakes-ca-mahjong.html">Mammoth Lakes</a> · <a href="south-lake-tahoe-ca-mahjong.html">South Lake Tahoe</a> · <a href="truckee-ca-mahjong.html">Truckee</a> · <a href="sonora-ca-mahjong.html">Sonora CA</a></p>
<p><a href="california-mahjong-hub.html">California hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "monterey-bay-ca-mahjong-hub.html",
            "Monterey Bay CA Mahjong | Monterey, Carmel & Santa Cruz",
            "Monterey Bay California mahjong — Monterey, Carmel, Santa Cruz coast private events.",
            "monterey bay california mahjong hub, monterey mah jongg",
            "Monterey Bay CA Mahjong Guide",
            """<p><strong>Monterey Bay mahjong</strong> — central coast private lessons:</p>
<p><a href="monterey-ca-mahjong.html">Monterey</a> · <a href="carmel-by-the-sea-ca-mahjong.html">Carmel</a> · <a href="santa-cruz-ca-mahjong.html">Santa Cruz</a> · <a href="salinas-ca-mahjong.html">Salinas</a></p>
<p><a href="california-central-coast-mahjong-hub.html">Central Coast hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "white-mountains-nh-mahjong-hub.html",
            "White Mountains NH Mahjong | North Conway & Lincoln",
            "White Mountains NH mahjong — North Conway, Lincoln, ski country private events.",
            "white mountains new hampshire mahjong hub, north conway mah jongg",
            "White Mountains NH Mahjong Guide",
            """<p><strong>White Mountains mahjong</strong> — NH ski country private lessons:</p>
<p><a href="north-conway-nh-mahjong.html">North Conway</a> · <a href="lincoln-nh-mahjong.html">Lincoln NH</a> · <a href="laconia-nh-mahjong.html">Laconia</a> · <a href="manchester-nh-mahjong.html">Manchester NH</a></p>
<p><a href="new-hampshire-mahjong-hub.html">NH hub</a> · <a href="new-england-mahjong-hub.html">New England</a></p>""",
        ),
        (
            "litchfield-hills-ct-mahjong-hub.html",
            "Litchfield Hills CT Mahjong | Litchfield & Kent",
            "Litchfield Hills Connecticut mahjong — Litchfield, Kent, northwest CT private events.",
            "litchfield hills connecticut mahjong hub, litchfield ct mah jongg",
            "Litchfield Hills CT Mahjong Guide",
            """<p><strong>Litchfield Hills mahjong</strong> — NW Connecticut private lessons:</p>
<p><a href="litchfield-ct-mahjong.html">Litchfield</a> · <a href="kent-ct-mahjong.html">Kent CT</a> · <a href="torrington-ct-mahjong.html">Torrington</a> · <a href="hartford-ct-mahjong.html">Hartford</a></p>
<p><a href="connecticut-mahjong-hub.html">Connecticut hub</a> · <a href="gold-coast-ct-mahjong-hub.html">Gold Coast</a></p>""",
        ),
        (
            "southern-maryland-mahjong-hub.html",
            "Southern Maryland Mahjong | Annapolis, Solomons & St Marys",
            "Southern Maryland mahjong — Annapolis, Solomons Island, Chesapeake private events.",
            "southern maryland mahjong hub, annapolis mah jongg",
            "Southern Maryland Mahjong Guide",
            """<p><strong>Southern Maryland mahjong</strong> — Chesapeake private lessons:</p>
<p><a href="annapolis-md-mahjong.html">Annapolis</a> · <a href="solomons-md-mahjong.html">Solomons</a> · <a href="lexington-park-md-mahjong.html">Lexington Park</a> · <a href="bethesda-md-mahjong.html">Bethesda</a></p>
<p><a href="maryland-mahjong-hub.html">Maryland hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "kanawha-valley-wv-mahjong-hub.html",
            "Kanawha Valley WV Mahjong | Charleston & Huntington",
            "Kanawha Valley WV mahjong — Charleston, Huntington, river valley private events.",
            "kanawha valley west virginia mahjong hub, charleston wv mah jongg",
            "Kanawha Valley WV Mahjong Guide",
            """<p><strong>Kanawha Valley mahjong</strong> — WV metro private lessons:</p>
<p><a href="charleston-wv-mahjong.html">Charleston WV</a> · <a href="huntington-wv-mahjong.html">Huntington</a> · <a href="beckley-wv-mahjong.html">Beckley</a> · <a href="morgantown-wv-mahjong.html">Morgantown</a></p>
<p><a href="west-virginia-mahjong-hub.html">West Virginia hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "black-belt-al-mahjong-hub.html",
            "Black Belt AL Mahjong | Selma, Tuskegee & Montgomery",
            "Black Belt Alabama mahjong — Selma, Tuskegee, Montgomery corridor private events.",
            "black belt alabama mahjong hub, selma mah jongg",
            "Black Belt AL Mahjong Guide",
            """<p><strong>Black Belt mahjong</strong> — central AL private lessons:</p>
<p><a href="selma-al-mahjong.html">Selma</a> · <a href="tuskegee-al-mahjong.html">Tuskegee</a> · <a href="montgomery-al-mahjong.html">Montgomery</a> · <a href="birmingham-mahjong.html">Birmingham</a></p>
<p><a href="alabama-mahjong-hub.html">Alabama hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "piney-woods-tx-mahjong-hub.html",
            "Piney Woods TX Mahjong | Tyler, Longview & Nacogdoches",
            "Piney Woods Texas mahjong — Tyler, Longview, Nacogdoches East Texas private events.",
            "piney woods texas mahjong hub, tyler mah jongg",
            "Piney Woods TX Mahjong Guide",
            """<p><strong>Piney Woods mahjong</strong> — East Texas private lessons:</p>
<p><a href="tyler-tx-mahjong.html">Tyler</a> · <a href="longview-tx-mahjong.html">Longview</a> · <a href="nacogdoches-tx-mahjong.html">Nacogdoches</a> · <a href="shreveport-mahjong.html">Shreveport</a></p>
<p><a href="texas-mahjong-hub.html">Texas hub</a> · <a href="arklatex-mahjong-hub.html">Arklatex</a></p>""",
        ),
        (
            "flint-river-ga-mahjong-hub.html",
            "Flint River GA Mahjong | Albany, Americus & Columbus GA",
            "Flint River Georgia mahjong — Albany, Americus, Columbus GA southwest private events.",
            "flint river georgia mahjong hub, albany ga mah jongg",
            "Flint River GA Mahjong Guide",
            """<p><strong>Flint River mahjong</strong> — southwest GA private lessons:</p>
<p><a href="albany-ga-mahjong.html">Albany GA</a> · <a href="americus-ga-mahjong.html">Americus</a> · <a href="columbus-ga-mahjong.html">Columbus GA</a> · <a href="macon-ga-mahjong.html">Macon</a></p>
<p><a href="georgia-mahjong-hub.html">Georgia hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "cumberland-gap-tn-mahjong-hub.html",
            "Cumberland Gap TN Mahjong | Cumberland Gap & Middlesboro",
            "Cumberland Gap TN mahjong — Cumberland Gap, Middlesboro, tri-state mountain private events.",
            "cumberland gap tennessee mahjong hub, middlesboro mah jongg",
            "Cumberland Gap TN Mahjong Guide",
            """<p><strong>Cumberland Gap mahjong</strong> — tri-state mountain private lessons:</p>
<p><a href="middlesboro-ky-mahjong.html">Middlesboro</a> · <a href="harrogate-tn-mahjong.html">Harrogate</a> · <a href="knoxville-mahjong.html">Knoxville</a> · <a href="lexington-ky-mahjong.html">Lexington</a></p>
<p><a href="tennessee-mahjong-hub.html">Tennessee hub</a> · <a href="kentucky-mahjong-hub.html">Kentucky hub</a></p>""",
        ),
        (
            "lake-of-ozarks-mo-mahjong-hub.html",
            "Lake of the Ozarks MO Mahjong | Osage Beach & Lake Ozark",
            "Lake of the Ozarks MO mahjong — Osage Beach, Lake Ozark, resort lake private events.",
            "lake of the ozarks missouri mahjong hub, osage beach mah jongg",
            "Lake of the Ozarks MO Mahjong Guide",
            """<p><strong>Lake of the Ozarks mahjong</strong> — Missouri lake resort private lessons:</p>
<p><a href="osage-beach-mo-mahjong.html">Osage Beach</a> · <a href="lake-ozark-mo-mahjong.html">Lake Ozark</a> · <a href="camdenton-mo-mahjong.html">Camdenton</a> · <a href="springfield-mo-mahjong.html">Springfield MO</a></p>
<p><a href="missouri-mahjong-hub.html">Missouri hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "red-rocks-co-mahjong-hub.html",
            "Red Rocks CO Mahjong | Morrison, Golden & Evergreen",
            "Red Rocks Colorado mahjong — Morrison, Golden, Evergreen foothills private events.",
            "red rocks colorado mahjong hub, golden co mah jongg",
            "Red Rocks CO Mahjong Guide",
            """<p><strong>Red Rocks mahjong</strong> — Denver foothills private lessons:</p>
<p><a href="golden-co-mahjong.html">Golden</a> · <a href="evergreen-co-mahjong.html">Evergreen</a> · <a href="morrison-co-mahjong.html">Morrison</a> · <a href="denver-mahjong.html">Denver</a></p>
<p><a href="colorado-mahjong-hub.html">Colorado hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE34_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("alpha-gamma-sigma-fr", "Alpha Gamma Sigma", "AGS"),
        ("beta-phi-alpha-fr", "Beta Phi Alpha", "Beta Phi Alpha"),
        ("chi-gamma-epsilon-fr", "Chi Gamma Epsilon", "CGE"),
        ("delta-sigma-pi-fr", "Delta Sigma Pi", "DSP Biz"),
        ("epsilon-pi-alpha-fr", "Epsilon Pi Alpha", "EPA"),
        ("eta-psi-psilon-fr", "Eta Psi Epsilon", "Eta Psi"),
        ("gamma-zeta-alpha-fr", "Gamma Zeta Alpha", "GZA"),
        ("kappa-eta-kappa-fr", "Kappa Eta Kappa", "KEK"),
        ("lambda-alpha-upsilon-fr", "Lambda Alpha Upsilon", "LAU"),
        ("mu-beta-lambda-fr", "Mu Beta Lambda", "MBL"),
        ("nu-sigma-nu-fr", "Nu Sigma Nu", "Nu Sig"),
        ("omicron-epsilon-pi-fr", "Omicron Epsilon Pi", "OEP"),
        ("pi-alpha-phi-fr", "Pi Alpha Phi", "Pi Alpha Phi"),
        ("rho-alpha-phi-fr", "Rho Alpha Phi", "Rho Alpha Phi"),
        ("sigma-beta-chi-fr", "Sigma Beta Chi", "SBC"),
        ("tau-kappa-epsilon-alumni-fr", "TKE Alumni", "TKE"),
        ("upsilon-psi-psilon-fr", "Upsilon Psi Epsilon", "YPE"),
        ("zeta-phi-rho-fr", "Zeta Phi Rho", "ZPR"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("alpha-lambda-sigma", "Alpha Lambda Sigma", "ALS"),
        ("beta-chi-theta-sorority", "Beta Chi Theta", "Beta Chi Theta"),
        ("chi-sigma-alpha", "Chi Sigma Alpha", "CSA"),
        ("delta-eta-iota", "Delta Eta Iota", "DEI"),
        ("epsilon-sigma-alpha", "Epsilon Sigma Alpha", "ESA"),
        ("gamma-phi-circles", "Gamma Phi Circles", "GPC"),
        ("kappa-upsilon-chi", "Kappa Upsilon Chi", "KUX"),
        ("lambda-sigma-upsilon", "Lambda Sigma Upsilon", "LSU"),
        ("mu-phi-epsilon", "Mu Phi Epsilon", "MPE"),
        ("nu-sigma-alpha", "Nu Sigma Alpha", "NSA"),
        ("omicron-chi-theta", "Omicron Chi Theta", "OCT"),
        ("phi-chi-omega", "Phi Chi Omega", "PCO"),
        ("rho-lambda-chi", "Rho Lambda Chi", "RLC"),
        ("sigma-upsilon-nu", "Sigma Upsilon Nu", "SUN"),
        ("tau-sigma-phi", "Tau Sigma Phi", "TSP"),
        ("upsilon-phi-upsilon", "Upsilon Phi Upsilon", "UPU"),
        ("zeta-chi-phi", "Zeta Chi Phi", "ZCP"),
        ("alpha-pi-sigma", "Alpha Pi Sigma", "APS"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ('w34-occasion-1', 'Event Style 1', 'w34 occasion 1 mahjong event', '<p><strong>Event Style 1</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-2', 'Event Style 2', 'w34 occasion 2 mahjong event', '<p><strong>Event Style 2</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-3', 'Event Style 3', 'w34 occasion 3 mahjong event', '<p><strong>Event Style 3</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-4', 'Event Style 4', 'w34 occasion 4 mahjong event', '<p><strong>Event Style 4</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-5', 'Event Style 5', 'w34 occasion 5 mahjong event', '<p><strong>Event Style 5</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-6', 'Event Style 6', 'w34 occasion 6 mahjong event', '<p><strong>Event Style 6</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-7', 'Event Style 7', 'w34 occasion 7 mahjong event', '<p><strong>Event Style 7</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-8', 'Event Style 8', 'w34 occasion 8 mahjong event', '<p><strong>Event Style 8</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-9', 'Event Style 9', 'w34 occasion 9 mahjong event', '<p><strong>Event Style 9</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-10', 'Event Style 10', 'w34 occasion 10 mahjong event', '<p><strong>Event Style 10</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-11', 'Event Style 11', 'w34 occasion 11 mahjong event', '<p><strong>Event Style 11</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-12', 'Event Style 12', 'w34 occasion 12 mahjong event', '<p><strong>Event Style 12</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-13', 'Event Style 13', 'w34 occasion 13 mahjong event', '<p><strong>Event Style 13</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-14', 'Event Style 14', 'w34 occasion 14 mahjong event', '<p><strong>Event Style 14</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-15', 'Event Style 15', 'w34 occasion 15 mahjong event', '<p><strong>Event Style 15</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-16', 'Event Style 16', 'w34 occasion 16 mahjong event', '<p><strong>Event Style 16</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-17', 'Event Style 17', 'w34 occasion 17 mahjong event', '<p><strong>Event Style 17</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-18', 'Event Style 18', 'w34 occasion 18 mahjong event', '<p><strong>Event Style 18</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-19', 'Event Style 19', 'w34 occasion 19 mahjong event', '<p><strong>Event Style 19</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-20', 'Event Style 20', 'w34 occasion 20 mahjong event', '<p><strong>Event Style 20</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-21', 'Event Style 21', 'w34 occasion 21 mahjong event', '<p><strong>Event Style 21</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-22', 'Event Style 22', 'w34 occasion 22 mahjong event', '<p><strong>Event Style 22</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-23', 'Event Style 23', 'w34 occasion 23 mahjong event', '<p><strong>Event Style 23</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-24', 'Event Style 24', 'w34 occasion 24 mahjong event', '<p><strong>Event Style 24</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-25', 'Event Style 25', 'w34 occasion 25 mahjong event', '<p><strong>Event Style 25</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-26', 'Event Style 26', 'w34 occasion 26 mahjong event', '<p><strong>Event Style 26</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-27', 'Event Style 27', 'w34 occasion 27 mahjong event', '<p><strong>Event Style 27</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-28', 'Event Style 28', 'w34 occasion 28 mahjong event', '<p><strong>Event Style 28</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-29', 'Event Style 29', 'w34 occasion 29 mahjong event', '<p><strong>Event Style 29</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-30', 'Event Style 30', 'w34 occasion 30 mahjong event', '<p><strong>Event Style 30</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-31', 'Event Style 31', 'w34 occasion 31 mahjong event', '<p><strong>Event Style 31</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-32', 'Event Style 32', 'w34 occasion 32 mahjong event', '<p><strong>Event Style 32</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-33', 'Event Style 33', 'w34 occasion 33 mahjong event', '<p><strong>Event Style 33</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-34', 'Event Style 34', 'w34 occasion 34 mahjong event', '<p><strong>Event Style 34</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-35', 'Event Style 35', 'w34 occasion 35 mahjong event', '<p><strong>Event Style 35</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-36', 'Event Style 36', 'w34 occasion 36 mahjong event', '<p><strong>Event Style 36</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-37', 'Event Style 37', 'w34 occasion 37 mahjong event', '<p><strong>Event Style 37</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-38', 'Event Style 38', 'w34 occasion 38 mahjong event', '<p><strong>Event Style 38</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-39', 'Event Style 39', 'w34 occasion 39 mahjong event', '<p><strong>Event Style 39</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
        ('w34-occasion-40', 'Event Style 40', 'w34 occasion 40 mahjong event', '<p><strong>Event Style 40</strong> — book with Lookout Mountain Mahjong. <a href="/mahjong.html">Main site</a> · <a href="/book-mahjong-lesson.html">Book</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ('mahjong-w34-rule-1.html', 'Rule Topic 1', 'rule topic 1 in mahjong', '<p><strong>Rule Topic 1</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-2.html', 'Rule Topic 2', 'rule topic 2 in mahjong', '<p><strong>Rule Topic 2</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-3.html', 'Rule Topic 3', 'rule topic 3 in mahjong', '<p><strong>Rule Topic 3</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-4.html', 'Rule Topic 4', 'rule topic 4 in mahjong', '<p><strong>Rule Topic 4</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-5.html', 'Rule Topic 5', 'rule topic 5 in mahjong', '<p><strong>Rule Topic 5</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-6.html', 'Rule Topic 6', 'rule topic 6 in mahjong', '<p><strong>Rule Topic 6</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-7.html', 'Rule Topic 7', 'rule topic 7 in mahjong', '<p><strong>Rule Topic 7</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-8.html', 'Rule Topic 8', 'rule topic 8 in mahjong', '<p><strong>Rule Topic 8</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-9.html', 'Rule Topic 9', 'rule topic 9 in mahjong', '<p><strong>Rule Topic 9</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-10.html', 'Rule Topic 10', 'rule topic 10 in mahjong', '<p><strong>Rule Topic 10</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-11.html', 'Rule Topic 11', 'rule topic 11 in mahjong', '<p><strong>Rule Topic 11</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-12.html', 'Rule Topic 12', 'rule topic 12 in mahjong', '<p><strong>Rule Topic 12</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-13.html', 'Rule Topic 13', 'rule topic 13 in mahjong', '<p><strong>Rule Topic 13</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-14.html', 'Rule Topic 14', 'rule topic 14 in mahjong', '<p><strong>Rule Topic 14</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-15.html', 'Rule Topic 15', 'rule topic 15 in mahjong', '<p><strong>Rule Topic 15</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-16.html', 'Rule Topic 16', 'rule topic 16 in mahjong', '<p><strong>Rule Topic 16</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-17.html', 'Rule Topic 17', 'rule topic 17 in mahjong', '<p><strong>Rule Topic 17</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-18.html', 'Rule Topic 18', 'rule topic 18 in mahjong', '<p><strong>Rule Topic 18</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-19.html', 'Rule Topic 19', 'rule topic 19 in mahjong', '<p><strong>Rule Topic 19</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-20.html', 'Rule Topic 20', 'rule topic 20 in mahjong', '<p><strong>Rule Topic 20</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-21.html', 'Rule Topic 21', 'rule topic 21 in mahjong', '<p><strong>Rule Topic 21</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-22.html', 'Rule Topic 22', 'rule topic 22 in mahjong', '<p><strong>Rule Topic 22</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-23.html', 'Rule Topic 23', 'rule topic 23 in mahjong', '<p><strong>Rule Topic 23</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-24.html', 'Rule Topic 24', 'rule topic 24 in mahjong', '<p><strong>Rule Topic 24</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-25.html', 'Rule Topic 25', 'rule topic 25 in mahjong', '<p><strong>Rule Topic 25</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-26.html', 'Rule Topic 26', 'rule topic 26 in mahjong', '<p><strong>Rule Topic 26</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-27.html', 'Rule Topic 27', 'rule topic 27 in mahjong', '<p><strong>Rule Topic 27</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-28.html', 'Rule Topic 28', 'rule topic 28 in mahjong', '<p><strong>Rule Topic 28</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-29.html', 'Rule Topic 29', 'rule topic 29 in mahjong', '<p><strong>Rule Topic 29</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-30.html', 'Rule Topic 30', 'rule topic 30 in mahjong', '<p><strong>Rule Topic 30</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-31.html', 'Rule Topic 31', 'rule topic 31 in mahjong', '<p><strong>Rule Topic 31</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-32.html', 'Rule Topic 32', 'rule topic 32 in mahjong', '<p><strong>Rule Topic 32</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-33.html', 'Rule Topic 33', 'rule topic 33 in mahjong', '<p><strong>Rule Topic 33</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-34.html', 'Rule Topic 34', 'rule topic 34 in mahjong', '<p><strong>Rule Topic 34</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
        ('mahjong-w34-rule-35.html', 'Rule Topic 35', 'rule topic 35 in mahjong', '<p><strong>Rule Topic 35</strong> — learn NMJL with <a href="/mahjong-101.html">Mahjong 101</a> · <a href="/mahjong.html">Main site</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
