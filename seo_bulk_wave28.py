# -*- coding: utf-8 -*-
"""Mega Wave 28 — ~500 pages (397 remaining cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave27_cities_data import WAVE27_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule

WAVE28_CITY_START = 424


def bulk_pages_mega_wave_28(city, page, mahjong_kw) -> list:
    """Mega Wave 28 — exhaust remaining WAVE27 city buffer + regional hubs."""
    out: list = []

    hubs = [
        (
            "shenandoah-valley-mahjong-hub.html",
            "Shenandoah Valley Mahjong | Winchester, Staunton & Harrisonburg",
            "Shenandoah Valley mahjong — Winchester, Staunton, Harrisonburg, VA wine country.",
            "shenandoah valley mahjong hub, winchester va mah jongg",
            "Shenandoah Valley Mahjong Guide",
            """<p><strong>Shenandoah Valley mahjong</strong> — Blue Ridge foothills private events:</p>
<p><a href="winchester-va-mahjong.html">Winchester</a> · <a href="staunton-va-mahjong.html">Staunton</a> · <a href="harrisonburg-va-mahjong.html">Harrisonburg</a> · <a href="charlottesville-mahjong.html">Charlottesville</a> · <a href="lexington-va-mahjong.html">Lexington VA</a></p>
<p><a href="virginia-mahjong-hub.html">Virginia hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "outer-banks-nc-mahjong-hub.html",
            "Outer Banks NC Mahjong | Kitty Hawk, Nags Head & Duck",
            "Outer Banks NC mahjong — Kitty Hawk, Nags Head, Duck, Corolla vacation rentals.",
            "outer banks nc mahjong hub, nags head mah jongg",
            "Outer Banks NC Mahjong Guide",
            """<p><strong>Outer Banks mahjong</strong> — beach week private lessons:</p>
<p><a href="outer-banks-mahjong.html">Outer Banks</a> · <a href="kitty-hawk-nc-mahjong.html">Kitty Hawk</a> · <a href="nags-head-nc-mahjong.html">Nags Head</a> · <a href="duck-nc-mahjong.html">Duck</a> · <a href="corolla-nc-mahjong.html">Corolla</a></p>
<p><a href="north-carolina-mahjong-hub.html">NC hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "black-hills-mahjong-hub.html",
            "Black Hills Mahjong | Rapid City, Deadwood & Spearfish",
            "Black Hills mahjong — Rapid City, Deadwood, Spearfish, Mount Rushmore area.",
            "black hills mahjong hub, rapid city mah jongg",
            "Black Hills Mahjong Guide",
            """<p><strong>Black Hills mahjong</strong> — Badlands and mountain town private events:</p>
<p><a href="rapid-city-sd-mahjong.html">Rapid City</a> · <a href="deadwood-sd-mahjong.html">Deadwood</a> · <a href="spearfish-sd-mahjong.html">Spearfish</a> · <a href="sturgis-sd-mahjong.html">Sturgis</a> · <a href="hill-city-sd-mahjong.html">Hill City</a></p>
<p><a href="south-dakota-mahjong-hub.html">South Dakota hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "upper-peninsula-mi-mahjong-hub.html",
            "Upper Peninsula Michigan Mahjong | Marquette, Sault Ste. Marie",
            "Upper Peninsula MI mahjong — Marquette, Sault Ste. Marie, Escanaba, Mackinac area.",
            "upper peninsula michigan mahjong hub, marquette mah jongg",
            "Upper Peninsula Michigan Mahjong Guide",
            """<p><strong>UP Michigan mahjong</strong> — lake and forest private lessons:</p>
<p><a href="marquette-mi-mahjong.html">Marquette</a> · <a href="sault-ste-marie-mi-mahjong.html">Sault Ste. Marie</a> · <a href="escanaba-mi-mahjong.html">Escanaba</a> · <a href="petoskey-mi-mahjong.html">Petoskey</a> · <a href="traverse-city-mi-mahjong.html">Traverse City</a></p>
<p><a href="michigan-mahjong-hub.html">Michigan hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "florida-keys-mahjong-hub.html",
            "Florida Keys Mahjong | Key West, Marathon & Islamorada",
            "Florida Keys mahjong — Key West, Marathon, Islamorada, Key Largo private events.",
            "florida keys mahjong hub, key west mah jongg",
            "Florida Keys Mahjong Guide",
            """<p><strong>Florida Keys mahjong</strong> — island vacation private lessons:</p>
