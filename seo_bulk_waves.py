# -*- coding: utf-8 -*-
"""Bulk SEO waves — add large batches without hand-writing hundreds of page() calls.

Default target per mega wave: ~500 pages (see Mega Wave 27).
Adjust MEGA_WAVE_PAGE_TARGET when you want even longer single runs.
"""
from __future__ import annotations

MEGA_WAVE_PAGE_TARGET = 500


def _greek_fr(mahjong_kw, slug: str, name: str, nick: str) -> dict:
    return mahjong_kw(
        f"{slug}-mahjong.html",
        f"{name} Events",
        f"{name} mahjong — {nick} chapter philanthropy and social events.",
        f"{slug.replace('-', ' ')} mahjong, {nick} mah jongg fraternity",
        f"{name} Mahjong",
        f"<p><strong>{name}</strong> chapters — stand out with a mahjong philanthropy event. "
        f'<a href="fraternity-mahjong.html">Fraternity</a> · <a href="greek-life-mahjong.html">Greek life</a>.</p>',
    )


def _greek_sor(mahjong_kw, slug: str, name: str, nick: str) -> dict:
    return mahjong_kw(
        f"{slug}-mahjong.html",
        f"{name} Events",
        f"{name} mahjong — {nick} chapter philanthropy events.",
        f"{slug.replace('-', ' ')} mahjong, {nick} mah jongg sorority",
        f"{name} Mahjong",
        f"<p><strong>{name}</strong> chapters — bid day and philanthropy mahjong. "
        f'<a href="sorority-mahjong-parties.html">Sorority parties</a> · <a href="greek-life-mahjong.html">Greek life</a>.</p>',
    )


def _occasion_file(slug: str) -> str:
    if slug.endswith(".html"):
        return slug
    if slug.endswith("-mahjong"):
        return f"{slug}.html"
    return f"{slug}-mahjong.html"


def _occasion(mahjong_kw, slug: str, title: str, desc: str, body: str) -> dict:
    file = _occasion_file(slug)
    stem = file.replace("-mahjong.html", "").replace(".html", "")
    return mahjong_kw(
        file,
        title,
        desc,
        f"{stem.replace('-', ' ')} mahjong, {stem.replace('-', ' ')} mah jongg",
        f"{title} Mahjong",
        body,
    )


def _rule(mahjong_kw, slug: str, title: str, desc: str, body: str) -> dict:
    file = slug if slug.endswith(".html") else f"{slug}-mahjong.html"
    stem = file.replace("-mahjong.html", "").replace(".html", "")
    return mahjong_kw(
        file,
        title,
        desc,
        f"{stem.replace('-', ' ')} mahjong, mah jongg {stem.replace('-', ' ')}",
        title if "Mahjong" in title else f"{title} in Mahjong",
        body,
    )


