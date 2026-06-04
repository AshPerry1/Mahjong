# -*- coding: utf-8 -*-
"""Mega Wave 30 — ~500 pages (410 cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave30_cities_data import WAVE30_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_30(city, page, mahjong_kw) -> list:
    out: list = []

    hubs = [
        (
            "space-coast-fl-mahjong-hub.html",
            "Space Coast FL Mahjong | Melbourne, Cocoa Beach & Titusville",
            "Space Coast FL mahjong — Melbourne, Cocoa Beach, Titusville, Kennedy Space Coast area.",
            "space coast florida mahjong hub, melbourne fl mah jongg",
            "Space Coast FL Mahjong Guide",
            """<p><strong>Space Coast mahjong</strong> — Atlantic and lagoon private events:</p>
<p><a href="melbourne-fl-fl-mahjong.html">Melbourne FL</a> · <a href="cocoa-beach-fl-mahjong.html">Cocoa Beach</a> · <a href="titusville-fl-mahjong.html">Titusville</a> · <a href="vero-beach-fl-mahjong.html">Vero Beach</a></p>
<p><a href="florida-mahjong-hub.html">Florida hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "emerald-coast-fl-mahjong-hub.html",
            "Emerald Coast FL Mahjong | Destin, Panama City & 30A",
            "Emerald Coast FL mahjong — Destin, Panama City Beach, Seaside, Rosemary Beach.",
            "emerald coast florida mahjong hub, destin mah jongg",
            "Emerald Coast FL Mahjong Guide",
            """<p><strong>Emerald Coast mahjong</strong> — white sand private lessons:</p>
<p><a href="destin-florida-mahjong.html">Destin</a> · <a href="panama-city-beach-fl-mahjong.html">Panama City Beach</a> · <a href="seaside-florida-mahjong.html">30A / Seaside</a> · <a href="pensacola-fl-mahjong.html">Pensacola</a></p>
<p><a href="florida-mahjong-hub.html">Florida hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "napa-sonoma-mahjong-hub.html",
            "Napa & Sonoma Mahjong | Wine Country Private Events",
            "Napa Sonoma mahjong — wine country private lessons and vineyard weekend events.",
            "napa sonoma mahjong hub, wine country mah jongg california",
            "Napa & Sonoma Mahjong Guide",
            """<p><strong>Wine Country mahjong</strong> — Napa and Sonoma private events:</p>
<p><a href="napa-ca-mahjong.html">Napa</a> · <a href="sonoma-ca-mahjong.html">Sonoma</a> · <a href="healdsburg-ca-mahjong.html">Healdsburg</a> · <a href="calistoga-ca-mahjong.html">Calistoga</a> · <a href="santa-rosa-ca-mahjong.html">Santa Rosa</a></p>
<p><a href="california-mahjong-hub.html">California hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "puget-sound-mahjong-hub.html",
            "Puget Sound Mahjong | Seattle, Tacoma & Islands",
            "Puget Sound mahjong — Seattle, Tacoma, Bainbridge, San Juan corridor private events.",
            "puget sound mahjong hub, seattle metro mah jongg",
            "Puget Sound Mahjong Guide",
            """<p><strong>Puget Sound mahjong</strong> — metro and island private lessons:</p>
<p><a href="seattle-mahjong.html">Seattle</a> · <a href="tacoma-wa-mahjong.html">Tacoma</a> · <a href="bellevue-wa-mahjong.html">Bellevue</a> · <a href="bellingham-wa-mahjong.html">Bellingham</a></p>
<p><a href="washington-mahjong-hub.html">Washington hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "door-county-wi-mahjong-hub.html",
            "Door County WI Mahjong | Sturgeon Bay & Fish Creek",
            "Door County WI mahjong — Sturgeon Bay, Fish Creek, Egg Harbor peninsula events.",
            "door county wisconsin mahjong hub, fish creek mah jongg",
            "Door County WI Mahjong Guide",
            """<p><strong>Door County mahjong</strong> — peninsula vacation private lessons:</p>