<p><a href="key-west-fl-mahjong.html">Key West</a> · <a href="marathon-fl-mahjong.html">Marathon</a> · <a href="islamorada-fl-mahjong.html">Islamorada</a> · <a href="key-largo-fl-mahjong.html">Key Largo</a> · <a href="miami-mahjong.html">Miami</a></p>
<p><a href="florida-mahjong-hub.html">Florida hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "hudson-valley-mahjong-hub.html",
            "Hudson Valley Mahjong | Poughkeepsie, Newburgh & Rhinebeck",
            "Hudson Valley mahjong — Poughkeepsie, Newburgh, Rhinebeck, Hudson NY private events.",
            "hudson valley mahjong hub, poughkeepsie mah jongg",
            "Hudson Valley Mahjong Guide",
            """<p><strong>Hudson Valley mahjong</strong> — river towns and farm-to-table private lessons:</p>
<p><a href="poughkeepsie-ny-mahjong.html">Poughkeepsie</a> · <a href="newburgh-ny-mahjong.html">Newburgh</a> · <a href="rhinebeck-ny-mahjong.html">Rhinebeck</a> · <a href="hudson-ny-mahjong.html">Hudson NY</a> · <a href="woodstock-ny-mahjong.html">Woodstock NY</a></p>
<p><a href="new-york-mahjong-hub.html">New York hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "sandhills-nc-mahjong-hub.html",
            "Sandhills NC Mahjong | Pinehurst, Southern Pines & Aberdeen",
            "Sandhills NC mahjong — Pinehurst, Southern Pines, golf resort private events.",
            "sandhills nc mahjong hub, pinehurst mah jongg",
            "Sandhills NC Mahjong Guide",
            """<p><strong>Sandhills NC mahjong</strong> — golf and resort community private lessons:</p>
<p><a href="pinehurst-nc-mahjong.html">Pinehurst</a> · <a href="southern-pines-nc-mahjong.html">Southern Pines</a> · <a href="aberdeen-nc-mahjong.html">Aberdeen NC</a> · <a href="fayetteville-nc-mahjong.html">Fayetteville</a> · <a href="raleigh-mahjong.html">Raleigh</a></p>
<p><a href="north-carolina-mahjong-hub.html">NC hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "lakes-region-nh-mahjong-hub.html",
            "Lakes Region NH Mahjong | Laconia, Wolfeboro & Meredith",
            "Lakes Region NH mahjong — Laconia, Wolfeboro, Meredith, Lake Winnipesaukee.",
            "lakes region nh mahjong hub, laconia mah jongg",
            "Lakes Region NH Mahjong Guide",
            """<p><strong>Lakes Region NH mahjong</strong> — summer lake house private events:</p>
<p><a href="laconia-nh-mahjong.html">Laconia</a> · <a href="wolfeboro-nh-mahjong.html">Wolfeboro</a> · <a href="meredith-nh-mahjong.html">Meredith</a> · <a href="portsmouth-nh-mahjong.html">Portsmouth</a> · <a href="concord-nh-mahjong.html">Concord NH</a></p>
<p><a href="new-hampshire-mahjong-hub.html">NH hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "wisconsin-dells-mahjong-hub.html",
            "Wisconsin Dells Mahjong | Dells, Baraboo & Lake Delton",
            "Wisconsin Dells mahjong — family vacation and lake resort private events.",
            "wisconsin dells mahjong hub, lake delton mah jongg",
            "Wisconsin Dells Mahjong Guide",
            """<p><strong>Wisconsin Dells mahjong</strong> — waterpark vacation private lessons:</p>
