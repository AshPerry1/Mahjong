#!/usr/bin/env python3
"""Generate hidden crawler-only SEO pages — never linked from index/shop/faq."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

BASE = "https://lookoutmountainmahjong.com"
HOME = f"{BASE}/"
TODAY = date.today().isoformat()

ORG = {
    "@type": "Organization",
    "@id": f"{HOME}#organization",
    "name": "Lookout Mountain Mahjong",
    "alternateName": ["Mountain Mahjong", "Lookout Mountain Mahjong"],
    "url": HOME,
    "logo": f"{BASE}/logo.png",
    "email": "lookoutmountainmahjong@gmail.com",
    "telephone": "+1-919-247-3392",
    "sameAs": [
        "https://www.instagram.com/lookoutmountainmahjong/",
        "https://www.tiktok.com/@lookoutmountainmahjong",
    ],
}

PUBLIC_SITE = [
    ("", "weekly", "1.0"),
    ("shop.html", "weekly", "0.9"),
    ("faq.html", "monthly", "0.8"),
]


def city(slug: str, city_name: str, desc: str, keywords: str, blurb: str, links: str = "") -> dict:
    return {
        "file": slug,
        "title": f"{city_name} Mahjong Lessons | Lookout Mountain Mahjong",
        "description": desc,
        "keywords": keywords,
        "h1": f"{city_name} Mahjong",
        "body": f"<p>{blurb}</p>{links}",
        "priority": "0.72",
    }


def page(file: str, title: str, desc: str, kw: str, h1: str, body: str, **extra) -> dict:
    p = {"file": file, "title": title, "description": desc, "keywords": kw, "h1": h1, "body": body}
    p.update(extra)
    return p


PAGES = [
    page(
        "mahjong.html",
        "Mahjong | American Mahjong Lessons — Lookout Mountain Mahjong",
        "American mahjong lessons, Mahjong 101 & 102, Greenbrier tournaments, and private events with certified TML Ambassadors Mahj Jen and Mahj Hen.",
        "mahjong, american mahjong, mah jongg, mountain mahjong, lookout mountain mahjong",
        "American Mahjong — Lookout Mountain Mahjong",
        """<p><strong>Lookout Mountain Mahjong</strong> teaches <strong>American mahjong</strong> (mah jongg) nationwide — beginner lessons, private parties, corporate events, and luxury resort tournaments including The Greenbrier.</p>
