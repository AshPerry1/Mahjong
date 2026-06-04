# -*- coding: utf-8 -*-
"""Mega Wave 31 — ~600+ pages (500 cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave31_cities_data import WAVE31_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_31(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "lake-tahoe-mahjong-hub.html",
            "Lake Tahoe Mahjong | Incline Village, South Lake & Truckee",
            "Lake Tahoe mahjong — Incline Village, South Lake Tahoe, Truckee, North Shore private events.",
            "lake tahoe mahjong hub, incline village mah jongg",
            "Lake Tahoe Mahjong Guide",
            """<p><strong>Lake Tahoe mahjong</strong> — mountain-lake private lessons:</p>
<p><a href="incline-village-nv-mahjong.html">Incline Village</a> · <a href="south-lake-tahoe-ca-mahjong.html">South Lake Tahoe</a> · <a href="truckee-ca-mahjong.html">Truckee</a> · <a href="reno-nv-mahjong.html">Reno</a></p>
<p><a href="nevada-mahjong-hub.html">Nevada hub</a> · <a href="california-mahjong-hub.html">California hub</a></p>""",
        ),
        (
            "berkshires-ma-mahjong-hub.html",
            "Berkshires MA Mahjong | Lenox, Stockbridge & Great Barrington",
            "Berkshires Massachusetts mahjong — Lenox, Stockbridge, Williamstown, summer culture corridor.",
            "berkshires massachusetts mahjong hub, lenox mah jongg",
            "Berkshires MA Mahjong Guide",
            """<p><strong>Berkshires mahjong</strong> — summer and fall private events:</p>
<p><a href="lenox-ma-mahjong.html">Lenox</a> · <a href="stockbridge-ma-mahjong.html">Stockbridge</a> · <a href="great-barrington-ma-mahjong.html">Great Barrington</a> · <a href="williamstown-ma-mahjong.html">Williamstown</a></p>
<p><a href="massachusetts-mahjong-hub.html">Massachusetts hub</a> · <a href="new-england-mahjong-hub.html">New England</a></p>""",
        ),
        (
            "oregon-coast-mahjong-hub.html",
            "Oregon Coast Mahjong | Cannon Beach, Newport & Seaside",
            "Oregon Coast mahjong — Cannon Beach, Newport, Seaside, coastal highway private events.",
            "oregon coast mahjong hub, cannon beach mah jongg",
            "Oregon Coast Mahjong Guide",
            """<p><strong>Oregon Coast mahjong</strong> — Pacific private lessons:</p>
<p><a href="cannon-beach-or-mahjong.html">Cannon Beach</a> · <a href="newport-or-mahjong.html">Newport OR</a> · <a href="seaside-or-mahjong.html">Seaside OR</a> · <a href="lincoln-city-or-mahjong.html">Lincoln City</a></p>
<p><a href="oregon-mahjong-hub.html">Oregon hub</a> · <a href="pacific-northwest-mahjong-hub.html">PNW hub</a></p>""",
        ),
        (
            "delmarva-mahjong-hub.html",
            "Delmarva Mahjong | Rehoboth, Ocean City & Salisbury",
            "Delmarva mahjong — Delaware and Maryland beaches, Rehoboth, Ocean City, Salisbury.",
            "delmarva mahjong hub, rehoboth beach mah jongg",
            "Delmarva Mahjong Guide",
            """<p><strong>Delmarva mahjong</strong> — beach week private events:</p>
<p><a href="rehoboth-beach-de-mahjong.html">Rehoboth Beach</a> · <a href="lewes-de-mahjong.html">Lewes</a> · <a href="ocean-city-md-mahjong.html">Ocean City MD</a> · <a href="salisbury-md-mahjong.html">Salisbury</a></p>
<p><a href="delaware-mahjong-hub.html">Delaware hub</a> · <a href="maryland-mahjong-hub.html">Maryland hub</a></p>""",
        ),
        (
            "western-slope-co-mahjong-hub.html",
            "Western Slope CO Mahjong | Grand Junction, Aspen & Vail",
            "Western Slope Colorado mahjong — Grand Junction, Aspen, Vail, mountain resort private events.",
            "western slope colorado mahjong hub, grand junction mah jongg",
            "Western Slope CO Mahjong Guide",
            """<p><strong>Western Slope mahjong</strong> — resort and valley private lessons:</p>