def bulk_pages_mega_wave_26(city, page, mahjong_kw) -> list:
    """Mega Wave 26 — ~156 pages in one generator run."""
    out: list = []

    # ── State hubs (8) ──
    hubs = [
        (
            "maine-mahjong-hub.html",
            "Maine Mahjong | Portland, Coast & Vacation",
            "Maine mahjong — Portland, Bar Harbor, Kennebunk, Bangor. Lookout Mountain Mahjong travels ME.",
            "maine mahjong hub, mahjong maine cities",
            "Maine Mahjong Guide",
            """<p><strong>Maine mahjong</strong> — Vacationland private events:</p>
<p><a href="portland-me-mahjong.html">Portland ME</a> · <a href="bangor-me-mahjong.html">Bangor</a> · <a href="augusta-me-mahjong.html">Augusta</a> · <a href="bar-harbor-me-mahjong.html">Bar Harbor</a> · <a href="rockland-me-mahjong.html">Rockland</a> · <a href="kennebunk-me-mahjong.html">Kennebunk</a> · <a href="freeport-me-mahjong.html">Freeport</a> · <a href="ogunquit-me-mahjong.html">Ogunquit</a></p>
<p><a href="maine-mahjong.html">Maine statewide</a> · <a href="new-england-mahjong-hub.html">New England hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "vermont-mahjong-hub.html",
            "Vermont Mahjong | Burlington, Stowe & Ski Country",
            "Vermont mahjong — Burlington, Stowe, Rutland, Montpelier. Lookout Mountain Mahjong travels VT.",
            "vermont mahjong hub, mahjong vermont cities",
            "Vermont Mahjong Guide",
            """<p><strong>Vermont mahjong</strong> — Green Mountain State private lessons:</p>
<p><a href="burlington-vt-mahjong.html">Burlington</a> · <a href="rutland-vt-mahjong.html">Rutland</a> · <a href="montpelier-vt-mahjong.html">Montpelier</a> · <a href="stowe-vt-mahjong.html">Stowe</a> · <a href="brattleboro-vt-mahjong.html">Brattleboro</a> · <a href="bennington-vt-mahjong.html">Bennington</a></p>
<p><a href="vermont-mahjong.html">Vermont statewide</a> · <a href="new-england-mahjong-hub.html">New England hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "new-hampshire-mahjong-hub.html",
            "New Hampshire Mahjong | Manchester, Seacoast & Lakes",
            "New Hampshire mahjong — Manchester, Nashua, Portsmouth, Concord. Lookout Mountain Mahjong travels NH.",
            "new hampshire mahjong hub, mahjong nh cities",
            "New Hampshire Mahjong Guide",
            """<p><strong>New Hampshire mahjong</strong> — Granite State private events:</p>
<p><a href="manchester-nh-mahjong.html">Manchester</a> · <a href="nashua-nh-mahjong.html">Nashua</a> · <a href="concord-nh-mahjong.html">Concord</a> · <a href="portsmouth-nh-mahjong.html">Portsmouth</a> · <a href="keene-nh-mahjong.html">Keene</a> · <a href="hanover-nh-mahjong.html">Hanover</a></p>
<p><a href="new-hampshire-mahjong.html">New Hampshire statewide</a> · <a href="new-england-mahjong-hub.html">New England hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "massachusetts-mahjong-hub.html",
            "Massachusetts Mahjong | Boston, Cape & Western MA",
            "Massachusetts mahjong — Boston, Cape Cod, Worcester, Springfield. Lookout Mountain Mahjong travels MA.",
            "massachusetts mahjong hub, mahjong massachusetts cities",
            "Massachusetts Mahjong Guide",
            """<p><strong>Massachusetts mahjong</strong> — Bay State private lessons:</p>
<p><a href="boston-mahjong.html">Boston</a> · <a href="worcester-ma-mahjong.html">Worcester</a> · <a href="springfield-ma-mahjong.html">Springfield</a> · <a href="cape-cod-mahjong.html">Cape Cod</a> · <a href="nantucket-mahjong.html">Nantucket</a> · <a href="lowell-ma-mahjong.html">Lowell</a> · <a href="brookline-ma-mahjong.html">Brookline</a> · <a href="plymouth-ma-mahjong.html">Plymouth</a></p>
<p><a href="massachusetts-mahjong.html">Massachusetts statewide</a> · <a href="new-england-mahjong-hub.html">New England hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "washington-mahjong-hub.html",
            "Washington Mahjong | Seattle, Tacoma & Puget Sound",
            "Washington mahjong — Seattle, Bellevue, Spokane, Tacoma. Lookout Mountain Mahjong travels WA.",
            "washington mahjong hub, mahjong washington state cities",
            "Washington Mahjong Guide",
            """<p><strong>Washington mahjong</strong> — Evergreen State private events:</p>
<p><a href="seattle-mahjong.html">Seattle</a> · <a href="tacoma-wa-mahjong.html">Tacoma</a> · <a href="spokane-wa-mahjong.html">Spokane</a> · <a href="bellevue-wa-mahjong.html">Bellevue</a> · <a href="bellingham-wa-mahjong.html">Bellingham</a> · <a href="olympia-wa-mahjong.html">Olympia</a></p>
<p><a href="washington-state-mahjong.html">Washington statewide</a> · <a href="pacific-northwest-mahjong-hub.html">PNW hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "oregon-mahjong-hub.html",
            "Oregon Mahjong | Portland, Bend & Willamette Valley",
            "Oregon mahjong — Portland, Eugene, Bend, Salem. Lookout Mountain Mahjong travels OR.",
            "oregon mahjong hub, mahjong oregon cities",
            "Oregon Mahjong Guide",
            """<p><strong>Oregon mahjong</strong> — Beaver State private lessons:</p>
<p><a href="portland-mahjong.html">Portland</a> · <a href="salem-or-mahjong.html">Salem</a> · <a href="bend-or-mahjong.html">Bend</a> · <a href="eugene-or-mahjong.html">Eugene</a> · <a href="medford-or-mahjong.html">Medford</a> · <a href="ashland-or-mahjong.html">Ashland</a></p>
<p><a href="oregon-mahjong.html">Oregon statewide</a> · <a href="pacific-northwest-mahjong-hub.html">PNW hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "north-carolina-mountains-mahjong-hub.html",
            "NC Mountains Mahjong | Asheville, Boone & Highlands",
            "North Carolina mountains mahjong — Asheville, Boone, Highlands, Hendersonville.",
            "north carolina mountains mahjong hub, asheville area mah jongg",
            "NC Mountains Mahjong Guide",
            """<p><strong>North Carolina mountains mahjong</strong> — Blue Ridge private events:</p>
<p><a href="asheville-mahjong.html">Asheville</a> · <a href="boone-nc-mahjong.html">Boone</a> · <a href="hendersonville-nc-mahjong.html">Hendersonville</a> · <a href="highlands-nc-mahjong.html">Highlands</a> · <a href="brevard-nc-mahjong.html">Brevard</a></p>
<p><a href="north-carolina-mahjong-hub.html">NC hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
        (
            "smoky-mountains-mahjong-hub.html",
            "Smoky Mountains Mahjong | Gatlinburg, Pigeon Forge & Asheville",
            "Smoky Mountains mahjong — Gatlinburg, Pigeon Forge, Townsend, Asheville corridor.",
            "smoky mountains mahjong hub, gatlinburg mah jongg",
            "Smoky Mountains Mahjong Guide",
            """<p><strong>Smoky Mountains mahjong</strong> — vacation rental and resort private events:</p>
<p><a href="gatlinburg-tn-mahjong.html">Gatlinburg</a> · <a href="pigeon-forge-tn-mahjong.html">Pigeon Forge</a> · <a href="townsend-tn-mahjong.html">Townsend</a> · <a href="asheville-mahjong.html">Asheville</a> · <a href="sevierville-tn-mahjong.html">Sevierville</a></p>
<p><a href="tennessee-mahjong-hub.html">Tennessee hub</a> · <a href="north-carolina-mountains-mahjong-hub.html">NC mountains hub</a> · <a href="book-mahjong-lesson.html">Book</a></p>""",
        ),
    ]
    for file, title, desc, kw, h1, body in hubs:
        out.append(page(file, title, desc, kw, h1, body, priority="0.86"))

    # ── Cities (80) — slug, name, desc, keywords, blurb, links ──
    cities = [
        ("freeport-me-mahjong.html", "Freeport ME", "Freeport ME mahjong — L.L.Bean village events.", "freeport maine mahjong, mahjong freeport me", "Freeport and southern Maine coast private lessons.", '<p><a href="portland-me-mahjong.html">Portland ME</a> · <a href="maine-mahjong.html">Maine</a></p>'),
        ("ogunquit-me-mahjong.html", "Ogunquit ME", "Ogunquit ME mahjong — coastal vacation events.", "ogunquit mahjong, mahjong ogunquit maine", "Ogunquit and York Beach private events.", '<p><a href="maine-mahjong.html">Maine</a> · <a href="kennebunk-me-mahjong.html">Kennebunk</a></p>'),
        ("kennebunk-me-mahjong.html", "Kennebunk ME", "Kennebunk ME mahjong — Kennebunkport area events.", "kennebunk mahjong, mahjong kennebunk maine", "Kennebunk and Kennebunkport private lessons.", '<p><a href="maine-mahjong-hub.html">Maine hub</a> · <a href="portland-me-mahjong.html">Portland</a></p>'),
        ("bath-me-mahjong.html", "Bath ME", "Bath ME mahjong — midcoast Maine events.", "bath maine mahjong, mahjong bath me", "Bath and midcoast private events.", '<p><a href="maine-mahjong.html">Maine</a></p>'),
        ("ellsworth-me-mahjong.html", "Ellsworth ME", "Ellsworth ME mahjong — Downeast gateway events.", "ellsworth maine mahjong, mahjong ellsworth me", "Ellsworth and Downeast gateway private lessons.", '<p><a href="bar-harbor-me-mahjong.html">Bar Harbor</a> · <a href="maine-mahjong.html">Maine</a></p>'),
        ("stowe-vt-mahjong.html", "Stowe VT", "Stowe VT mahjong — ski resort events.", "stowe vermont mahjong, mahjong stowe vt", "Stowe and ski country private vacation lessons.", '<p><a href="vermont-mahjong.html">Vermont</a> · <a href="burlington-vt-mahjong.html">Burlington</a></p>'),
        ("brattleboro-vt-mahjong.html", "Brattleboro VT", "Brattleboro VT mahjong — southern Vermont events.", "brattleboro mahjong, mahjong brattleboro vermont", "Brattleboro and southern VT private events.", '<p><a href="vermont-mahjong.html">Vermont</a></p>'),
        ("bennington-vt-mahjong.html", "Bennington VT", "Bennington VT mahjong — southwest Vermont events.", "bennington mahjong, mahjong bennington vermont", "Bennington and southwest VT private lessons.", '<p><a href="vermont-mahjong.html">Vermont</a></p>'),
        ("keene-nh-mahjong.html", "Keene NH", "Keene NH mahjong — Monadnock region events.", "keene mahjong, mahjong keene new hampshire", "Keene and Monadnock region private events.", '<p><a href="new-hampshire-mahjong.html">New Hampshire</a></p>'),
        ("hanover-nh-mahjong.html", "Hanover NH", "Hanover NH mahjong — Upper Valley events.", "hanover nh mahjong, mahjong hanover new hampshire", "Hanover and Dartmouth-area private lessons.", '<p><a href="new-hampshire-mahjong.html">New Hampshire</a> · <a href="lebanon-nh-mahjong.html">Lebanon</a></p>'),
        ("lebanon-nh-mahjong.html", "Lebanon NH", "Lebanon NH mahjong — Upper Valley events.", "lebanon nh mahjong, mahjong lebanon new hampshire", "Lebanon and Upper Valley private events.", '<p><a href="hanover-nh-mahjong.html">Hanover</a> · <a href="new-hampshire-mahjong.html">New Hampshire</a></p>'),
        ("exeter-nh-mahjong.html", "Exeter NH", "Exeter NH mahjong — Seacoast events.", "exeter nh mahjong, mahjong exeter new hampshire", "Exeter and Seacoast private lessons.", '<p><a href="portsmouth-nh-mahjong.html">Portsmouth</a> · <a href="new-hampshire-mahjong.html">New Hampshire</a></p>'),
        ("lowell-ma-mahjong.html", "Lowell MA", "Lowell MA mahjong — Merrimack Valley events.", "lowell mahjong, mahjong lowell massachusetts", "Lowell and Merrimack Valley private events.", '<p><a href="boston-mahjong.html">Boston</a> · <a href="massachusetts-mahjong.html">Massachusetts</a></p>'),
        ("brookline-ma-mahjong.html", "Brookline MA", "Brookline MA mahjong — Boston suburb events.", "brookline mahjong, mahjong brookline massachusetts", "Brookline and inner suburb private lessons.", '<p><a href="boston-mahjong.html">Boston</a> · <a href="massachusetts-mahjong.html">Massachusetts</a></p>'),
        ("plymouth-ma-mahjong.html", "Plymouth MA", "Plymouth MA mahjong — South Shore events.", "plymouth massachusetts mahjong, mahjong plymouth ma", "Plymouth and South Shore private events.", '<p><a href="cape-cod-mahjong.html">Cape Cod</a> · <a href="massachusetts-mahjong.html">Massachusetts</a></p>'),
        ("northampton-ma-mahjong.html", "Northampton MA", "Northampton MA mahjong — Pioneer Valley events.", "northampton mahjong, mahjong northampton massachusetts", "Northampton and Pioneer Valley private lessons.", '<p><a href="springfield-ma-mahjong.html">Springfield</a> · <a href="massachusetts-mahjong.html">Massachusetts</a></p>'),
        ("bellevue-wa-mahjong.html", "Bellevue WA", "Bellevue WA mahjong — Eastside Seattle events.", "bellevue mahjong, mahjong bellevue washington", "Bellevue and Eastside private lessons.", '<p><a href="seattle-mahjong.html">Seattle</a> · <a href="washington-state-mahjong.html">Washington</a></p>'),
        ("bellingham-wa-mahjong.html", "Bellingham WA", "Bellingham WA mahjong — north Puget Sound events.", "bellingham mahjong, mahjong bellingham washington", "Bellingham and Whatcom County private events.", '<p><a href="washington-state-mahjong.html">Washington</a></p>'),
        ("olympia-wa-mahjong.html", "Olympia WA", "Olympia WA mahjong — capital region events.", "olympia mahjong, mahjong olympia washington", "Olympia and south Puget Sound private lessons.", '<p><a href="seattle-mahjong.html">Seattle</a> · <a href="washington-state-mahjong.html">Washington</a></p>'),
        ("vancouver-wa-mahjong.html", "Vancouver WA", "Vancouver WA mahjong — Portland metro events.", "vancouver washington mahjong, mahjong vancouver wa", "Vancouver WA and Columbia River private events.", '<p><a href="portland-mahjong.html">Portland</a> · <a href="washington-state-mahjong.html">Washington</a></p>'),
        ("eugene-or-mahjong.html", "Eugene OR", "Eugene OR mahjong — Willamette Valley events.", "eugene mahjong, mahjong eugene oregon", "Eugene and UO-area private lessons.", '<p><a href="portland-mahjong.html">Portland</a> · <a href="oregon-mahjong.html">Oregon</a></p>'),
        ("ashland-or-mahjong.html", "Ashland OR", "Ashland OR mahjong — southern Oregon events.", "ashland oregon mahjong, mahjong ashland or", "Ashland and Shakespeare country private events.", '<p><a href="oregon-mahjong.html">Oregon</a> · <a href="medford-or-mahjong.html">Medford</a></p>'),
        ("hood-river-or-mahjong.html", "Hood River OR", "Hood River OR mahjong — Columbia Gorge events.", "hood river mahjong, mahjong hood river oregon", "Hood River and Gorge private lessons.", '<p><a href="portland-mahjong.html">Portland</a> · <a href="oregon-mahjong.html">Oregon</a></p>'),
        ("boone-nc-mahjong.html", "Boone NC", "Boone NC mahjong — High Country events.", "boone mahjong, mahjong boone north carolina", "Boone and High Country private events.", '<p><a href="asheville-mahjong.html">Asheville</a> · <a href="north-carolina-mahjong.html">North Carolina</a></p>'),
        ("hendersonville-nc-mahjong.html", "Hendersonville NC", "Hendersonville NC mahjong — mountain town events.", "hendersonville mahjong, mahjong hendersonville nc", "Hendersonville and Henderson County private lessons.", '<p><a href="asheville-mahjong.html">Asheville</a> · <a href="north-carolina-mountains-mahjong-hub.html">NC mountains hub</a></p>'),
        ("highlands-nc-mahjong.html", "Highlands NC", "Highlands NC mahjong — mountain resort events.", "highlands nc mahjong, mahjong highlands north carolina", "Highlands and Cashiers area private events.", '<p><a href="asheville-mahjong.html">Asheville</a> · <a href="north-carolina-mahjong.html">North Carolina</a></p>'),
        ("brevard-nc-mahjong.html", "Brevard NC", "Brevard NC mahjong — Pisgah region events.", "brevard nc mahjong, mahjong brevard north carolina", "Brevard and Transylvania County private lessons.", '<p><a href="asheville-mahjong.html">Asheville</a></p>'),
        ("greensboro-nc-mahjong.html", "Greensboro NC", "Greensboro NC mahjong — Triad events.", "greensboro mahjong, mahjong greensboro north carolina", "Greensboro and Piedmont Triad private events.", '<p><a href="north-carolina-mahjong.html">North Carolina</a> · <a href="winston-salem-nc-mahjong.html">Winston-Salem</a></p>'),
        ("winston-salem-nc-mahjong.html", "Winston-Salem NC", "Winston-Salem NC mahjong — Triad events.", "winston salem mahjong, mahjong winston salem nc", "Winston-Salem and Triad private lessons.", '<p><a href="greensboro-nc-mahjong.html">Greensboro</a> · <a href="north-carolina-mahjong.html">North Carolina</a></p>'),
        ("durham-nc-mahjong.html", "Durham NC", "Durham NC mahjong — Research Triangle events.", "durham mahjong, mahjong durham north carolina", "Durham and Triangle private events.", '<p><a href="raleigh-mahjong.html">Raleigh</a> · <a href="chapel-hill-nc-mahjong.html">Chapel Hill</a></p>'),
        ("chapel-hill-nc-mahjong.html", "Chapel Hill NC", "Chapel Hill NC mahjong — Triangle events.", "chapel hill mahjong, mahjong chapel hill nc", "Chapel Hill and UNC-area private lessons.", '<p><a href="durham-nc-mahjong.html">Durham</a> · <a href="raleigh-mahjong.html">Raleigh</a></p>'),
        ("jekyll-island-ga-mahjong.html", "Jekyll Island GA", "Jekyll Island GA mahjong — Golden Isles events.", "jekyll island mahjong, mahjong jekyll island georgia", "Jekyll Island resort private vacation lessons.", '<p><a href="saint-simons-mahjong.html">St. Simons</a> · <a href="georgia-coast-mahjong-hub.html">GA coast hub</a></p>'),
        ("brunswick-ga-mahjong.html", "Brunswick GA", "Brunswick GA mahjong — coastal Georgia events.", "brunswick georgia mahjong, mahjong brunswick ga", "Brunswick and Glynn County private events.", '<p><a href="savannah-mahjong.html">Savannah</a> · <a href="georgia-mahjong.html">Georgia</a></p>'),
        ("tybee-island-ga-mahjong.html", "Tybee Island GA", "Tybee Island GA mahjong — Savannah beach events.", "tybee island mahjong, mahjong tybee island georgia", "Tybee Island beach private lessons.", '<p><a href="savannah-mahjong.html">Savannah</a> · <a href="georgia-coast-mahjong-hub.html">GA coast hub</a></p>'),
        ("macon-ga-mahjong.html", "Macon GA", "Macon GA mahjong — central Georgia events.", "macon mahjong, mahjong macon georgia", "Macon and middle Georgia private events.", '<p><a href="atlanta-mahjong.html">Atlanta</a> · <a href="georgia-mahjong.html">Georgia</a></p>'),
        ("columbus-ga-mahjong.html", "Columbus GA", "Columbus GA mahjong — Chattahoochee Valley events.", "columbus georgia mahjong, mahjong columbus ga", "Columbus and Fort Benning area private lessons.", '<p><a href="georgia-mahjong.html">Georgia</a></p>'),
        ("fontana-ca-mahjong.html", "Fontana CA", "Fontana CA mahjong — Inland Empire events.", "fontana mahjong, mahjong fontana california", "Fontana and Inland Empire private events.", '<p><a href="los-angeles-mahjong.html">Los Angeles</a> · <a href="california-mahjong.html">California</a></p>'),
        ("riverside-ca-mahjong.html", "Riverside CA", "Riverside CA mahjong — Inland Empire events.", "riverside mahjong, mahjong riverside california", "Riverside and IE private lessons.", '<p><a href="california-mahjong.html">California</a></p>'),
        ("stockton-ca-mahjong.html", "Stockton CA", "Stockton CA mahjong — Central Valley events.", "stockton mahjong, mahjong stockton california", "Stockton and San Joaquin County private events.", '<p><a href="california-mahjong.html">California</a> · <a href="sacramento-mahjong.html">Sacramento</a></p>'),
        ("santa-barbara-ca-mahjong.html", "Santa Barbara CA", "Santa Barbara CA mahjong — Central Coast events.", "santa barbara mahjong, mahjong santa barbara california", "Santa Barbara and Central Coast private lessons.", '<p><a href="california-mahjong.html">California</a></p>'),
        ("monterey-ca-mahjong.html", "Monterey CA", "Monterey CA mahjong — Monterey Peninsula events.", "monterey mahjong, mahjong monterey california", "Monterey and Carmel area private events.", '<p><a href="california-mahjong.html">California</a></p>'),
        ("palm-desert-ca-mahjong.html", "Palm Desert CA", "Palm Desert CA mahjong — Coachella Valley events.", "palm desert mahjong, mahjong palm desert california", "Palm Desert and desert resort private lessons.", '<p><a href="palm-springs-mahjong.html">Palm Springs</a> · <a href="california-mahjong.html">California</a></p>'),
        ("mcallen-tx-mahjong.html", "McAllen TX", "McAllen TX mahjong — Rio Grande Valley events.", "mcallen mahjong, mahjong mcallen texas", "McAllen and RGV private events.", '<p><a href="texas-mahjong.html">Texas</a> · <a href="brownsville-tx-mahjong.html">Brownsville</a></p>'),
        ("abilene-tx-mahjong.html", "Abilene TX", "Abilene TX mahjong — west central Texas events.", "abilene mahjong, mahjong abilene texas", "Abilene and west central TX private lessons.", '<p><a href="texas-mahjong.html">Texas</a></p>'),
        ("baytown-tx-mahjong.html", "Baytown TX", "Baytown TX mahjong — Houston east bay events.", "baytown mahjong, mahjong baytown texas", "Baytown and east Houston metro private events.", '<p><a href="houston-mahjong.html">Houston</a> · <a href="texas-mahjong.html">Texas</a></p>'),
        ("key-west-fl-mahjong.html", "Key West FL", "Key West FL mahjong — Florida Keys events.", "key west mahjong, mahjong key west florida", "Key West and Keys private vacation lessons.", '<p><a href="miami-mahjong.html">Miami</a> · <a href="florida-mahjong.html">Florida</a></p>'),
        ("marco-island-fl-mahjong.html", "Marco Island FL", "Marco Island FL mahjong — southwest Florida island events.", "marco island mahjong, mahjong marco island florida", "Marco Island and Ten Thousand Islands private events.", '<p><a href="naples-florida-mahjong.html">Naples</a> · <a href="florida-mahjong.html">Florida</a></p>'),
        ("boca-raton-fl-mahjong.html", "Boca Raton FL", "Boca Raton FL mahjong — Palm Beach County events.", "boca raton mahjong, mahjong boca raton florida", "Boca Raton and south Palm Beach private lessons.", '<p><a href="palm-beach-mahjong.html">Palm Beach</a> · <a href="florida-mahjong.html">Florida</a></p>'),
        ("vero-beach-fl-mahjong.html", "Vero Beach FL", "Vero Beach FL mahjong — Treasure Coast events.", "vero beach mahjong, mahjong vero beach florida", "Vero Beach and Treasure Coast private events.", '<p><a href="florida-mahjong.html">Florida</a></p>'),
        ("panama-city-beach-fl-mahjong.html", "Panama City Beach FL", "Panama City Beach FL mahjong — Emerald Coast events.", "panama city beach mahjong, mahjong panama city beach florida", "Panama City Beach and Emerald Coast private lessons.", '<p><a href="destin-florida-mahjong.html">Destin</a> · <a href="florida-mahjong.html">Florida</a></p>'),
        ("louisville-ky-mahjong.html", "Louisville KY", "Louisville KY mahjong — Derby City events.", "louisville mahjong, mahjong louisville kentucky", "Louisville metro private events.", '<p><a href="kentucky-mahjong.html">Kentucky</a></p>'),
        ("owensboro-ky-mahjong.html", "Owensboro KY", "Owensboro KY mahjong — western Kentucky events.", "owensboro mahjong, mahjong owensboro kentucky", "Owensboro and western KY private lessons.", '<p><a href="kentucky-mahjong.html">Kentucky</a> · <a href="louisville-mahjong.html">Louisville</a></p>'),
        ("baton-rouge-la-mahjong.html", "Baton Rouge LA", "Baton Rouge LA mahjong — capital region events.", "baton rouge mahjong, mahjong baton rouge louisiana", "Baton Rouge and capital area private events.", '<p><a href="louisiana-mahjong.html">Louisiana</a> · <a href="new-orleans-mahjong.html">New Orleans</a></p>'),
        ("shreveport-la-mahjong.html", "Shreveport LA", "Shreveport LA mahjong — northwest Louisiana events.", "shreveport mahjong, mahjong shreveport louisiana", "Shreveport and northwest LA private lessons.", '<p><a href="louisiana-mahjong.html">Louisiana</a></p>'),
        ("mobile-al-mahjong.html", "Mobile AL", "Mobile AL mahjong — Gulf Coast events.", "mobile alabama mahjong, mahjong mobile al", "Mobile and Gulf Coast private events.", '<p><a href="alabama-mahjong.html">Alabama</a> · <a href="gulf-coast-mahjong-hub.html">Gulf Coast hub</a></p>'),
        ("montgomery-al-mahjong.html", "Montgomery AL", "Montgomery AL mahjong — capital region events.", "montgomery mahjong, mahjong montgomery alabama", "Montgomery and River Region private lessons.", '<p><a href="alabama-mahjong.html">Alabama</a> · <a href="birmingham-mahjong.html">Birmingham</a></p>'),
        ("myrtle-beach-sc-mahjong.html", "Myrtle Beach SC", "Myrtle Beach SC mahjong — Grand Strand events.", "myrtle beach mahjong, mahjong myrtle beach south carolina", "Myrtle Beach and Grand Strand private events.", '<p><a href="south-carolina-mahjong.html">South Carolina</a></p>'),
        ("hilton-head-sc-mahjong.html", "Hilton Head SC", "Hilton Head SC mahjong — Lowcountry resort events.", "hilton head mahjong, mahjong hilton head sc", "Hilton Head Island private vacation lessons.", '<p><a href="charleston-sc-mahjong.html">Charleston</a> · <a href="south-carolina-mahjong-hub.html">SC hub</a></p>'),
        ("spartanburg-sc-mahjong.html", "Spartanburg SC", "Spartanburg SC mahjong — Upstate events.", "spartanburg mahjong, mahjong spartanburg south carolina", "Spartanburg and Upstate private lessons.", '<p><a href="greenville-sc-mahjong.html">Greenville</a> · <a href="south-carolina-mahjong.html">South Carolina</a></p>'),
        ("cookeville-tn-mahjong.html", "Cookeville TN", "Cookeville TN mahjong — Upper Cumberland events.", "cookeville mahjong, mahjong cookeville tennessee", "Cookeville and Upper Cumberland private events.", '<p><a href="tennessee-mahjong.html">Tennessee</a> · <a href="nashville-mahjong.html">Nashville</a></p>'),
        ("gallatin-tn-mahjong.html", "Gallatin TN", "Gallatin TN mahjong — Nashville suburb events.", "gallatin mahjong, mahjong gallatin tennessee", "Gallatin and Sumner County private lessons.", '<p><a href="nashville-mahjong.html">Nashville</a> · <a href="tennessee-mahjong.html">Tennessee</a></p>'),
        ("boulder-co-mahjong.html", "Boulder CO", "Boulder CO mahjong — Front Range events.", "boulder mahjong, mahjong boulder colorado", "Boulder and Front Range private lessons.", '<p><a href="denver-mahjong.html">Denver</a> · <a href="colorado-mahjong.html">Colorado</a></p>'),
        ("fort-collins-co-mahjong.html", "Fort Collins CO", "Fort Collins CO mahjong — northern Colorado events.", "fort collins mahjong, mahjong fort collins colorado", "Fort Collins and NoCo private events.", '<p><a href="colorado-mahjong.html">Colorado</a> · <a href="denver-mahjong.html">Denver</a></p>'),
        ("ames-ia-mahjong.html", "Ames IA", "Ames IA mahjong — central Iowa events.", "ames iowa mahjong, mahjong ames ia", "Ames and Iowa State area private lessons.", '<p><a href="des-moines-mahjong.html">Des Moines</a> · <a href="iowa-mahjong.html">Iowa</a></p>'),
        ("missoula-mt-mahjong.html", "Missoula MT", "Missoula MT mahjong — western Montana events.", "missoula mahjong, mahjong missoula montana", "Missoula and western MT private events.", '<p><a href="montana-mahjong.html">Montana</a></p>'),
        ("great-falls-mt-mahjong.html", "Great Falls MT", "Great Falls MT mahjong — north central Montana events.", "great falls mahjong, mahjong great falls montana", "Great Falls and north central MT private lessons.", '<p><a href="montana-mahjong.html">Montana</a></p>'),
        ("omaha-ne-mahjong.html", "Omaha NE", "Omaha NE mahjong — metro events.", "omaha mahjong, mahjong omaha nebraska", "Omaha and Council Bluffs metro private events.", '<p><a href="nebraska-mahjong.html">Nebraska</a> · <a href="nebraska-mahjong-hub.html">Nebraska hub</a></p>'),
        ("lincoln-ne-mahjong.html", "Lincoln NE", "Lincoln NE mahjong — capital region events.", "lincoln nebraska mahjong, mahjong lincoln ne", "Lincoln and Lancaster County private lessons.", '<p><a href="nebraska-mahjong.html">Nebraska</a></p>'),
        ("gatlinburg-tn-mahjong.html", "Gatlinburg TN", "Gatlinburg TN mahjong — Smoky Mountains events.", "gatlinburg mahjong, mahjong gatlinburg tennessee", "Gatlinburg and Smoky Mountains private events.", '<p><a href="smoky-mountains-mahjong-hub.html">Smoky Mountains hub</a> · <a href="tennessee-mahjong.html">Tennessee</a></p>'),
        ("pigeon-forge-tn-mahjong.html", "Pigeon Forge TN", "Pigeon Forge TN mahjong — Smoky Mountains events.", "pigeon forge mahjong, mahjong pigeon forge tennessee", "Pigeon Forge and Dollywood area private lessons.", '<p><a href="gatlinburg-tn-mahjong.html">Gatlinburg</a> · <a href="smoky-mountains-mahjong-hub.html">Smoky Mountains hub</a></p>'),
        ("sevierville-tn-mahjong.html", "Sevierville TN", "Sevierville TN mahjong — Smoky Mountains events.", "sevierville mahjong, mahjong sevierville tennessee", "Sevierville and Smoky Mountains private events.", '<p><a href="pigeon-forge-tn-mahjong.html">Pigeon Forge</a></p>'),
        ("townsend-tn-mahjong.html", "Townsend TN", "Townsend TN mahjong — peaceful Smokies events.", "townsend mahjong, mahjong townsend tennessee", "Townsend and quiet Smokies private lessons.", '<p><a href="gatlinburg-tn-mahjong.html">Gatlinburg</a></p>'),
        ("sioux-falls-sd-mahjong.html", "Sioux Falls SD", "Sioux Falls SD mahjong — largest city events.", "sioux falls south dakota mahjong, mahjong sioux falls sd", "Sioux Falls metro private lessons.", '<p><a href="south-dakota-mahjong.html">South Dakota</a></p>'),
        ("fargo-sd-mahjong.html", "Fargo SD", "Fargo SD mahjong — eastern South Dakota events.", "fargo south dakota mahjong, mahjong fargo sd", "Fargo area private events.", '<p><a href="fargo-nd-mahjong.html">Fargo ND</a> · <a href="south-dakota-mahjong.html">South Dakota</a></p>'),
    ]
    for slug, name, desc, kw, blurb, links in cities:
        out.append(city(slug, name, desc, kw, blurb, links))

    # ── Greek life (24) — orgs not yet in PAGES ──
    fraternities = [
        ("beta-upsilon-chi", "Beta Upsilon Chi", "BYX"),
        ("delta-phi", "Delta Phi", "Delta Phi"),
        ("pi-lambda-phi", "Pi Lambda Phi", "Pi Lam"),
        ("sigma-phi", "Sigma Phi", "Sigma Phi"),
        ("alpha-kappa-lambda", "Alpha Kappa Lambda", "AKL"),
        ("delta-sigma-iota", "Delta Sigma Iota", "DSI"),
        ("kappa-sigma-kappa", "Kappa Sigma Kappa", "KSK"),
        ("sigma-alpha-iota", "Sigma Alpha Iota", "SAI"),
        ("tau-beta-sigma", "Tau Beta Sigma", "TBS"),
        ("alpha-gamma-rho", "Alpha Gamma Rho", "AGR"),
        ("pi-alpha-phi", "Pi Alpha Phi", "Pi A Phi"),
        ("beta-upsilon-xi", "Beta Upsilon Xi", "BUXi"),
        ("sigma-lambda-gamma", "Sigma Lambda Gamma", "SLG"),
    ]
    for slug, name, nick in fraternities:
        out.append(_greek_fr(mahjong_kw, slug, name, nick))

    sororities = [
        ("gamma-sigma-sigma", "Gamma Sigma Sigma", "GSS"),
        ("sigma-sigma-rho", "Sigma Sigma Rho", "SSR"),
        ("theta-phi-alpha", "Theta Phi Alpha", "TPA"),
        ("kappa-beta-gamma", "Kappa Beta Gamma", "KBG"),
        ("alpha-delta-chi", "Alpha Delta Chi", "ADC"),
        ("zeta-phi-eta", "Zeta Phi Eta", "ZPhiE"),
        ("kappa-phi-lambda", "Kappa Phi Lambda", "KPL"),
    ]
    for slug, name, nick in sororities:
        out.append(_greek_sor(mahjong_kw, slug, name, nick))

    # ── Occasions (24) ──
    occasions = [
        ("ladies-night-mahjong", "Ladies Night", "ladies night mahjong — evening social with tiles", '<p>Book a <strong>ladies night mahjong</strong> lesson — the group chat will thank you. <a href="girls-night-mahjong.html">Girls night</a> · <a href="ladies-mahjong.html">Ladies mahjong</a>.</p>'),
        ("couples-game-night-mahjong", "Couples Game Night", "couples game night mahjong — date night with tiles", '<p>Swap movie night for <strong>couples game night mahjong</strong>. <a href="date-night-mahjong.html">Date night</a> · <a href="screen-free-game-night.html">Screen-free game night</a>.</p>'),
        ("empty-nesters-mahjong", "Empty Nesters", "empty nesters mahjong — parents reconnect with tiles", '<p><strong>Empty nesters</strong> — rediscover fun with a mahjong lesson. <a href="ladies-mahjong.html">Ladies mahjong</a> · <a href="book-club-mahjong.html">Book club swap</a>.</p>'),
        ("grandparents-day-mahjong", "Grandparents Day", "grandparents day mahjong — multigenerational tiles", '<p>Celebrate <strong>Grandparents Day</strong> with a family mahjong lesson. <a href="mahjong-for-seniors.html">For seniors</a> · <a href="family-reunion-mahjong.html">Family reunion</a>.</p>'),
        ("veterans-day-mahjong", "Veterans Day", "veterans day mahjong — honor veterans with community tiles", '<p>Honor veterans with a <strong>Veterans Day mahjong</strong> community lesson. <a href="church-mahjong.html">Church</a> · <a href="nonprofit-mahjong.html">Nonprofit</a>.</p>'),
        ("thanksgiving-weekend-mahjong", "Thanksgiving Weekend", "thanksgiving weekend mahjong — holiday gathering with tiles", '<p>Add <strong>Thanksgiving weekend mahjong</strong> to your family lineup. <a href="thanksgiving-mahjong.html">Thanksgiving</a> · <a href="holiday-brunch-mahjong.html">Holiday brunch</a>.</p>'),
        ("super-bowl-party-mahjong", "Super Bowl Party Swap", "super bowl party mahjong — pregame tiles instead of football", '<p>Host <strong>Super Bowl party mahjong</strong> for guests who want tiles over touchdowns. <a href="girls-night-mahjong.html">Girls night</a> · <a href="happy-hour-mahjong.html">Happy hour</a>.</p>'),
        ("oscar-night-mahjong", "Oscar Night", "oscar night mahjong — awards watch party with tiles", '<p>Red carpet? Try <strong>Oscar night mahjong</strong> during the show. <a href="girls-night-mahjong.html">Girls night</a> · <a href="cocktail-mahjong.html">Cocktail party</a>.</p>'),
        ("presidents-day-weekend-mahjong", "Presidents Day Weekend", "presidents day weekend mahjong — February long weekend with tiles", '<p>Book <strong>Presidents Day weekend mahjong</strong> for your crew. <a href="fall-mahjong.html">Fall &amp; winter gatherings</a> · <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("st-patricks-brunch-mahjong", "St. Patrick's Brunch", "st patricks brunch mahjong — March gathering with tiles", '<p><strong>St. Patrick\'s brunch mahjong</strong> — festive and social. <a href="mahjong-brunch.html">Mahjong brunch</a> · <a href="sunday-brunch-mahjong.html">Sunday brunch</a>.</p>'),
        ("easter-brunch-mahjong", "Easter Brunch", "easter brunch mahjong — spring holiday gathering with tiles", '<p>Celebrate <strong>Easter brunch</strong> with a mahjong lesson. <a href="spring-mahjong.html">Spring</a> · <a href="church-mahjong.html">Church</a>.</p>'),
        ("prom-afterparty-mahjong", "Prom Afterparty", "prom afterparty mahjong — safe post-prom activity with tiles", '<p>A memorable <strong>prom afterparty mahjong</strong> — supervised and fun. <a href="graduation-party-mahjong.html">Graduation party</a> · <a href="moms-night-out-mahjong.html">Mom\'s night out</a>.</p>'),
        ("homecoming-weekend-mahjong", "Homecoming Weekend", "homecoming weekend mahjong — college celebration with tiles", '<p>Make <strong>homecoming weekend</strong> unforgettable with mahjong. <a href="college-alumni-mahjong.html">College alumni</a> · <a href="greek-life-mahjong.html">Greek life</a>.</p>'),
        ("tailgate-mahjong", "Tailgate Mahjong", "tailgate mahjong — pregame parking lot tiles", '<p>Upgrade the <strong>tailgate</strong> with a portable mahjong lesson. <a href="college-alumni-mahjong.html">Alumni</a> · <a href="company-picnic-mahjong.html">Company picnic</a>.</p>'),
        ("wine-and-cheese-mahjong", "Wine and Cheese", "wine and cheese mahjong — tasting party with tiles", '<p>Pair <strong>wine and cheese</strong> with mahjong — our favorite format. <a href="wine-tasting-mahjong.html">Wine tasting</a> · <a href="ladies-luncheon-mahjong.html">Luncheon</a>.</p>'),
        ("charcuterie-night-mahjong", "Charcuterie Night", "charcuterie night mahjong — boards and tiles", '<p><strong>Charcuterie night mahjong</strong> — graze, sip, and play. <a href="wine-and-mahjong.html">Wine &amp; mahjong</a> · <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("paint-and-sip-mahjong", "Paint and Sip Swap", "paint and sip mahjong — creative night with tiles", '<p>Swap canvas night for <strong>paint and sip mahjong</strong>. <a href="craft-night-mahjong.html">Craft night</a> · <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("yoga-retreat-mahjong", "Yoga Retreat", "yoga retreat mahjong — wellness weekend with tiles", '<p>After savasana — unwind with <strong>yoga retreat mahjong</strong>. <a href="spa-day-mahjong.html">Spa day</a> · <a href="team-retreat-mahjong.html">Team retreat</a>.</p>'),
        ("condo-association-mahjong", "Condo Association", "condo association mahjong — building social with tiles", '<p>Build community with <strong>condo association mahjong</strong>. <a href="hoa-mahjong.html">HOA</a> · <a href="neighborhood-mahjong.html">Neighborhood</a>.</p>'),
        ("country-inn-mahjong", "Country Inn", "country inn mahjong — boutique hotel event with tiles", '<p>Draw guests to your <strong>country inn</strong> with live mahjong. <a href="resort-mahjong.html">Resort</a> · <a href="bed-and-breakfast-mahjong.html">B&amp;B</a>.</p>'),
        ("bed-and-breakfast-mahjong", "Bed and Breakfast", "bed and breakfast mahjong — inn guest activity with tiles", '<p>Give B&amp;B guests a reason to stay in — <strong>bed and breakfast mahjong</strong>. <a href="vacation-mahjong.html">Vacation</a> · <a href="cottage-mahjong.html">Cottage</a>.</p>'),
        ("antique-show-mahjong", "Antique Show", "antique show mahjong — market weekend with tiles", '<p>Pair your <strong>antique show</strong> with a mahjong pop-up. <a href="vendor-fair-mahjong.html">Vendor fair</a> · <a href="pop-up-mahjong.html">Pop-up</a>.</p>'),
        ("farm-to-table-mahjong", "Farm to Table Dinner", "farm to table mahjong — dinner party with tiles after the meal", '<p>After the farm dinner — play <strong>farm to table mahjong</strong>. <a href="supper-club-mahjong.html">Supper club</a> · <a href="dinner-party-mahjong.html">Dinner party</a>.</p>'),
    ]
    for slug, title, desc, body in occasions:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    # ── Gameplay / rules (18) ──
    rules = [
        ("mahjong-singleton-mahjong.html", "Singleton", "singleton in mahjong — a single tile in a hand pattern", '<p>A <strong>singleton</strong> is a lone tile in many NMJL hands. <a href="mahjong-singles.html">Singles</a> · <a href="read-nmjl-card.html">Read the card</a>.</p>'),
        ("mahjong-replace-joker.html", "Replace a Joker", "replace a joker in mahjong — swapping wild tiles in exposures", '<p>You may <strong>replace a joker</strong> in an exposure under NMJL rules. <a href="redeem-joker-mahjong.html">Redeem joker</a> · <a href="mahjong-jokers.html">Jokers</a>.</p>'),
        ("mahjong-blind-pass.html", "Blind Pass", "blind pass in mahjong — passing without looking during Charleston", '<p>A <strong>blind pass</strong> speeds up the Charleston — tiles passed face-down. <a href="mahjong-charleston.html">Charleston</a> · <a href="pass-three-tiles-mahjong.html">Pass three tiles</a>.</p>'),
        ("mahjong-courtesy-discard.html", "Courtesy Discard", "courtesy discard in mahjong — optional final pass tile", '<p>Some tables allow a <strong>courtesy discard</strong> after the Charleston. <a href="charleston-courtesy-mahjong.html">Courtesy pass</a> · <a href="mahjong-101.html">101</a>.</p>'),
        ("mahjong-claim-kong.html", "Claim for Kong", "claim for kong in mahjong — calling a discard to complete four of a kind", '<p>You may <strong>claim for a kong</strong> when a discard completes four matching tiles. <a href="mahjong-kong.html">Kong</a> · <a href="calling-mahjong.html">Calling</a>.</p>'),
        ("mahjong-claim-quint.html", "Claim for Quint", "claim for quint in mahjong — calling for five of a kind", '<p>A <strong>claim for quint</strong> completes five matching tiles from a discard. <a href="mahjong-quints.html">Quints</a> · <a href="mahjong-quint-meld.html">Quint meld</a>.</p>'),
        ("mahjong-joker-exchange.html", "Joker Exchange", "joker exchange in mahjong — redeeming a joker from an exposure", '<p><strong>Joker exchange</strong> lets you swap a natural tile for a joker on someone\'s rack. <a href="redeem-joker-mahjong.html">Redeem joker</a>.</p>'),
        ("mahjong-table-speed.html", "Table Speed", "table speed in mahjong — pace of play and courtesy", '<p><strong>Table speed</strong> — pick, discard, and pass with courtesy. <a href="mahjong-etiquette.html">Etiquette</a> · <a href="mahjong-turn-order.html">Turn order</a>.</p>'),
        ("mahjong-win-on-last-tile.html", "Win on Last Tile", "win on last tile in mahjong — wall game vs winning from the wall", '<p>Can you <strong>win on the last tile</strong>? Learn wall game rules in <a href="mahjong-wall-game.html">Wall game</a> · <a href="mahjong-dead-wall.html">Dead wall</a>.</p>'),
        ("mahjong-exposed-pair.html", "Exposed Pair", "exposed pair in mahjong — when a pair may be shown on the rack", '<p>Most hands need a concealed pair — learn when an <strong>exposed pair</strong> is allowed. <a href="mahjong-pair-requirement.html">Pair requirement</a>.</p>'),
        ("mahjong-wrong-call-mahjong.html", "Wrong Call", "wrong call in mahjong — incorrect claims and penalties", '<p>A <strong>wrong call</strong> — claiming a tile you cannot use — may foul your hand. <a href="foul-hand-mahjong.html">Foul hand</a> · <a href="mahjong-call-rules.html">Call rules</a>.</p>'),
        ("mahjong-rack-concealed.html", "Concealed on Rack", "concealed tiles on rack in mahjong — face-down tile order", '<p>Keep <strong>concealed tiles</strong> face-down on your rack until you expose or win. <a href="rack-order-mahjong.html">Rack order</a>.</p>'),
        ("mahjong-passed-joker.html", "Passed Joker", "passed joker in mahjong — jokers during the Charleston", '<p><strong>Jokers</strong> are not passed in the Charleston — only during play. <a href="mahjong-jokers.html">Jokers guide</a> · <a href="mahjong-charleston.html">Charleston</a>.</p>'),
        ("mahjong-optional-pair.html", "Optional Pair", "optional pair in mahjong — hands where the pair category varies", '<p>Some NMJL hands list an <strong>optional pair</strong> — read the card carefully. <a href="read-nmjl-card.html">Read the card</a>.</p>'),
        ("mahjong-two-player-rules.html", "Two Player Rules", "two player mahjong rules — not standard American four-player", '<p>American NMJL is <strong>four players</strong> — we teach standard table rules in <a href="mahjong-101.html">Mahjong 101</a>.</p>'),
        ("mahjong-table-assignments.html", "Seat Assignments", "seat assignments in mahjong — winds and dealing order", '<p><strong>Seat assignments</strong> set winds and dealing — east starts. <a href="east-seat-mahjong.html">East seat</a> · <a href="mahjong-winds.html">Winds</a>.</p>'),
        ("mahjong-hot-wall-tile.html", "Hot Wall Tile", "hot wall tile in mahjong — drawing the winning tile yourself", '<p>A <strong>hot wall tile</strong> — self-pick from the wall — wins the hand. <a href="self-pick-mahjong.html">Self-pick</a> · <a href="mahjong-hot-tile.html">Hot tile</a>.</p>'),
        ("mahjong-cold-wall.html", "Cold Wall", "cold wall in mahjong — reserved tiles at end of wall", '<p>The <strong>cold wall</strong> — tiles reserved and not drawn in play. <a href="mahjong-dead-wall.html">Dead wall</a> · <a href="break-wall-mahjong.html">Break the wall</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out


def _dedup_extend(pages: list, new_pages: list) -> int:
    seen = {p["file"] for p in pages}
    added = 0
    for p in new_pages:
        if p["file"] not in seen:
            pages.append(p)
            seen.add(p["file"])
            added += 1
    return added


def extend_pages_with_bulk_waves(pages: list, city, page, mahjong_kw) -> None:
    """Append all bulk mega waves to the main PAGES list (deduped by file slug)."""
    from seo_bulk_wave27 import bulk_pages_mega_wave_27

    _dedup_extend(pages, bulk_pages_mega_wave_26(city, page, mahjong_kw))
    _dedup_extend(pages, bulk_pages_mega_wave_27(city, page, mahjong_kw))
