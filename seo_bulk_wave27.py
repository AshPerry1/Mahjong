# -*- coding: utf-8 -*-
"""Mega Wave 27 — ~500 pages (380 cities + hubs + Greek + occasions + rules)."""
from __future__ import annotations

from seo_bulk_wave27_cities_data import WAVE27_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule

WAVE27_CITY_TARGET = 424


def _city_from_tuple(city, tup) -> dict:
    slug, label, st, state_page, hub_page = tup
    kw_slug = slug.replace("-mahjong.html", "").replace("-", " ")
    desc = f"{label} mahjong — private lessons and group events."
    blurb = f"{label} private mahjong lessons — Lookout Mountain Mahjong travels to your venue or home."
    links = (
        f'<p><a href="{state_page}">{st} statewide</a> · '
        f'<a href="{hub_page}">Regional hub</a> · '
        f'<a href="cities-mahjong-hub.html">All cities</a> · '
        f'<a href="book-mahjong-lesson.html">Book</a></p>'
    )
    return city(
        slug,
        label,
        desc,
        f"{kw_slug} mahjong, mahjong {label.lower()}",
        blurb,
        links,
    )


def bulk_pages_mega_wave_27(city, page, mahjong_kw) -> list:
    """Mega Wave 27 — ~500 pages in one generator run."""
    out: list = []

    hubs = [
        (
            "texas-hill-country-mahjong-hub.html",
            "Texas Hill Country Mahjong | Fredericksburg, Kerrville & Austin",
            "Texas Hill Country mahjong — Fredericksburg, Kerrville, Marble Falls, Austin corridor.",
            "texas hill country mahjong hub, fredericksburg mah jongg",
            "Texas Hill Country Mahjong Guide",
            """<p><strong>Texas Hill Country mahjong</strong> — winery towns and lake houses:</p>
<p><a href="fredericksburg-tx-mahjong.html">Fredericksburg</a> · <a href="kerrville-tx-mahjong.html">Kerrville</a> · <a href="marble-falls-tx-mahjong.html">Marble Falls</a> · <a href="boerne-tx-mahjong.html">Boerne</a> · <a href="new-braunfels-tx-mahjong.html">New Braunfels</a> · <a href="austin-mahjong.html">Austin</a></p>
<p><a href="texas-mahjong-hub.html">Texas hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "texas-gulf-coast-mahjong-hub.html",
            "Texas Gulf Coast Mahjong | Galveston, Corpus & South Texas",
            "Texas Gulf Coast mahjong — Galveston, Corpus Christi, South Padre, Houston beaches.",
            "texas gulf coast mahjong hub, galveston mah jongg",
            "Texas Gulf Coast Mahjong Guide",
            """<p><strong>Texas Gulf Coast mahjong</strong> — beach and bay private events:</p>
<p><a href="galveston-tx-mahjong.html">Galveston</a> · <a href="corpus-christi-tx-mahjong.html">Corpus Christi</a> · <a href="port-aransas-tx-mahjong.html">Port Aransas</a> · <a href="south-padre-island-tx-mahjong.html">South Padre</a> · <a href="baytown-tx-mahjong.html">Baytown</a></p>
<p><a href="gulf-coast-mahjong-hub.html">Gulf Coast hub</a> · <a href="texas-mahjong.html">Texas</a></p>""",
        ),
        (
            "california-central-coast-mahjong-hub.html",
            "California Central Coast Mahjong | SLO, Santa Barbara & Monterey",
            "California Central Coast mahjong — San Luis Obispo, Santa Barbara, Monterey, Paso Robles.",
            "california central coast mahjong hub, slo mah jongg",
            "California Central Coast Mahjong Guide",
            """<p><strong>Central Coast mahjong</strong> — wine country and Pacific private lessons:</p>
<p><a href="san-luis-obispo-ca-mahjong.html">San Luis Obispo</a> · <a href="santa-barbara-ca-mahjong.html">Santa Barbara</a> · <a href="monterey-ca-mahjong.html">Monterey</a> · <a href="paso-robles-ca-mahjong.html">Paso Robles</a> · <a href="cambria-ca-mahjong.html">Cambria</a></p>
<p><a href="california-mahjong-hub.html">California hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "southern-california-mahjong-hub.html",
            "Southern California Mahjong | LA, OC, IE & Desert",
            "Southern California mahjong — Los Angeles, Orange County, Inland Empire, Coachella Valley.",
            "southern california mahjong hub, los angeles mah jongg",
            "Southern California Mahjong Guide",
            """<p><strong>SoCal mahjong</strong> — metro and desert resort private events:</p>
<p><a href="los-angeles-mahjong.html">Los Angeles</a> · <a href="riverside-ca-mahjong.html">Riverside</a> · <a href="fontana-ca-mahjong.html">Fontana</a> · <a href="palm-desert-ca-mahjong.html">Palm Desert</a> · <a href="santa-monica-ca-mahjong.html">Santa Monica</a></p>
<p><a href="california-mahjong-hub.html">California hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "jersey-shore-mahjong-hub.html",
            "Jersey Shore Mahjong | Cape May, Atlantic City & LBI",
            "Jersey Shore mahjong — Cape May, Atlantic City, Long Beach Island, Asbury Park.",
            "jersey shore mahjong hub, cape may mah jongg",
            "Jersey Shore Mahjong Guide",
            """<p><strong>Jersey Shore mahjong</strong> — boardwalk summers and beach houses:</p>
<p><a href="cape-may-nj-mahjong.html">Cape May</a> · <a href="atlantic-city-nj-mahjong.html">Atlantic City</a> · <a href="asbury-park-nj-mahjong.html">Asbury Park</a> · <a href="point-pleasant-nj-mahjong.html">Point Pleasant</a> · <a href="ocean-city-nj-mahjong.html">Ocean City NJ</a></p>
<p><a href="new-jersey-mahjong-hub.html">New Jersey hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "finger-lakes-mahjong-hub.html",
            "Finger Lakes Mahjong | Ithaca, Geneva & Wine Country",
            "Finger Lakes mahjong — Ithaca, Geneva, Skaneateles, Watkins Glen, wine trail events.",
            "finger lakes mahjong hub, ithaca mah jongg",
            "Finger Lakes Mahjong Guide",
            """<p><strong>Finger Lakes mahjong</strong> — lake houses and vineyard private lessons:</p>
<p><a href="ithaca-ny-mahjong.html">Ithaca</a> · <a href="geneva-ny-mahjong.html">Geneva NY</a> · <a href="skaneateles-ny-mahjong.html">Skaneateles</a> · <a href="watkins-glen-ny-mahjong.html">Watkins Glen</a> · <a href="corning-ny-mahjong.html">Corning</a></p>
<p><a href="new-york-mahjong-hub.html">New York hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "ozarks-mahjong-hub.html",
            "Ozarks Mahjong | Branson, Eureka Springs & Table Rock",
            "Ozarks mahjong — Branson, Eureka Springs, Springfield MO, Table Rock Lake.",
            "ozarks mahjong hub, branson mah jongg",
            "Ozarks Mahjong Guide",
            """<p><strong>Ozarks mahjong</strong> — lake cabins and show-town private events:</p>
<p><a href="branson-mo-mahjong.html">Branson</a> · <a href="eureka-springs-ar-mahjong.html">Eureka Springs</a> · <a href="springfield-mo-mahjong.html">Springfield MO</a> · <a href="bentonville-ar-mahjong.html">Bentonville</a> · <a href="fayetteville-ar-mahjong.html">Fayetteville</a></p>
<p><a href="arkansas-mahjong-hub.html">Arkansas hub</a> · <a href="missouri-mahjong-hub.html">Missouri hub</a></p>""",
        ),
        (
            "mississippi-gulf-coast-mahjong-hub.html",
            "Mississippi Gulf Coast Mahjong | Biloxi, Gulfport & Bay St. Louis",
            "Mississippi Gulf Coast mahjong — Biloxi, Gulfport, Ocean Springs, Bay St. Louis.",
            "mississippi gulf coast mahjong hub, biloxi mah jongg",
            "Mississippi Gulf Coast Mahjong Guide",
            """<p><strong>MS Gulf Coast mahjong</strong> — casino resorts and beach condos:</p>
<p><a href="biloxi-ms-mahjong.html">Biloxi</a> · <a href="gulfport-ms-mahjong.html">Gulfport</a> · <a href="ocean-springs-ms-mahjong.html">Ocean Springs</a> · <a href="bay-st-louis-ms-mahjong.html">Bay St. Louis</a> · <a href="pass-christian-ms-mahjong.html">Pass Christian</a></p>
<p><a href="mississippi-mahjong-hub.html">Mississippi hub</a> · <a href="gulf-coast-mahjong-hub.html">Gulf Coast hub</a></p>""",
        ),
        (
            "palm-beaches-mahjong-hub.html",
            "Palm Beaches Mahjong | West Palm, Boca & Jupiter",
            "Palm Beaches mahjong — West Palm Beach, Boca Raton, Jupiter, Delray, snowbird season.",
            "palm beaches mahjong hub, west palm mah jongg",
            "Palm Beaches Mahjong Guide",
            """<p><strong>Palm Beaches mahjong</strong> — country clubs and condo socials:</p>
<p><a href="palm-beach-mahjong.html">Palm Beach</a> · <a href="boca-raton-fl-mahjong.html">Boca Raton</a> · <a href="jupiter-fl-mahjong.html">Jupiter</a> · <a href="delray-beach-fl-mahjong.html">Delray Beach</a> · <a href="west-palm-beach-fl-mahjong.html">West Palm Beach</a></p>
<p><a href="florida-mahjong-hub.html">Florida hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "blue-ridge-south-mahjong-hub.html",
            "Blue Ridge South Mahjong | Highlands, Helen & Blue Ridge GA",
            "Blue Ridge South mahjong — Highlands NC, Helen GA, Blue Ridge GA, mountain cabins.",
            "blue ridge south mahjong hub, highlands nc mah jongg",
            "Blue Ridge South Mahjong Guide",
            """<p><strong>Blue Ridge South mahjong</strong> — mountain town private events:</p>
<p><a href="highlands-nc-mahjong.html">Highlands NC</a> · <a href="helen-ga-mahjong.html">Helen GA</a> · <a href="blue-ridge-ga-mahjong.html">Blue Ridge GA</a> · <a href="dahlonega-ga-mahjong.html">Dahlonega</a> · <a href="clayton-ga-mahjong.html">Clayton GA</a></p>
<p><a href="north-carolina-mountains-mahjong-hub.html">NC mountains</a> · <a href="georgia-mahjong-hub.html">Georgia hub</a></p>""",
        ),
        (
            "great-lakes-mahjong-hub.html",
            "Great Lakes Mahjong | Chicago, Milwaukee & Michigan Shores",
            "Great Lakes mahjong — Chicago, Milwaukee, Grand Rapids, Traverse City, lake house events.",
            "great lakes mahjong hub, chicago mah jongg midwest",
            "Great Lakes Mahjong Guide",
            """<p><strong>Great Lakes mahjong</strong> — lakefront and metro private lessons:</p>
<p><a href="chicago-mahjong.html">Chicago</a> · <a href="milwaukee-wi-mahjong.html">Milwaukee</a> · <a href="grand-rapids-mi-mahjong.html">Grand Rapids</a> · <a href="traverse-city-mi-mahjong.html">Traverse City</a> · <a href="ann-arbor-mi-mahjong.html">Ann Arbor</a></p>
<p><a href="michigan-mahjong-hub.html">Michigan hub</a> · <a href="illinois-mahjong-hub.html">Illinois hub</a></p>""",
        ),
        (
            "nevada-resorts-mahjong-hub.html",
            "Nevada Resorts Mahjong | Tahoe, Laughlin & Mesquite",
            "Nevada resort mahjong — Lake Tahoe, Laughlin, Mesquite, Stateline, vacation rentals.",
            "nevada resorts mahjong hub, lake tahoe mah jongg",
            "Nevada Resorts Mahjong Guide",
            """<p><strong>Nevada resort mahjong</strong> — casinos and mountain lake private events:</p>
<p><a href="incline-village-nv-mahjong.html">Incline Village</a> · <a href="stateline-nv-mahjong.html">Stateline</a> · <a href="laughlin-nv-mahjong.html">Laughlin</a> · <a href="mesquite-nv-mahjong.html">Mesquite</a> · <a href="las-vegas-mahjong.html">Las Vegas</a></p>
<p><a href="nevada-mahjong-hub.html">Nevada hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE27_CITIES[:WAVE27_CITY_TARGET]:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("phi-kappa-sigma", "Phi Kappa Sigma", "Phi Kap"),
        ("theta-xi", "Theta Xi", "Theta Xi"),
        ("sigma-nu", "Sigma Nu", "Sigma Nu"),
        ("phi-sigma-kappa", "Phi Sigma Kappa", "Phi Sig Kap"),
        ("kappa-psi", "Kappa Psi", "Kappa Psi"),
        ("phi-mu-alpha-sinfonia", "Phi Mu Alpha Sinfonia", "PMA"),
        ("kappa-kappa-psi", "Kappa Kappa Psi", "KKPsi"),
        ("phi-beta-sigma", "Phi Beta Sigma", "Phi Beta"),
        ("iota-phi-theta", "Iota Phi Theta", "IPT"),
        ("sigma-pi", "Sigma Pi", "Sigma Pi"),
        ("tau-kappa-epsilon", "Tau Kappa Epsilon", "TKE"),
        ("phi-gamma-delta", "Phi Gamma Delta", "FIJI"),
        ("delta-upsilon", "Delta Upsilon", "DU"),
        ("beta-theta-pi", "Beta Theta Pi", "Beta"),
        ("phi-kappa-psi", "Phi Kappa Psi", "Phi Psi"),
        ("sigma-chi", "Sigma Chi", "Sigma Chi"),
        ("theta-chi", "Theta Chi", "Theta Chi"),
        ("pi-kappa-alpha", "Pi Kappa Alpha", "Pike"),
        ("kappa-sigma", "Kappa Sigma", "Kappa Sig"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("phi-sigma-sigma", "Phi Sigma Sigma", "Phi Sig"),
        ("sigma-delta-tau", "Sigma Delta Tau", "SDT"),
        ("alpha-phi-gamma", "Alpha Phi Gamma", "APG"),
        ("delta-phi-epsilon", "Delta Phi Epsilon", "DPhiE"),
        ("sigma-sigma-sigma", "Sigma Sigma Sigma", "Tri Sig"),
        ("alpha-sigma-tau", "Alpha Sigma Tau", "AST"),
        ("kappa-phi-lambda", "Kappa Phi Lambda", "KPL"),
        ("lambda-phi-epsilon", "Lambda Phi Epsilon", "LPhiE"),
        ("sigma-psi-zeta", "Sigma Psi Zeta", "SPZ"),
        ("alpha-psi-lambda", "Alpha Psi Lambda", "APL"),
        ("delta-phi-lambda", "Delta Phi Lambda", "DPhiL"),
        ("kappa-phi-iota", "Kappa Phi Iota", "KPhiI"),
        ("sigma-alpha-omega", "Sigma Alpha Omega", "SAO"),
        ("theta-phi-alpha", "Theta Phi Alpha", "TPA"),
        ("zeta-phi-beta", "Zeta Phi Beta", "ZPB"),
        ("sigma-gamma-rho", "Sigma Gamma Rho", "SGRho"),
        ("alpha-kappa-alpha", "Alpha Kappa Alpha", "AKA"),
        ("delta-sigma-theta", "Delta Sigma Theta", "DST"),
        ("alpha-chi-omega", "Alpha Chi Omega", "AXO"),
    ]
    seen_sor: set[str] = set()
    for slug, name, nick in sororities:
        if slug in seen_sor:
            continue
        seen_sor.add(slug)
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ("juneteenth-mahjong", "Juneteenth", "juneteenth mahjong — community celebration with tiles", '<p>Honor <strong>Juneteenth</strong> with a community mahjong lesson. <a href="church-mahjong.html">Church</a> · <a href="nonprofit-mahjong.html">Nonprofit</a>.</p>'),
        ("fourth-of-july-picnic-mahjong", "Fourth of July Picnic", "fourth of july picnic mahjong — patriotic gathering with tiles", '<p>Add <strong>Fourth of July picnic mahjong</strong> to your backyard lineup. <a href="summer-mahjong.html">Summer</a> · <a href="family-reunion-mahjong.html">Family reunion</a>.</p>'),
        ("labor-day-weekend-mahjong", "Labor Day Weekend", "labor day weekend mahjong — end-of-summer gathering with tiles", '<p>Book <strong>Labor Day weekend mahjong</strong> before calendars fill. <a href="fall-mahjong.html">Fall gatherings</a> · <a href="lake-house-mahjong.html">Lake house</a>.</p>'),
        ("friendsgiving-mahjong", "Friendsgiving", "friendsgiving mahjong — Friendsgiving dinner with tiles after the meal", '<p>After the turkey — play <strong>Friendsgiving mahjong</strong>. <a href="thanksgiving-mahjong.html">Thanksgiving</a> · <a href="dinner-party-mahjong.html">Dinner party</a>.</p>'),
        ("new-years-day-brunch-mahjong", "New Year's Day Brunch", "new years day brunch mahjong — January 1 gathering with tiles", '<p>Start the year with <strong>New Year\'s Day brunch mahjong</strong>. <a href="new-years-mahjong.html">New Year\'s</a> · <a href="mahjong-brunch.html">Brunch</a>.</p>'),
        ("valentines-weekend-mahjong", "Valentine's Weekend", "valentines weekend mahjong — February couples and friends event", '<p><strong>Valentine\'s weekend mahjong</strong> — couples or galentines. <a href="galentines-mahjong.html">Galentine\'s</a> · <a href="date-night-mahjong.html">Date night</a>.</p>'),
        ("mardi-gras-mahjong", "Mardi Gras", "mardi gras mahjong — Fat Tuesday party with tiles", '<p>Let the good tiles roll — <strong>Mardi Gras mahjong</strong>. <a href="cocktail-mahjong.html">Cocktail party</a> · <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("memorial-day-pool-mahjong", "Memorial Day Pool Party", "memorial day pool mahjong — poolside tiles", '<p><strong>Memorial Day pool mahjong</strong> — sunscreen and racks. <a href="pool-party-mahjong.html">Pool party</a> · <a href="summer-mahjong.html">Summer</a>.</p>'),
        ("summer-solstice-mahjong", "Summer Solstice", "summer solstice mahjong — longest day gathering with tiles", '<p>Celebrate the <strong>summer solstice</strong> with an evening mahjong lesson. <a href="patio-party-mahjong.html">Patio party</a>.</p>'),
        ("back-to-school-night-mahjong", "Back to School Night", "back to school night mahjong — PTA and parent social with tiles", '<p>Upgrade <strong>back to school night</strong> with a parent mahjong social. <a href="pta-mahjong.html">PTA</a> · <a href="school-fundraiser-mahjong.html">Fundraiser</a>.</p>'),
        ("neighborhood-block-party-mahjong", "Neighborhood Block Party", "neighborhood block party mahjong — street social with tiles", '<p>Close the street for <strong>neighborhood block party mahjong</strong>. <a href="neighborhood-mahjong.html">Neighborhood</a> · <a href="hoa-mahjong.html">HOA</a>.</p>'),
        ("rooftop-party-mahjong", "Rooftop Party", "rooftop party mahjong — city skyline event with tiles", '<p><strong>Rooftop party mahjong</strong> — skyline views and tiles. <a href="cocktail-mahjong.html">Cocktail</a> · <a href="happy-hour-mahjong.html">Happy hour</a>.</p>'),
        ("patio-party-mahjong", "Patio Party", "patio party mahjong — backyard social with tiles", '<p>Host a <strong>patio party mahjong</strong> lesson this season. <a href="backyard-mahjong.html">Backyard</a> · <a href="summer-mahjong.html">Summer</a>.</p>'),
        ("high-tea-mahjong", "High Tea", "high tea mahjong — afternoon tea service with tiles", '<p>Pair scones with <strong>high tea mahjong</strong>. <a href="tea-party-mahjong.html">Tea party</a> · <a href="ladies-luncheon-mahjong.html">Luncheon</a>.</p>'),
        ("progressive-dinner-mahjong", "Progressive Dinner", "progressive dinner mahjong — multi-home dinner crawl with tiles", '<p>End your <strong>progressive dinner</strong> route with mahjong at the final house. <a href="dinner-party-mahjong.html">Dinner party</a>.</p>'),
        ("potluck-supper-mahjong", "Potluck Supper", "potluck supper mahjong — bring-a-dish night with tiles", '<p>After the potluck — play <strong>potluck supper mahjong</strong>. <a href="supper-club-mahjong.html">Supper club</a>.</p>'),
        ("bbq-night-mahjong", "BBQ Night", "bbq night mahjong — grill night with tiles after dinner", '<p>Smoke, eat, then <strong>BBQ night mahjong</strong>. <a href="summer-mahjong.html">Summer</a> · <a href="patio-party-mahjong.html">Patio</a>.</p>'),
        ("oyster-roast-mahjong", "Oyster Roast", "oyster roast mahjong — Lowcountry roast with tiles", '<p>Shuck and play — <strong>oyster roast mahjong</strong>. <a href="charleston-sc-mahjong.html">Charleston</a> · <a href="coastal-mahjong.html">Coastal</a>.</p>'),
        ("crawfish-boil-mahjong", "Crawfish Boil", "crawfish boil mahjong — Louisiana boil with tiles", '<p>After the boil — <strong>crawfish boil mahjong</strong>. <a href="new-orleans-mahjong.html">New Orleans</a> · <a href="louisiana-mahjong.html">Louisiana</a>.</p>'),
        ("brewery-taproom-mahjong", "Brewery Taproom", "brewery taproom mahjong — craft beer venue with tiles", '<p>Book <strong>brewery taproom mahjong</strong> for your taproom event night. <a href="happy-hour-mahjong.html">Happy hour</a>.</p>'),
        ("wine-club-mahjong", "Wine Club", "wine club mahjong — monthly wine club with tiles", '<p>Your <strong>wine club</strong> deserves a mahjong lesson between pours. <a href="wine-tasting-mahjong.html">Wine tasting</a>.</p>'),
        ("knitting-circle-mahjong", "Knitting Circle Swap", "knitting circle mahjong — craft group night with tiles", '<p>Swap yarn night for <strong>knitting circle mahjong</strong>. <a href="craft-night-mahjong.html">Craft night</a>.</p>'),
        ("quilting-bee-mahjong", "Quilting Bee", "quilting bee mahjong — guild social with tiles", '<p><strong>Quilting bee mahjong</strong> — stitch, then play. <a href="craft-night-mahjong.html">Craft night</a> · <a href="church-mahjong.html">Church guild</a>.</p>'),
        ("pickleball-club-mahjong", "Pickleball Club", "pickleball club mahjong — active club social with tiles", '<p>After dinks — <strong>pickleball club mahjong</strong>. <a href="country-club-mahjong.html">Country club</a>.</p>'),
        ("yacht-club-mahjong", "Yacht Club", "yacht club mahjong — marina club social with tiles", '<p><strong>Yacht club mahjong</strong> — dockside or clubhouse. <a href="country-club-mahjong.html">Country club</a> · <a href="lake-house-mahjong.html">Lake house</a>.</p>'),
        ("lake-house-weekend-mahjong", "Lake House Weekend", "lake house weekend mahjong — waterfront cabin with tiles", '<p>Book a <strong>lake house weekend mahjong</strong> lesson at the dock. <a href="lake-house-mahjong.html">Lake house</a> · <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("cabin-weekend-mahjong", "Cabin Weekend", "cabin weekend mahjong — mountain cabin gathering with tiles", '<p><strong>Cabin weekend mahjong</strong> — fireside tiles. <a href="ski-lodge-mahjong.html">Ski lodge</a> · <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("ski-lodge-mahjong", "Ski Lodge", "ski lodge mahjong — après-ski social with tiles", '<p>After the slopes — <strong>ski lodge mahjong</strong>. <a href="winter-mahjong.html">Winter</a> · <a href="stowe-vt-mahjong.html">Stowe</a>.</p>'),
        ("beach-house-mahjong", "Beach House", "beach house mahjong — shore rental week with tiles", '<p>Rainy beach day? <strong>Beach house mahjong</strong> saves the week. <a href="vacation-mahjong.html">Vacation</a> · <a href="florida-mahjong.html">Florida</a>.</p>'),
        ("timeshare-week-mahjong", "Timeshare Week", "timeshare week mahjong — resort week activity with tiles", '<p>Fill your <strong>timeshare week</strong> with a group mahjong lesson. <a href="resort-mahjong.html">Resort</a> · <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("garden-tour-mahjong", "Garden Tour Weekend", "garden tour mahjong — garden club weekend with tiles", '<p>After the tour — <strong>garden tour mahjong</strong>. <a href="garden-party-mahjong.html">Garden party</a> · <a href="ladies-luncheon-mahjong.html">Luncheon</a>.</p>'),
        ("art-walk-mahjong", "Art Walk Night", "art walk mahjong — downtown gallery night with tiles", '<p>Pair your <strong>art walk</strong> with a late-night mahjong pop-up. <a href="pop-up-mahjong.html">Pop-up</a> · <a href="vendor-fair-mahjong.html">Vendor fair</a>.</p>'),
        ("farmers-market-mahjong", "Farmers Market", "farmers market mahjong — Saturday market social with tiles", '<p>Draw crowds with <strong>farmers market mahjong</strong>. <a href="pop-up-mahjong.html">Pop-up</a> · <a href="vendor-fair-mahjong.html">Vendor fair</a>.</p>'),
        ("church-picnic-mahjong", "Church Picnic", "church picnic mahjong — fellowship picnic with tiles", '<p>Add tiles to your <strong>church picnic</strong>. <a href="church-mahjong.html">Church</a> · <a href="fellowship-mahjong.html">Fellowship</a>.</p>'),
        ("synagogue-sisterhood-mahjong", "Synagogue Sisterhood", "synagogue sisterhood mahjong — sisterhood social with tiles", '<p><strong>Synagogue sisterhood mahjong</strong> — luncheon and lesson. <a href="ladies-luncheon-mahjong.html">Luncheon</a>.</p>'),
        ("mosque-community-mahjong", "Mosque Community Night", "mosque community mahjong — community center social with tiles", '<p>Host <strong>mosque community night mahjong</strong> for families. <a href="community-center-mahjong.html">Community center</a>.</p>'),
        ("temple-sisterhood-mahjong", "Temple Sisterhood", "temple sisterhood mahjong — sisterhood event with tiles", '<p><strong>Temple sisterhood mahjong</strong> — social and fundraiser-friendly. <a href="fundraiser-mahjong.html">Fundraiser</a>.</p>'),
        ("rotary-club-mahjong", "Rotary Club", "rotary club mahjong — service club meeting with tiles", '<p>Engage members with <strong>Rotary club mahjong</strong>. <a href="nonprofit-mahjong.html">Nonprofit</a> · <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("kiwanis-mahjong", "Kiwanis Club", "kiwanis mahjong — service club social with tiles", '<p><strong>Kiwanis mahjong</strong> — family-friendly service club fun. <a href="church-mahjong.html">Church</a> · <a href="school-fundraiser-mahjong.html">School</a>.</p>'),
        ("junior-league-mahjong", "Junior League", "junior league mahjong — league social with tiles", '<p><strong>Junior League mahjong</strong> — philanthropy and social. <a href="ladies-luncheon-mahjong.html">Luncheon</a> · <a href="fundraiser-mahjong.html">Fundraiser</a>.</p>'),
        ("garden-club-mahjong", "Garden Club", "garden club mahjong — garden club meeting with tiles", '<p>Your <strong>garden club</strong> will love a mahjong lesson. <a href="garden-party-mahjong.html">Garden party</a>.</p>'),
        ("historical-society-mahjong", "Historical Society", "historical society mahjong — museum fundraiser with tiles", '<p>Fundraise with <strong>historical society mahjong</strong>. <a href="museum-mahjong.html">Museum</a> · <a href="fundraiser-mahjong.html">Fundraiser</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("mahjong-wall-break-mahjong.html", "Break the Wall", "break the wall in mahjong — starting the draw wall", '<p><strong>Break the wall</strong> — roll dice and count to start play. <a href="mahjong-wall-game.html">Wall game</a> · <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-dead-hand-mahjong.html", "Dead Hand", "dead hand in mahjong — when your hand is out of play", '<p>A <strong>dead hand</strong> cannot win — learn common fouls. <a href="foul-hand-mahjong.html">Foul hand</a> · <a href="mahjong-call-rules.html">Call rules</a>.</p>'),
        ("mahjong-wrong-exposure-mahjong.html", "Wrong Exposure", "wrong exposure in mahjong — incorrect meld on the rack", '<p>A <strong>wrong exposure</strong> may dead your hand under NMJL rules. <a href="mahjong-exposure-rules.html">Exposure rules</a>.</p>'),
        ("mahjong-pung-from-wall-mahjong.html", "Pung from Wall", "pung from wall in mahjong — drawing three of a kind yourself", '<p>Draw a <strong>pung from the wall</strong> — three matching tiles from your draw. <a href="mahjong-pung.html">Pung</a>.</p>'),
        ("mahjong-kong-from-wall-mahjong.html", "Kong from Wall", "kong from wall in mahjong — four of a kind from self-draw", '<p>A <strong>kong from the wall</strong> — four matching from your draw. <a href="mahjong-kong.html">Kong</a>.</p>'),
        ("mahjong-quint-from-wall-mahjong.html", "Quint from Wall", "quint from wall in mahjong — five of a kind from self-draw", '<p>Some hands allow a <strong>quint from the wall</strong>. <a href="mahjong-quints.html">Quints</a>.</p>'),
        ("mahjong-call-for-pair-mahjong.html", "Call for Pair", "call for pair in mahjong — when the pair may be claimed", '<p>Most NMJL hands need a <strong>concealed pair</strong> — rarely call for pair. <a href="mahjong-pair-requirement.html">Pair requirement</a>.</p>'),
        ("mahjong-last-discard-mahjong.html", "Last Discard", "last discard in mahjong — winning on the final discard", '<p>Win on the <strong>last discard</strong> before the wall ends. <a href="mahjong-wall-game.html">Wall game</a>.</p>'),
        ("mahjong-table-talk-mahjong.html", "Table Talk", "table talk in mahjong — what you may say during play", '<p>Limit <strong>table talk</strong> — hints help opponents. <a href="mahjong-etiquette.html">Etiquette</a>.</p>'),
        ("mahjong-score-sheet-mahjong.html", "Score Sheet", "score sheet in mahjong — tracking wins at casual tables", '<p>Use a simple <strong>score sheet</strong> for friendly stakes. <a href="mahjong-scoring.html">Scoring</a>.</p>'),
        ("mahjong-dealer-rotation-mahjong.html", "Dealer Rotation", "dealer rotation in mahjong — passing east after a win", '<p><strong>Dealer rotation</strong> — east passes after someone wins. <a href="east-seat-mahjong.html">East seat</a>.</p>'),
        ("mahjong-reserved-tiles-mahjong.html", "Reserved Tiles", "reserved tiles in mahjong — dead wall and cold wall", '<p><strong>Reserved tiles</strong> are not drawn in play. <a href="mahjong-dead-wall.html">Dead wall</a> · <a href="mahjong-cold-wall.html">Cold wall</a>.</p>'),
        ("mahjong-charleston-order-mahjong.html", "Charleston Order", "charleston order in mahjong — pass right, across, left", '<p>Remember <strong>Charleston order</strong>: right, across, left — then optional second. <a href="mahjong-charleston.html">Charleston</a>.</p>'),
        ("mahjong-joker-in-charleston-mahjong.html", "Jokers in Charleston", "jokers in charleston in mahjong — jokers are not passed", '<p><strong>Jokers</strong> stay out of the Charleston — only naturals pass. <a href="mahjong-passed-joker.html">Passed joker</a>.</p>'),
        ("mahjong-call-window-mahjong.html", "Call Window", "call window in mahjong — when you may claim a discard", '<p>The <strong>call window</strong> closes when the next player racks or discards. <a href="calling-mahjong.html">Calling</a>.</p>'),
        ("mahjong-exposure-order-mahjong.html", "Exposure Order", "exposure order in mahjong — order melds left to right on rack", '<p>Keep <strong>exposure order</strong> clear on your rack for opponents. <a href="rack-order-mahjong.html">Rack order</a>.</p>'),
        ("mahjong-win-by-default-mahjong.html", "Win by Default", "win by default in mahjong — rare table rules", '<p>American NMJL does not use <strong>win by default</strong> — play standard rules in <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-table-fee-mahjong.html", "Table Fee", "table fee in mahjong — house rules for casual games", '<p>Some groups use a <strong>table fee</strong> — agree before the first Charleston. <a href="mahjong-etiquette.html">Etiquette</a>.</p>'),
        ("mahjong-spectator-rules-mahjong.html", "Spectator Rules", "spectator rules in mahjong — watching without coaching", '<p><strong>Spectators</strong> watch silently — no coaching active players. <a href="mahjong-etiquette.html">Etiquette</a>.</p>'),
        ("mahjong-tile-count-mahjong.html", "Tile Count", "tile count in mahjong — 152 tiles American set", '<p>American mahjong uses <strong>152 tiles</strong> including jokers and flowers. <a href="mahjong-tiles.html">Tiles guide</a>.</p>'),
        ("mahjong-rack-height-mahjong.html", "Rack Height", "rack height in mahjong — stacking exposures cleanly", '<p>Keep <strong>rack height</strong> tidy — exposures visible, concealed face-down. <a href="mahjong-rack-concealed.html">Concealed on rack</a>.</p>'),
        ("mahjong-wall-length-mahjong.html", "Wall Length", "wall length in mahjong — building the double wall", '<p>Build a <strong>wall</strong> of face-down tiles — length per NMJL dealing. <a href="break-wall-mahjong.html">Break the wall</a>.</p>'),
        ("mahjong-courtesy-after-charleston-mahjong.html", "Courtesy After Charleston", "courtesy after charleston in mahjong — optional pass tile", '<p>Some tables allow a <strong>courtesy pass</strong> after the Charleston. <a href="mahjong-courtesy-discard.html">Courtesy discard</a>.</p>'),
        ("mahjong-misdeal-mahjong.html", "Misdeal", "misdeal in mahjong — when to redealand tiles", '<p>A <strong>misdeal</strong> — wrong tile count — means redealand. <a href="mahjong-dealing.html">Dealing</a>.</p>'),
        ("mahjong-table-stakes-mahjong.html", "Table Stakes", "table stakes in mahjong — friendly betting norms", '<p>Agree <strong>table stakes</strong> before play — many groups play for fun only. <a href="mahjong-scoring.html">Scoring</a>.</p>'),
        ("mahjong-skip-charleston-mahjong.html", "Skip Charleston", "skip charleston in mahjong — house rules variation", '<p>NMJL always includes the <strong>Charleston</strong> — we teach standard passes in <a href="mahjong-charleston.html">Charleston guide</a>.</p>'),
        ("mahjong-win-on-discard-mahjong.html", "Win on Discard", "win on discard in mahjong — mahjong on another player's discard", '<p>You may <strong>win on a discard</strong> when your hand is ready and the discard completes it. <a href="calling-mahjong.html">Calling</a>.</p>'),
        ("mahjong-self-draw-win-mahjong.html", "Self-Draw Win", "self draw win in mahjong — picking the winning tile yourself", '<p>A <strong>self-draw win</strong> — tile from the wall — is a classic mahjong moment. <a href="self-pick-mahjong.html">Self-pick</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
