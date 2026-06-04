# -*- coding: utf-8 -*-
"""Southeast Targeted Wave — ~600 pages focused on GA, TN, Carolinas, AL, FL & travel states."""
from __future__ import annotations

from seo_bulk_wave39_cities_data import WAVE39_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def _city_from_tuple_southeast(city, tup) -> dict:
    slug, label, st, state_page, hub_page = tup
    kw_slug = slug.replace("-mahjong.html", "").replace("-", " ")
    desc = (
        f"{label} mahjong — private lessons across the Southeast. "
        "Lookout Mountain Mahjong home base Georgia & Tennessee."
    )
    blurb = (
        f"<strong>{label}</strong> — we teach American mahjong throughout the Southeast "
        f"from our Lookout Mountain, Georgia &amp; Tennessee home. Private events at your home, "
        "club, resort, or vacation rental."
    )
    links = (
        '<p class="seo-inline-cta"><strong>Southeast:</strong> '
        '<a href="southeast-mahjong-hub.html">★ Southeast guide</a> · '
        '<a href="/">Main site</a> · '
        '<a href="/mahjong.html">Mahjong</a> · '
        '<a href="/book-mahjong-lesson.html">Book</a> · '
        '<a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">Instagram</a></p>'
        f'<p><a href="{state_page}">{st} statewide</a> · '
        f'<a href="{hub_page}">Regional hub</a> · '
        f'<a href="chattanooga-area-mahjong-hub.html">Chattanooga area</a> · '
        f'<a href="southern-mahjong.html">Southern mahjong</a> · '
        f'<a href="{slug.replace("-mahjong.html", "-lessons-near-me.html")}">Lessons near me</a> · '
        f'<a href="book-mahjong-{slug.replace("-mahjong.html", "")}.html">Book here</a></p>'
    )
    return city(
        slug,
        label,
        desc,
        f"{kw_slug} mahjong, mahjong {label.lower()}, southeast mahjong lessons",
        blurb,
        links,
    )