<p><a href="wisconsin-dells-wi-mahjong.html">Wisconsin Dells</a> · <a href="baraboo-wi-mahjong.html">Baraboo</a> · <a href="madison-wi-mahjong.html">Madison</a> · <a href="milwaukee-wi-mahjong.html">Milwaukee</a></p>
<p><a href="wisconsin-mahjong-hub.html">Wisconsin hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "cape-cod-ma-mahjong-hub.html",
            "Cape Cod MA Mahjong | Hyannis, Provincetown & Chatham",
            "Cape Cod MA mahjong — Hyannis, Provincetown, Chatham, summer rental events.",
            "cape cod ma mahjong hub, hyannis mah jongg",
            "Cape Cod MA Mahjong Guide",
            """<p><strong>Cape Cod mahjong</strong> — seaside private lessons:</p>
<p><a href="cape-cod-mahjong.html">Cape Cod</a> · <a href="hyannis-ma-mahjong.html">Hyannis</a> · <a href="provincetown-ma-mahjong.html">Provincetown</a> · <a href="chatham-ma-mahjong.html">Chatham</a> · <a href="falmouth-ma-mahjong.html">Falmouth MA</a></p>
<p><a href="massachusetts-mahjong-hub.html">Massachusetts hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "pennsylvania-dutch-mahjong-hub.html",
            "Pennsylvania Dutch Country Mahjong | Lancaster, Hershey & York",
            "PA Dutch Country mahjong — Lancaster, Hershey, York, Amish country events.",
            "pennsylvania dutch country mahjong hub, lancaster pa mah jongg",
            "Pennsylvania Dutch Country Mahjong Guide",
            """<p><strong>PA Dutch Country mahjong</strong> — farmhouse and inn private lessons:</p>