<p><a href="grand-junction-co-mahjong.html">Grand Junction</a> · <a href="aspen-co-mahjong.html">Aspen</a> · <a href="vail-co-mahjong.html">Vail</a> · <a href="durango-co-mahjong.html">Durango</a></p>
<p><a href="colorado-mahjong-hub.html">Colorado hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "alabama-gulf-coast-mahjong-hub.html",
            "Alabama Gulf Coast Mahjong | Gulf Shores & Orange Beach",
            "Alabama Gulf Coast mahjong — Gulf Shores, Orange Beach, Mobile Bay private events.",
            "alabama gulf coast mahjong hub, gulf shores mah jongg",
            "Alabama Gulf Coast Mahjong Guide",
            """<p><strong>AL Gulf Coast mahjong</strong> — beach rental tile nights:</p>
<p><a href="gulf-shores-al-mahjong.html">Gulf Shores</a> · <a href="orange-beach-al-mahjong.html">Orange Beach</a> · <a href="mobile-mahjong.html">Mobile</a> · <a href="fairhope-al-mahjong.html">Fairhope</a></p>
<p><a href="alabama-mahjong-hub.html">Alabama hub</a> · <a href="gulf-coast-mahjong-hub.html">Gulf Coast hub</a></p>""",
        ),
        (
            "san-juan-islands-wa-mahjong-hub.html",
            "San Juan Islands WA Mahjong | Friday Harbor & Orcas",
            "San Juan Islands WA mahjong — Friday Harbor, Orcas Island, ferry-country private events.",
            "san juan islands washington mahjong hub, friday harbor mah jongg",
            "San Juan Islands WA Mahjong Guide",
            """<p><strong>San Juan Islands mahjong</strong> — island getaway private lessons:</p>
<p><a href="friday-harbor-wa-mahjong.html">Friday Harbor</a> · <a href="anacortes-wa-mahjong.html">Anacortes</a> · <a href="bellingham-wa-mahjong.html">Bellingham</a> · <a href="seattle-mahjong.html">Seattle</a></p>
<p><a href="washington-mahjong-hub.html">Washington hub</a> · <a href="puget-sound-mahjong-hub.html">Puget Sound</a></p>""",
        ),
        (
            "brandywine-valley-pa-mahjong-hub.html",
            "Brandywine Valley PA Mahjong | Chadds Ford & Wilmington Area",
            "Brandywine Valley mahjong — Chadds Ford, Kennett Square, Wilmington DE corridor events.",
            "brandywine valley mahjong hub, chadds ford mah jongg",
            "Brandywine Valley Mahjong Guide",
            """<p><strong>Brandywine Valley mahjong</strong> — garden country private events:</p>
<p><a href="chadds-ford-pa-mahjong.html">Chadds Ford</a> · <a href="kennett-square-pa-mahjong.html">Kennett Square</a> · <a href="west-chester-pa-mahjong.html">West Chester</a> · <a href="wilmington-de-mahjong.html">Wilmington DE</a></p>
<p><a href="pennsylvania-mahjong-hub.html">Pennsylvania hub</a> · <a href="delaware-mahjong-hub.html">Delaware hub</a></p>""",
        ),
        (
            "catskills-ny-mahjong-hub.html",
            "Catskills NY Mahjong | Woodstock, Hudson & Rhinebeck",
            "Catskills NY mahjong — Woodstock, Hudson, Rhinebeck, mountain getaway private events.",
            "catskills new york mahjong hub, woodstock ny mah jongg",
            "Catskills NY Mahjong Guide",
            """<p><strong>Catskills mahjong</strong> — Hudson Valley adjacent private lessons:</p>
<p><a href="woodstock-ny-mahjong.html">Woodstock NY</a> · <a href="hudson-ny-mahjong.html">Hudson NY</a> · <a href="rhinebeck-ny-mahjong.html">Rhinebeck</a> · <a href="kingston-ny-mahjong.html">Kingston NY</a></p>
<p><a href="hudson-valley-mahjong-hub.html">Hudson Valley hub</a> · <a href="new-york-mahjong-hub.html">New York hub</a></p>""",
        ),
        (
            "nebraska-panhandle-mahjong-hub.html",
            "Nebraska Panhandle Mahjong | Scottsbluff & North Platte",
            "Nebraska Panhandle mahjong — Scottsbluff, North Platte, High Plains private events.",
            "nebraska panhandle mahjong hub, scottsbluff mah jongg",
            "Nebraska Panhandle Mahjong Guide",
            """<p><strong>Nebraska Panhandle mahjong</strong> — High Plains private lessons:</p>
<p><a href="scottsbluff-ne-mahjong.html">Scottsbluff</a> · <a href="north-platte-ne-mahjong.html">North Platte</a> · <a href="grand-island-ne-mahjong.html">Grand Island</a> · <a href="omaha-ne-mahjong.html">Omaha</a></p>
<p><a href="nebraska-mahjong-hub.html">Nebraska hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "arklatex-mahjong-hub.html",
            "Arklatex Mahjong | Shreveport, Texarkana & Tyler",
            "Arklatex mahjong — Shreveport, Texarkana, Tyler, AR/LA/TX border private events.",
            "arklatex mahjong hub, shreveport mah jongg",
            "Arklatex Mahjong Guide",
            """<p><strong>Arklatex mahjong</strong> — tri-state private lessons:</p>
<p><a href="shreveport-mahjong.html">Shreveport</a> · <a href="texarkana-tx-mahjong.html">Texarkana</a> · <a href="tyler-tx-mahjong.html">Tyler</a> · <a href="monroe-la-mahjong.html">Monroe LA</a></p>
<p><a href="louisiana-mahjong-hub.html">Louisiana hub</a> · <a href="texas-mahjong-hub.html">Texas hub</a></p>""",
        ),
        (
            "southwest-florida-mahjong-hub.html",
            "Southwest Florida Mahjong | Naples, Fort Myers & Marco",
            "Southwest Florida mahjong — Naples, Fort Myers, Marco Island, Gulf private events.",
            "southwest florida mahjong hub, naples florida mah jongg",
            "Southwest Florida Mahjong Guide",
            """<p><strong>SW Florida mahjong</strong> — Gulf Coast snowbird private lessons:</p>
<p><a href="naples-florida-mahjong.html">Naples</a> · <a href="fort-myers-fl-mahjong.html">Fort Myers</a> · <a href="cape-coral-fl-mahjong.html">Cape Coral</a> · <a href="sarasota-mahjong.html">Sarasota</a></p>
<p><a href="florida-mahjong-hub.html">Florida hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE31_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("alpha-epsilon-pi", "Alpha Epsilon Pi", "AEPi"),
        ("alpha-gamma-rho", "Alpha Gamma Rho", "AGR"),
        ("alpha-sigma-phi", "Alpha Sigma Phi", "Alpha Sig"),
        ("beta-chi-theta", "Beta Chi Theta", "Beta Chi"),
        ("delta-chi", "Delta Chi", "Delta Chi"),
        ("delta-phi", "Delta Phi", "Delta Phi"),
        ("delta-sigma-phi", "Delta Sigma Phi", "DSP"),
        ("kappa-sigma", "Kappa Sigma", "Kappa Sig"),
        ("lambda-phi-epsilon", "Lambda Phi Epsilon", "Lambda Phi"),
        ("phi-gamma-delta", "Phi Gamma Delta", "FIJI"),
        ("phi-kappa-psi", "Phi Kappa Psi", "Phi Psi"),
        ("phi-kappa-sigma", "Phi Kappa Sigma", "Phi Kap Sig"),
        ("phi-sigma-kappa", "Phi Sigma Kappa", "Phi Sig Kap"),
        ("pi-kappa-alpha", "Pi Kappa Alpha", "Pike"),
        ("pi-kappa-phi", "Pi Kappa Phi", "Pi Kapp"),
        ("sigma-alpha-epsilon", "Sigma Alpha Epsilon", "SAE"),
        ("sigma-phi-epsilon", "Sigma Phi Epsilon", "Sig Ep"),
        ("tau-kappa-epsilon", "Tau Kappa Epsilon", "TKE"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("alpha-chi-omega", "Alpha Chi Omega", "Alpha Chi"),
        ("alpha-gamma-delta", "Alpha Gamma Delta", "AGD"),
        ("alpha-omicron-pi", "Alpha Omicron Pi", "AOII"),
        ("alpha-sigma-alpha", "Alpha Sigma Alpha", "ASA"),
        ("alpha-sigma-tau", "Alpha Sigma Tau", "AST"),
        ("delta-phi-epsilon", "Delta Phi Epsilon", "DPhiE"),
        ("delta-zeta", "Delta Zeta", "DZ"),
        ("gamma-sigma-sigma", "Gamma Sigma Sigma", "GSS"),
        ("kappa-kappa-gamma", "Kappa Kappa Gamma", "KKG"),
        ("phi-sigma-sigma", "Phi Sigma Sigma", "Phi Sig"),
        ("sigma-delta-tau", "Sigma Delta Tau", "SDT"),
        ("sigma-sigma-sigma", "Sigma Sigma Sigma", "Tri Sigma"),
        ("theta-eta", "Theta Eta", "Theta Eta"),
        ("zeta-phi-beta", "Zeta Phi Beta", "ZPhiB"),
        ("delta-delta-delta", "Delta Delta Delta", "Tri Delt"),
        ("kappa-kappa-psi", "Kappa Kappa Psi", "KKPsi"),
        ("sigma-alpha-iota", "Sigma Alpha Iota", "SAI"),
        ("tau-beta-sigma", "Tau Beta Sigma", "TBS"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ("mahjong-club-startup", "Club Startup", "mahjong club startup — launch your weekly group", '<p><strong>Club startup</strong> — we teach your first four tables. <a href="weekly-mahjong-club-mahjong.html">Weekly club</a>.</p>'),
        ("monthly-mahjong-meetup", "Monthly Meetup", "monthly mahjong meetup — recurring social tile night", '<p><strong>Monthly meetup</strong> — same crew, new hands. <a href="mahjong-club.html">Mahjong club</a>.</p>'),
        ("quarterly-mahjong-social", "Quarterly Social", "quarterly mahjong social — seasonal group event", '<p><strong>Quarterly social</strong> — mark the calendar. <a href="ladies-luncheon-mahjong.html">Luncheon</a>.</p>'),
        ("annual-mahjong-retreat", "Annual Retreat", "annual mahjong retreat — weekend getaway tiles", '<p><strong>Annual retreat</strong> — your group\'s signature weekend. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("neighbors-night", "Neighbors Night", "neighbors night mahjong — block party with tiles", '<p><strong>Neighbors night</strong> — HOA-friendly fun. <a href="hoa-mahjong.html">HOA</a>.</p>'),
        ("block-party-mahjong", "Block Party", "block party mahjong — street festival tile station", '<p><strong>Block party mahjong</strong> — we run a teaching table. <a href="community-center-mahjong.html">Community</a>.</p>'),
        ("open-house-mahjong", "Open House", "open house mahjong — realtor open house activity", '<p><strong>Open house mahjong</strong> — memorable listing event. <a href="realtor-mahjong.html">Realtor</a>.</p>'),
        ("listing-celebration", "Listing Celebration", "listing celebration mahjong — sold sign party tiles", '<p><strong>Listing celebration</strong> — celebrate closings with tiles. <a href="realtor-mahjong.html">Realtor</a>.</p>'),
        ("client-appreciation", "Client Appreciation", "client appreciation mahjong — thank your best clients", '<p><strong>Client appreciation mahjong</strong> — boutique service. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("employee-appreciation", "Employee Appreciation", "employee appreciation mahjong — staff thank-you tiles", '<p><strong>Employee appreciation</strong> — morale booster. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("holiday-office-party", "Holiday Office Party", "holiday office party mahjong — December team event", '<p><strong>Holiday office party mahjong</strong> — better than Secret Santa. <a href="holiday-mahjong-party.html">Holiday party</a>.</p>'),
        ("summer-intern-event", "Summer Intern Event", "summer intern event mahjong — onboarding with tiles", '<p><strong>Summer intern event</strong> — team bonding. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("board-retreat", "Board Retreat", "board retreat mahjong — nonprofit board social", '<p><strong>Board retreat mahjong</strong> — icebreaker before business. <a href="nonprofit-mahjong.html">Nonprofit</a>.</p>'),
        ("donor-appreciation", "Donor Appreciation", "donor appreciation mahjong — thank major donors", '<p><strong>Donor appreciation</strong> — cultured stewardship. <a href="charity-mahjong-event.html">Charity</a>.</p>'),
        ("volunteer-thank-you", "Volunteer Thank You", "volunteer thank you mahjong — reward your volunteers", '<p><strong>Volunteer thank you</strong> — tiles for the team. <a href="charity-mahjong-event.html">Charity</a>.</p>'),
        ("museum-gala", "Museum Gala", "museum gala mahjong — cultural fundraiser tiles", '<p><strong>Museum gala mahjong</strong> — upscale add-on. <a href="art-gallery-mahjong.html">Art gallery</a>.</p>'),
        ("library-friends", "Library Friends", "library friends mahjong — friends of the library event", '<p><strong>Library friends mahjong</strong> — quiet fun, big impact. <a href="community-center-mahjong.html">Community</a>.</p>'),
        ("historical-society", "Historical Society", "historical society mahjong — heritage group social", '<p><strong>Historical society mahjong</strong> — timeless game night. <a href="civic-club-mahjong.html">Civic club</a>.</p>'),
        ("rotary-club", "Rotary Club", "rotary club mahjong — rotary social with tiles", '<p><strong>Rotary club mahjong</strong> — service club crossover. <a href="civic-club-mahjong.html">Civic club</a>.</p>'),
        ("lions-club", "Lions Club", "lions club mahjong — lions club game night", '<p><strong>Lions club mahjong</strong> — community fellowship. <a href="civic-club-mahjong.html">Civic club</a>.</p>'),
        ("kiwanis-club", "Kiwanis Club", "kiwanis club mahjong — kiwanis social tiles", '<p><strong>Kiwanis club mahjong</strong> — family-friendly format. <a href="civic-club-mahjong.html">Civic club</a>.</p>'),
        ("chamber-of-commerce", "Chamber of Commerce", "chamber of commerce mahjong — business mixer tiles", '<p><strong>Chamber mixer mahjong</strong> — networking with play. <a href="womens-networking-mahjong.html">Networking</a>.</p>'),
        ("coworking-space", "Coworking Space", "coworking space mahjong — coworking community night", '<p><strong>Coworking space mahjong</strong> — member perk event. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("startup-team", "Startup Team", "startup team mahjong — startup offsite tiles", '<p><strong>Startup team mahjong</strong> — culture building. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("franchise-meeting", "Franchise Meeting", "franchise meeting mahjong — franchisee conference social", '<p><strong>Franchise meeting mahjong</strong> — energize the room. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("sales-kickoff", "Sales Kickoff", "sales kickoff mahjong — SKO team building tiles", '<p><strong>Sales kickoff mahjong</strong> — break the keynote fatigue. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("leadership-offsite", "Leadership Offsite", "leadership offsite mahjong — executive retreat tiles", '<p><strong>Leadership offsite mahjong</strong> — connect beyond slides. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("womens-leadership", "Women's Leadership", "womens leadership mahjong — women leaders tile night", '<p><strong>Women\'s leadership mahjong</strong> — empower through play. <a href="womens-networking-mahjong.html">Networking</a>.</p>'),
        ("mompreneur-meetup", "Mompreneur Meetup", "mompreneur meetup mahjong — mom business owners tiles", '<p><strong>Mompreneur meetup mahjong</strong> — network and laugh. <a href="moms-night-mahjong.html">Moms night</a>.</p>'),
        ("dad-gang-night", "Dad Gang Night", "dad gang night mahjong — dads group tile night", '<p><strong>Dad gang night mahjong</strong> — grill then play. <a href="guys-trip-mahjong.html">Guys trip</a>.</p>'),
        ("grandparents-day", "Grandparents Day", "grandparents day mahjong — multigenerational tile lesson", '<p><strong>Grandparents day mahjong</strong> — teach the grandkids. <a href="family-reunion-mahjong.html">Family</a>.</p>'),
        ("multigenerational-brunch", "Multigenerational Brunch", "multigenerational brunch mahjong — three generations tiles", '<p><strong>Multigenerational brunch mahjong</strong> — everyone plays. <a href="family-reunion-mahjong.html">Family</a>.</p>'),
        ("college-reunion", "College Reunion", "college reunion mahjong — alumni weekend tiles", '<p><strong>College reunion mahjong</strong> — same chaos, new game. <a href="reunion-mahjong.html">Reunion</a>.</p>'),
        ("high-school-reunion", "High School Reunion", "high school reunion mahjong — class reunion tile night", '<p><strong>High school reunion mahjong</strong> — break the ice. <a href="reunion-mahjong.html">Reunion</a>.</p>'),
        ("military-spouse", "Military Spouse", "military spouse mahjong — base spouse group tiles", '<p><strong>Military spouse mahjong</strong> — PCS-friendly fun. <a href="military-wives-mahjong.html">Military wives</a>.</p>'),
        ("deployment-sendoff", "Deployment Sendoff", "deployment sendoff mahjong — sendoff party tiles", '<p><strong>Deployment sendoff mahjong</strong> — gather before they ship. <a href="military-wives-mahjong.html">Military</a>.</p>'),
        ("welcome-home-party", "Welcome Home Party", "welcome home party mahjong — homecoming celebration tiles", '<p><strong>Welcome home party mahjong</strong> — celebrate return. <a href="military-wives-mahjong.html">Military</a>.</p>'),
        ("retirement-community", "Retirement Community", "retirement community mahjong — senior living social", '<p><strong>Retirement community mahjong</strong> — activity director favorite. <a href="senior-center-mahjong.html">Senior center</a>.</p>'),
        ("assisted-living", "Assisted Living", "assisted living mahjong — assisted living activity", '<p><strong>Assisted living mahjong</strong> — gentle pace, big smiles. <a href="senior-center-mahjong.html">Senior center</a>.</p>'),
        ("memory-care", "Memory Care", "memory care mahjong — adapted lesson for memory care", '<p><strong>Memory care mahjong</strong> — simplified, joyful format. <a href="senior-center-mahjong.html">Senior center</a>.</p>'),
        ("birthday-milestone", "Milestone Birthday", "milestone birthday mahjong — 40th 50th 60th tile party", '<p><strong>Milestone birthday mahjong</strong> — the main event. <a href="birthday-mahjong.html">Birthday</a>.</p>'),
        ("surprise-party", "Surprise Party", "surprise party mahjong — surprise guest activity", '<p><strong>Surprise party mahjong</strong> — keep them busy until reveal. <a href="birthday-mahjong.html">Birthday</a>.</p>'),
        ("divorce-party", "Divorce Party", "divorce party mahjong — fresh start celebration tiles", '<p><strong>Divorce party mahjong</strong> — new chapter energy. <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("promotion-party", "Promotion Party", "promotion party mahjong — celebrate the new title", '<p><strong>Promotion party mahjong</strong> — toast with tiles. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("new-home-celebration", "New Home Celebration", "new home celebration mahjong — housewarming tiles", '<p><strong>New home celebration mahjong</strong> — break in the living room. <a href="housewarming-mahjong.html">Housewarming</a>.</p>'),
        ("closing-day-party", "Closing Day Party", "closing day party mahjong — real estate closing celebration", '<p><strong>Closing day party mahjong</strong> — keys and tiles. <a href="realtor-mahjong.html">Realtor</a>.</p>'),
        ("pool-house-party", "Pool House Party", "pool house party mahjong — pool house tile night", '<p><strong>Pool house party mahjong</strong> — après swim. <a href="pool-party-mahjong.html">Pool party</a>.</p>'),
        ("rooftop-party", "Rooftop Party", "rooftop party mahjong — rooftop social with tiles", '<p><strong>Rooftop party mahjong</strong> — skyline views and tiles. <a href="dinner-party-mahjong.html">Dinner party</a>.</p>'),
        ("patio-season", "Patio Season", "patio season mahjong — spring patio tile night", '<p><strong>Patio season mahjong</strong> — outdoor tables, indoor backup. <a href="spring-mahjong-party.html">Spring party</a>.</p>'),
        ("firepit-night", "Firepit Night", "firepit night mahjong — firepit and tiles", '<p><strong>Firepit night mahjong</strong> — cozy outdoor lesson. <a href="fall-mahjong-party.html">Fall party</a>.</p>'),
        ("snow-day-party", "Snow Day Party", "snow day party mahjong — snow day indoor tiles", '<p><strong>Snow day party mahjong</strong> — schools out, tiles on. <a href="winter-mahjong-party.html">Winter party</a>.</p>'),
        ("rainy-day-activity", "Rainy Day Activity", "rainy day activity mahjong — beach week backup plan", '<p><strong>Rainy day mahjong</strong> — vacation rental savior. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("mahjong-pair-hand.html", "Pair Hand", "pair hand in mahjong — hands built around a pair", '<p>A <strong>pair hand</strong> centers on a required pair — read the card. <a href="mahjong-pair-requirement.html">Pair requirement</a>.</p>'),
        ("mahjong-pung-hand.html", "Pung Hand", "pung hand in mahjong — three of a kind in pattern", '<p><strong>Pung hands</strong> use three matching tiles — exposures allowed per card.</p>'),
        ("mahjong-kong-hand.html", "Kong Hand", "kong hand in mahjong — four of a kind meld", '<p><strong>Kong hands</strong> — four tiles — <a href="mahjong-kong.html">Kong guide</a>.</p>'),
        ("mahjong-quint-hand.html", "Quint Hand", "quint hand in mahjong — five of a kind category", '<p><strong>Quint hands</strong> — five tiles — <a href="mahjong-quints.html">Quints</a>.</p>'),
        ("mahjong-singles-and-pairs.html", "Singles and Pairs", "singles and pairs in mahjong — category on NMJL card", '<p><strong>Singles and pairs</strong> — unique category — <a href="mahjong-singles.html">Singles</a>.</p>'),
        ("mahjong-like-numbers.html", "Like Numbers", "like numbers in mahjong — matching number across suits", '<p><strong>Like numbers</strong> — same rank in different suits — read the card.</p>'),
        ("mahjong-369-category.html", "369 Category", "369 category in mahjong — threes sixes nines hands", '<p>The <strong>369 category</strong> — tiles 3, 6, 9 — yearly card lines.</p>'),
        ("mahjong-even-numbers.html", "Even Numbers", "even numbers in mahjong — 2 4 6 8 category hands", '<p><strong>Even numbers</strong> category — check exposures carefully.</p>'),
        ("mahjong-odd-numbers.html", "Odd Numbers", "odd numbers in mahjong — 1 3 5 7 9 category", '<p><strong>Odd numbers</strong> — another major NMJL section.</p>'),
        ("mahjong-consecutive-run.html", "Consecutive Run", "consecutive run in mahjong — sequential tile runs", '<p><strong>Consecutive run</strong> hands — in-order ranks — read the card.</p>'),
        ("mahjong-winds-dragons.html", "Winds and Dragons", "winds and dragons in mahjong — honors category", '<p><strong>Winds and dragons</strong> — <a href="mahjong-winds.html">Winds</a> · <a href="mahjong-dragons.html">Dragons</a>.</p>'),
        ("mahjong-year-hand.html", "Year Hand", "year hand in mahjong — annual year category on card", '<p><strong>Year hands</strong> change yearly — <a href="mahjong-card-2026.html">2026 card</a>.</p>'),
        ("mahjong-quints-category.html", "Quints Category", "quints category in mahjong — five-of-a-kind section", '<p>The <strong>quints category</strong> — advanced — <a href="mahjong-102.html">102</a>.</p>'),
        ("mahjong-singles-category.html", "Singles Category", "singles category in mahjong — singles and pairs section", '<p><strong>Singles category</strong> — often concealed — read carefully.</p>'),
        ("mahjong-any-tile.html", "Any Tile Wild", "any tile wild in mahjong — when card allows any tile", '<p>Some lines say <strong>any tile</strong> — rare — match the card exactly.</p>'),
        ("mahjong-fixed-tile.html", "Fixed Tile", "fixed tile in mahjong — specific tile required in hand", '<p>A <strong>fixed tile</strong> cannot be substituted — card specifies.</p>'),
        ("mahjong-duplicate-suit.html", "Duplicate Suit", "duplicate suit in mahjong — same suit twice in hand", '<p><strong>Duplicate suit</strong> patterns — multi-suit reading skill.</p>'),
        ("mahjong-opposite-suit.html", "Opposite Suit", "opposite suit in mahjong — paired suits on card", '<p><strong>Opposite suit</strong> — card pairing logic — study exposures.</p>'),
        ("mahjong-matching-wind.html", "Matching Wind", "matching wind in mahjong — wind must match category", '<p><strong>Matching wind</strong> — seat vs round — <a href="mahjong-winds.html">Winds</a>.</p>'),
        ("mahjong-round-wind.html", "Round Wind", "round wind in mahjong — prevailing wind for the deal", '<p><strong>Round wind</strong> — changes by round — tournament tables track it.</p>'),
        ("mahjong-seat-wind.html", "Seat Wind", "seat wind in mahjong — your chair wind assignment", '<p>Your <strong>seat wind</strong> — east south west north — <a href="east-seat-mahjong.html">East seat</a>.</p>'),
        ("mahjong-claim-priority.html", "Claim Priority", "claim priority in mahjong — who wins a discard claim", '<p><strong>Claim priority</strong> — mahjong beats exposure — table order matters.</p>'),
        ("mahjong-exposure-limit.html", "Exposure Limit", "exposure limit in mahjong — max exposures per hand", '<p>Some hands cap <strong>exposures</strong> — card states the limit.</p>'),
        ("mahjong-concealed-only.html", "Concealed Only", "concealed only in mahjong — hand must stay concealed", '<p><strong>Concealed only</strong> — no exposures — higher skill ceiling.</p>'),
        ("mahjong-wrong-exposure.html", "Wrong Exposure", "wrong exposure in mahjong — incorrect meld shown", '<p>A <strong>wrong exposure</strong> may dead your hand — <a href="foul-hand-mahjong.html">Foul hand</a>.</p>'),
        ("mahjong-revoke-call.html", "Revoke Call", "revoke call in mahjong — taking back a claim", '<p>Can you <strong>revoke a call</strong>? Table rules vary — we teach NMJL standard.</p>'),
        ("mahjong-short-handed.html", "Short Handed", "short handed in mahjong — fewer than four players", '<p>NMJL is <strong>four players</strong> — short-handed is house rules only.</p>'),
        ("mahjong-table-fee.html", "Table Fee", "table fee in mahjong — social games and stakes etiquette", '<p>We teach social play — not <strong>table fee</strong> gambling — <a href="mahjong-etiquette.html">Etiquette</a>.</p>'),
        ("mahjong-score-card.html", "Score Card", "score card in mahjong — tracking wins American style", '<p>American NMJL uses the <strong>card</strong> not point chips — <a href="nmjl-card.html">NMJL card</a>.</p>'),
        ("mahjong-verification.html", "Win Verification", "win verification in mahjong — checking a mahjong call", '<p><strong>Win verification</strong> — table confirms hand matches card before tiles are thrown in.</p>'),
        ("mahjong-dead-hand-call.html", "Dead Hand Call", "dead hand call in mahjong — when hand is declared dead", '<p>A <strong>dead hand call</strong> — stop play — <a href="dead-hand-mahjong.html">Dead hand</a>.</p>'),
        ("mahjong-redeal-rules.html", "Redeal Rules", "redeal rules in mahjong — when to shuffle and redeploy", '<p><strong>Redeal rules</strong> — wall game or misdeal — <a href="mahjong-wall-game.html">Wall game</a>.</p>'),
        ("mahjong-tile-count.html", "Tile Count", "tile count in mahjong — 152 tiles American set", '<p>Standard <strong>tile count</strong> — 152 tiles — <a href="mahjong-tiles.html">Tiles</a>.</p>'),
        ("mahjong-rack-etiquette.html", "Rack Etiquette", "rack etiquette in mahjong — arranging tiles on rack", '<p><strong>Rack etiquette</strong> — face down, orderly — <a href="rack-order-mahjong.html">Rack order</a>.</p>'),
        ("mahjong-charleston-order.html", "Charleston Order", "charleston order in mahjong — pass direction sequence", '<p><strong>Charleston order</strong> — right, across, left — <a href="mahjong-charleston.html">Charleston</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
