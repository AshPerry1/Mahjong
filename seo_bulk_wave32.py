# -*- coding: utf-8 -*-
"""Mega Wave 32 — ~600+ pages (500 cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave32_cities_data import WAVE32_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_32(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "olympic-peninsula-wa-mahjong-hub.html",
            "Olympic Peninsula WA Mahjong | Port Angeles & Sequim",
            "Olympic Peninsula WA mahjong — Port Angeles, Sequim, Olympic National Park corridor events.",
            "olympic peninsula washington mahjong hub, port angeles mah jongg",
            "Olympic Peninsula WA Mahjong Guide",
            """<p><strong>Olympic Peninsula mahjong</strong> — rainforest coast private lessons:</p>
<p><a href="port-angeles-wa-mahjong.html">Port Angeles</a> · <a href="sequim-wa-mahjong.html">Sequim</a> · <a href="olympia-wa-mahjong.html">Olympia</a> · <a href="bellingham-wa-mahjong.html">Bellingham</a></p>
<p><a href="washington-mahjong-hub.html">Washington hub</a> · <a href="pacific-northwest-mahjong-hub.html">PNW hub</a></p>""",
        ),
        (
            "rio-grande-valley-tx-mahjong-hub.html",
            "Rio Grande Valley TX Mahjong | McAllen, Brownsville & Harlingen",
            "Rio Grande Valley TX mahjong — McAllen, Brownsville, Harlingen border region private events.",
            "rio grande valley texas mahjong hub, mcallen mah jongg",
            "Rio Grande Valley TX Mahjong Guide",
            """<p><strong>RGV mahjong</strong> — South Texas private lessons:</p>
<p><a href="mcallen-tx-mahjong.html">McAllen</a> · <a href="brownsville-tx-mahjong.html">Brownsville</a> · <a href="harlingen-tx-mahjong.html">Harlingen</a> · <a href="laredo-tx-mahjong.html">Laredo</a></p>
<p><a href="texas-mahjong-hub.html">Texas hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "lehigh-valley-pa-mahjong-hub.html",
            "Lehigh Valley PA Mahjong | Allentown, Bethlehem & Easton",
            "Lehigh Valley PA mahjong — Allentown, Bethlehem, Easton private events.",
            "lehigh valley pennsylvania mahjong hub, allentown mah jongg",
            "Lehigh Valley PA Mahjong Guide",
            """<p><strong>Lehigh Valley mahjong</strong> — eastern PA private lessons:</p>
<p><a href="allentown-pa-mahjong.html">Allentown</a> · <a href="bethlehem-pa-mahjong.html">Bethlehem</a> · <a href="easton-pa-mahjong.html">Easton PA</a> · <a href="reading-pa-mahjong.html">Reading</a></p>
<p><a href="pennsylvania-mahjong-hub.html">Pennsylvania hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "golden-isles-ga-mahjong-hub.html",
            "Golden Isles GA Mahjong | St. Simons, Jekyll & Brunswick",
            "Golden Isles Georgia mahjong — St. Simons, Jekyll Island, Brunswick coast private events.",
            "golden isles georgia mahjong hub, st simons mah jongg",
            "Golden Isles GA Mahjong Guide",
            """<p><strong>Golden Isles mahjong</strong> — Georgia coast private lessons:</p>
<p><a href="saint-simons-mahjong.html">St. Simons</a> · <a href="jekyll-island-ga-mahjong.html">Jekyll Island</a> · <a href="brunswick-ga-mahjong.html">Brunswick GA</a> · <a href="savannah-mahjong.html">Savannah</a></p>
<p><a href="georgia-coast-mahjong-hub.html">GA Coast hub</a> · <a href="georgia-mahjong-hub.html">Georgia hub</a></p>""",
        ),
        (
            "flint-hills-ks-mahjong-hub.html",
            "Flint Hills KS Mahjong | Manhattan & Emporia",
            "Flint Hills Kansas mahjong — Manhattan, Emporia, tallgrass prairie region private events.",
            "flint hills kansas mahjong hub, manhattan ks mah jongg",
            "Flint Hills KS Mahjong Guide",
            """<p><strong>Flint Hills mahjong</strong> — Kansas prairie private lessons:</p>