<p><a href="sturgeon-bay-wi-mahjong.html">Sturgeon Bay</a> · <a href="fish-creek-wi-mahjong.html">Fish Creek</a> · <a href="sister-bay-wi-mahjong.html">Sister Bay</a> · <a href="green-bay-wi-mahjong.html">Green Bay</a></p>
<p><a href="wisconsin-mahjong-hub.html">Wisconsin hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "acadiana-la-mahjong-hub.html",
            "Acadiana LA Mahjong | Lafayette, Lake Charles & Cajun Country",
            "Acadiana Louisiana mahjong — Lafayette, Lake Charles, Cajun country private events.",
            "acadiana louisiana mahjong hub, lafayette mah jongg",
            "Acadiana Louisiana Mahjong Guide",
            """<p><strong>Acadiana mahjong</strong> — Cajun country private lessons:</p>
<p><a href="lafayette-la-mahjong.html">Lafayette</a> · <a href="lake-charles-la-mahjong.html">Lake Charles</a> · <a href="opelousas-la-mahjong.html">Opelousas</a> · <a href="new-orleans-mahjong.html">New Orleans</a></p>
<p><a href="louisiana-mahjong-hub.html">Louisiana hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "kentucky-bluegrass-mahjong-hub.html",
            "Kentucky Bluegrass Mahjong | Lexington, Versailles & Georgetown",
            "Kentucky Bluegrass mahjong — Lexington, Versailles, Georgetown horse country events.",
            "kentucky bluegrass mahjong hub, lexington mah jongg",
            "Kentucky Bluegrass Mahjong Guide",
            """<p><strong>Bluegrass mahjong</strong> — horse country private lessons:</p>
<p><a href="lexington-ky-mahjong.html">Lexington</a> · <a href="versailles-ky-mahjong.html">Versailles KY</a> · <a href="georgetown-ky-mahjong.html">Georgetown KY</a> · <a href="louisville-mahjong.html">Louisville</a></p>
<p><a href="kentucky-mahjong-hub.html">Kentucky hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "texas-panhandle-mahjong-hub.html",
            "Texas Panhandle Mahjong | Amarillo, Lubbock & Canyon",
            "Texas Panhandle mahjong — Amarillo, Lubbock, Canyon private events.",
            "texas panhandle mahjong hub, amarillo mah jongg",
            "Texas Panhandle Mahjong Guide",
            """<p><strong>Texas Panhandle mahjong</strong> — High Plains private lessons:</p>
<p><a href="amarillo-tx-mahjong.html">Amarillo</a> · <a href="lubbock-tx-mahjong.html">Lubbock</a> · <a href="midland-tx-mahjong.html">Midland</a> · <a href="odessa-tx-mahjong.html">Odessa</a></p>
<p><a href="texas-mahjong-hub.html">Texas hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "hampton-roads-va-mahjong-hub.html",
            "Hampton Roads VA Mahjong | Norfolk, Virginia Beach & Williamsburg",
            "Hampton Roads VA mahjong — Norfolk, Virginia Beach, Chesapeake, Williamsburg.",
            "hampton roads virginia mahjong hub, virginia beach mah jongg",
            "Hampton Roads VA Mahjong Guide",
            """<p><strong>Hampton Roads mahjong</strong> — coastal VA private events:</p>