<p>Certified TML Ambassadors <strong>Jenn Kline (Mahj Jen)</strong> and <strong>Ann Henley Perry (Mahj Hen)</strong> offer Mahjong 101 ($125/person) and Mahjong 102 ($115/person). We bring tiles, tables, and the NMJL card.</p>
<h2>Mahjong Services</h2>
<ul>
<li><a href="learn-american-mahjong.html">Learn American Mahjong</a></li>
<li><a href="mahjong-101.html">Mahjong 101</a> — beginners, $125/person</li>
<li><a href="mahjong-102.html">Mahjong 102</a> — strategy, $115/person</li>
<li><a href="mahjong-lessons-near-me.html">Mahjong lessons near me</a></li>
<li><a href="greenbrier-mahjong.html">Greenbrier mahjong</a></li>
<li><a href="book-mahjong-lesson.html">Book a mahjong lesson</a></li>
<li><a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a></li>
</ul>
<p>Follow <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a> on Instagram. Brand: <a href="get-mahjn.html">Get Mahj'n</a> · <a href="a-bam-good-time.html">A Bam Good Time</a>.</p>""",
        priority="0.95",
        schema={"@type": "WebPage", "name": "Mahjong | Lookout Mountain Mahjong"},
    ),
    page("m.html", "M — Mahjong | Lookout Mountain Mahjong", "M is for Mahjong. Lookout Mountain Mahjong — American mahjong lessons with Mahj Jen & Mahj Hen.", "mahjong, m mahjong, mountain mahjong, get mahjn", "M is for Mahjong", """<p><strong>Mountain Mahjong</strong> with Mahj Jen &amp; Mahj Hen. American mahjong lessons, Greenbrier events, TML tiles.</p>
<p><a href="mahjong.html">Everything mahjong</a> · <a href="book-mahjong-lesson.html">Book a lesson</a> · <a href="lookoutmountainmahjong.html">Instagram</a></p>""", priority="0.9"),
    page(
        "find-us.html",
        "Find Lookout Mountain Mahjong Online",
        "How to find Lookout Mountain Mahjong — mahjong lessons, Mahj Jen, Mahj Hen, Greenbrier, cities, Instagram @lookoutmountainmahjong.",
        "find lookout mountain mahjong, mahj jen, mahj hen, lookoutmountainmahjong",
        "Find Lookout Mountain Mahjong",
        """<p>Search by name, city, or topic — all pages below are part of Lookout Mountain Mahjong (Mountain Mahjong).</p>
<h2>Names &amp; Brand</h2>
<p><a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a> · <a href="jen-kline-mahjong.html">Jen Kline</a> · <a href="ann-henley-perry-mahjong.html">Ann Henley Perry</a> · <a href="lookout-mountain-mahjong.html">Lookout Mountain Mahjong</a> · <a href="mountain-mahjong.html">Mountain Mahjong</a> · <a href="get-mahjn.html">Get Mahj'n</a> · <a href="a-bam-good-time.html">A Bam Good Time</a> · <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a></p>
<h2>Lessons &amp; Booking</h2>
<p><a href="mahjong-101.html">Mahjong 101</a> · <a href="mahjong-102.html">Mahjong 102</a> · <a href="book-mahjong-lesson.html">Book a lesson</a> · <a href="beginner-mahjong.html">Beginner</a> · <a href="private-mahjong-lessons.html">Private lessons</a> · <a href="mahjong-lessons-near-me.html">Near me</a> · <a href="mahjong-class.html">Mahjong class</a> · <a href="mahjong-instructor.html">Instructor</a></p>
<h2>Learn &amp; Tips</h2>
<p><a href="learn-american-mahjong.html">Learn American mahjong</a> · <a href="american-mah-jongg.html">American mah jongg</a> · <a href="how-to-play-mahjong.html">How to play</a> · <a href="mahjong-rules.html">Rules</a> · <a href="mahjong-charleston.html">Charleston</a> · <a href="mahjong-jokers.html">Jokers</a> · <a href="nmjl-card.html">NMJL card</a> · <a href="mahjong-tips.html">Tips</a> · <a href="mahjong-faq.html">FAQ</a></p>
<h2>Events</h2>
<p><a href="greenbrier-mahjong.html">Greenbrier</a> · <a href="corporate-mahjong-events.html">Corporate</a> · <a href="sorority-mahjong-parties.html">Sorority</a> · <a href="girls-night-mahjong.html">Girls night</a> · <a href="country-club-mahjong.html">Country club</a> · <a href="mahjong-tournament.html">Tournament</a> · <a href="marthas-vineyard-mahjong.html">Martha's Vineyard</a></p>
<h2>Tiles &amp; Shop</h2>
<p><a href="mahjong-tiles.html">Mahjong tiles</a> · <a href="the-mahjong-line.html">The Mahjong Line</a> · TML code <strong>LOOKOUTMOUNTAIN</strong></p>
<h2>Contact</h2>
<p>lookoutmountainmahjong@gmail.com · (919) 247-3392 · <a href="press.html">Press</a></p>""",
        priority="0.92",
    ),
    page("mahj-jen-mahj-hen.html", "Mahj Jen & Mahj Hen | Jenn Kline & Ann Henley Perry", "Meet Mahj Jen (Jenn Kline) and Mahj Hen (Ann Henley Perry), TML Ambassadors and co-founders of Lookout Mountain Mahjong.", "mahj jen, mahj hen, jen kline mahjong, ann henley perry mahjong", "Mahj Jen &amp; Mahj Hen", """<p><strong>Jenn Kline (Mahj Jen)</strong> and <strong>Ann Henley Perry (Mahj Hen)</strong> teach American mahjong from Lookout Mountain, Georgia to The Greenbrier and nationwide.</p>
<p>Mahjong 101: $125/person · Mahjong 102: $115/person · <a href="book-mahjong-lesson.html">Book a lesson</a></p>""", schema={"@type": "WebPage", "name": "Mahj Jen and Mahj Hen"}, priority="0.88"),
    page("jen-kline-mahjong.html", "Jen Kline Mahjong | Mahj Jen", "Jenn Kline (Mahj Jen) — American mahjong instructor, TML Ambassador, co-founder of Lookout Mountain Mahjong.", "jen kline mahjong, jenn kline mahjong, mahj jen", "Jen Kline — Mahj Jen", "<p>Certified TML Ambassador teaching <a href=\"mahjong-101.html\">Mahjong 101</a> and hosting <a href=\"greenbrier-mahjong.html\">Greenbrier</a> events. Partner: <a href=\"ann-henley-perry-mahjong.html\">Ann Henley Perry (Mahj Hen)</a>.</p>"),
    page("ann-henley-perry-mahjong.html", "Ann Henley Perry Mahjong | Mahj Hen", "Ann Henley Perry (Mahj Hen) — American mahjong instructor, TML Ambassador, co-founder of Lookout Mountain Mahjong.", "ann henley perry mahjong, mahj hen", "Ann Henley Perry — Mahj Hen", "<p>Co-founder of <a href=\"mountain-mahjong.html\">Mountain Mahjong</a> with <a href=\"jen-kline-mahjong.html\">Mahj Jen</a>. Book <a href=\"book-mahjong-lesson.html\">private lessons</a> nationwide.</p>"),
    page("lookout-mountain-mahjong.html", "Lookout Mountain Mahjong | Mountain Mahjong", "Lookout Mountain Mahjong — American mahjong on Lookout Mountain, Georgia. Mahj Jen & Mahj Hen.", "lookout mountain mahjong, mountain mahjong", "Lookout Mountain Mahjong", "<p>Official home of <a href=\"mountain-mahjong.html\">Mountain Mahjong</a> — TML Ambassadors in Georgia, Tennessee, and nationwide travel.</p>", priority="0.88"),
    page("mahjong-101.html", "Mahjong 101 — Beginner Lesson | $125/person", "Mahjong 101 beginner lesson — tiles, NMJL card, Charleston, first full game. $125/person.", "mahjong 101, beginner mahjong class", "Mahjong 101", """<p>Complete beginner American mahjong — 2–3 hours, 4–8 players, <strong>$125/person</strong>. We bring tiles, tables, and the NMJL card.</p>
<h2>What You Learn</h2>
<ul><li>All 152 tiles and suits</li><li>Reading the NMJL card</li><li>The Charleston</li><li>Calling, jokers, and scoring</li><li>Your first full game</li></ul>
<p>Next step: <a href="mahjong-102.html">Mahjong 102</a> ($115/person).</p>""", schema={"@type": "Course", "name": "Mahjong 101", "offers": {"@type": "Offer", "price": "125", "priceCurrency": "USD"}}, priority="0.88"),
    page("mahjong-102.html", "Mahjong 102 — Advanced Strategy | $115/person", "Mahjong 102 — strategy, Siamese & Patio play, tournament prep. $115/person.", "mahjong 102, advanced mahjong", "Mahjong 102", "<p>Advanced strategy after Mahjong 101. Siamese, Patio, tournament etiquette. <strong>$115/person</strong>.</p>", schema={"@type": "Course", "name": "Mahjong 102", "offers": {"@type": "Offer", "price": "115", "priceCurrency": "USD"}}, priority="0.85"),
    page("book-mahjong-lesson.html", "Book a Mahjong Lesson", "Book Mahjong 101 ($125) or 102 ($115). Email lookoutmountainmahjong@gmail.com · (919) 247-3392.", "book mahjong lesson, schedule mahjong class", "Book a Mahjong Lesson", """<p><a href="mahjong-101.html">Mahjong 101</a> — $125/person · <a href="mahjong-102.html">Mahjong 102</a> — $115/person</p>
<p>Email: lookoutmountainmahjong@gmail.com · Phone: (919) 247-3392</p>
<p>Private events: <a href="corporate-mahjong-events.html">corporate</a>, <a href="sorority-mahjong-parties.html">sorority</a>, <a href="girls-night-mahjong.html">girls night</a>, <a href="country-club-mahjong.html">country club</a>.</p>""", priority="0.9"),
    page("learn-american-mahjong.html", "Learn American Mahjong", "Learn American mahjong — tiles, NMJL card, jokers, Charleston. Lookout Mountain Mahjong.", "learn american mahjong, how to play american mahjong", "Learn American Mahjong", """<p>American mahjong differs from Chinese mahjong: 152 tiles, jokers, the annual <a href="nmjl-card.html">NMJL card</a>, and the <a href="mahjong-charleston.html">Charleston</a>.</p>
<p>Best way to learn: book <a href="mahjong-101.html">Mahjong 101</a> with a certified instructor.</p>""", priority="0.85"),
    page("beginner-mahjong.html", "Beginner Mahjong Lessons", "Beginner American mahjong — Mahjong 101 from $125/person.", "beginner mahjong, mahjong for beginners", "Beginner Mahjong", "<p>Never played? <a href=\"mahjong-101.html\">Mahjong 101</a> takes you from zero to your first game. Read <a href=\"how-to-play-mahjong.html\">how to play mahjong</a>.</p>"),
    page("how-to-play-mahjong.html", "How to Play Mahjong | American Mah Jongg", "How to play American mahjong — tiles, Charleston, NMJL card, four players. Lookout Mountain Mahjong.", "how to play mahjong, how to play mah jongg, mahjong rules for beginners", "How to Play American Mahjong", """<p>Four players, 152 tiles, the NMJL card, and hundreds of winning hands that change every year.</p>
<ol><li>Learn the tiles</li><li>Study the NMJL card</li><li>Pass tiles in the Charleston</li><li>Call tiles and use jokers</li><li>Declare mahjong!</li></ol>
<p>Fastest path: <a href="mahjong-101.html">Mahjong 101</a> with <a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a>.</p>""", priority="0.82"),
    page("mahjong-rules.html", "American Mahjong Rules", "American mahjong rules — NMJL, jokers, Charleston, scoring. Lookout Mountain Mahjong instructors.", "american mahjong rules, mah jongg rules, mahjong scoring rules", "American Mahjong Rules", "<p>Official American mah jongg follows the National Mah Jongg League (NMJL). We teach rules hands-on in <a href=\"mahjong-101.html\">Mahjong 101</a>. See <a href=\"mahjong-faq.html\">mahjong FAQ</a>.</p>"),
    page("mahjong-charleston.html", "The Charleston in American Mahjong", "What is the Charleston in mahjong? Passing tiles before play — American mah jongg.", "mahjong charleston, charleston mah jongg, what is charleston mahjong", "The Charleston in Mahjong", "<p>The Charleston is the tile-passing ritual unique to American mahjong — three rounds of passing before play begins. Learn it in <a href=\"mahjong-101.html\">Mahjong 101</a>.</p>"),
    page("mahjong-jokers.html", "Jokers in American Mahjong", "How jokers work in American mah jongg — wild tiles on the NMJL card.", "mahjong jokers, american mahjong jokers, joker rules mahjong", "Mahjong Jokers", "<p>Jokers are wild tiles in American mahjong — essential for many hands on the NMJL card. We cover jokers in every <a href=\"mahjong-101.html\">beginner lesson</a>.</p>"),
    page("nmjl-card.html", "NMJL Card | National Mah Jongg League", "The NMJL card — annual American mah jongg hands. Learn to read it with Lookout Mountain Mahjong.", "NMJL card, national mah jongg league card, mah jongg card", "The NMJL Card", "<p>The National Mah Jongg League publishes a new card each year with winning hand combinations. We provide cards at every lesson. Book <a href=\"mahjong-101.html\">Mahjong 101</a>.</p>"),
    page("mahjong-lessons-near-me.html", "Mahjong Lessons Near Me", "Mahjong lessons near you — GA, TN, NC, AL, nationwide travel.", "mahjong lessons near me, mahjong near me", "Mahjong Lessons Near Me", """<p>Based on Lookout Mountain, Georgia — we travel for private lessons and events.</p>
<ul>
<li><a href="chattanooga-mahjong.html">Chattanooga</a></li>
<li><a href="atlanta-mahjong.html">Atlanta</a></li>
<li><a href="nashville-mahjong.html">Nashville</a></li>
<li><a href="charlotte-mahjong.html">Charlotte</a></li>
<li><a href="raleigh-mahjong.html">Raleigh</a></li>
<li><a href="birmingham-mahjong.html">Birmingham</a></li>
<li><a href="savannah-mahjong.html">Savannah</a></li>
</ul>""", priority="0.88"),
    page("private-mahjong-lessons.html", "Private Mahjong Lessons", "Private mahjong at your home, club, or event — nationwide.", "private mahjong lessons, in home mahjong", "Private Mahjong Lessons", "<p>4–8 players · we bring tiles &amp; tables · <a href=\"mahjong-101.html\">Mahjong 101</a> $125/person</p>"),
    page("mahjong-tips.html", "American Mahjong Tips", "Mahjong tips — NMJL card, Charleston, jokers, strategy.", "mahjong tips, american mahjong tips", "Mahjong Tips", """<ol>
<li>Learn the NMJL card early</li>
<li>Pay attention during the Charleston</li>
<li>Use jokers on high-value hands</li>
<li>Play often — hands change every year</li>
<li>Book <a href="mahjong-101.html">Mahjong 101</a> for hands-on coaching</li>
</ol>"""),
    page("mahjong-tiles.html", "Mahjong Tiles | TML Pink Purple Green", "TML mahjong tiles — pink, purple, green. Code LOOKOUTMOUNTAIN.", "mahjong tiles, TML tiles, pink purple green mahjong", "Mahjong Tiles", "<p>Certified <a href=\"the-mahjong-line.html\">The Mahjong Line</a> ambassadors. Code: <strong>LOOKOUTMOUNTAIN</strong>.</p>"),
    page("the-mahjong-line.html", "The Mahjong Line | TML LOOKOUTMOUNTAIN", "The Mahjong Line tiles — TML Ambassador code LOOKOUTMOUNTAIN.", "the mahjong line, TML, mahjong line tiles", "The Mahjong Line", "<p>Premium American mahjong tiles. Referral: <strong>LOOKOUTMOUNTAIN</strong>. <a href=\"mahjong-tiles.html\">Tile guide</a>.</p>"),
    page("greenbrier-mahjong.html", "Greenbrier Mahjong | The Greenbrier Resort", "Greenbrier mahjong tournaments at The Greenbrier Resort, West Virginia.", "greenbrier mahjong, the greenbrier mahjong", "Greenbrier Mahjong", """<p>American mahjong at <strong>The Greenbrier Resort</strong>, White Sulphur Springs, WV — luxury tournaments and lessons with <a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a>.</p>
<p>Prepare with <a href="mahjong-102.html">Mahjong 102</a> · <a href="white-sulphur-springs-mahjong.html">White Sulphur Springs</a></p>""", priority="0.88"),
    page("white-sulphur-springs-mahjong.html", "White Sulphur Springs Mahjong | Greenbrier", "Mahjong at White Sulphur Springs and The Greenbrier, West Virginia.", "white sulphur springs mahjong, greenbrier wv mahjong", "White Sulphur Springs Mahjong", "<p>Home of <a href=\"greenbrier-mahjong.html\">The Greenbrier mahjong</a> tournaments.</p>"),
    page("west-virginia-mahjong.html", "West Virginia Mahjong", "West Virginia mahjong — The Greenbrier and statewide events.", "west virginia mahjong", "West Virginia Mahjong", "<p><a href=\"greenbrier-mahjong.html\">Greenbrier mahjong</a> · <a href=\"mahjong-tournament.html\">tournaments</a></p>"),
    city("chattanooga-mahjong.html", "Chattanooga & Lookout Mountain", "Chattanooga and Lookout Mountain mahjong lessons. TN & GA.", "chattanooga mahjong, lookout mountain mahjong", "Lookout Mountain, Georgia — minutes from Chattanooga, Tennessee. Home base for Mountain Mahjong.", "<p>Also: <a href=\"tennessee-mahjong.html\">Tennessee</a> · <a href=\"georgia-mahjong.html\">Georgia</a></p>"),
    city("atlanta-mahjong.html", "Atlanta", "Atlanta metro mahjong lessons and events.", "atlanta mahjong, mahjong atlanta", "Private lessons and events throughout the Atlanta metro.", "<p><a href=\"georgia-mahjong.html\">Georgia mahjong</a></p>"),
    city("georgia-mahjong.html", "Georgia", "Georgia mahjong lessons statewide.", "georgia mahjong", "Lookout Mountain home base · Atlanta · Savannah · statewide travel.", "<p><a href=\"atlanta-mahjong.html\">Atlanta</a> · <a href=\"savannah-mahjong.html\">Savannah</a> · <a href=\"chattanooga-mahjong.html\">Chattanooga area</a></p>"),
    city("tennessee-mahjong.html", "Tennessee", "Tennessee mahjong — Chattanooga, Nashville, Knoxville.", "tennessee mahjong", "TN-wide private lessons and events.", "<p><a href=\"nashville-mahjong.html\">Nashville</a> · <a href=\"knoxville-mahjong.html\">Knoxville</a> · <a href=\"memphis-mahjong.html\">Memphis</a></p>"),
    city("nashville-mahjong.html", "Nashville", "Nashville mahjong lessons.", "nashville mahjong", "Private mahjong parties and lessons in Nashville, TN."),
    city("knoxville-mahjong.html", "Knoxville", "Knoxville & East TN mahjong.", "knoxville mahjong", "East Tennessee events from Lookout Mountain Mahjong."),
    city("memphis-mahjong.html", "Memphis", "Memphis TN mahjong lessons.", "memphis mahjong", "We travel to Memphis for private lessons and corporate events.", "<p><a href=\"tennessee-mahjong.html\">Tennessee</a></p>"),
    city("charlotte-mahjong.html", "Charlotte", "Charlotte NC mahjong.", "charlotte mahjong", "Charlotte metro private and corporate mahjong."),
    city("raleigh-mahjong.html", "Raleigh", "Raleigh & Triangle NC mahjong.", "raleigh mahjong, north carolina mahjong", "Triangle area lessons.", "<p><a href=\"charlotte-mahjong.html\">Charlotte</a></p>"),
    city("birmingham-mahjong.html", "Birmingham", "Birmingham AL mahjong.", "birmingham mahjong, alabama mahjong", "Alabama statewide travel."),
    city("savannah-mahjong.html", "Savannah", "Savannah GA mahjong.", "savannah mahjong", "Coastal Georgia private lessons.", "<p><a href=\"georgia-mahjong.html\">Georgia</a></p>"),
    city("asheville-mahjong.html", "Asheville", "Asheville NC mahjong.", "asheville mahjong", "Western North Carolina events."),
    city("greenville-sc-mahjong.html", "Greenville SC", "Greenville South Carolina mahjong.", "greenville sc mahjong, greenville mahjong", "Upstate SC private lessons."),
    city("huntsville-mahjong.html", "Huntsville", "Huntsville AL mahjong.", "huntsville mahjong", "North Alabama mahjong events."),
    city("louisville-mahjong.html", "Louisville", "Louisville KY mahjong.", "louisville mahjong", "Kentucky private lessons and travel events."),
    page("marthas-vineyard-mahjong.html", "Martha's Vineyard Mahjong", "Martha's Vineyard destination mahjong lessons.", "martha's vineyard mahjong", "Martha&rsquo;s Vineyard Mahjong", "<p>Destination private lessons on Martha&rsquo;s Vineyard — vacation mahjong with Mahj Jen &amp; Mahj Hen.</p>"),
    page("corporate-mahjong-events.html", "Corporate Mahjong Team Building", "Corporate mahjong — screen-free team building.", "corporate mahjong, mahjong team building", "Corporate Mahjong", "<p>Offsites, retreats, and office events. We teach <a href=\"mahjong-101.html\">Mahjong 101</a> — no experience needed.</p>"),
    page("sorority-mahjong-parties.html", "Sorority Mahjong Parties", "Sorority mahjong — bid day, philanthropy, chapter events.", "sorority mahjong, greek life mahjong", "Sorority Mahjong Parties", "<p>Popular for bid day and philanthropy. See <a href=\"chi-o-mahjong.html\">Chi Omega mahjong</a> · <a href=\"bid-day-mahjong.html\">bid day</a>.</p>"),
    page("chi-o-mahjong.html", "Chi Omega Mahjong | Sorority Events", "Chi Omega and sorority mahjong parties with Lookout Mountain Mahjong.", "chi omega mahjong, chi o mahjong, sorority mahjong party", "Chi Omega Mahjong", "<p>Sorority events including Chi O — <a href=\"sorority-mahjong-parties.html\">sorority mahjong parties</a> nationwide.</p>"),
    page("bid-day-mahjong.html", "Bid Day Mahjong Party", "Bid day mahjong party for sororities — unique rush week programming.", "bid day mahjong, sorority bid day", "Bid Day Mahjong", "<p>Stand out during rush with a <a href=\"mahjong-101.html\">Mahjong 101</a> party. <a href=\"sorority-mahjong-parties.html\">Sorority events</a>.</p>"),
    page("girls-night-mahjong.html", "Girls Night Mahjong", "Girls night mahjong party — $125/person, 4–8 friends.", "girls night mahjong, mahjong party", "Girls Night Mahjong", "<p>Book <a href=\"mahjong-101.html\">Mahjong 101</a> — we bring pink, purple &amp; green <a href=\"mahjong-tiles.html\">TML tiles</a>.</p>"),
    page("mahjong-brunch.html", "Mahjong Brunch", "Mahjong brunch party — learn to play over brunch with friends.", "mahjong brunch, brunch mahjong party", "Mahjong Brunch", "<p>Combine brunch with <a href=\"mahjong-101.html\">Mahjong 101</a> — the social trend sweeping the South.</p>"),
    page("country-club-mahjong.html", "Country Club Mahjong", "Country club mahjong lessons and member tournaments.", "country club mahjong", "Country Club Mahjong", "<p>Member intro days and ladies' programming. <a href=\"private-mahjong-lessons.html\">Private club events</a>.</p>"),
    page("mahjong-club.html", "Start a Mahjong Club", "How to start a mahjong club — lessons and league kickoffs.", "mahjong club, start mahjong club, mahjong league", "Mahjong Club", "<p>We help groups launch mahjong clubs with <a href=\"mahjong-101.html\">101</a> and <a href=\"mahjong-102.html\">102</a> sessions.</p>"),
    page("mahjong-board-game.html", "Mahjong Board Game | American Mah Jongg", "Mahjong is the social board game trend — American mah jongg with friends.", "mahjong board game, mahjong game, social board games mahjong", "Mahjong — The Social Board Game", "<p>American mahjong is the screen-free social hit of the decade. Learn with <a href=\"mahj-jen-mahj-hen.html\">certified instructors</a>.</p>"),
    page("mahjong-tournament.html", "Mahjong Tournament", "Mahjong tournaments — Greenbrier and private mini-tournaments.", "mahjong tournament, mah jongg tournament", "Mahjong Tournament", "<p><a href=\"greenbrier-mahjong.html\">Greenbrier</a> resort tournaments · private mini-tournaments · <a href=\"mahjong-102.html\">102 prep</a>.</p>"),
    page("luxury-mahjong-retreat.html", "Luxury Mahjong Retreat", "Luxury mahjong retreats at The Greenbrier and destination venues.", "luxury mahjong, mahjong retreat, resort mahjong", "Luxury Mahjong Retreat", "<p>Resort mahjong at <a href=\"greenbrier-mahjong.html\">The Greenbrier</a> and <a href=\"marthas-vineyard-mahjong.html\">Martha&rsquo;s Vineyard</a>.</p>"),
    page("press.html", "Press | Lookout Mountain Mahjong", "Press contact — mahjong trend, Greenbrier, Mahj Jen & Mahj Hen.", "mahjong press, mahjong news", "Press &amp; Media", "<p>Jenn Kline &amp; Ann Henley Perry · lookoutmountainmahjong@gmail.com · (919) 247-3392 · @lookoutmountainmahjong</p>"),
    page("invite.html", "Invite Friends to Mahjong", "Invite friends to a mahjong lesson.", "invite friends mahjong", "Invite Friends to Mahjong", "<p>Book <a href=\"mahjong-101.html\">Mahjong 101</a> for your group — Mahj Jen &amp; Mahj Hen bring the tiles.</p>"),
    page("get-mahjn.html", "Get Mahj'n | Lookout Mountain Mahjong", "Get Mahj'n... It's Good For You!", "get mahjn, get mahj'n", "Get Mahj'n... It's Good For You", "<p>The viral American mahjong movement. <a href=\"mahj-jen-mahj-hen.html\">Mahj Jen &amp; Mahj Hen</a> · @lookoutmountainmahjong</p>"),
    page("a-bam-good-time.html", "A Bam Good Time | Mountain Mahjong", "A Bam Good Time — Lookout Mountain Mahjong brand.", "a bam good time, bam good time mahjong", "A Bam Good Time", "<p><em>A Bam Good Time</em> — American mahjong with <a href=\"mountain-mahjong.html\">Mountain Mahjong</a>.</p>"),
    page("mountain-mahjong.html", "Mountain Mahjong", "Mountain Mahjong with Mahj Jen and Mahj Hen.", "mountain mahjong", "Mountain Mahjong", "<p><a href=\"lookout-mountain-mahjong.html\">Lookout Mountain Mahjong</a> · TML Ambassadors · <a href=\"book-mahjong-lesson.html\">Book</a></p>"),
    page("american-mah-jongg.html", "American Mah Jongg Lessons", "American mah jongg lessons — NMJL, jokers, Charleston.", "american mah jongg, mah jongg lessons", "American Mah Jongg", "<p>Spelled mah jongg or mahjong — same great game. <a href=\"learn-american-mahjong.html\">Learn more</a>.</p>"),
    page("mahjong-instructor.html", "Mahjong Instructor", "Certified mahjong instructors — TML Ambassadors.", "mahjong instructor, mahjong teacher", "Mahjong Instructor", "<p><a href=\"mahj-jen-mahj-hen.html\">Mahj Jen &amp; Mahj Hen</a> — certified, nationwide travel.</p>"),
    page("mahjong-class.html", "Mahjong Class", "Mahjong class — 101 and 102.", "mahjong class, mahjong classes near me", "Mahjong Class", "<p><a href=\"mahjong-101.html\">101</a> $125 · <a href=\"mahjong-102.html\">102</a> $115</p>"),
    page("lookoutmountainmahjong.html", "@lookoutmountainmahjong", "Instagram & TikTok @lookoutmountainmahjong — mahjong community.", "lookoutmountainmahjong, instagram mahjong", "@lookoutmountainmahjong", "<p>Daily mahjong on Instagram &amp; TikTok. Lessons with <a href=\"mahj-jen-mahj-hen.html\">Mahj Jen &amp; Mahj Hen</a>.</p>"),
    page(
        "mahjong-faq.html",
        "Mahjong FAQ | American Mah Jongg Questions",
        "Frequently asked mahjong questions — pricing, rules, booking, beginners.",
        "mahjong faq, mahjong questions, american mahjong faq",
        "Mahjong FAQ",
        """<h2>How much are lessons?</h2><p>Mahjong 101 is $125/person. Mahjong 102 is $115/person. <a href="book-mahjong-lesson.html">Book here</a>.</p>
<h2>Do I need my own tiles?</h2><p>No — we bring tiles, tables, and NMJL cards.</p>
<h2>How many players?</h2><p>4–8 for Mahjong 101 (2–3 hours).</p>
<h2>Where do you teach?</h2><p>Lookout Mountain, GA and nationwide travel. <a href="mahjong-lessons-near-me.html">Near me</a>.</p>
<h2>Who teaches?</h2><p><a href="mahj-jen-mahj-hen.html">Mahj Jen (Jenn Kline) &amp; Mahj Hen (Ann Henley Perry)</a>, certified TML Ambassadors.</p>""",
        schema={
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": "How much are mahjong lessons?", "acceptedAnswer": {"@type": "Answer", "text": "Mahjong 101 is $125/person. Mahjong 102 is $115/person."}},
                {"@type": "Question", "name": "Do I need my own mahjong tiles?", "acceptedAnswer": {"@type": "Answer", "text": "No. We bring tiles, tables, and NMJL cards."}},
                {"@type": "Question", "name": "How many players for Mahjong 101?", "acceptedAnswer": {"@type": "Answer", "text": "4–8 players for a 2–3 hour lesson."}},
            ],
        },
        priority="0.8",
    ),
]