<p><a href="manhattan-ks-mahjong.html">Manhattan KS</a> · <a href="emporia-ks-mahjong.html">Emporia</a> · <a href="topeka-ks-mahjong.html">Topeka</a> · <a href="wichita-ks-mahjong.html">Wichita</a></p>
<p><a href="kansas-mahjong-hub.html">Kansas hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "palouse-wa-mahjong-hub.html",
            "Palouse WA Mahjong | Pullman & Moscow Area",
            "Palouse WA mahjong — Pullman, Moscow ID area, university corridor private events.",
            "palouse washington mahjong hub, pullman mah jongg",
            "Palouse WA Mahjong Guide",
            """<p><strong>Palouse mahjong</strong> — wheat country private lessons:</p>
<p><a href="pullman-wa-mahjong.html">Pullman</a> · <a href="moscow-id-mahjong.html">Moscow ID</a> · <a href="spokane-wa-mahjong.html">Spokane</a> · <a href="lewiston-id-mahjong.html">Lewiston</a></p>
<p><a href="washington-mahjong-hub.html">Washington hub</a> · <a href="idaho-mahjong-hub.html">Idaho hub</a></p>""",
        ),
        (
            "sonoran-desert-az-mahjong-hub.html",
            "Sonoran Desert AZ Mahjong | Scottsdale, Tucson & Sedona",
            "Sonoran Desert AZ mahjong — Scottsdale, Tucson, Sedona, desert resort private events.",
            "sonoran desert arizona mahjong hub, scottsdale mah jongg",
            "Sonoran Desert AZ Mahjong Guide",
            """<p><strong>Sonoran Desert mahjong</strong> — AZ resort and metro private lessons:</p>
<p><a href="scottsdale-az-mahjong.html">Scottsdale</a> · <a href="tucson-az-mahjong.html">Tucson</a> · <a href="sedona-az-mahjong.html">Sedona</a> · <a href="phoenix-mahjong.html">Phoenix</a></p>
<p><a href="arizona-mahjong-hub.html">Arizona hub</a> · <a href="southwest-mahjong-hub.html">Southwest hub</a></p>""",
        ),
        (
            "wine-country-va-mahjong-hub.html",
            "Virginia Wine Country Mahjong | Charlottesville & Middleburg",
            "Virginia wine country mahjong — Charlottesville, Middleburg, vineyard weekend private events.",
            "virginia wine country mahjong hub, charlottesville mah jongg",
            "Virginia Wine Country Mahjong Guide",
            """<p><strong>VA wine country mahjong</strong> — vineyard corridor private lessons:</p>
<p><a href="charlottesville-va-mahjong.html">Charlottesville</a> · <a href="middleburg-va-mahjong.html">Middleburg</a> · <a href="winchester-va-mahjong.html">Winchester</a> · <a href="richmond-mahjong.html">Richmond</a></p>
<p><a href="virginia-mahjong-hub.html">Virginia hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "north-shore-ma-mahjong-hub.html",
            "North Shore MA Mahjong | Salem, Gloucester & Newburyport",
            "North Shore Massachusetts mahjong — Salem, Gloucester, Newburyport coastal private events.",
            "north shore massachusetts mahjong hub, salem ma mah jongg",
            "North Shore MA Mahjong Guide",
            """<p><strong>North Shore mahjong</strong> — coastal MA private lessons:</p>
<p><a href="salem-ma-mahjong.html">Salem MA</a> · <a href="gloucester-ma-mahjong.html">Gloucester</a> · <a href="newburyport-ma-mahjong.html">Newburyport</a> · <a href="boston-mahjong.html">Boston</a></p>
<p><a href="massachusetts-mahjong-hub.html">Massachusetts hub</a> · <a href="new-england-mahjong-hub.html">New England</a></p>""",
        ),
        (
            "poconos-pa-mahjong-hub.html",
            "Poconos PA Mahjong | Stroudsburg & Lake Wallenpaupack",
            "Poconos Pennsylvania mahjong — Stroudsburg, mountain resorts, lake country private events.",
            "poconos pennsylvania mahjong hub, stroudsburg mah jongg",
            "Poconos PA Mahjong Guide",
            """<p><strong>Poconos mahjong</strong> — mountain getaway private lessons:</p>
<p><a href="stroudsburg-pa-mahjong.html">Stroudsburg</a> · <a href="scranton-pa-mahjong.html">Scranton</a> · <a href="wilkes-barre-pa-mahjong.html">Wilkes-Barre</a> · <a href="harrisburg-pa-mahjong.html">Harrisburg</a></p>
<p><a href="pennsylvania-mahjong-hub.html">Pennsylvania hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "willamette-valley-or-mahjong-hub.html",
            "Willamette Valley OR Mahjong | Eugene, Salem & Corvallis",
            "Willamette Valley Oregon mahjong — Eugene, Salem, Corvallis, wine and university corridor.",
            "willamette valley oregon mahjong hub, eugene mah jongg",
            "Willamette Valley OR Mahjong Guide",
            """<p><strong>Willamette Valley mahjong</strong> — Oregon valley private lessons:</p>
<p><a href="eugene-or-mahjong.html">Eugene</a> · <a href="salem-or-mahjong.html">Salem OR</a> · <a href="corvallis-or-mahjong.html">Corvallis</a> · <a href="portland-mahjong.html">Portland</a></p>
<p><a href="oregon-mahjong-hub.html">Oregon hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "driftless-region-wi-mahjong-hub.html",
            "Driftless Region WI Mahjong | La Crosse & Viroqua",
            "Driftless Region Wisconsin mahjong — La Crosse, Viroqua, bluff country private events.",
            "driftless region wisconsin mahjong hub, la crosse mah jongg",
            "Driftless Region WI Mahjong Guide",
            """<p><strong>Driftless Region mahjong</strong> — bluff country private lessons:</p>
<p><a href="la-crosse-wi-mahjong.html">La Crosse</a> · <a href="viroqua-wi-mahjong.html">Viroqua</a> · <a href="madison-wi-mahjong.html">Madison</a> · <a href="dubuque-ia-mahjong.html">Dubuque</a></p>
<p><a href="wisconsin-mahjong-hub.html">Wisconsin hub</a> · <a href="iowa-mahjong-hub.html">Iowa hub</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE32_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("acacia", "Acacia", "Acacia"),
        ("alpha-kappa-lambda", "Alpha Kappa Lambda", "AKL"),
        ("alpha-phi-alpha", "Alpha Phi Alpha", "Alpha Phi Alpha"),
        ("alpha-tau-omega", "Alpha Tau Omega", "ATO"),
        ("beta-sigma-psi", "Beta Sigma Psi", "Beta Sig Psi"),
        ("chi-phi", "Chi Phi", "Chi Phi"),
        ("delta-kappa-epsilon", "Delta Kappa Epsilon", "DKE"),
        ("farmhouse", "FarmHouse", "FarmHouse"),
        ("kappa-alpha-psi", "Kappa Alpha Psi", "Kappa Alpha Psi"),
        ("lambda-chi-alpha", "Lambda Chi Alpha", "Lambda Chi"),
        ("omega-psi-phi", "Omega Psi Phi", "Omega Psi Phi"),
        ("phi-beta-sigma", "Phi Beta Sigma", "Phi Beta Sigma"),
        ("phi-iota-alpha", "Phi Iota Alpha", "Phi Iota"),
        ("psi-upsilon", "Psi Upsilon", "Psi U"),
        ("sigma-alpha-mu", "Sigma Alpha Mu", "Sammy"),
        ("sigma-phi-sigma", "Sigma Phi Sigma", "Sigma Phi Sigma"),
        ("tau-epsilon-phi", "Tau Epsilon Phi", "TEP"),
        ("theta-tau", "Theta Tau", "Theta Tau"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("alpha-beta-chi", "Alpha Beta Chi", "ABC"),
        ("alpha-epsilon-phi", "Alpha Epsilon Phi", "AEPhi"),
        ("alpha-phi-gamma", "Alpha Phi Gamma", "APG"),
        ("alpha-sigma-gamma", "Alpha Sigma Gamma", "ASG"),
        ("chi-upsilon-sigma", "Chi Upsilon Sigma", "CUS"),
        ("gamma-alpha-omega", "Gamma Alpha Omega", "GAO"),
        ("kappa-phi-lambda", "Kappa Phi Lambda", "KPL"),
        ("sigma-alpha-omega", "Sigma Alpha Omega", "SAO"),
        ("sigma-gamma-rho", "Sigma Gamma Rho", "SGRho"),
        ("sigma-iota-alpha", "Sigma Iota Alpha", "SIA"),
        ("theta-alpha", "Theta Alpha", "Theta Alpha"),
        ("theta-upsilon", "Theta Upsilon", "Theta Upsilon"),
        ("alpha-kappa-delta-phi", "Alpha Kappa Delta Phi", "aKDPhi"),
        ("delta-phi-lambda", "Delta Phi Lambda", "DPhiL"),
        ("lambda-phi-epsilon-sorority", "Lambda Phi Epsilon", "LPhiE"),
        ("phi-alpha", "Phi Alpha", "Phi Alpha"),
        ("sigma-beta-rho", "Sigma Beta Rho", "Sig Rho"),
        ("tau-omega-phi", "Tau Omega Phi", "TOP"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ("mahjong-lunch-learn", "Lunch and Learn", "lunch and learn mahjong — midday office lesson", '<p><strong>Lunch and learn mahjong</strong> — 90-minute power lesson. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("happy-hour-mahjong", "Happy Hour", "happy hour mahjong — after-work tile social", '<p><strong>Happy hour mahjong</strong> — drinks optional, tiles required. <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("sunrise-mahjong", "Sunrise Session", "sunrise mahjong — early morning beach week tiles", '<p><strong>Sunrise mahjong</strong> — before the beach crowd. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("sunset-mahjong", "Sunset Session", "sunset mahjong — golden hour tile night", '<p><strong>Sunset mahjong</strong> — porch views and tiles. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("midweek-break", "Midweek Break", "midweek break mahjong — Wednesday escape tiles", '<p><strong>Midweek break mahjong</strong> — hump day upgrade. <a href="ladies-luncheon-mahjong.html">Luncheon</a>.</p>'),
        ("sunday-supper", "Sunday Supper", "sunday supper mahjong — supper club with tiles", '<p><strong>Sunday supper mahjong</strong> — dine then deal. <a href="supper-club-mahjong.html">Supper club</a>.</p>'),
        ("monday-motivation", "Monday Motivation", "monday motivation mahjong — start the week with tiles", '<p><strong>Monday motivation mahjong</strong> — book club energy. <a href="book-club-mahjong.html">Book club</a>.</p>'),
        ("friday-fundays", "Friday Funday", "friday funday mahjong — end of week tile party", '<p><strong>Friday funday mahjong</strong> — office optional. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("staycation-mahjong", "Staycation", "staycation mahjong — local luxury staycation tiles", '<p><strong>Staycation mahjong</strong> — hotel suite or home spa day. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("babymoon-mahjong", "Babymoon", "babymoon mahjong — pre-baby couples getaway tiles", '<p><strong>Babymoon mahjong</strong> — relaxed pace lesson. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("push-present-party", "Push Present Party", "push present party mahjong — celebrate new baby", '<p><strong>Push present party mahjong</strong> — shower alternative. <a href="baby-shower-mahjong.html">Baby shower</a>.</p>'),
        ("gender-reveal", "Gender Reveal", "gender reveal mahjong — reveal party activity", '<p><strong>Gender reveal mahjong</strong> — keep guests entertained. <a href="baby-shower-mahjong.html">Baby shower</a>.</p>'),
        ("sip-and-paint-mahjong", "Sip and Paint", "sip and paint mahjong — creative night crossover", '<p><strong>Sip and paint mahjong</strong> — art then tiles. <a href="craft-night-mahjong.html">Craft night</a>.</p>'),
        ("cookie-exchange", "Cookie Exchange", "cookie exchange mahjong — holiday cookie swap tiles", '<p><strong>Cookie exchange mahjong</strong> — December tradition. <a href="holiday-mahjong-party.html">Holiday party</a>.</p>'),
        ("ornament-exchange", "Ornament Exchange", "ornament exchange mahjong — ornament swap tile night", '<p><strong>Ornament exchange mahjong</strong> — festive add-on. <a href="christmas-mahjong-party.html">Christmas party</a>.</p>'),
        ("super-bowl-party", "Super Bowl Party", "super bowl party mahjong — pregame tile station", '<p><strong>Super Bowl party mahjong</strong> — halftime hero. <a href="tailgate-mahjong.html">Tailgate</a>.</p>'),
        ("kentucky-derby-party", "Derby Party", "kentucky derby party mahjong — derby day tiles", '<p><strong>Derby party mahjong</strong> — hats and hands. <a href="kentucky-bluegrass-mahjong-hub.html">Bluegrass</a>.</p>'),
        ("masters-weekend", "Masters Weekend", "masters weekend mahjong — Augusta area tile night", '<p><strong>Masters weekend mahjong</strong> — golf trip add-on. <a href="augusta-ga-mahjong.html">Augusta</a>.</p>'),
        ("wine-harvest", "Wine Harvest", "wine harvest mahjong — fall crush season tiles", '<p><strong>Wine harvest mahjong</strong> — vineyard weekend. <a href="wine-and-mahjong.html">Wine night</a>.</p>'),
        ("apple-orchard", "Apple Orchard", "apple orchard mahjong — fall orchard outing tiles", '<p><strong>Apple orchard mahjong</strong> — cider then play. <a href="fall-mahjong-party.html">Fall party</a>.</p>'),
        ("pumpkin-patch", "Pumpkin Patch", "pumpkin patch mahjong — fall family outing tiles", '<p><strong>Pumpkin patch mahjong</strong> — group lesson after picking. <a href="fall-mahjong-party.html">Fall party</a>.</p>'),
        ("corn-maze", "Corn Maze", "corn maze mahjong — farm fall festival tiles", '<p><strong>Corn maze mahjong</strong> — farm venue fun. <a href="community-center-mahjong.html">Community</a>.</p>'),
        ("easter-brunch", "Easter Brunch", "easter brunch mahjong — spring brunch tiles", '<p><strong>Easter brunch mahjong</strong> — family gathering. <a href="easter-mahjong.html">Easter</a>.</p>'),
        ("passover-seder", "Passover Gathering", "passover gathering mahjong — post-seder social tiles", '<p><strong>Passover gathering mahjong</strong> — multigenerational fun. <a href="family-reunion-mahjong.html">Family</a>.</p>'),
        ("ramadan-iftar", "Iftar Social", "iftar social mahjong — community iftar add-on tiles", '<p><strong>Iftar social mahjong</strong> — respectful social format. <a href="community-center-mahjong.html">Community</a>.</p>'),
        ("diwali-party", "Diwali Party", "diwali party mahjong — festival of lights tile night", '<p><strong>Diwali party mahjong</strong> — celebrate with play. <a href="holiday-mahjong-party.html">Holiday party</a>.</p>'),
        ("lunar-new-year", "Lunar New Year", "lunar new year mahjong — lunar new year tile tradition", '<p><strong>Lunar New Year mahjong</strong> — cultural crossover. <a href="chinese-new-year-mahjong.html">Chinese New Year</a>.</p>'),
        ("st-patricks-social", "St Patricks Social", "st patricks social mahjong — march social tile night", '<p><strong>St Patrick\'s social mahjong</strong> — green tiles optional. <a href="st-patricks-day-mahjong.html">St Patricks</a>.</p>'),
        ("cinco-de-mayo", "Cinco de Mayo", "cinco de mayo mahjong — may fiesta tile night", '<p><strong>Cinco de Mayo mahjong</strong> — festive group lesson. <a href="holiday-mahjong-party.html">Holiday party</a>.</p>'),
        ("memorial-day-weekend", "Memorial Day Weekend", "memorial day weekend mahjong — lake house tile kickoff", '<p><strong>Memorial Day weekend mahjong</strong> — summer starts here. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("labor-day-weekend", "Labor Day Weekend", "labor day weekend mahjong — end of summer tile night", '<p><strong>Labor Day weekend mahjong</strong> — last lake trip. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("veterans-day", "Veterans Day", "veterans day mahjong — honor veterans with tile social", '<p><strong>Veterans Day mahjong</strong> — community hall event. <a href="civic-club-mahjong.html">Civic club</a>.</p>'),
        ("flag-day", "Flag Day", "flag day mahjong — patriotic community tiles", '<p><strong>Flag Day mahjong</strong> — civic group social. <a href="civic-club-mahjong.html">Civic club</a>.</p>'),
        ("election-night", "Election Night", "election night mahjong — distract while results roll", '<p><strong>Election night mahjong</strong> — stress relief tiles. <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("inauguration-watch", "Inauguration Watch", "inauguration watch mahjong — watch party tile break", '<p><strong>Inauguration watch mahjong</strong> — living room lesson. <a href="dinner-party-mahjong.html">Dinner party</a>.</p>'),
        ("oscar-party", "Oscar Party", "oscar party mahjong — awards night tile intermission", '<p><strong>Oscar party mahjong</strong> — commercial break fun. <a href="dinner-party-mahjong.html">Dinner party</a>.</p>'),
        ("book-launch", "Book Launch", "book launch mahjong — author event crossover tiles", '<p><strong>Book launch mahjong</strong> — bookstore event. <a href="book-club-mahjong.html">Book club</a>.</p>'),
        ("podcast-live", "Podcast Live", "podcast live mahjong — live show audience tiles", '<p><strong>Podcast live mahjong</strong> — fan community night. <a href="community-center-mahjong.html">Community</a>.</p>'),
        ("influencer-event", "Influencer Event", "influencer event mahjong — content creator tile night", '<p><strong>Influencer event mahjong</strong> — photogenic tiles. <a href="viral-mahjong.html">Viral mahjong</a>.</p>'),
        ("pop-up-mahjong", "Pop-Up Event", "pop up mahjong — temporary pop-up tile lesson", '<p><strong>Pop-up mahjong</strong> — retail or market activation. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("farmers-market", "Farmers Market", "farmers market mahjong — market day demo tiles", '<p><strong>Farmers market mahjong</strong> — demo table. <a href="community-center-mahjong.html">Community</a>.</p>'),
        ("flea-market", "Flea Market", "flea market mahjong — vintage market tile demo", '<p><strong>Flea market mahjong</strong> — vintage tile curiosity. <a href="mahjong-tiles.html">Tiles</a>.</p>'),
        ("antique-show", "Antique Show", "antique show mahjong — antique show social tiles", '<p><strong>Antique show mahjong</strong> — collector crowd. <a href="mahjong-tiles.html">Tiles</a>.</p>'),
        ("estate-sale", "Estate Sale", "estate sale mahjong — estate sale group finds tiles", '<p><strong>Estate sale mahjong</strong> — neighborhood social. <a href="neighborhood-mahjong.html">Neighborhood</a>.</p>'),
        ("garage-sale-day", "Garage Sale Day", "garage sale day mahjong — block sale tile station", '<p><strong>Garage sale day mahjong</strong> — block party energy. <a href="block-party-mahjong.html">Block party</a>.</p>'),
        ("neighborhood-watch", "Neighborhood Watch", "neighborhood watch mahjong — safety night social tiles", '<p><strong>Neighborhood watch mahjong</strong> — meet the neighbors. <a href="hoa-mahjong.html">HOA</a>.</p>'),
        ("welcome-wagon", "Welcome Wagon", "welcome wagon mahjong — new neighbor welcome tiles", '<p><strong>Welcome wagon mahjong</strong> — introduce the block. <a href="neighborhood-mahjong.html">Neighborhood</a>.</p>'),
        ("going-away-party", "Going Away Party", "going away party mahjong — send-off tile night", '<p><strong>Going away party mahjong</strong> — one last hurrah. <a href="relocation-mahjong.html">Relocation</a>.</p>'),
        ("welcome-back", "Welcome Back", "welcome back mahjong — return from assignment tiles", '<p><strong>Welcome back mahjong</strong> — home again. <a href="military-wives-mahjong.html">Military</a>.</p>'),
        ("house-sitting", "House Sitting", "house sitting mahjong — housesit week tile night", '<p><strong>House sitting mahjong</strong> — use the great room. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("pet-sitting", "Pet Sitting", "pet sitting mahjong — pet sitter friend group tiles", '<p><strong>Pet sitting mahjong</strong> — dogs welcome off-table. <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("mahjong-call-wait.html", "Call Wait", "call wait in mahjong — waiting after a call", '<p>After a <strong>call</strong> — know when you must wait — <a href="mahjong-call-rules.html">Call rules</a>.</p>'),
        ("mahjong-exposure-order.html", "Exposure Order", "exposure order in mahjong — order of melds on rack", '<p><strong>Exposure order</strong> — left to right convention — <a href="rack-order-mahjong.html">Rack order</a>.</p>'),
        ("mahjong-joker-count.html", "Joker Count", "joker count in mahjong — how many jokers in the set", '<p>Standard set <strong>joker count</strong> — <a href="mahjong-jokers.html">Jokers</a>.</p>'),
        ("mahjong-flower-count.html", "Flower Count", "flower count in mahjong — flowers in American set", '<p><strong>Flower count</strong> — eight flowers — <a href="mahjong-flowers.html">Flowers</a>.</p>'),
        ("mahjong-wind-count.html", "Wind Count", "wind count in mahjong — four winds in play", '<p><strong>Wind count</strong> — four winds — <a href="mahjong-winds.html">Winds</a>.</p>'),
        ("mahjong-dragon-count.html", "Dragon Count", "dragon count in mahjong — three dragons", '<p><strong>Dragon count</strong> — red green white — <a href="mahjong-dragons.html">Dragons</a>.</p>'),
        ("mahjong-suit-tiles.html", "Suit Tiles", "suit tiles in mahjong — dots bams cracks", '<p><strong>Suit tiles</strong> — 108 suited tiles — <a href="mahjong-suits.html">Suits</a>.</p>'),
        ("mahjong-honor-tiles.html", "Honor Tiles", "honor tiles in mahjong — winds dragons flowers", '<p><strong>Honor tiles</strong> — winds and dragons — <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-blank-tile.html", "Blank Tile", "blank tile in mahjong — spare tile in set", '<p>The <strong>blank tile</strong> — spare — not used in NMJL play.</p>'),
        ("mahjong-discard-pile.html", "Discard Pile", "discard pile in mahjong — thrown tiles pool", '<p>The <strong>discard pile</strong> — claim source — <a href="calling-mahjong.html">Calling</a>.</p>'),
        ("mahjong-wall-break.html", "Wall Break", "wall break in mahjong — breaking the wall to deal", '<p><strong>Wall break</strong> — dice roll — <a href="break-wall-mahjong.html">Break the wall</a>.</p>'),
        ("mahjong-dealer-east.html", "Dealer East", "dealer east in mahjong — east deals first", '<p><strong>Dealer east</strong> starts — <a href="east-seat-mahjong.html">East seat</a>.</p>'),
        ("mahjong-pass-direction.html", "Pass Direction", "pass direction in mahjong — charleston pass order", '<p><strong>Pass direction</strong> — Charleston sequence — <a href="mahjong-charleston.html">Charleston</a>.</p>'),
        ("mahjong-courtesy-pass.html", "Courtesy Pass", "courtesy pass in mahjong — optional charleston pass", '<p><strong>Courtesy pass</strong> — table option — <a href="charleston-courtesy-mahjong.html">Courtesy pass</a>.</p>'),
        ("mahjong-stop-pass.html", "Stop Pass", "stop pass in mahjong — when charleston stops", '<p>You may <strong>stop passing</strong> after the first Charleston round — table rules.</p>'),
        ("mahjong-call-mahjong-first.html", "Call Mahjong First", "call mahjong first in mahjong — mahjong claim priority", '<p><strong>Mahjong call first</strong> — beats exposure claims on same tile.</p>'),
        ("mahjong-exposure-call.html", "Exposure Call", "exposure call in mahjong — claiming for meld", '<p>An <strong>exposure call</strong> — pung kong quint — not winning hand.</p>'),
        ("mahjong-false-mahjong.html", "False Mahjong", "false mahjong in mahjong — incorrect win declaration", '<p><strong>False mahjong</strong> — hand dead — <a href="foul-hand-mahjong.html">Foul hand</a>.</p>'),
        ("mahjong-table-talk.html", "Table Talk", "table talk in mahjong — what you may say during play", '<p>Limit <strong>table talk</strong> — etiquette — <a href="mahjong-etiquette.html">Etiquette</a>.</p>'),
        ("mahjong-rack-touch.html", "Rack Touch", "rack touch in mahjong — touching tiles on rack", '<p><strong>Rack touch</strong> — arrange without revealing — <a href="rack-order-mahjong.html">Rack order</a>.</p>'),
        ("mahjong-sort-tiles.html", "Sort Tiles", "sort tiles in mahjong — organizing your hand", '<p><strong>Sort tiles</strong> — suit order helps — beginners welcome.</p>'),
        ("mahjong-new-card-night.html", "New Card Night", "new card night in mahjong — learning the yearly card", '<p><strong>New card night</strong> — April tradition — <a href="nmjl-card.html">NMJL card</a>.</p>'),
        ("mahjong-category-hunt.html", "Category Hunt", "category hunt in mahjong — finding your hand category", '<p><strong>Category hunt</strong> — read exposures — <a href="read-nmjl-card.html">Read the card</a>.</p>'),
        ("mahjong-safe-tile.html", "Safe Tile", "safe tile in mahjong — discard unlikely to help", '<p>A <strong>safe tile</strong> — defensive discard — advanced play.</p>'),
        ("mahjong-hot-discard.html", "Hot Discard", "hot discard in mahjong — discard that may win for opponent", '<p>A <strong>hot discard</strong> — dangerous throw — think twice.</p>'),
        ("mahjong-call-bluff.html", "Call Bluff", "call bluff in mahjong — reading fake exposures", '<p>Spot a <strong>call bluff</strong> — category misdirection — advanced.</p>'),
        ("mahjong-wall-count.html", "Wall Count", "wall count in mahjong — tiles left in wall", '<p>Track <strong>wall count</strong> — wall game approaching — <a href="mahjong-wall-game.html">Wall game</a>.</p>'),
        ("mahjong-table-rotation.html", "Table Rotation", "table rotation in mahjong — rotating seats between games", '<p><strong>Table rotation</strong> — mix partners — social play.</p>'),
        ("mahjong-wind-rotation.html", "Wind Rotation", "wind rotation in mahjong — winds shift each round", '<p><strong>Wind rotation</strong> — east moves — tournament format.</p>'),
        ("mahjong-score-sheet.html", "Score Sheet", "score sheet in mahjong — tracking wins informally", '<p>Social tables use a simple <strong>score sheet</strong> — wins not points.</p>'),
        ("mahjong-tournament-rules.html", "Tournament Rules", "tournament rules in mahjong — NMJL tournament standards", '<p><strong>Tournament rules</strong> — stricter calling — <a href="mahjong-tournament.html">Tournament</a>.</p>'),
        ("mahjong-house-rule.html", "House Rule", "house rule in mahjong — local variations vs NMJL", '<p>We teach NMJL — not local <strong>house rules</strong> — <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-beginner-table.html", "Beginner Table", "beginner table in mahjong — learning table etiquette", '<p>A <strong>beginner table</strong> — patient pace — <a href="beginner-mahjong.html">Beginner</a>.</p>'),
        ("mahjong-mentor-hand.html", "Mentor Hand", "mentor hand in mahjong — coach helping read the card", '<p><strong>Mentor hand</strong> — we coach during lessons — <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("mahjong-table-foul.html", "Table Foul", "table foul in mahjong — minor infractions", '<p>A <strong>table foul</strong> — wrong tile touched — may require penalty per house.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