<p><a href="lancaster-pa-mahjong.html">Lancaster PA</a> · <a href="hershey-pa-mahjong.html">Hershey</a> · <a href="york-pa-mahjong.html">York PA</a> · <a href="harrisburg-pa-mahjong.html">Harrisburg</a> · <a href="reading-pa-mahjong.html">Reading PA</a></p>
<p><a href="pennsylvania-mahjong-hub.html">Pennsylvania hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "tennessee-river-valley-mahjong-hub.html",
            "Tennessee River Valley Mahjong | Chattanooga, Knoxville & Decatur AL",
            "Tennessee River Valley mahjong — Chattanooga, Knoxville, Decatur AL corridor.",
            "tennessee river valley mahjong hub, chattanooga mah jongg",
            "Tennessee River Valley Mahjong Guide",
            """<p><strong>Tennessee River Valley mahjong</strong> — Lookout Mountain home region:</p>
<p><a href="chattanooga-mahjong.html">Chattanooga</a> · <a href="knoxville-mahjong.html">Knoxville</a> · <a href="decatur-al-mahjong.html">Decatur AL</a> · <a href="huntsville-mahjong.html">Huntsville</a> · <a href="lookout-mountain-georgia-mahjong.html">Lookout Mountain</a></p>
<p><a href="chattanooga-area-mahjong-hub.html">Chattanooga area</a> · <a href="tennessee-mahjong-hub.html">Tennessee hub</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE27_CITIES[WAVE28_CITY_START:]:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("alpha-tau-omega", "Alpha Tau Omega", "ATO"),
        ("beta-sigma-psi", "Beta Sigma Psi", "BSP"),
        ("delta-chi", "Delta Chi", "Delta Chi"),
        ("delta-psi", "Delta Psi", "St. Anthony Hall"),
        ("delta-tau-delta", "Delta Tau Delta", "DTD"),
        ("kappa-alpha-society", "Kappa Alpha Society", "KAS"),
        ("lambda-chi-alpha", "Lambda Chi Alpha", "Lambda Chi"),
        ("phi-delta-theta", "Phi Delta Theta", "Phi Delt"),
        ("phi-gamma-delta", "Phi Gamma Delta", "FIJI"),
        ("phi-kappa-theta", "Phi Kappa Theta", "PKT"),
        ("psi-upsilon", "Psi Upsilon", "Psi U"),
        ("sigma-alpha-epsilon", "Sigma Alpha Epsilon", "SAE"),
        ("sigma-nu", "Sigma Nu", "Sigma Nu"),
        ("theta-delta-chi", "Theta Delta Chi", "TDX"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("alpha-xi-delta", "Alpha Xi Delta", "AXiD"),
        ("chi-omega", "Chi Omega", "Chi O"),
        ("delta-gamma", "Delta Gamma", "DG"),
        ("gamma-phi-beta", "Gamma Phi Beta", "GPhiB"),
        ("kappa-delta", "Kappa Delta", "KD"),
        ("phi-mu", "Phi Mu", "Phi Mu"),
        ("pi-beta-phi", "Pi Beta Phi", "Pi Phi"),
        ("sigma-kappa", "Sigma Kappa", "Sigma Kappa"),
        ("theta-phi-alpha", "Theta Phi Alpha", "TPA"),
        ("zeta-tau-alpha", "Zeta Tau Alpha", "ZTA"),
        ("alpha-omicron-pi", "Alpha Omicron Pi", "AOII"),
        ("delta-zeta", "Delta Zeta", "DZ"),
        ("kappa-alpha-theta", "Kappa Alpha Theta", "Theta"),
        ("pi-kappa-phi", "Pi Kappa Phi", "Pi Kappa Phi"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ("national-mahjong-day", "National Mahjong Day", "national mahjong day — celebrate with a group lesson", '<p>Celebrate <strong>National Mahjong Day</strong> with a private lesson. <a href="mahjong-101.html">Mahjong 101</a> · <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("tile-tasting-party", "Tile Tasting Party", "tile tasting party mahjong — compare sets and learn", '<p>Host a <strong>tile tasting party</strong> — compare racks then play. <a href="mahjong-tiles.html">Tiles guide</a>.</p>'),
        ("nmjl-card-party", "NMJL Card Party", "nmjl card party mahjong — new card season kickoff", '<p>Kick off card season with an <strong>NMJL card party</strong>. <a href="read-nmjl-card.html">Read the card</a>.</p>'),
        ("mahjong-marathon", "Mahjong Marathon", "mahjong marathon — all-day tile event", '<p>Book a <strong>mahjong marathon</strong> for your club — breaks included. <a href="mahjong-tournament.html">Tournament</a>.</p>'),
        ("intro-to-mahjong-night", "Intro Night", "intro to mahjong night — beginners welcome", '<p><strong>Intro to mahjong night</strong> — zero experience welcome. <a href="mahjong-101.html">101</a> · <a href="learn-mahjong-hub.html">Learn hub</a>.</p>'),
        ("refresher-mahjong-clinic", "Refresher Clinic", "refresher mahjong clinic — returning players", '<p><strong>Refresher clinic</strong> for players returning after a break. <a href="mahjong-rules.html">Rules</a>.</p>'),
        ("charleston-practice-night", "Charleston Practice", "charleston practice night mahjong — pass drills", '<p>Master the <strong>Charleston</strong> with a practice night. <a href="mahjong-charleston.html">Charleston guide</a>.</p>'),
        ("joker-workshop", "Joker Workshop", "joker workshop mahjong — wild tile deep dive", '<p><strong>Joker workshop</strong> — exposures, redemption, strategy. <a href="mahjong-jokers.html">Jokers</a>.</p>'),
        ("quints-workshop", "Quints Workshop", "quints workshop mahjong — five-of-a-kind hands", '<p><strong>Quints workshop</strong> for advanced card hands. <a href="mahjong-quints.html">Quints</a>.</p>'),
        ("pairs-workshop", "Pairs Workshop", "pairs workshop mahjong — pair-only hands", '<p><strong>Pairs workshop</strong> — read pair categories on the card. <a href="mahjong-pair-requirement.html">Pair requirement</a>.</p>'),
        ("wedding-shower-mahjong", "Wedding Shower", "wedding shower mahjong — bridal shower with tiles", '<p>Upgrade the <strong>wedding shower</strong> with mahjong. <a href="wedding-mahjong.html">Wedding weekend</a> · <a href="bridal-shower-mahjong.html">Bridal shower</a>.</p>'),
        ("bachelorette-mahjong", "Bachelorette Party", "bachelorette mahjong — bride tribe tiles", '<p><strong>Bachelorette mahjong</strong> — the group chat will thank you. <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("engagement-party-mahjong", "Engagement Party", "engagement party mahjong — celebrate with tiles", '<p>Celebrate your <strong>engagement party</strong> with a mahjong lesson. <a href="cocktail-mahjong.html">Cocktail party</a>.</p>'),
        ("retirement-sendoff-mahjong", "Retirement Sendoff", "retirement sendoff mahjong — office farewell with tiles", '<p>Send them off with <strong>retirement sendoff mahjong</strong>. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("office-holiday-party-mahjong", "Office Holiday Party", "office holiday party mahjong — December team event", '<p>Add tiles to your <strong>office holiday party</strong>. <a href="holiday-party-mahjong.html">Holiday party</a>.</p>'),
        ("summer-camp-counselor-mahjong", "Summer Camp Counselor", "summer camp counselor mahjong — camp staff night", '<p><strong>Camp counselor mahjong</strong> — screen-free staff fun. <a href="summer-camp-mahjong.html">Summer camp</a>.</p>'),
        ("college-reunion-mahjong", "College Reunion", "college reunion mahjong — alumni weekend tiles", '<p><strong>College reunion mahjong</strong> — class years mix at the table. <a href="college-alumni-mahjong.html">Alumni</a>.</p>'),
        ("high-school-reunion-mahjong", "High School Reunion", "high school reunion mahjong — hometown gathering", '<p>Book <strong>high school reunion mahjong</strong> for your weekend. <a href="reunion-mahjong.html">Reunion</a>.</p>'),
        ("military-spouses-club-mahjong", "Military Spouses Club", "military spouses club mahjong — base social with tiles", '<p><strong>Military spouses club mahjong</strong> — community and connection. <a href="military-mahjong.html">Military</a>.</p>'),
        ("baseball-watch-party-mahjong", "Baseball Watch Party", "baseball watch party mahjong — pregame tiles", '<p>Pregame <strong>baseball watch party mahjong</strong> for fans who want tiles. <a href="tailgate-mahjong.html">Tailgate</a>.</p>'),
        ("kentucky-derby-party-mahjong", "Kentucky Derby Party", "kentucky derby party mahjong — derby day social", '<p><strong>Kentucky Derby party mahjong</strong> — hats optional. <a href="cocktail-mahjong.html">Cocktail</a>.</p>'),
        ("kentucky-derby-brunch-mahjong", "Derby Brunch", "derby brunch mahjong — May brunch with tiles", '<p><strong>Derby brunch mahjong</strong> — mint juleps and tiles. <a href="mahjong-brunch.html">Brunch</a>.</p>'),
        ("halloween-costume-mahjong", "Halloween Costume Party", "halloween costume party mahjong — October social", '<p><strong>Halloween costume mahjong</strong> — spooky fun. <a href="halloween-mahjong.html">Halloween</a>.</p>'),
        ("day-after-thanksgiving-mahjong", "Day After Thanksgiving", "day after thanksgiving mahjong — Friday family tiles", '<p><strong>Day after Thanksgiving mahjong</strong> — Black Friday alternative. <a href="thanksgiving-mahjong.html">Thanksgiving</a>.</p>'),
        ("christmas-eve-mahjong", "Christmas Eve", "christmas eve mahjong — family gathering with tiles", '<p><strong>Christmas Eve mahjong</strong> — multigenerational fun. <a href="christmas-mahjong.html">Christmas</a>.</p>'),
        ("boxing-day-mahjong", "Boxing Day", "boxing day mahjong — December 26 gathering", '<p><strong>Boxing Day mahjong</strong> for houseguests. <a href="holiday-mahjong.html">Holiday</a>.</p>'),
        ("snow-day-mahjong", "Snow Day", "snow day mahjong — school closure activity", '<p>Rainy or <strong>snow day mahjong</strong> — screen-free indoors. <a href="winter-mahjong.html">Winter</a>.</p>'),
        ("hurricane-prep-mahjong", "Storm Day Indoors", "storm day indoors mahjong — weather closure activity", '<p>When the storm keeps you in — <strong>storm day mahjong</strong>. <a href="rainy-day-mahjong.html">Rainy day</a>.</p>'),
        ("power-outage-mahjong", "Power Outage Party", "power outage party mahjong — candles and tiles", '<p>No Wi‑Fi? <strong>Power outage mahjong</strong> saves the day. <a href="screen-free-game-night.html">Screen-free</a>.</p>'),
        ("moving-party-mahjong", "Moving Party", "moving party mahjong — housewarming with tiles", '<p>New keys? Host <strong>moving party mahjong</strong>. <a href="housewarming-mahjong.html">Housewarming</a>.</p>'),
        ("open-house-mahjong", "Open House", "open house mahjong — realtor event with tiles", '<p>Draw crowds at your <strong>open house</strong> with mahjong. <a href="realtor-mahjong.html">Realtor</a>.</p>'),
        ("closing-gift-mahjong", "Closing Gift Lesson", "closing gift mahjong lesson — gift a lesson at closing", '<p>Gift a <strong>closing mahjong lesson</strong> to new homeowners. <a href="realtor-mahjong.html">Realtor</a>.</p>'),
        ("airbnb-experience-mahjong", "Airbnb Experience", "airbnb experience mahjong — vacation rental add-on", '<p>Offer an <strong>Airbnb experience</strong> mahjong lesson. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("vrbo-welcome-mahjong", "VRBO Welcome", "vrbo welcome mahjong — rental welcome activity", '<p>Welcome <strong>VRBO guests</strong> with a mahjong lesson. <a href="vacation-rental-mahjong.html">Vacation rental</a>.</p>'),
        ("cruise-shore-excursion-mahjong", "Cruise Shore Excursion", "cruise shore excursion mahjong — port day private lesson", '<p>Port day <strong>cruise shore excursion mahjong</strong>. <a href="cruise-mahjong.html">Cruise</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("mahjong-declare-win.html", "Declare Mahjong", "declare mahjong — calling mahjong on a win", '<p><strong>Declare mahjong</strong> when your hand is complete. <a href="calling-mahjong.html">Calling</a> · <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-false-mahjong.html", "False Mahjong", "false mahjong — incorrect win declaration", '<p><strong>False mahjong</strong> may penalize your hand. <a href="foul-hand-mahjong.html">Foul hand</a>.</p>'),
        ("mahjong-exposure-limit.html", "Exposure Limit", "exposure limit in mahjong — max exposures per hand", '<p>Know the <strong>exposure limit</strong> on your NMJL hand. <a href="mahjong-exposure-rules.html">Exposure rules</a>.</p>'),
        ("mahjong-joker-count.html", "Joker Count", "joker count in mahjong — how many jokers in the set", '<p>American sets include <strong>eight jokers</strong> — <a href="mahjong-jokers.html">Jokers guide</a>.</p>'),
        ("mahjong-flower-tiles.html", "Flower Tiles", "flower tiles in mahjong — using flowers in American play", '<p><strong>Flower tiles</strong> — see NMJL card for your year. <a href="mahjong-tiles.html">Tiles</a>.</p>'),
        ("mahjong-wind-round.html", "Wind Round", "wind round in mahjong — when winds rotate", '<p><strong>Wind rounds</strong> — east deals first; winds rotate after wins. <a href="mahjong-winds.html">Winds</a>.</p>'),
        ("mahjong-pay-the-winner.html", "Pay the Winner", "pay the winner in mahjong — casual scoring between players", '<p>Many groups <strong>pay the winner</strong> — agree stakes first. <a href="mahjong-scoring.html">Scoring</a>.</p>'),
        ("mahjong-table-rotation.html", "Table Rotation", "table rotation in mahjong — switching tables at parties", '<p><strong>Table rotation</strong> keeps party play fresh. <a href="mahjong-etiquette.html">Etiquette</a>.</p>'),
        ("mahjong-sit-out.html", "Sit Out a Hand", "sit out a hand in mahjong — when a player skips a deal", '<p>You may <strong>sit out</strong> between deals at casual tables. <a href="mahjong-etiquette.html">Etiquette</a>.</p>'),
        ("mahjong-new-player-seat.html", "New Player Seat", "new player seat in mahjong — where beginners sit", '<p>Seat <strong>new players</strong> between experienced players when possible. <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-rack-review.html", "Rack Review", "rack review in mahjong — checking exposures before discard", '<p>Quick <strong>rack review</strong> before each discard avoids errors. <a href="rack-order-mahjong.html">Rack order</a>.</p>'),
        ("mahjong-call-priority.html", "Call Priority", "call priority in mahjong — who wins a contested discard", '<p><strong>Call priority</strong> — mahjong beats kong beats pung. <a href="mahjong-call-rules.html">Call rules</a>.</p>'),
        ("mahjong-same-turn-kong.html", "Same Turn Kong", "same turn kong in mahjong — drawing replacement after kong", '<p>After a <strong>kong</strong>, draw a replacement tile from the wall end. <a href="mahjong-kong.html">Kong</a>.</p>'),
        ("mahjong-replace-flower.html", "Replace Flower", "replace flower in mahjong — drawing after a flower", '<p>Some tables <strong>replace flowers</strong> with a wall draw — check house rules. <a href="mahjong-flower-tiles.html">Flowers</a>.</p>'),
        ("mahjong-wall-game-tie.html", "Wall Game Tie", "wall game tie in mahjong — no winner when wall ends", '<p>A <strong>wall game</strong> — no winner — redeals the hand. <a href="mahjong-wall-game.html">Wall game</a>.</p>'),
        ("mahjong-pick-from-wall.html", "Pick from Wall", "pick from wall in mahjong — drawing your turn tile", '<p>On your turn, <strong>pick from the wall</strong> unless you called a discard. <a href="mahjong-turn-order.html">Turn order</a>.</p>'),
        ("mahjong-discard-pile.html", "Discard Pile", "discard pile in mahjong — face-up discards in center", '<p>The <strong>discard pile</strong> — only the latest discard may be called. <a href="calling-mahjong.html">Calling</a>.</p>'),
        ("mahjong-hand-only-tiles.html", "Hand Only Tiles", "hand only tiles in mahjong — tiles needed from your hand alone", '<p>Some categories need <strong>hand only tiles</strong> — read the card. <a href="read-nmjl-card.html">Read the card</a>.</p>'),
        ("mahjong-minimum-points.html", "Minimum Points", "minimum points in mahjong — American NMJL has no point score", '<p>American NMJL uses <strong>card categories</strong>, not point minimums. <a href="read-nmjl-card.html">Read the card</a>.</p>'),
        ("mahjong-table-language.html", "Table Language", "table language in mahjong — calling tiles clearly", '<p>Use clear <strong>table language</strong> — name the tile when calling. <a href="mahjong-etiquette.html">Etiquette</a>.</p>'),
        ("mahjong-verify-win.html", "Verify Win", "verify win in mahjong — checking hand before exposing", '<p><strong>Verify your win</strong> before exposing all tiles. <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-teach-at-table.html", "Teach at Table", "teach at table in mahjong — coaching during play", '<p>We teach <strong>at the table</strong> in lessons — casual play may allow hints. <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("mahjong-slow-play.html", "Slow Play", "slow play in mahjong — pace and courtesy", '<p>Avoid <strong>slow play</strong> — plan during others\' turns. <a href="mahjong-table-speed.html">Table speed</a>.</p>'),
        ("mahjong-fast-charleston.html", "Fast Charleston", "fast charleston in mahjong — speeding up passes", '<p><strong>Fast Charleston</strong> — pass quickly, verify counts. <a href="mahjong-charleston.html">Charleston</a>.</p>'),
        ("mahjong-optional-second-charleston.html", "Second Charleston", "second charleston in mahjong — optional extra pass round", '<p>NMJL includes an <strong>optional second Charleston</strong>. <a href="second-charleston-round-mahjong.html">Second round</a>.</p>'),
        ("mahjong-courtesy-pass-left.html", "Courtesy Pass Left", "courtesy pass left in mahjong — final optional pass", '<p>Some tables pass one tile <strong>courtesy left</strong> after Charleston. <a href="charleston-courtesy-mahjong.html">Courtesy pass</a>.</p>'),
        ("mahjong-claim-stop-turn.html", "Claim Stops Turn", "claim stops turn in mahjong — calling ends the discarder's turn", '<p>A <strong>claim stops the turn</strong> — exposure then discard. <a href="calling-mahjong.html">Calling</a>.</p>'),
        ("mahjong-next-player-discard.html", "Next Player Discard", "next player discard in mahjong — turn order after pass", '<p>After Charleston, <strong>east discards first</strong>. <a href="east-seat-mahjong.html">East seat</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