def build_schema(page: dict) -> dict:
    url = f"{BASE}/{page['file']}"
    graph = [ORG, {"@type": "WebPage", "@id": url, "url": url, "name": page["title"], "description": page["description"], "isPartOf": {"@id": f"{HOME}#website"}}]
    extra = page.get("schema")
    if extra:
        node = {"@context": "https://schema.org", **extra, "url": url}
        if node.get("@type") == "Course":
            node.setdefault("provider", {"@id": f"{HOME}#organization"})
        graph.append(node)
    return {"@context": "https://schema.org", "@graph": graph}


def render(page: dict) -> str:
    url = f"{BASE}/{page['file']}"
    schema_json = json.dumps(build_schema(page), indent=2)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page["title"]}</title>
    <meta name="description" content="{page["description"]}">
    <meta name="keywords" content="{page["keywords"]}">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{page["title"]}">
    <meta property="og:description" content="{page["description"]}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}/Hero.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{page["title"]}">
    <meta name="twitter:description" content="{page["description"]}">
    <meta name="twitter:image" content="{BASE}/Hero.png">
    <link rel="icon" href="/logo.png">
    <script type="application/ld+json">
{schema_json}
    </script>
    <link rel="stylesheet" href="/seo.css">
</head>
<body>
    <!-- Crawler-only SEO page — not linked from index.html, shop.html, or faq.html -->
    <article class="seo-page">
        <h1>{page["h1"]}</h1>
        {page["body"]}
        <p class="seo-home-link"><a href="{HOME}">Lookout Mountain Mahjong</a></p>
    </article>