<p><a href="virginia-beach-va-mahjong.html">Virginia Beach</a> · <a href="norfolk-va-mahjong.html">Norfolk</a> · <a href="chesapeake-va-mahjong.html">Chesapeake</a> · <a href="williamsburg-va-mahjong.html">Williamsburg</a></p>
<p><a href="virginia-mahjong-hub.html">Virginia hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "columbia-river-gorge-mahjong-hub.html",
            "Columbia River Gorge Mahjong | Hood River & The Dalles",
            "Columbia River Gorge mahjong — Hood River, The Dalles, windsurfing country events.",
            "columbia river gorge mahjong hub, hood river mah jongg",
            "Columbia River Gorge Mahjong Guide",
            """<p><strong>Columbia Gorge mahjong</strong> — OR/WA gorge private lessons:</p>
<p><a href="hood-river-or-mahjong.html">Hood River</a> · <a href="the-dalles-or-mahjong.html">The Dalles</a> · <a href="portland-mahjong.html">Portland</a> · <a href="vancouver-wa-mahjong.html">Vancouver WA</a></p>
<p><a href="oregon-mahjong-hub.html">Oregon hub</a> · <a href="pacific-northwest-mahjong-hub.html">PNW hub</a></p>""",
        ),
        (
            "mohawk-valley-ny-mahjong-hub.html",
            "Mohawk Valley NY Mahjong | Utica, Rome & Cooperstown",
            "Mohawk Valley NY mahjong — Utica, Rome, Cooperstown, central NY private events.",
            "mohawk valley new york mahjong hub, utica mah jongg",
            "Mohawk Valley NY Mahjong Guide",
            """<p><strong>Mohawk Valley mahjong</strong> — central NY private lessons:</p>
<p><a href="utica-ny-mahjong.html">Utica</a> · <a href="rome-ny-mahjong.html">Rome NY</a> · <a href="cooperstown-ny-mahjong.html">Cooperstown</a> · <a href="syracuse-ny-mahjong.html">Syracuse</a></p>
<p><a href="new-york-mahjong-hub.html">New York hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "lake-michigan-shore-wi-mahjong-hub.html",
            "Lake Michigan Shore WI Mahjong | Kenosha, Racine & Sheboygan",
            "Lake Michigan shore WI mahjong — Kenosha, Racine, Sheboygan, shoreline towns.",
            "lake michigan shore wisconsin mahjong hub, kenosha mah jongg",
            "Lake Michigan Shore WI Mahjong Guide",
            """<p><strong>Lake Michigan shore mahjong</strong> — Wisconsin shoreline private events:</p>
<p><a href="kenosha-wi-mahjong.html">Kenosha</a> · <a href="racine-wi-mahjong.html">Racine</a> · <a href="sheboygan-wi-mahjong.html">Sheboygan</a> · <a href="milwaukee-wi-mahjong.html">Milwaukee</a></p>
<p><a href="wisconsin-mahjong-hub.html">Wisconsin hub</a> · <a href="great-lakes-mahjong-hub.html">Great Lakes hub</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE30_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("alpha-sigma-lambda", "Alpha Sigma Lambda", "ASL"),
        ("beta-theta-pi", "Beta Theta Pi", "Beta"),
        ("chi-psi", "Chi Psi", "Chi Psi"),
        ("delta-tau-delta", "Delta Tau Delta", "DTD"),
        ("delta-upsilon", "Delta Upsilon", "DU"),
        ("kappa-alpha-order", "Kappa Alpha Order", "KA"),
        ("lambda-chi-alpha", "Lambda Chi Alpha", "Lambda Chi"),
        ("phi-delta-theta", "Phi Delta Theta", "Phi Delt"),
        ("phi-kappa-theta", "Phi Kappa Theta", "Phi Kap"),
        ("sigma-chi", "Sigma Chi", "Sigma Chi"),
        ("sigma-nu", "Sigma Nu", "Sigma Nu"),
        ("theta-chi", "Theta Chi", "Theta Chi"),
        ("theta-xi", "Theta Xi", "Theta Xi"),
        ("zeta-psi", "Zeta Psi", "Zeta Psi"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("alpha-delta-pi", "Alpha Delta Pi", "ADPi"),
        ("alpha-phi", "Alpha Phi", "Alpha Phi"),
        ("alpha-xi-delta", "Alpha Xi Delta", "AXiD"),
        ("chi-omega", "Chi Omega", "Chi O"),
        ("delta-gamma", "Delta Gamma", "DG"),
        ("gamma-phi-beta", "Gamma Phi Beta", "GPhiB"),
        ("kappa-alpha-theta", "Kappa Alpha Theta", "Theta"),
        ("kappa-delta", "Kappa Delta", "KD"),
        ("phi-mu", "Phi Mu", "Phi Mu"),
        ("pi-beta-phi", "Pi Beta Phi", "Pi Phi"),
        ("sigma-kappa", "Sigma Kappa", "Sigma Kappa"),
        ("theta-phi-alpha", "Theta Phi Alpha", "TPA"),
        ("zeta-tau-alpha", "Zeta Tau Alpha", "ZTA"),
        ("kappa-kappa-gamma", "Kappa Kappa Gamma", "KKG"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ("mahjong-teacher-training", "Teacher Training", "mahjong teacher training — learn to teach your group", '<p><strong>Teacher training</strong> — we coach you to lead your club. <a href="learn-mahjong-hub.html">Learn hub</a>.</p>'),
        ("host-mahjong-night", "Host Mahjong Night", "host mahjong night — we teach, you host", '<p><strong>Host mahjong night</strong> — you invite, we teach. <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("first-timer-party", "First Timer Party", "first timer mahjong party — zero experience welcome", '<p><strong>First timer party</strong> — everyone starts at zero. <a href="mahjong-101.html">101</a>.</p>'),
        ("girls-trip-mahjong", "Girls Trip", "girls trip mahjong — vacation rental tile night", '<p><strong>Girls trip mahjong</strong> — the highlight of the weekend. <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("guys-trip-mahjong", "Guys Trip", "guys trip mahjong — golf trip add-on tiles", '<p><strong>Guys trip mahjong</strong> — après-golf alternative. <a href="tailgate-mahjong.html">Tailgate</a>.</p>'),
        ("family-reunion-day", "Family Reunion Day", "family reunion day mahjong — multigenerational tiles", '<p><strong>Family reunion day mahjong</strong> — ages 12 to 92. <a href="family-reunion-mahjong.html">Family reunion</a>.</p>'),
        ("cousins-weekend", "Cousins Weekend", "cousins weekend mahjong — cousin crew tile night", '<p><strong>Cousins weekend mahjong</strong> — annual tradition starter. <a href="family-reunion-mahjong.html">Family</a>.</p>'),
        ("siblings-weekend", "Siblings Weekend", "siblings weekend mahjong — brothers and sisters tile night", '<p><strong>Siblings weekend mahjong</strong> — competitive but fun. <a href="family-reunion-mahjong.html">Family</a>.</p>'),
        ("in-laws-weekend", "In-Laws Weekend", "in laws weekend mahjong — break the ice with tiles", '<p><strong>In-laws weekend mahjong</strong> — better than small talk. <a href="family-reunion-mahjong.html">Family</a>.</p>'),
        ("empty-nest-party", "Empty Nest Party", "empty nest party mahjong — celebrate the kids leaving", '<p><strong>Empty nest party mahjong</strong> — new chapter energy. <a href="empty-nesters-mahjong.html">Empty nesters</a>.</p>'),
        ("retirement-brunch", "Retirement Brunch", "retirement brunch mahjong — send-off with tiles", '<p><strong>Retirement brunch mahjong</strong> — classy send-off. <a href="retirement-sendoff-mahjong.html">Retirement</a>.</p>'),
        ("office-team-building", "Office Team Building", "office team building mahjong — corporate tiles", '<p><strong>Office team building mahjong</strong> — actually fun. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("sales-team-meeting", "Sales Team Meeting", "sales team meeting mahjong — energize the team", '<p><strong>Sales team meeting mahjong</strong> — break the slide deck. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("real-estate-team", "Real Estate Team", "real estate team mahjong — brokerage social", '<p><strong>Real estate team mahjong</strong> — client-ready icebreaker. <a href="realtor-mahjong.html">Realtor</a>.</p>'),
        ("insurance-agency", "Insurance Agency", "insurance agency mahjong — agency retreat tiles", '<p><strong>Insurance agency mahjong</strong> — book the conference room. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("law-firm-social", "Law Firm Social", "law firm social mahjong — associate social committee", '<p><strong>Law firm social mahjong</strong> — billable hours paused. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("medical-practice", "Medical Practice", "medical practice mahjong — staff appreciation tiles", '<p><strong>Medical practice mahjong</strong> — staff wellness event. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("dental-office", "Dental Office", "dental office mahjong — team appreciation day", '<p><strong>Dental office mahjong</strong> — team building with flair. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("veterinary-clinic", "Veterinary Clinic", "veterinary clinic mahjong — staff night with tiles", '<p><strong>Veterinary clinic mahjong</strong> — destress the team. <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("school-faculty", "School Faculty", "school faculty mahjong — teacher appreciation tiles", '<p><strong>School faculty mahjong</strong> — faculty meeting upgrade. <a href="school-fundraiser-mahjong.html">School</a>.</p>'),
        ("pta-social", "PTA Social", "pta social mahjong — parent night with tiles", '<p><strong>PTA social mahjong</strong> — fundraiser preview. <a href="pta-mahjong.html">PTA</a>.</p>'),
        ("booster-club", "Booster Club", "booster club mahjong — sports parents tile night", '<p><strong>Booster club mahjong</strong> — raise spirits and funds. <a href="school-fundraiser-mahjong.html">School</a>.</p>'),
        ("scout-troop", "Scout Troop", "scout troop mahjong — badge-friendly game night", '<p><strong>Scout troop mahjong</strong> — supervised group lesson. <a href="community-center-mahjong.html">Community</a>.</p>'),
        ("youth-group", "Youth Group", "youth group mahjong — church youth tile night", '<p><strong>Youth group mahjong</strong> — screen-free fellowship. <a href="church-mahjong.html">Church</a>.</p>'),
        ("mens-club", "Mens Club", "mens club mahjong — mens club social with tiles", '<p><strong>Mens club mahjong</strong> — lodge or club social. <a href="civic-club-mahjong.html">Civic club</a>.</p>'),
        ("womens-club", "Womens Club", "womens club mahjong — garden club crossover", '<p><strong>Womens club mahjong</strong> — luncheon and tiles. <a href="garden-club-mahjong.html">Garden club</a>.</p>'),
        ("garden-club-swap", "Garden Club Swap", "garden club swap mahjong — garden club tries tiles", '<p>Your <strong>garden club</strong> will love a mahjong swap night. <a href="garden-club-mahjong.html">Garden club</a>.</p>'),
        ("book-club-finale", "Book Club Finale", "book club finale mahjong — end of season tile party", '<p>End book club season with <strong>book club finale mahjong</strong>. <a href="book-club-mahjong.html">Book club</a>.</p>'),
        ("supper-society", "Supper Society", "supper society mahjong — dining club with tiles", '<p><strong>Supper society mahjong</strong> — dine, then play. <a href="supper-club-mahjong.html">Supper club</a>.</p>'),
        ("cooking-club", "Cooking Club", "cooking club mahjong — cook club tile night", '<p>After the recipe — <strong>cooking club mahjong</strong>. <a href="cooking-class-mahjong.html">Cooking class</a>.</p>'),
        ("art-collective", "Art Collective", "art collective mahjong — studio social with tiles", '<p><strong>Art collective mahjong</strong> — creative crew night. <a href="art-walk-mahjong.html">Art walk</a>.</p>'),
        ("makers-space", "Makers Space", "makers space mahjong — craft space tile night", '<p><strong>Makers space mahjong</strong> — build, then play. <a href="craft-night-mahjong.html">Craft night</a>.</p>'),
        ("fiber-guild", "Fiber Guild", "fiber guild mahjong — knit and spin guild social", '<p><strong>Fiber guild mahjong</strong> — between projects. <a href="knitting-circle-mahjong.html">Knitting circle</a>.</p>'),
        ("running-club", "Running Club", "running club mahjong — post-run social tiles", '<p>After the 5K — <strong>running club mahjong</strong>. <a href="pickleball-club-mahjong.html">Active club</a>.</p>'),
        ("cycling-club", "Cycling Club", "cycling club mahjong — cycling club rest day tiles", '<p>Rest day <strong>cycling club mahjong</strong>. <a href="country-club-mahjong.html">Club</a>.</p>'),
        ("swim-club", "Swim Club", "swim club mahjong — summer swim club social", '<p><strong>Swim club mahjong</strong> — pool deck energy indoors. <a href="pool-party-mahjong.html">Pool party</a>.</p>'),
        ("beach-club", "Beach Club", "beach club mahjong — seasonal beach club event", '<p><strong>Beach club mahjong</strong> — members-only fun. <a href="country-club-mahjong.html">Country club</a>.</p>'),
        ("ski-club", "Ski Club", "ski club mahjong — ski club apres tiles", '<p><strong>Ski club mahjong</strong> — lodge night. <a href="ski-lodge-mahjong.html">Ski lodge</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("mahjong-card-section.html", "Card Section", "card section in mahjong — reading NMJL categories", '<p>Each <strong>card section</strong> — Like Numbers, 369, etc. — has rules. <a href="read-nmjl-card.html">Read the card</a>.</p>'),
        ("mahjong-concealed-hand.html", "Concealed Hand", "concealed hand in mahjong — no exposures allowed", '<p>A <strong>concealed hand</strong> wins with no exposures — read the card. <a href="mahjong-exposure-rules.html">Exposures</a>.</p>'),
        ("mahjong-exposed-hand.html", "Exposed Hand", "exposed hand in mahjong — melds shown on rack", '<p>An <strong>exposed hand</strong> uses melds on your rack — category rules apply.</p>'),
        ("mahjong-jokerless-hand.html", "Jokerless Hand", "jokerless hand in mahjong — hands that forbid jokers", '<p>Some hands are <strong>jokerless</strong> — no wild tiles allowed. <a href="mahjong-jokers.html">Jokers</a>.</p>'),
        ("mahjong-only-jokers.html", "Only Jokers", "only jokers in mahjong — when only jokers complete a set", '<p>Rare lines allow <strong>only jokers</strong> in a set — read the card carefully.</p>'),
        ("mahjong-any-dragon.html", "Any Dragon", "any dragon in mahjong — red green or white dragon", '<p><strong>Any dragon</strong> means any of the three dragons satisfy that line.</p>'),
        ("mahjong-matching-dragons.html", "Matching Dragons", "matching dragons in mahjong — dragon must match suit", '<p><strong>Matching dragons</strong> tie dragons to the hand\'s suit category.</p>'),
        ("mahjong-opposite-wind.html", "Opposite Wind", "opposite wind in mahjong — wind tile opposite your seat", '<p><strong>Opposite wind</strong> — seat wind vs round wind — read the card. <a href="mahjong-winds.html">Winds</a>.</p>'),
        ("mahjong-own-wind.html", "Own Wind", "own wind in mahjong — your seat wind tile", '<p>Your <strong>own wind</strong> matches your seat — east, south, west, or north. <a href="east-seat-mahjong.html">East seat</a>.</p>'),
        ("mahjong-flower-any.html", "Any Flower", "any flower in mahjong — flower tile wild on some hands", '<p>Some hands accept <strong>any flower</strong> — check the NMJL card yearly.</p>'),
        ("mahjong-specific-flower.html", "Specific Flower", "specific flower in mahjong — numbered flower required", '<p>Some lines need a <strong>specific flower</strong> — match the card exactly.</p>'),
        ("mahjong-soap-zero.html", "Soap as Zero", "soap as zero in mahjong — white dragon counts as zero", '<p><strong>Soap as zero</strong> — white dragon — appears in 2020s year hands. <a href="mahjong-soap-tile.html">Soap tile</a>.</p>'),
        ("mahjong-multi-suit.html", "Multi Suit", "multi suit in mahjong — hand uses more than one suit", '<p><strong>Multi suit</strong> hands mix dots, bams, and cracks — read exposures.</p>'),
        ("mahjong-one-suit.html", "One Suit", "one suit in mahjong — entire hand one suit only", '<p><strong>One suit</strong> hands use only dots, only bams, or only cracks.</p>'),
        ("mahjong-no-jokers-exposure.html", "No Jokers in Exposure", "no jokers in exposure in mahjong — jokerless exposure rules", '<p>Some exposures cannot use <strong>jokers</strong> — card specifies.</p>'),
        ("mahjong-replace-in-exposure.html", "Replace in Exposure", "replace in exposure in mahjong — swapping a natural for joker", '<p>You may <strong>replace in an exposure</strong> with a matching natural tile. <a href="redeem-joker-mahjong.html">Redeem joker</a>.</p>'),
        ("mahjong-call-for-exposure.html", "Call for Exposure", "call for exposure in mahjong — claiming to meld", '<p><strong>Call for exposure</strong> — claim a discard to expose a pung, kong, or quint.</p>'),
        ("mahjong-mahjong-on-discard.html", "Mahjong on Discard", "mahjong on discard in mahjong — winning on a thrown tile", '<p><strong>Mahjong on discard</strong> — declare when a discard completes your hand. <a href="calling-mahjong.html">Calling</a>.</p>'),
        ("mahjong-self-pick-rules.html", "Self-Pick Rules", "self pick rules in mahjong — winning from the wall", '<p><strong>Self-pick rules</strong> — draw the winning tile yourself. <a href="self-pick-mahjong.html">Self-pick</a>.</p>'),
        ("mahjong-table-variant.html", "Table Variant", "table variant in mahjong — house rules vs NMJL", '<p>We teach standard NMJL — not local <strong>table variants</strong>. <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-beginner-mistakes.html", "Beginner Mistakes", "beginner mistakes in mahjong — common new player errors", '<p>Avoid <strong>beginner mistakes</strong> — wrong exposures, early calls. <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-advanced-call.html", "Advanced Call", "advanced call in mahjong — when to call vs conceal", '<p><strong>Advanced call</strong> strategy — calling opens your hand to opponents.</p>'),
        ("mahjong-defensive-discard.html", "Defensive Discard", "defensive discard in mahjong — safe discard strategy", '<p>A <strong>defensive discard</strong> — discard tiles opponents likely do not need.</p>'),
        ("mahjong-read-the-table.html", "Read the Table", "read the table in mahjong — watching opponents exposures", '<p><strong>Read the table</strong> — opponents\' exposures reveal their category.</p>'),
        ("mahjong-card-change.html", "Card Change", "card change in mahjong — new NMJL card each year", '<p>The <strong>card changes</strong> every year — <a href="mahjong-card-2026.html">2026 card</a> · <a href="nmjl-card.html">NMJL card</a>.</p>'),
        ("mahjong-practice-hand.html", "Practice Hand", "practice hand in mahjong — learning a category off-card", '<p>Use a <strong>practice hand</strong> in lessons before tournament play. <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("mahjong-wall-game-rules.html", "Wall Game Rules", "wall game rules in mahjong — no winner when wall ends", '<p><strong>Wall game rules</strong> — tiles run out, no winner, redeal. <a href="mahjong-wall-game.html">Wall game</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
