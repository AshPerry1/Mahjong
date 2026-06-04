# -*- coding: utf-8 -*-
"""Mega Wave 29 — ~500 pages (410 new cities + hubs + keywords)."""
from __future__ import annotations

from seo_bulk_wave27 import _city_from_tuple
from seo_bulk_wave29_cities_data import WAVE29_CITIES
from seo_bulk_waves import _greek_fr, _greek_sor, _occasion, _rule


def bulk_pages_mega_wave_29(city, page, mahjong_kw) -> list:
    """Mega Wave 29 — plotly top-1k + suburb seeds, filtered for new slugs."""
    out: list = []

    hubs = [
        (
            "charlotte-metro-mahjong-hub.html",
            "Charlotte Metro Mahjong | Ballantyne, Matthews & Lake Norman",
            "Charlotte metro mahjong — Ballantyne, Matthews, Cornelius, Lake Norman private events.",
            "charlotte metro mahjong hub, ballantyne mah jongg",
            "Charlotte Metro Mahjong Guide",
            """<p><strong>Charlotte metro mahjong</strong> — Mecklenburg and suburb private lessons:</p>
<p><a href="charlotte-mahjong.html">Charlotte</a> · <a href="matthews-nc-mahjong.html">Matthews</a> · <a href="cornelius-nc-mahjong.html">Cornelius</a> · <a href="huntersville-nc-mahjong.html">Huntersville</a> · <a href="lake-norman-mahjong.html">Lake Norman</a></p>
<p><a href="north-carolina-mahjong-hub.html">NC hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "atlanta-metro-mahjong-hub.html",
            "Atlanta Metro Mahjong | Buckhead, Alpharetta & Sandy Springs",
            "Atlanta metro mahjong — Buckhead, Alpharetta, Dunwoody, Sandy Springs private events.",
            "atlanta metro mahjong hub, buckhead mah jongg",
            "Atlanta Metro Mahjong Guide",
            """<p><strong>Atlanta metro mahjong</strong> — north metro private lessons:</p>
<p><a href="atlanta-mahjong.html">Atlanta</a> · <a href="buckhead-mahjong.html">Buckhead</a> · <a href="alpharetta-mahjong.html">Alpharetta</a> · <a href="dunwoody-ga-mahjong.html">Dunwoody</a> · <a href="sandy-springs-ga-mahjong.html">Sandy Springs</a></p>
<p><a href="georgia-mahjong-hub.html">Georgia hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "nashville-metro-mahjong-hub.html",
            "Nashville Metro Mahjong | Franklin, Brentwood & Gallatin",
            "Nashville metro mahjong — Franklin, Brentwood, Gallatin, Spring Hill private events.",
            "nashville metro mahjong hub, franklin tn mah jongg",
            "Nashville Metro Mahjong Guide",
            """<p><strong>Nashville metro mahjong</strong> — Music City suburbs private lessons:</p>
<p><a href="nashville-mahjong.html">Nashville</a> · <a href="franklin-tn-mahjong.html">Franklin</a> · <a href="brentwood-tn-mahjong.html">Brentwood</a> · <a href="gallatin-tn-mahjong.html">Gallatin</a> · <a href="spring-hill-tn-mahjong.html">Spring Hill</a></p>
<p><a href="tennessee-mahjong-hub.html">Tennessee hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "raleigh-durham-mahjong-hub.html",
            "Raleigh-Durham Mahjong | Triangle Cities & Suburbs",
            "Raleigh-Durham mahjong — Raleigh, Durham, Chapel Hill, Cary, Apex private events.",
            "raleigh durham mahjong hub, triangle nc mah jongg",
            "Raleigh-Durham Mahjong Guide",
            """<p><strong>Research Triangle mahjong</strong> — RTP private lessons:</p>
<p><a href="raleigh-mahjong.html">Raleigh</a> · <a href="durham-nc-mahjong.html">Durham</a> · <a href="chapel-hill-nc-mahjong.html">Chapel Hill</a> · <a href="cary-nc-mahjong.html">Cary</a> · <a href="apex-nc-mahjong.html">Apex</a></p>
<p><a href="north-carolina-mahjong-hub.html">NC hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "treasure-coast-fl-mahjong-hub.html",
            "Treasure Coast FL Mahjong | Stuart, Vero & Port St. Lucie",
            "Treasure Coast FL mahjong — Stuart, Vero Beach, Port St. Lucie private events.",
            "treasure coast florida mahjong hub, stuart fl mah jongg",
            "Treasure Coast FL Mahjong Guide",
            """<p><strong>Treasure Coast mahjong</strong> — Atlantic private lessons:</p>
<p><a href="vero-beach-fl-mahjong.html">Vero Beach</a> · <a href="stuart-fl-mahjong.html">Stuart</a> · <a href="port-st-lucie-fl-mahjong.html">Port St. Lucie</a> · <a href="fort-pierce-fl-mahjong.html">Fort Pierce</a> · <a href="jupiter-fl-mahjong.html">Jupiter</a></p>
<p><a href="florida-mahjong-hub.html">Florida hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "pinellas-county-fl-mahjong-hub.html",
            "Pinellas County FL Mahjong | St. Pete, Clearwater & Dunedin",
            "Pinellas County mahjong — St. Petersburg, Clearwater, Dunedin, beach towns.",
            "pinellas county florida mahjong hub, clearwater mah jongg",
            "Pinellas County FL Mahjong Guide",
            """<p><strong>Pinellas County mahjong</strong> — Gulf beach private events:</p>
<p><a href="st-petersburg-fl-mahjong.html">St. Petersburg</a> · <a href="clearwater-mahjong.html">Clearwater</a> · <a href="dunedin-fl-mahjong.html">Dunedin</a> · <a href="tampa-mahjong.html">Tampa Bay</a></p>
<p><a href="florida-mahjong-hub.html">Florida hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "chicago-suburbs-mahjong-hub.html",
            "Chicago Suburbs Mahjong | Naperville, Evanston & Oak Park",
            "Chicago suburbs mahjong — Naperville, Evanston, Oak Park, North Shore private events.",
            "chicago suburbs mahjong hub, naperville mah jongg",
            "Chicago Suburbs Mahjong Guide",
            """<p><strong>Chicago suburbs mahjong</strong> — collar county private lessons:</p>
<p><a href="chicago-mahjong.html">Chicago</a> · <a href="naperville-il-mahjong.html">Naperville</a> · <a href="evanston-il-mahjong.html">Evanston</a> · <a href="oak-park-il-mahjong.html">Oak Park</a> · <a href="schaumburg-il-mahjong.html">Schaumburg</a></p>
<p><a href="illinois-mahjong-hub.html">Illinois hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "denver-metro-mahjong-hub.html",
            "Denver Metro Mahjong | Boulder, Aurora & Highlands Ranch",
            "Denver metro mahjong — Boulder, Aurora, Highlands Ranch, Cherry Hills private events.",
            "denver metro mahjong hub, boulder mah jongg",
            "Denver Metro Mahjong Guide",
            """<p><strong>Denver metro mahjong</strong> — Front Range private lessons:</p>
<p><a href="denver-mahjong.html">Denver</a> · <a href="boulder-co-mahjong.html">Boulder</a> · <a href="aurora-co-mahjong.html">Aurora</a> · <a href="highlands-ranch-co-mahjong.html">Highlands Ranch</a> · <a href="fort-collins-co-mahjong.html">Fort Collins</a></p>
<p><a href="colorado-mahjong-hub.html">Colorado hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "phoenix-metro-mahjong-hub.html",
            "Phoenix Metro Mahjong | Scottsdale, Mesa & Chandler",
            "Phoenix metro mahjong — Scottsdale, Mesa, Chandler, Gilbert private events.",
            "phoenix metro mahjong hub, scottsdale mah jongg",
            "Phoenix Metro Mahjong Guide",
            """<p><strong>Phoenix metro mahjong</strong> — Valley of the Sun private lessons:</p>
<p><a href="phoenix-mahjong.html">Phoenix</a> · <a href="scottsdale-az-mahjong.html">Scottsdale</a> · <a href="mesa-az-mahjong.html">Mesa</a> · <a href="chandler-az-mahjong.html">Chandler</a> · <a href="gilbert-az-mahjong.html">Gilbert</a></p>
<p><a href="arizona-mahjong-hub.html">Arizona hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "adirondacks-mahjong-hub.html",
            "Adirondacks Mahjong | Lake Placid, Saranac Lake & Lake George",
            "Adirondacks mahjong — Lake Placid, Saranac Lake, Lake George cabin events.",
            "adirondacks mahjong hub, lake placid mah jongg",
            "Adirondacks Mahjong Guide",
            """<p><strong>Adirondacks mahjong</strong> — mountain lake private lessons:</p>
<p><a href="lake-placid-ny-mahjong.html">Lake Placid</a> · <a href="saranac-lake-ny-mahjong.html">Saranac Lake</a> · <a href="lake-george-ny-mahjong.html">Lake George</a> · <a href="saratoga-springs-ny-mahjong.html">Saratoga Springs</a></p>
<p><a href="new-york-mahjong-hub.html">New York hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "gold-coast-ct-mahjong-hub.html",
            "Connecticut Gold Coast Mahjong | Greenwich, Darien & Westport",
            "Connecticut Gold Coast mahjong — Greenwich, Darien, Westport, Fairfield private events.",
            "connecticut gold coast mahjong hub, greenwich mah jongg",
            "Connecticut Gold Coast Mahjong Guide",
            """<p><strong>CT Gold Coast mahjong</strong> — Fairfield County private lessons:</p>
<p><a href="greenwich-ct-mahjong.html">Greenwich</a> · <a href="darien-ct-mahjong.html">Darien</a> · <a href="westport-ct-mahjong.html">Westport</a> · <a href="fairfield-ct-mahjong.html">Fairfield</a> · <a href="stamford-ct-mahjong.html">Stamford</a></p>
<p><a href="connecticut-mahjong-hub.html">Connecticut hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "lowcountry-sc-mahjong-hub.html",
            "Lowcountry SC Mahjong | Beaufort, Bluffton & Hilton Head",
            "Lowcountry SC mahjong — Beaufort, Bluffton, Hilton Head Island private events.",
            "lowcountry south carolina mahjong hub, hilton head mah jongg",
            "Lowcountry SC Mahjong Guide",
            """<p><strong>Lowcountry mahjong</strong> — coastal SC private lessons:</p>
<p><a href="hilton-head-sc-mahjong.html">Hilton Head</a> · <a href="bluffton-sc-mahjong.html">Bluffton</a> · <a href="beaufort-sc-mahjong.html">Beaufort</a> · <a href="charleston-sc-mahjong.html">Charleston</a></p>
<p><a href="south-carolina-mahjong-hub.html">SC hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    for tup in WAVE29_CITIES:
        out.append(_city_from_tuple(city, tup))

    fraternities = [
        ("alpha-epsilon-pi", "Alpha Epsilon Pi", "AEPi"),
        ("alpha-sigma-phi", "Alpha Sigma Phi", "ASPhi"),
        ("beta-chi-theta", "Beta Chi Theta", "BXT"),
        ("delta-kappa-epsilon", "Delta Kappa Epsilon", "DKE"),
        ("delta-phi-epsilon", "Delta Phi Epsilon", "DPhiE"),
        ("delta-sigma-phi", "Delta Sigma Phi", "DSP"),
        ("kappa-alpha", "Kappa Alpha Order", "KA"),
        ("lambda-phi-epsilon", "Lambda Phi Epsilon", "LPhiE"),
        ("phi-kappa-tau", "Phi Kappa Tau", "Phi Tau"),
        ("sigma-alpha-mu", "Sigma Alpha Mu", "SAM"),
        ("sigma-phi-delta", "Sigma Phi Delta", "SPD"),
        ("tau-epsilon-phi", "Tau Epsilon Phi", "TEP"),
        ("triangle", "Triangle", "Triangle"),
        ("zeta-beta-tau", "Zeta Beta Tau", "ZBT"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("alpha-gamma-delta", "Alpha Gamma Delta", "AGD"),
        ("alpha-phi", "Alpha Phi", "Alpha Phi"),
        ("delta-delta-delta", "Delta Delta Delta", "Tri Delta"),
        ("gamma-phi-beta", "Gamma Phi Beta", "GPhiB"),
        ("kappa-kappa-gamma", "Kappa Kappa Gamma", "KKG"),
        ("phi-sigma-sigma", "Phi Sigma Sigma", "PSS"),
        ("pi-beta-phi", "Pi Beta Phi", "Pi Phi"),
        ("sigma-delta-tau", "Sigma Delta Tau", "SDT"),
        ("sigma-sigma-sigma", "Sigma Sigma Sigma", "Tri Sig"),
        ("theta-phi-alpha", "Theta Phi Alpha", "TPA"),
        ("zeta-tau-alpha", "Zeta Tau Alpha", "ZTA"),
        ("alpha-chi-omega", "Alpha Chi Omega", "AXO"),
        ("alpha-delta-pi", "Alpha Delta Pi", "ADPi"),
        ("alpha-omicron-pi", "Alpha Omicron Pi", "AOII"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    occasions = [
        ("mahjong-club-launch", "Mahjong Club Launch", "mahjong club launch — start a weekly club with a lesson", '<p>Launch your <strong>mahjong club</strong> with a Mahjong 101 lesson. <a href="mahjong-101.html">101</a> · <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("weekly-mahjong-club", "Weekly Mahjong Club", "weekly mahjong club — recurring group lesson", '<p>Book a <strong>weekly mahjong club</strong> kickoff — we teach the first four weeks. <a href="learn-mahjong-hub.html">Learn hub</a>.</p>'),
        ("monthly-mahjong-brunch", "Monthly Mahjong Brunch", "monthly mahjong brunch — recurring ladies brunch with tiles", '<p>Your <strong>monthly mahjong brunch</strong> — same group, new card hands. <a href="mahjong-brunch.html">Brunch</a>.</p>'),
        ("quarterly-mahjong-social", "Quarterly Mahjong Social", "quarterly mahjong social — HOA or club quarterly event", '<p>Host a <strong>quarterly mahjong social</strong> for your community. <a href="hoa-mahjong.html">HOA</a> · <a href="country-club-mahjong.html">Country club</a>.</p>'),
        ("senior-living-mahjong", "Senior Living Mahjong", "senior living mahjong — assisted living activity with tiles", '<p><strong>Senior living mahjong</strong> — gentle pace, big tiles. <a href="mahjong-for-seniors.html">For seniors</a>.</p>'),
        ("assisted-living-mahjong", "Assisted Living", "assisted living mahjong — memory care friendly lesson", '<p>Book <strong>assisted living mahjong</strong> — patient instructors. <a href="senior-center-mahjong.html">Senior center</a>.</p>'),
        ("memory-care-mahjong", "Memory Care", "memory care mahjong — cognitive-friendly tile activity", '<p><strong>Memory care mahjong</strong> — simplified intro format. <a href="mahjong-for-seniors.html">Seniors</a>.</p>'),
        ("library-mahjong-program", "Library Program", "library mahjong program — public library intro class", '<p>Your <strong>library mahjong program</strong> fills fast — book early. <a href="community-center-mahjong.html">Community center</a>.</p>'),
        ("ymca-mahjong", "YMCA Mahjong", "ymca mahjong — community center social with tiles", '<p>Add <strong>YMCA mahjong</strong> to your adult programming. <a href="community-center-mahjong.html">Community center</a>.</p>'),
        ("jewish-community-center-mahjong", "JCC Mahjong", "jcc mahjong — Jewish community center social with tiles", '<p><strong>JCC mahjong</strong> — multigenerational fun. <a href="community-center-mahjong.html">Community</a>.</p>'),
        ("country-club-ladies-day", "Country Club Ladies Day", "country club ladies day mahjong — member programming", '<p>Member <strong>country club ladies day mahjong</strong>. <a href="country-club-mahjong.html">Country club</a>.</p>'),
        ("golf-club-ladies-day", "Golf Club Ladies Day", "golf club ladies day mahjong — après-golf tiles", '<p>After nine holes — <strong>golf club ladies day mahjong</strong>. <a href="country-club-mahjong.html">Country club</a>.</p>'),
        ("tennis-club-social", "Tennis Club Social", "tennis club social mahjong — club crossover event", '<p><strong>Tennis club social mahjong</strong> — new court-side tradition. <a href="pickleball-club-mahjong.html">Pickleball club</a>.</p>'),
        ("euchre-night-swap", "Euchre Night Swap", "euchre night swap mahjong — card night becomes tile night", '<p>Swap <strong>euchre night</strong> for mahjong — same crew, new game. <a href="game-night-mahjong.html">Game night</a>.</p>'),
        ("bridge-night-swap", "Bridge Night Swap", "bridge night swap mahjong — bridge group tries tiles", '<p>Your <strong>bridge group</strong> will love a mahjong lesson. <a href="bridge-club-mahjong.html">Bridge club</a>.</p>'),
        ("canasta-night-swap", "Canasta Night Swap", "canasta night swap mahjong — card group tries American mahjong", '<p>From canasta to <strong>mahjong</strong> in one afternoon. <a href="game-night-mahjong.html">Game night</a>.</p>'),
        ("dominoes-night-swap", "Dominoes Night Swap", "dominoes night swap mahjong — tile lovers upgrade", '<p>If you love dominoes — try <strong>dominoes night swap mahjong</strong>. <a href="mahjong-tiles.html">Tiles</a>.</p>'),
        ("poker-night-swap", "Poker Night Swap", "poker night swap mahjong — guys or girls night tiles", '<p>Swap <strong>poker night</strong> for mahjong — still competitive, more social. <a href="poker-night-mahjong.html">Poker night swap</a>.</p>'),
        ("game-night-host", "Game Night Host", "game night host mahjong — you host, we teach", '<p>Be the <strong>game night host</strong> who introduced mahjong. <a href="screen-free-game-night.html">Screen-free</a>.</p>'),
        ("neighbors-first-mahjong", "Neighbors First", "neighbors first mahjong — meet your street with tiles", '<p>Meet neighbors with <strong>neighbors first mahjong</strong>. <a href="neighborhood-mahjong.html">Neighborhood</a>.</p>'),
        ("new-neighbor-welcome", "New Neighbor Welcome", "new neighbor welcome mahjong — welcome wagon with tiles", '<p>Welcome new neighbors with <strong>mahjong</strong>. <a href="new-neighbors-mahjong.html">New neighbors</a>.</p>'),
        ("street-party-mahjong", "Street Party", "street party mahjong — block closed, tiles open", '<p>Close the street for <strong>street party mahjong</strong>. <a href="neighborhood-block-party-mahjong.html">Block party</a>.</p>'),
        ("cul-de-sac-mahjong", "Cul-de-Sac Party", "cul de sac mahjong — dead-end street social with tiles", '<p>Your <strong>cul-de-sac</strong> needs a mahjong afternoon. <a href="patio-party-mahjong.html">Patio party</a>.</p>'),
        ("driveway-mahjong", "Driveway Mahjong", "driveway mahjong — outdoor summer lesson", '<p>Summer <strong>driveway mahjong</strong> — shade tent optional. <a href="summer-mahjong.html">Summer</a>.</p>'),
        ("garage-mahjong", "Garage Mahjong", "garage mahjong — heated garage winter lesson", '<p>Rainy day? <strong>Garage mahjong</strong> saves the plan. <a href="winter-mahjong.html">Winter</a>.</p>'),
        ("basement-mahjong", "Basement Mahjong", "basement mahjong — rec room tile night", '<p>Finished basement + <strong>basement mahjong</strong> = perfect Friday. <a href="game-night-mahjong.html">Game night</a>.</p>'),
        ("sunroom-mahjong", "Sunroom Mahjong", "sunroom mahjong — bright room afternoon lesson", '<p>Host in the <strong>sunroom</strong> — afternoon light and tiles. <a href="ladies-luncheon-mahjong.html">Luncheon</a>.</p>'),
        ("screened-porch-mahjong", "Screened Porch Mahjong", "screened porch mahjong — bug-free summer tiles", '<p><strong>Screened porch mahjong</strong> — breeze without bugs. <a href="patio-party-mahjong.html">Patio</a>.</p>'),
        ("lanai-mahjong", "Lanai Mahjong", "lanai mahjong — Florida lanai tile party", '<p>Florida <strong>lanai mahjong</strong> — snowbirds welcome. <a href="florida-mahjong.html">Florida</a>.</p>'),
        ("pool-house-mahjong", "Pool House Mahjong", "pool house mahjong — cabana tile afternoon", '<p>After laps — <strong>pool house mahjong</strong>. <a href="pool-party-mahjong.html">Pool party</a>.</p>'),
        ("clubhouse-mahjong", "Clubhouse Mahjong", "clubhouse mahjong — HOA clubhouse event with tiles", '<p>Book the <strong>clubhouse</strong> for mahjong — we bring tiles. <a href="hoa-mahjong.html">HOA</a>.</p>'),
        ("community-pool-mahjong", "Community Pool", "community pool mahjong — summer HOA pool event", '<p><strong>Community pool mahjong</strong> — summer HOA hit. <a href="hoa-mahjong.html">HOA</a> · <a href="summer-mahjong.html">Summer</a>.</p>'),
        ("farmhouse-mahjong-party", "Farmhouse Party", "farmhouse mahjong party — barn or farmhouse gathering", '<p><strong>Farmhouse mahjong</strong> — rustic and social. <a href="farmhouse-mahjong.html">Farmhouse</a>.</p>'),
        ("barn-wedding-mahjong", "Barn Wedding Weekend", "barn wedding weekend mahjong — wedding guest activity", '<p><strong>Barn wedding weekend mahjong</strong> for guests. <a href="wedding-mahjong.html">Wedding</a>.</p>'),
        ("vineyard-mahjong", "Vineyard Mahjong", "vineyard mahjong — winery tasting with tiles", '<p>Pair pours with <strong>vineyard mahjong</strong>. <a href="wine-tasting-mahjong.html">Wine tasting</a>.</p>'),
        ("winery-member-event", "Winery Member Event", "winery member event mahjong — wine club with tiles", '<p><strong>Winery member event mahjong</strong> — loyal members love it. <a href="wine-club-mahjong.html">Wine club</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("mahjong-table-setup-rules.html", "Table Setup", "mahjong table setup — racks, tiles, and wall", '<p>Proper <strong>table setup</strong> — four racks, 152 tiles, wall built. <a href="mahjong-table-setup.html">Table setup guide</a>.</p>'),
        ("mahjong-seat-wind.html", "Seat Wind", "seat wind in mahjong — east south west north at the table", '<p>Your <strong>seat wind</strong> — east, south, west, north — sets dealing. <a href="mahjong-winds.html">Winds</a>.</p>'),
        ("mahjong-round-wind.html", "Round Wind", "round wind in mahjong — prevailing wind for the deal", '<p>The <strong>round wind</strong> appears on some NMJL hands — read the card. <a href="read-nmjl-card.html">Read the card</a>.</p>'),
        ("mahjong-player-count.html", "Four Players", "four players in mahjong — standard American table", '<p>American mahjong needs <strong>four players</strong> — we teach standard rules. <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-tile-faces.html", "Tile Faces", "tile faces in mahjong — recognizing suits and honors", '<p>Learn <strong>tile faces</strong> — dots, bams, cracks, winds, dragons. <a href="mahjong-suits.html">Suits</a>.</p>'),
        ("mahjong-honor-tiles.html", "Honor Tiles", "honor tiles in mahjong — winds and dragons", '<p><strong>Honor tiles</strong> — winds and dragons — key on the NMJL card. <a href="mahjong-winds.html">Winds</a>.</p>'),
        ("mahjong-red-dragon.html", "Red Dragon", "red dragon in mahjong — dragon tile in American sets", '<p><strong>Red dragon</strong> — one of three dragons in American mahjong. <a href="mahjong-dragons.html">Dragons</a>.</p>'),
        ("mahjong-green-dragon.html", "Green Dragon", "green dragon in mahjong — dragon tile category", '<p><strong>Green dragon</strong> matches green dragon hands on the card.</p>'),
        ("mahjong-white-dragon.html", "White Dragon", "white dragon in mahjong — soap or zero dragon tile", '<p><strong>White dragon</strong> — often called soap — can represent zero. <a href="mahjong-dragons.html">Dragons</a>.</p>'),
        ("mahjong-soap-tile.html", "Soap Tile", "soap tile in mahjong — white dragon as zero", '<p>The <strong>soap tile</strong> (white dragon) can count as zero in some hands. <a href="read-nmjl-card.html">Read the card</a>.</p>'),
        ("mahjong-like-numbers.html", "Like Numbers", "like numbers in mahjong — same digit across suits", '<p><strong>Like numbers</strong> hands use the same digit on dots, bams, and cracks. <a href="like-numbers-mahjong.html">Like numbers guide</a>.</p>'),
        ("mahjong-consecutive-run.html", "Consecutive Run", "consecutive run in mahjong — sequential tiles across suits", '<p>A <strong>consecutive run</strong> — 1-2-3 across suits — common on the card. <a href="mahjong-runs.html">Runs</a>.</p>'),
        ("mahjong-13579-hand.html", "13579 Hand", "13579 hand in mahjong — odd numbers hand category", '<p><strong>13579</strong> hands use odd digits only — read exposures carefully. <a href="odd-numbers-mahjong.html">Odd numbers</a>.</p>'),
        ("mahjong-2468-hand.html", "2468 Hand", "2468 hand in mahjong — even numbers hand category", '<p><strong>2468</strong> hands use even digits — popular category on the card. <a href="even-numbers-mahjong.html">Even numbers</a>.</p>'),
        ("mahjong-quints-category.html", "Quints Category", "quints category in mahjong — five of a kind hands", '<p>The <strong>quints category</strong> requires five matching tiles — advanced play. <a href="mahjong-quints.html">Quints</a>.</p>'),
        ("mahjong-singles-pairs.html", "Singles and Pairs", "singles and pairs in mahjong — pair-only hand section", '<p><strong>Singles and pairs</strong> — often no exposures allowed. <a href="mahjong-pairs.html">Pairs</a>.</p>'),
        ("mahjong-year-hand.html", "Year Hand", "year hand in mahjong — matching the year on the card", '<p>A <strong>year hand</strong> uses digits of the year — e.g. 2026 on the 2026 card. <a href="year-hand-mahjong.html">Year hands</a>.</p>'),
        ("mahjong-any-like-numbers.html", "Any Like Numbers", "any like numbers in mahjong — flexible like number hands", '<p><strong>Any like numbers</strong> — pick one digit for the whole hand. <a href="like-numbers-mahjong.html">Like numbers</a>.</p>'),
        ("mahjong-multiplication-hand.html", "Multiplication Hand", "multiplication hand in mahjong — products on the card", '<p>Some hands use <strong>multiplication</strong> patterns — read the card line carefully.</p>'),
        ("mahjong-addition-hand.html", "Addition Hand", "addition hand in mahjong — sums on the NMJL card", '<p><strong>Addition hands</strong> add tile values — rare but on the card yearly.</p>'),
        ("mahjong-traffic-light.html", "Traffic Light", "traffic light in mahjong — red green white dragon hand", '<p>The <strong>traffic light</strong> uses red, green, and white dragons together.</p>'),
        ("mahjong-elevens-hand.html", "Elevens Hand", "elevens hand in mahjong — 1 and 1 patterns on card", '<p><strong>Elevens</strong> hands pair ones across suits — check the card section.</p>'),
        ("mahjong-winds-hand.html", "Winds Hand", "winds hand in mahjong — wind tile combinations", '<p><strong>Winds hands</strong> use east, south, west, north combinations. <a href="mahjong-winds.html">Winds</a>.</p>'),
        ("mahjong-dragons-hand.html", "Dragons Hand", "dragons hand in mahjong — dragon pungs and kongs", '<p><strong>Dragons hands</strong> lean on red, green, and white dragons. <a href="mahjong-dragons.html">Dragons</a>.</p>'),
        ("mahjong-throw-in-tiles.html", "Throw In Tiles", "throw in tiles in mahjong — unplayed tiles at wall end", '<p><strong>Throw in tiles</strong> remain after the wall game — not drawn.</p>'),
        ("mahjong-redeal.html", "Redeal", "redeal in mahjong — when the hand is redealt", '<p>After a <strong>wall game</strong> or misdeal — redeal the tiles. <a href="mahjong-wall-game.html">Wall game</a>.</p>'),
        ("mahjong-table-fouls.html", "Table Fouls", "table fouls in mahjong — common mistakes", '<p><strong>Table fouls</strong> — wrong exposure, wrong call — may kill the hand. <a href="foul-hand-mahjong.html">Foul hand</a>.</p>'),
        ("mahjong-courtesy-rules.html", "Courtesy Rules", "courtesy rules in mahjong — house manners at the table", '<p><strong>Courtesy rules</strong> — no coaching, clear calls, tidy rack. <a href="mahjong-etiquette.html">Etiquette</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