</body>
</html>
"""


def write_sitemap(root: Path):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, freq, priority in PUBLIC_SITE:
        loc = HOME if not path else f"{BASE}/{path}"
        lines += ["  <url>", f"    <loc>{loc}</loc>", f"    <lastmod>{TODAY}</lastmod>", f"    <changefreq>{freq}</changefreq>", f"    <priority>{priority}</priority>", "  </url>"]
    for p in PAGES:
        lines += [
            "  <url>",
            f"    <loc>{BASE}/{p['file']}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{p.get('changefreq', 'monthly')}</changefreq>",
            f"    <priority>{p.get('priority', '0.72')}</priority>",
            "  </url>",
        ]
    lines += ["</urlset>", ""]
    (root / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def write_llms_txt(root: Path):
    urls = [f"- {HOME} (public home)", f"- {BASE}/shop.html (public shop)", f"- {BASE}/faq.html (public FAQ)", f"- {BASE}/sitemap.xml (all URLs)"]
    urls.append(f"- {BASE}/find-us.html (keyword index)")
    for p in sorted(PAGES, key=lambda x: x["file"]):
        if p["file"] not in ("find-us.html",):
            urls.append(f"- {BASE}/{p['file']}")
    text = f"""# Lookout Mountain Mahjong
# Crawler reference — public site is index, shop, FAQ only

> TML Ambassadors Mahj Jen (Jenn Kline) & Mahj Hen (Ann Henley Perry). American mahjong lessons, Greenbrier tournaments, nationwide travel.

## Public website (linked in navigation)
{chr(10).join(urls[:3])}

## Hidden SEO pages ({len(PAGES)} URLs — sitemap only, not in site nav)
{chr(10).join(urls[3:])}

## Contact
- Email: lookoutmountainmahjong@gmail.com
- Phone: +1-919-247-3392
- Instagram: https://www.instagram.com/lookoutmountainmahjong/
- TML code: LOOKOUTMOUNTAIN

## Topics
mahjong, american mah jongg, mahjong lessons near me, greenbrier mahjong, mahj jen, mahj hen, mountain mahjong, get mahjn, chattanooga atlanta nashville charlotte mahjong
"""
    (root / "llms.txt").write_text(text, encoding="utf-8")


def main():
    root = Path(__file__).parent
    for p in PAGES:
        (root / p["file"]).write_text(render(p), encoding="utf-8")
    write_sitemap(root)
    write_llms_txt(root)
    print(f"Generated {len(PAGES)} hidden SEO pages, sitemap.xml, llms.txt")


if __name__ == "__main__":
    main()