def bulk_pages_southeast_wave(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "southeast-mahjong-hub.html",
            "Southeast Mahjong | GA, TN, Carolinas, AL, FL & Beyond",
            "Southeast mahjong lessons — Lookout Mountain Mahjong home base GA & TN. Charlotte, Atlanta, Nashville, Charleston, Florida coast.",
            "southeast mahjong hub, southern mahjong lessons, mahjong southeast us",
            "Southeast Mahjong — Regional Guide",
            """<p><strong>Southeast mahjong</strong> is our home turf. Lookout Mountain Mahjong teaches from <strong>Georgia &amp; Tennessee</strong> and travels across the Carolinas, Alabama, Florida, Kentucky, Mississippi, Louisiana &amp; Virginia.</p>
<h2>Home Base</h2>
<p><a href="lookout-mountain-georgia-mahjong.html">Lookout Mountain GA</a> · <a href="lookout-mountain-tn-mahjong.html">Lookout Mountain TN</a> · <a href="chattanooga-area-mahjong-hub.html">Chattanooga area</a> · <a href="fairyland-ga-mahjong.html">Fairyland</a> · <a href="ringgold-ga-mahjong.html">Ringgold</a></p>
<h2>State Guides</h2>
<p><a href="georgia-mahjong-hub.html">Georgia</a> · <a href="tennessee-mahjong-hub.html">Tennessee</a> · <a href="north-carolina-mahjong-hub.html">North Carolina</a> · <a href="south-carolina-mahjong-hub.html">South Carolina</a> · <a href="alabama-mahjong-hub.html">Alabama</a> · <a href="florida-mahjong-hub.html">Florida</a> · <a href="kentucky-mahjong-hub.html">Kentucky</a> · <a href="mississippi-mahjong-hub.html">Mississippi</a> · <a href="louisiana-mahjong-hub.html">Louisiana</a> · <a href="virginia-mahjong-hub.html">Virginia</a></p>
<h2>Metro &amp; Coast Hubs</h2>
<p><a href="atlanta-metro-mahjong-hub.html">Atlanta metro</a> · <a href="nashville-metro-mahjong-hub.html">Nashville metro</a> · <a href="charlotte-metro-mahjong-hub.html">Charlotte metro</a> · <a href="raleigh-durham-mahjong-hub.html">Raleigh-Durham</a> · <a href="lowcountry-sc-mahjong-hub.html">Lowcountry SC</a> · <a href="georgia-coast-mahjong-hub.html">GA Coast</a> · <a href="gulf-coast-mahjong-hub.html">Gulf Coast</a> · <a href="palm-beaches-mahjong-hub.html">Palm Beaches</a> · <a href="hampton-roads-va-mahjong-hub.html">Hampton Roads</a></p>
<p><a href="southern-mahjong.html">Southern mahjong</a> · <a href="book-mahjong-lesson.html">Book a lesson</a> · <a href="mahjong-south.html">Mahjong in the South</a></p>""",
        ),
        (
            "carolinas-mahjong-hub.html",
            "Carolinas Mahjong | NC & SC City Guide",
            "Carolinas mahjong — Charlotte, Raleigh, Asheville, Charleston, Hilton Head. Lookout Mountain Mahjong travels NC & SC.",
            "carolinas mahjong hub, north south carolina mah jongg",
            "Carolinas Mahjong Guide",
            """<p><strong>Carolinas mahjong</strong> — mountains to coast:</p>
<p><a href="charlotte-mahjong.html">Charlotte</a> · <a href="raleigh-mahjong.html">Raleigh</a> · <a href="asheville-mahjong.html">Asheville</a> · <a href="charleston-sc-mahjong.html">Charleston</a> · <a href="hilton-head-mahjong.html">Hilton Head</a> · <a href="outer-banks-mahjong.html">Outer Banks</a></p>
<p><a href="north-carolina-mahjong-hub.html">NC hub</a> · <a href="south-carolina-mahjong-hub.html">SC hub</a> · <a href="southeast-mahjong-hub.html">Southeast hub</a></p>""",
        ),
        (
            "deep-south-mahjong-hub.html",
            "Deep South Mahjong | AL, MS & LA",
            "Deep South mahjong — Birmingham, Mobile, New Orleans, Biloxi, Jackson. Lookout Mountain Mahjong.",
            "deep south mahjong hub, alabama mississippi louisiana mah jongg",
            "Deep South Mahjong Guide",
            """<p><strong>Deep South mahjong</strong> — Gulf and river cities:</p>
<p><a href="birmingham-mahjong.html">Birmingham</a> · <a href="mobile-mahjong.html">Mobile</a> · <a href="new-orleans-mahjong.html">New Orleans</a> · <a href="jackson-ms-mahjong.html">Jackson MS</a> · <a href="biloxi-ms-mahjong.html">Biloxi</a></p>
<p><a href="gulf-coast-mahjong-hub.html">Gulf Coast</a> · <a href="southeast-mahjong-hub.html">Southeast hub</a></p>""",
        ),
        (
            "north-georgia-mahjong-hub.html",
            "North Georgia Mahjong | Blue Ridge, Dahlonega & Lake Lanier",
            "North Georgia mahjong — Blue Ridge, Dahlonega, Helen, Lake Lanier, North Atlanta suburbs.",
            "north georgia mahjong hub, blue ridge mah jongg",
            "North Georgia Mahjong Guide",
            """<p><strong>North Georgia mahjong</strong> — mountains &amp; lakes near Atlanta:</p>
<p><a href="blue-ridge-ga-mahjong.html">Blue Ridge</a> · <a href="dahlonega-ga-mahjong.html">Dahlonega</a> · <a href="alpharetta-mahjong.html">Alpharetta</a> · <a href="atlanta-mahjong.html">Atlanta</a> · <a href="lookout-mountain-georgia-mahjong.html">Lookout Mountain</a></p>
<p><a href="georgia-mahjong-hub.html">Georgia hub</a> · <a href="southeast-mahjong-hub.html">Southeast hub</a></p>""",
        ),
        (
            "middle-tennessee-mahjong-hub.html",
            "Middle Tennessee Mahjong | Nashville, Franklin & Murfreesboro",
            "Middle Tennessee mahjong — Nashville, Franklin, Murfreesboro, Brentwood private events.",
            "middle tennessee mahjong hub, nashville metro mah jongg",
            "Middle Tennessee Mahjong Guide",
            """<p><strong>Middle Tennessee mahjong</strong> — Music City &amp; suburbs:</p>
<p><a href="nashville-mahjong.html">Nashville</a> · <a href="franklin-tn-mahjong.html">Franklin</a> · <a href="murfreesboro-mahjong.html">Murfreesboro</a> · <a href="brentwood-tn-mahjong.html">Brentwood</a></p>
<p><a href="nashville-metro-mahjong-hub.html">Nashville metro</a> · <a href="tennessee-mahjong-hub.html">TN hub</a></p>""",
        ),
        (
            "east-tennessee-mahjong-hub.html",
            "East Tennessee Mahjong | Knoxville, Chattanooga & Smokies",
            "East Tennessee mahjong — Knoxville, Chattanooga, Gatlinburg, Maryville private lessons.",
            "east tennessee mahjong hub, knoxville chattanooga mah jongg",
            "East Tennessee Mahjong Guide",
            """<p><strong>East Tennessee mahjong</strong> — our backyard:</p>
<p><a href="chattanooga-mahjong.html">Chattanooga</a> · <a href="knoxville-mahjong.html">Knoxville</a> · <a href="gatlinburg-tn-mahjong.html">Gatlinburg</a> · <a href="maryville-tn-mahjong.html">Maryville</a> · <a href="lookout-mountain-tn-mahjong.html">Lookout Mountain TN</a></p>
<p><a href="chattanooga-area-mahjong-hub.html">Chattanooga area</a> · <a href="smoky-mountains-mahjong-hub.html">Smokies</a></p>""",
        ),
        (
            "florida-atlantic-coast-mahjong-hub.html",
            "Florida Atlantic Coast Mahjong | Palm Beach to Amelia Island",
            "Florida Atlantic Coast mahjong — Palm Beach, Boca, Jupiter, St Augustine, Amelia Island.",
            "florida atlantic coast mahjong hub, palm beach mah jongg",
            "Florida Atlantic Coast Mahjong Guide",
            """<p><strong>FL Atlantic Coast mahjong</strong> — snowbird &amp; resort private lessons:</p>
<p><a href="palm-beach-mahjong.html">Palm Beach</a> · <a href="boca-raton-fl-mahjong.html">Boca Raton</a> · <a href="jupiter-fl-mahjong.html">Jupiter</a> · <a href="st-augustine-mahjong.html">St Augustine</a></p>
<p><a href="palm-beaches-mahjong-hub.html">Palm Beaches</a> · <a href="florida-mahjong-hub.html">Florida hub</a></p>""",
        ),
        (
            "florida-gulf-south-mahjong-hub.html",
            "South Florida Gulf Mahjong | Naples, Sarasota & Tampa Bay",
            "South Florida Gulf mahjong — Naples, Sarasota, Tampa Bay, Fort Myers Gulf events.",
            "south florida gulf mahjong hub, naples sarasota mah jongg",
            "South Florida Gulf Mahjong Guide",
            """<p><strong>South FL Gulf mahjong</strong> — Gulf Coast private lessons:</p>
<p><a href="naples-florida-mahjong.html">Naples</a> · <a href="sarasota-mahjong.html">Sarasota</a> · <a href="tampa-mahjong.html">Tampa</a> · <a href="fort-myers-fl-mahjong.html">Fort Myers</a></p>
<p><a href="southwest-florida-mahjong-hub.html">SW Florida</a> · <a href="florida-mahjong-hub.html">Florida hub</a></p>""",
        ),
        (
            "lowcountry-southeast-mahjong-hub.html",
            "Lowcountry Southeast Mahjong | Charleston, Savannah & Beaufort",
            "Lowcountry Southeast mahjong — Charleston, Savannah, Beaufort, Hilton Head corridor.",
            "lowcountry southeast mahjong hub, charleston savannah mah jongg",
            "Lowcountry Southeast Mahjong Guide",
            """<p><strong>Lowcountry mahjong</strong> — coastal SC &amp; GA:</p>
<p><a href="charleston-sc-mahjong.html">Charleston</a> · <a href="savannah-mahjong.html">Savannah</a> · <a href="hilton-head-mahjong.html">Hilton Head</a> · <a href="beaufort-sc-mahjong.html">Beaufort SC</a></p>
<p><a href="lowcountry-sc-mahjong-hub.html">Lowcountry hub</a> · <a href="georgia-coast-mahjong-hub.html">GA Coast</a></p>""",
        ),
        (
            "virginia-tidewater-mahjong-hub.html",
            "Virginia Tidewater Mahjong | Virginia Beach, Norfolk & Williamsburg",
            "Virginia Tidewater mahjong — Virginia Beach, Norfolk, Williamsburg, Chesapeake.",
            "virginia tidewater mahjong hub, virginia beach mah jongg",
            "Virginia Tidewater Mahjong Guide",
            """<p><strong>Tidewater mahjong</strong> — Hampton Roads &amp; history coast:</p>
<p><a href="virginia-beach-mahjong.html">Virginia Beach</a> · <a href="norfolk-va-mahjong.html">Norfolk</a> · <a href="williamsburg-va-mahjong.html">Williamsburg</a> · <a href="richmond-mahjong.html">Richmond</a></p>
<p><a href="hampton-roads-va-mahjong-hub.html">Hampton Roads</a> · <a href="southeast-mahjong-hub.html">Southeast hub</a></p>""",
        ),
        (
            "sandhills-piedmont-mahjong-hub.html",
            "Sandhills & Piedmont Mahjong | Pinehurst, Greensboro & Columbia",
            "Sandhills Piedmont mahjong — Pinehurst, Greensboro, Winston-Salem, Columbia SC.",
            "sandhills piedmont mahjong hub, pinehurst greensboro mah jongg",
            "Sandhills & Piedmont Mahjong Guide",
            """<p><strong>Sandhills &amp; Piedmont mahjong</strong> — golf &amp; college towns:</p>
<p><a href="pinehurst-nc-mahjong.html">Pinehurst</a> · <a href="greensboro-mahjong.html">Greensboro</a> · <a href="winston-salem-mahjong.html">Winston-Salem</a> · <a href="columbia-sc-mahjong.html">Columbia SC</a></p>
<p><a href="sandhills-nc-mahjong-hub.html">Sandhills NC</a> · <a href="carolinas-mahjong-hub.html">Carolinas hub</a></p>""",
        ),
        (
            "gulf-coast-al-ms-mahjong-hub.html",
            "AL & MS Gulf Coast Mahjong | Mobile, Biloxi & Gulf Shores",
            "Alabama Mississippi Gulf Coast mahjong — Mobile, Gulf Shores, Biloxi, Ocean Springs.",
            "alabama mississippi gulf coast mahjong hub, gulf shores mah jongg",
            "AL & MS Gulf Coast Mahjong Guide",
            """<p><strong>AL &amp; MS Gulf Coast mahjong</strong> — beach week private lessons:</p>
<p><a href="gulf-shores-al-mahjong.html">Gulf Shores</a> · <a href="mobile-mahjong.html">Mobile</a> · <a href="biloxi-ms-mahjong.html">Biloxi</a> · <a href="ocean-springs-ms-mahjong.html">Ocean Springs</a></p>
<p><a href="alabama-gulf-coast-mahjong-hub.html">AL Gulf Coast</a> · <a href="gulf-coast-mahjong-hub.html">Gulf Coast hub</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.90"))

    for tup in WAVE39_CITIES:
        out.append(_city_from_tuple_southeast(city, tup))

    fraternities = [
        ("w39-se-uga", "University of Georgia", "UGA"),
        ("w39-se-auburn", "Auburn University", "Auburn"),
        ("w39-se-clemson", "Clemson University", "Clemson"),
        ("w39-se-usc", "University of South Carolina", "USC"),
        ("w39-se-unc", "UNC Chapel Hill", "UNC"),
        ("w39-se-duke", "Duke University", "Duke"),
        ("w39-se-vandy", "Vanderbilt", "Vandy"),
        ("w39-se-ut", "University of Tennessee", "UT"),
        ("w39-se-bama", "University of Alabama", "Bama"),
        ("w39-se-uf", "University of Florida", "UF"),
        ("w39-se-fsu", "Florida State", "FSU"),
        ("w39-se-gt", "Georgia Tech", "GT"),
        ("w39-se-wake", "Wake Forest", "Wake"),
        ("w39-se-furman", "Furman University", "Furman"),
        ("w39-se-samford", "Samford University", "Samford"),
        ("w39-se-mercer", "Mercer University", "Mercer"),
        ("w39-se-wofford", "Wofford College", "Wofford"),
        ("w39-se-citadel", "The Citadel", "Citadel"),
        ("w39-se-ccu", "Coastal Carolina", "CCU"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("w39-se-uga-sor", "UGA Sorority Events", "UGA"),
        ("w39-se-auburn-sor", "Auburn Sorority Events", "Auburn"),
        ("w39-se-clemson-sor", "Clemson Sorority Events", "Clemson"),
        ("w39-se-usc-sor", "USC SC Sorority Events", "USC"),
        ("w39-se-unc-sor", "UNC Sorority Events", "UNC"),
        ("w39-se-duke-sor", "Duke Sorority Events", "Duke"),
        ("w39-se-vandy-sor", "Vanderbilt Sorority Events", "Vandy"),
        ("w39-se-ut-sor", "UT Sorority Events", "UT"),
        ("w39-se-bama-sor", "Alabama Sorority Events", "Bama"),
        ("w39-se-uf-sor", "UF Sorority Events", "UF"),
        ("w39-se-fsu-sor", "FSU Sorority Events", "FSU"),
        ("w39-se-gt-sor", "Georgia Tech Sorority Events", "GT"),
        ("w39-se-wake-sor", "Wake Forest Sorority Events", "Wake"),
        ("w39-se-furman-sor", "Furman Sorority Events", "Furman"),
        ("w39-se-samford-sor", "Samford Sorority Events", "Samford"),
        ("w39-se-mercer-sor", "Mercer Sorority Events", "Mercer"),
        ("w39-se-wofford-sor", "Wofford Sorority Events", "Wofford"),
        ("w39-se-ccu-sor", "Coastal Carolina Sorority Events", "CCU"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ("lowcountry-luncheon-mahjong", "Lowcountry Luncheon", "lowcountry luncheon mahjong — Charleston style tile lunch", '<p><strong>Lowcountry luncheon mahjong</strong> — shrimp &amp; grits then tiles. <a href="charleston-sc-mahjong.html">Charleston</a> · <a href="southeast-mahjong-hub.html">Southeast hub</a>.</p>'),
        ("plantation-weekend-mahjong", "Plantation Weekend", "plantation weekend mahjong — South Georgia weekend tiles", '<p><strong>Plantation weekend mahjong</strong> — long tables, sweet tea. <a href="southern-mahjong.html">Southern mahjong</a>.</p>'),
        ("porch-swing-mahjong", "Porch Swing Party", "porch swing mahjong — Southern porch gathering", '<p><strong>Porch swing mahjong</strong> — front porch Southern style. <a href="porch-mahjong.html">Porch party</a>.</p>'),
        ("sec-tailgate-mahjong", "SEC Tailgate", "sec tailgate mahjong — football weekend tile party", '<p><strong>SEC tailgate mahjong</strong> — Saturday in the South. <a href="tailgate-mahjong.html">Tailgate</a>.</p>'),
        ("lake-lanier-weekend", "Lake Lanier Weekend", "lake lanier weekend mahjong — North Georgia lake house", '<p><strong>Lake Lanier weekend mahjong</strong> — Atlanta escape. <a href="north-georgia-mahjong-hub.html">North Georgia</a>.</p>'),
        ("buckhead-brunch-mahjong", "Buckhead Brunch", "buckhead brunch mahjong — Atlanta social brunch tiles", '<p><strong>Buckhead brunch mahjong</strong> — Atlanta social set. <a href="buckhead-mahjong.html">Buckhead</a>.</p>'),
        ("beach-club-south-mahjong", "Beach Club South", "beach club south mahjong — coastal club event", '<p><strong>Beach club South mahjong</strong> — members-only coast. <a href="country-club-mahjong.html">Country club</a>.</p>'),
        ("garden-club-south-mahjong", "Garden Club South", "garden club south mahjong — azalea season tiles", '<p><strong>Garden club South mahjong</strong> — spring garden tour add-on. <a href="garden-club-mahjong.html">Garden club</a>.</p>'),
        ("azalea-festival-mahjong", "Azalea Festival", "azalea festival mahjong — Wilmington festival week", '<p><strong>Azalea festival mahjong</strong> — coastal NC spring. <a href="wilmington-nc-mahjong.html">Wilmington</a>.</p>'),
        ("masters-hospitality-mahjong", "Masters Hospitality", "masters hospitality mahjong — Augusta week tiles", '<p><strong>Masters hospitality mahjong</strong> — Augusta area. <a href="augusta-ga-mahjong.html">Augusta</a>.</p>'),
        ("snowbird-southeast-mahjong", "Snowbird Southeast", "snowbird southeast mahjong — FL winter resident tiles", '<p><strong>Snowbird Southeast mahjong</strong> — winter in Florida. <a href="snowbird-mahjong.html">Snowbird</a>.</p>'),
        ("vacation-rental-beach-se", "Beach Rental SE", "beach rental southeast mahjong — OBX to 30A", '<p><strong>Beach rental Southeast mahjong</strong> — we come to the house. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("girls-weekend-charleston", "Girls Weekend Charleston", "girls weekend charleston mahjong — Charleston bachelorette alt", '<p><strong>Girls weekend Charleston mahjong</strong> — rainbow row energy. <a href="charleston-sc-mahjong.html">Charleston</a>.</p>'),
        ("girls-weekend-nashville", "Girls Weekend Nashville", "girls weekend nashville mahjong — bachelorette Broadway", '<p><strong>Girls weekend Nashville mahjong</strong> — honky tonk then tiles. <a href="nashville-mahjong.html">Nashville</a>.</p>'),
        ("bachelorette-savannah", "Bachelorette Savannah", "bachelorette savannah mahjong — historic district party", '<p><strong>Bachelorette Savannah mahjong</strong> — moss &amp; tiles. <a href="bachelorette-mahjong.html">Bachelorette</a>.</p>'),
        ("country-club-south-mahjong", "Country Club South", "country club south mahjong — Southern club social", '<p><strong>Country club South mahjong</strong> — league night upgrade. <a href="country-club-mahjong.html">Country club</a>.</p>'),
        ("church-supper-south", "Church Supper South", "church supper south mahjong — potluck and tiles", '<p><strong>Church supper South mahjong</strong> — fellowship hall fun. <a href="church-mahjong.html">Church</a>.</p>'),
        ("hoa-southeast-mahjong", "HOA Southeast", "hoa southeast mahjong — neighborhood social Southeast", '<p><strong>HOA Southeast mahjong</strong> — clubhouse lesson. <a href="hoa-mahjong.html">HOA</a>.</p>'),
        ("retirement-fl-mahjong", "Florida Retirement", "florida retirement community mahjong — active adult tiles", '<p><strong>Florida retirement mahjong</strong> — snowbird communities. <a href="retirement-community-mahjong.html">Retirement</a>.</p>'),
        ("tennessee-bachelorette", "Tennessee Bachelorette", "tennessee bachelorette mahjong — TN wedding weekend", '<p><strong>Tennessee bachelorette mahjong</strong> — Smokies or Nashville. <a href="wedding-mahjong.html">Wedding</a>.</p>'),
        ("carolina-shower-mahjong", "Carolina Shower", "carolina bridal shower mahjong — NC SC shower tiles", '<p><strong>Carolina shower mahjong</strong> — bridal shower classic. <a href="bridal-shower-mahjong.html">Bridal shower</a>.</p>'),
        ("atlanta-moms-night", "Atlanta Moms Night", "atlanta moms night mahjong — North Atlanta social", '<p><strong>Atlanta moms night mahjong</strong> — suburb social. <a href="moms-night-mahjong.html">Moms night</a>.</p>'),
        ("charlotte-book-club", "Charlotte Book Club", "charlotte book club mahjong — book club swap tiles", '<p><strong>Charlotte book club mahjong</strong> — Myers Park energy. <a href="book-club-mahjong.html">Book club</a>.</p>'),
        ("gulf-shores-week", "Gulf Shores Week", "gulf shores week mahjong — Alabama beach week", '<p><strong>Gulf Shores week mahjong</strong> — white sand tiles. <a href="gulf-shores-al-mahjong.html">Gulf Shores</a>.</p>'),
        ("hilton-head-golf", "Hilton Head Golf", "hilton head golf trip mahjong — golf trip tile night", '<p><strong>Hilton Head golf trip mahjong</strong> — après-18 holes. <a href="hilton-head-mahjong.html">Hilton Head</a>.</p>'),
        ("savannah-tybee-trip", "Savannah Tybee Trip", "savannah tybee trip mahjong — coastal GA weekend", '<p><strong>Savannah Tybee trip mahjong</strong> — historic coast. <a href="savannah-mahjong.html">Savannah</a>.</p>'),
        ("smokies-cabin-weekend", "Smokies Cabin Weekend", "smokies cabin weekend mahjong — Gatlinburg cabin", '<p><strong>Smokies cabin weekend mahjong</strong> — mountain cabin tiles. <a href="gatlinburg-tn-mahjong.html">Gatlinburg</a>.</p>'),
        ("lookout-mountain-retreat", "Lookout Mountain Retreat", "lookout mountain retreat mahjong — home turf getaway", '<p><strong>Lookout Mountain retreat mahjong</strong> — our backyard. <a href="lookout-mountain-georgia-mahjong.html">Lookout Mountain</a>.</p>'),
        ("new-orleans-brunch", "New Orleans Brunch", "new orleans brunch mahjong — NOLA brunch tiles", '<p><strong>New Orleans brunch mahjong</strong> — beignets &amp; tiles. <a href="new-orleans-mahjong.html">New Orleans</a>.</p>'),
        ("palm-beach-social", "Palm Beach Social", "palm beach social mahjong — Palm Beach season", '<p><strong>Palm Beach social mahjong</strong> — winter season. <a href="palm-beach-mahjong.html">Palm Beach</a>.</p>'),
        ("30a-rental-mahjong", "30A Rental", "30a rental mahjong — Rosemary Beach Seaside tiles", '<p><strong>30A rental mahjong</strong> — Florida panhandle chic. <a href="seaside-florida-mahjong.html">30A</a>.</p>'),
        ("mountain-brunswick", "Mountain to Coast", "mountain to coast mahjong — Asheville to coast trip", '<p><strong>Mountain to coast mahjong</strong> — Carolina road trip. <a href="carolinas-mahjong-hub.html">Carolinas</a>.</p>'),
        ("kentucky-derby-se", "Derby Party Southeast", "derby party southeast mahjong — Southern Derby gathering", '<p><strong>Derby party Southeast mahjong</strong> — hats &amp; hands. <a href="kentucky-derby-party-mahjong.html">Derby party</a>.</p>'),
        ("bourbon-trail-mahjong", "Bourbon Trail", "bourbon trail mahjong — Kentucky bourbon weekend", '<p><strong>Bourbon trail mahjong</strong> — Louisville &amp; Lexington. <a href="louisville-mahjong.html">Louisville</a>.</p>'),
        ("virginia-hunt-country", "Virginia Hunt Country", "virginia hunt country mahjong — Middleburg weekend", '<p><strong>Virginia hunt country mahjong</strong> — horse country tiles. <a href="middleburg-va-mahjong.html">Middleburg</a>.</p>'),
        ("tidewater-yacht-club", "Tidewater Yacht Club", "tidewater yacht club mahjong — Hampton Roads yacht club", '<p><strong>Tidewater yacht club mahjong</strong> — marina social. <a href="virginia-beach-mahjong.html">Virginia Beach</a>.</p>'),
        ("southern-book-tour", "Southern Book Tour", "southern book tour mahjong — author event crossover", '<p><strong>Southern book tour mahjong</strong> — bookstore event. <a href="book-club-mahjong.html">Book club</a>.</p>'),
        ("junior-league-south", "Junior League South", "junior league south mahjong — JL fundraiser tiles", '<p><strong>Junior League South mahjong</strong> — philanthropy classic. <a href="charity-mahjong-event.html">Charity</a>.</p>'),
        ("southeast-corporate", "Southeast Corporate", "southeast corporate mahjong — regional office event", '<p><strong>Southeast corporate mahjong</strong> — we travel to your office. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("real-estate-southeast", "Real Estate Southeast", "real estate southeast mahjong — brokerage client event", '<p><strong>Real estate Southeast mahjong</strong> — client appreciation. <a href="realtor-mahjong.html">Realtor</a>.</p>'),
        ("wedding-weekend-se", "Wedding Weekend SE", "wedding weekend southeast mahjong — Southern wedding tiles", '<p><strong>Wedding weekend Southeast mahjong</strong> — welcome party activity. <a href="wedding-mahjong.html">Wedding</a>.</p>'),
        ("family-reunion-se", "Family Reunion SE", "family reunion southeast mahjong — multigenerational South", '<p><strong>Family reunion Southeast mahjong</strong> — lake house or beach. <a href="family-reunion-mahjong.html">Family reunion</a>.</p>'),
        ("sunday-supper-south", "Sunday Supper South", "sunday supper south mahjong — Southern Sunday dinner tiles", '<p><strong>Sunday supper South mahjong</strong> — after church energy. <a href="sunday-supper-mahjong.html">Sunday supper</a>.</p>'),
        ("sweet-tea-social", "Sweet Tea Social", "sweet tea social mahjong — Southern hospitality tiles", '<p><strong>Sweet tea social mahjong</strong> — pour &amp; play. <a href="southern-mahjong.html">Southern mahjong</a>.</p>'),
        ("magnolia-market-trip", "Magnolia Market Trip", "magnolia market trip mahjong — Waco road trip add-on", '<p><strong>Magnolia market trip mahjong</strong> — girls trip tiles. <a href="waco-tx-mahjong.html">Waco</a>.</p>'),
        ("peach-season-mahjong", "Peach Season", "peach season mahjong — Georgia peach summer party", '<p><strong>Peach season mahjong</strong> — Georgia summer. <a href="georgia-mahjong.html">Georgia</a>.</p>'),
        ("coastal-georgia-islands", "Coastal GA Islands", "coastal georgia islands mahjong — St Simons Jekyll tiles", '<p><strong>Coastal GA islands mahjong</strong> — Golden Isles. <a href="golden-isles-ga-mahjong-hub.html">Golden Isles</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("southeast-mahjong-travel.html", "Travel Fees", "southeast mahjong travel — how booking works out of area", '<p>We travel across the <strong>Southeast</strong> — <a href="book-mahjong-lesson.html">Book</a> · <a href="southeast-mahjong-hub.html">Southeast hub</a>.</p>'),
        ("southeast-home-base.html", "Home Base", "southeast home base mahjong — Lookout Mountain GA TN", '<p>Our <strong>home base</strong> is Lookout Mountain — <a href="lookout-mountain-georgia-mahjong.html">GA</a> · <a href="lookout-mountain-tn-mahjong.html">TN</a>.</p>'),
        ("southeast-four-player.html", "Four Players", "southeast four player mahjong — standard table size", '<p>American mahjong needs <strong>four players</strong> — we teach at <a href="mahjong-101.html">Mahjong 101</a>.</p>'),
        ("southeast-nmjl-card.html", "NMJL Card Southeast", "nmjl card southeast — same card nationwide", '<p>The <strong>NMJL card</strong> is the same in every Southeast city — <a href="nmjl-card.html">NMJL card</a>.</p>'),
        ("southeast-beginner-class.html", "Beginner Class", "southeast beginner class mahjong — Mahjong 101 format", '<p><strong>Beginner class</strong> — $125/person — <a href="mahjong-101.html">Mahjong 101</a> · <a href="beginner-mahjong.html">Beginner</a>.</p>'),
        ("southeast-private-home.html", "Private Home", "private home southeast mahjong — we come to you", '<p>We teach in your <strong>private home</strong> across the Southeast — <a href="private-mahjong-lessons.html">Private lessons</a>.</p>'),
        ("southeast-country-club-lesson.html", "Country Club Lesson", "country club lesson southeast — club-hosted event", '<p><strong>Country club lessons</strong> — <a href="country-club-mahjong.html">Country club</a> · <a href="southeast-mahjong-hub.html">Southeast</a>.</p>'),
        ("southeast-resort-lesson.html", "Resort Lesson", "resort lesson southeast — resort and hotel events", '<p><strong>Resort lessons</strong> — <a href="resort-mahjong.html">Resort</a> · <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("southeast-charleston-rules.html", "Charleston Rules", "charleston rules southeast — American mahjong passing", '<p>The <strong>Charleston</strong> — <a href="mahjong-charleston.html">Charleston guide</a> · <a href="mahjong-101.html">101</a>.</p>'),
        ("southeast-jokers.html", "Jokers Southeast", "jokers southeast mahjong — wild tiles American rules", '<p><strong>Jokers</strong> in American mahjong — <a href="mahjong-jokers.html">Jokers guide</a>.</p>'),
        ("southeast-booking-email.html", "Booking Email", "book southeast mahjong — email to schedule", '<p>Book: lookoutmountainmahjong@gmail.com · (919) 247-3392 — <a href="book-mahjong-lesson.html">Book page</a>.</p>'),
        ("southeast-group-size.html", "Group Size", "group size southeast mahjong — 4 to 8 players ideal", '<p>Ideal <strong>group size</strong> 4–8 for Mahjong 101 — <a href="mahjong-101.html">101</a>.</p>'),
        ("southeast-tml-tiles.html", "TML Tiles", "tml tiles southeast — The Mahjong Line ambassador", '<p>We love <a href="the-mahjong-line.html">The Mahjong Line</a> — code LOOKOUTMOUNTAIN — <a href="mahjong-tiles.html">Tiles</a>.</p>'),
        ("southeast-greenbrier.html", "Greenbrier Southeast", "greenbrier southeast mahjong — Mahj Jen at Greenbrier", '<p><strong>Greenbrier</strong> events — <a href="greenbrier-mahjong.html">Greenbrier</a> · <a href="jen-kline-greenbrier-mahjong.html">Mahj Jen</a>.</p>'),
        ("southeast-lessons-near-me.html", "Lessons Near Me SE", "mahjong lessons near me southeast — find your city", '<p><strong>Lessons near me</strong> — <a href="mahjong-lessons-near-me.html">Near me</a> · <a href="southeast-mahjong-hub.html">Southeast cities</a>.</p>'),
        ("southeast-corporate-retreat.html", "Corporate Retreat SE", "corporate retreat southeast mahjong — team building South", '<p><strong>Corporate retreat</strong> — <a href="corporate-mahjong-events.html">Corporate</a> · <a href="leadership-offsite-mahjong.html">Offsite</a>.</p>'),
        ("southeast-snowbird-club.html", "Snowbird Club", "snowbird club southeast mahjong — winter club season FL", '<p><strong>Snowbird club</strong> season — <a href="snowbird-mahjong.html">Snowbird</a> · <a href="florida-mahjong-hub.html">Florida</a>.</p>'),
        ("southeast-ladies-luncheon.html", "Ladies Luncheon SE", "ladies luncheon southeast mahjong — Southern luncheon format", '<p><strong>Ladies luncheon</strong> — <a href="ladies-luncheon-mahjong.html">Luncheon</a> · <a href="southern-mahjong.html">Southern</a>.</p>'),
        ("southeast-mahjong-102.html", "Mahjong 102 SE", "mahjong 102 southeast — advanced lesson after 101", '<p>After 101 take <strong>Mahjong 102</strong> — $115/person — <a href="mahjong-102.html">102</a>.</p>'),
        ("southeast-holiday-party.html", "Holiday Party SE", "holiday party southeast mahjong — December Southern social", '<p><strong>Holiday party</strong> — <a href="holiday-mahjong-party.html">Holiday party</a> · <a href="christmas-mahjong-party.html">Christmas</a>.</p>'),
        ("southeast-spring-fling.html", "Spring Fling SE", "spring fling southeast mahjong — spring garden party tiles", '<p><strong>Spring fling</strong> — <a href="spring-mahjong-party.html">Spring party</a> · <a href="garden-club-mahjong.html">Garden club</a>.</p>'),
        ("southeast-summer-lake.html", "Summer Lake SE", "summer lake southeast mahjong — lake house summer", '<p><strong>Summer lake</strong> house mahjong — <a href="lake-house-mahjong.html">Lake house</a>.</p>'),
        ("southeast-fall-garden.html", "Fall Garden SE", "fall garden southeast mahjong — fall patio party", '<p><strong>Fall garden</strong> party — <a href="fall-mahjong-party.html">Fall party</a> · <a href="porch-mahjong.html">Porch</a>.</p>'),
        ("southeast-instagram-tips.html", "Instagram Tips SE", "instagram mahjong tips southeast — follow daily tips", '<p>Daily tips <a href="https://www.instagram.com/lookoutmountainmahjong/" rel="noopener noreferrer">@lookoutmountainmahjong</a> · <a href="instagram-mahjong.html">Instagram</a>.</p>'),
        ("southeast-viral-mahjong.html", "Viral Mahjong SE", "viral mahjong southeast — Get Mahjn trend", '<p><strong>Viral mahjong</strong> — <a href="viral-mahjong.html">Viral</a> · <a href="get-mahjn.html">Get Mahj\'n</a>.</p>'),
        ("southeast-charity-fundraiser.html", "Charity Fundraiser SE", "charity fundraiser southeast mahjong — philanthropy tiles", '<p><strong>Charity fundraiser</strong> — <a href="charity-mahjong-event.html">Charity events</a>.</p>'),
        ("southeast-mothers-day.html", "Mothers Day SE", "mothers day southeast mahjong — May Southern celebration", '<p><strong>Mother\'s Day</strong> mahjong — <a href="mothers-day-mahjong.html">Mother\'s Day</a>.</p>'),
        ("southeast-friendsgiving-se.html", "Friendsgiving SE", "friendsgiving southeast mahjong — November Southern gather", '<p><strong>Friendsgiving Southeast</strong> — <a href="friendsgiving-mahjong.html">Friendsgiving</a>.</p>'),
        ("southeast-new-year-brunch.html", "New Year Brunch SE", "new year brunch southeast mahjong — January social", '<p><strong>New Year brunch</strong> — <a href="new-years-mahjong.html">New Year</a> · <a href="mahjong-brunch.html">Brunch</a>.</p>'),
        ("southeast-engagement-party-se.html", "Engagement Party SE", "engagement party southeast mahjong — Southern engagement", '<p><strong>Engagement party</strong> — <a href="engagement-party-mahjong.html">Engagement</a> · <a href="wedding-mahjong.html">Wedding</a>.</p>'),
        ("southeast-bridal-luncheon-se.html", "Bridal Luncheon SE", "bridal luncheon southeast mahjong — pre-wedding luncheon", '<p><strong>Bridal luncheon</strong> — <a href="bridal-luncheon-mahjong.html">Bridal luncheon</a>.</p>'),
        ("southeast-girls-night-se.html", "Girls Night SE", "girls night southeast mahjong — Southern girls night", '<p><strong>Girls night Southeast</strong> — <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("southeast-wine-night-se.html", "Wine Night SE", "wine night southeast mahjong — wine and tiles South", '<p><strong>Wine night</strong> — <a href="wine-and-mahjong.html">Wine &amp; mahjong</a>.</p>'),
        ("southeast-cocktail-party-se.html", "Cocktail Party SE", "cocktail party southeast mahjong — cocktail then tiles", '<p><strong>Cocktail party</strong> — <a href="cocktail-party-mahjong.html">Cocktail party</a>.</p>'),
        ("southeast-pool-party-se.html", "Pool Party SE", "pool party southeast mahjong — summer pool social", '<p><strong>Pool party</strong> — <a href="pool-party-mahjong.html">Pool party</a> · <a href="beach-club-mahjong.html">Beach club</a>.</p>'),
        ("southeast-anniversary-party-se.html", "Anniversary Party SE", "anniversary party southeast mahjong — milestone celebration", '<p><strong>Anniversary party</strong> — <a href="anniversary-mahjong.html">Anniversary</a>.</p>'),
        ("southeast-neighborhood-social-se.html", "Neighborhood Social SE", "neighborhood social southeast mahjong — block social", '<p><strong>Neighborhood social</strong> — <a href="neighborhood-mahjong.html">Neighborhood</a> · <a href="hoa-mahjong.html">HOA</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
