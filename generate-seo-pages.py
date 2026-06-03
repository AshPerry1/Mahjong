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
    "slogan": "Get Mahj'n... It's Good For You",
    "description": "A Bam Good Time — certified TML Ambassadors teaching American mahjong nationwide.",
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


def mahjong_kw(file: str, suffix: str, desc: str, extra_kw: str, h1: str, body: str, **extra) -> dict:
    """Page optimized for 'mahjong' + suffix searches."""
    title = f"Mahjong {suffix} | Lookout Mountain Mahjong"
    keywords = f"mahjong, mahjong {suffix.lower()}, mah jongg, american mahjong, {extra_kw}"
    return page(file, title, desc, keywords, h1, body, **extra)


PAGES = [
    page(
        "mahjong.html",
        "Mahjong — Lessons, Events, Tiles & Instructors | Lookout Mountain Mahjong",
        "Mahjong lessons, Mahjong 101 & 102, private mahjong events, Greenbrier tournaments & TML tiles. Certified mahjong instructors Mahj Jen & Mahj Hen. Book American mahjong nationwide.",
        "mahjong, mah jongg, mahjong lessons, mahjong near me, american mahjong, learn mahjong, mahjong instructor, mahjong tiles, mahjong game",
        "Mahjong",
        """<p><strong>Mahjong</strong> is America's fastest-growing social tile game — and <strong>Lookout Mountain Mahjong</strong> is your home for <strong>American mahjong</strong> lessons, events, and tournaments nationwide.</p>
<p>Whether you searched <strong>mahjong</strong>, <strong>mah jongg</strong>, or <strong>mahjong near me</strong>, you found certified TML Ambassadors <a href="mahj-jen-mahj-hen.html">Mahj Jen (Jenn Kline)</a> and <a href="mahj-jen-mahj-hen.html">Mahj Hen (Ann Henley Perry)</a>. We teach <a href="mahjong-101.html">Mahjong 101</a> ($125/person) and <a href="mahjong-102.html">Mahjong 102</a> ($115/person) — tiles, tables, and NMJL cards included.</p>
<h2>Mahjong Lessons</h2>
<ul>
<li><a href="mahjong-lessons.html">Mahjong lessons</a> — beginner to advanced</li>
<li><a href="mahjong-lessons-near-me.html">Mahjong lessons near me</a></li>
<li><a href="book-mahjong-lesson.html">Book mahjong</a></li>
<li><a href="private-mahjong-lessons.html">Private mahjong lessons</a></li>
<li><a href="mahjong-for-beginners.html">Mahjong for beginners</a></li>
<li><a href="hire-mahjong-instructor.html">Hire a mahjong instructor</a></li>
</ul>
<h2>Learn Mahjong</h2>
<ul>
<li><a href="what-is-mahjong.html">What is mahjong?</a></li>
<li><a href="how-to-play-mahjong.html">How to play mahjong</a></li>
<li><a href="learn-american-mahjong.html">Learn American mahjong</a></li>
<li><a href="american-mah-jongg.html">American mah jongg</a></li>
<li><a href="mahjong-rules.html">Mahjong rules</a></li>
<li><a href="mahjong-tips.html">Mahjong tips</a></li>
<li><a href="mahjong-faq.html">Mahjong FAQ</a></li>
</ul>
<h2>Mahjong Events</h2>
<ul>
<li><a href="mahjong-events.html">Mahjong events</a></li>
<li><a href="mahjong-party.html">Mahjong party</a></li>
<li><a href="greenbrier-mahjong.html">Greenbrier mahjong</a></li>
<li><a href="mahjong-tournament.html">Mahjong tournament</a></li>
<li><a href="corporate-mahjong-events.html">Corporate mahjong</a></li>
<li><a href="girls-night-mahjong.html">Girls night mahjong</a></li>
</ul>
<h2>Mahjong Tiles &amp; Gear</h2>
<ul>
<li><a href="mahjong-tiles.html">Mahjong tiles</a></li>
<li><a href="buy-mahjong-tiles.html">Buy mahjong tiles</a></li>
<li><a href="the-mahjong-line.html">The Mahjong Line</a> — code LOOKOUTMOUNTAIN</li>
</ul>
<h2>Mahjong Near You</h2>
<p><a href="mahjong-keyword-hub.html">Complete mahjong search index</a> · <a href="chattanooga-mahjong.html">Chattanooga</a> · <a href="atlanta-mahjong.html">Atlanta</a> · <a href="nashville-mahjong.html">Nashville</a> · <a href="georgia-mahjong.html">Georgia</a> · <a href="tennessee-mahjong.html">Tennessee</a> · nationwide travel</p>
<p>Follow mahjong daily: <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a> · <a href="get-mahjn.html">Get Mahj'n</a></p>""",
        priority="1.0",
        changefreq="weekly",
        schema={
            "@type": "ItemList",
            "name": "Lookout Mountain Mahjong — Mahjong Services",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Mahjong 101", "url": f"{BASE}/mahjong-101.html"},
                {"@type": "ListItem", "position": 2, "name": "Mahjong Lessons Near Me", "url": f"{BASE}/mahjong-lessons-near-me.html"},
                {"@type": "ListItem", "position": 3, "name": "Book Mahjong", "url": f"{BASE}/book-mahjong-lesson.html"},
                {"@type": "ListItem", "position": 4, "name": "Greenbrier Mahjong", "url": f"{BASE}/greenbrier-mahjong.html"},
                {"@type": "ListItem", "position": 5, "name": "Mahjong Tiles", "url": f"{BASE}/mahjong-tiles.html"},
            ],
        },
    ),
    mahjong_kw(
        "mahjong-keyword-hub.html",
        "Search Index — Every Mahjong Topic",
        "Complete mahjong search index — lessons, rules, events, tiles, cities, instructors. Everything mahjong at Lookout Mountain Mahjong.",
        "mahjong search, everything mahjong, mahjong guide",
        "Mahjong — Complete Search Index",
        """<p>Every <strong>mahjong</strong> topic in one place. Click what you searched for:</p>
<h2>Mahjong Core</h2>
<p><a href="mahjong.html">Mahjong home</a> · <a href="what-is-mahjong.html">What is mahjong</a> · <a href="play-mahjong.html">Play mahjong</a> · <a href="mahjong-game.html">Mahjong game</a> · <a href="mahjong-explained.html">Mahjong explained</a></p>
<h2>Mahjong Lessons</h2>
<p><a href="mahjong-lessons.html">Mahjong lessons</a> · <a href="mahjong-lessons-near-me.html">Near me</a> · <a href="teach-me-mahjong.html">Teach me mahjong</a> · <a href="mahjong-teacher.html">Mahjong teacher</a> · <a href="mahjong-coach.html">Mahjong coach</a> · <a href="mahjong-tutor.html">Mahjong tutor</a> · <a href="hire-mahjong-instructor.html">Hire instructor</a> · <a href="certified-mahjong-instructor.html">Certified instructor</a> · <a href="best-mahjong-lessons.html">Best lessons</a></p>
<h2>Mahjong Spelling Variants</h2>
<p><a href="american-mah-jongg.html">Mah jongg</a> · <a href="mah-jongg-lessons.html">Mah jongg lessons</a> · <a href="mahjongg-lessons.html">Mahjongg lessons</a> · <a href="majong-lessons.html">Majong lessons</a></p>
<h2>Mahjong Events &amp; Social</h2>
<p><a href="mahjong-events.html">Events</a> · <a href="mahjong-party.html">Party</a> · <a href="mahjong-night.html">Mahjong night</a> · <a href="local-mahjong.html">Local mahjong</a> · <a href="ladies-mahjong.html">Ladies mahjong</a></p>
<h2>Mahjong Strategy</h2>
<p><a href="mahjong-strategy.html">Strategy</a> · <a href="mahjong-scoring.html">Scoring</a> · <a href="mahjong-hands.html">Hands</a> · <a href="win-at-mahjong.html">Win at mahjong</a> · <a href="mahjong-102.html">Mahjong 102</a></p>
<h2>Mahjong Tiles</h2>
<p><a href="mahjong-tiles.html">Tiles</a> · <a href="buy-mahjong-tiles.html">Buy tiles</a> · <a href="mahjong-set.html">Mahjong set</a> · <a href="mahjong-accessories.html">Accessories</a></p>
<p><a href="find-us.html">Find us</a> · <a href="book-mahjong-lesson.html">Book mahjong now</a></p>""",
        priority="0.98",
        changefreq="weekly",
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
<p><a href="mahjong.html">★ Mahjong home</a> · <a href="mahjong-keyword-hub.html">Mahjong search index</a> · <a href="mahjong-101.html">Mahjong 101</a> · <a href="mahjong-102.html">Mahjong 102</a> · <a href="mahjong-lessons.html">Mahjong lessons</a> · <a href="book-mahjong-lesson.html">Book</a> · <a href="beginner-mahjong.html">Beginner</a> · <a href="private-mahjong-lessons.html">Private</a> · <a href="mahjong-lessons-near-me.html">Near me</a> · <a href="hire-mahjong-instructor.html">Hire instructor</a></p>
<h2>Learn &amp; Tips</h2>
<p><a href="learn-american-mahjong.html">Learn American mahjong</a> · <a href="american-mah-jongg.html">American mah jongg</a> · <a href="how-to-play-mahjong.html">How to play</a> · <a href="mahjong-rules.html">Rules</a> · <a href="mahjong-charleston.html">Charleston</a> · <a href="mahjong-jokers.html">Jokers</a> · <a href="nmjl-card.html">NMJL card</a> · <a href="mahjong-tips.html">Tips</a> · <a href="mahjong-faq.html">FAQ</a></p>
<h2>Events</h2>
<p><a href="greenbrier-mahjong.html">Greenbrier</a> · <a href="corporate-mahjong-events.html">Corporate</a> · <a href="sorority-mahjong-parties.html">Sorority</a> · <a href="girls-night-mahjong.html">Girls night</a> · <a href="country-club-mahjong.html">Country club</a> · <a href="mahjong-tournament.html">Tournament</a> · <a href="marthas-vineyard-mahjong.html">Martha's Vineyard</a></p>
<h2>Tiles &amp; Shop</h2>
<p><a href="mahjong-tiles.html">Mahjong tiles</a> · <a href="the-mahjong-line.html">The Mahjong Line</a> · TML code <strong>LOOKOUTMOUNTAIN</strong></p>
<h2>Contact</h2>
<p>lookoutmountainmahjong@gmail.com · (919) 247-3392 · <a href="press.html">Press</a></p>
<h2>Viral &amp; Social</h2>
<p><a href="viral-mahjong-hub.html">★ Viral mahjong hub</a> · <a href="viral-share-pack.html">Share pack</a> · <a href="why-everyones-getting-mahjn.html">Why everyone's getting Mahj'n</a> · <a href="viral-mahjong.html">Viral mahjong</a> · <a href="share-mahjong.html">Share mahjong</a> · <a href="invite.html">Invite friends</a> · <a href="mahjong-captions.html">Captions</a> · <a href="mahjong-hashtags.html">Hashtags</a> · <a href="instagram-mahjong.html">Instagram</a> · <a href="tiktok-mahjong.html">TikTok</a> · <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a></p>""",
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
    page("mahjong-tips.html", "10 Mahjong Tips Everyone's Sharing", "10 viral American mahjong tips — Charleston, jokers, NMJL card, strategy. @lookoutmountainmahjong", "mahjong tips, viral mahjong tips, mahjong tricks, how to win mahjong", "10 Mahjong Tips Going Viral", """<p>Share these with your group chat — then book <a href="mahjong-101.html">Mahjong 101</a> with Mahj Jen &amp; Mahj Hen.</p>
<ol>
<li><strong>Learn the NMJL card first.</strong> American mah jongg hands change every year — skim the card before you play.</li>
<li><strong>Watch the Charleston.</strong> Three rounds of passing reveal what everyone is building.</li>
<li><strong>Save jokers for big hands.</strong> Don't waste wild tiles on cheap wins.</li>
<li><strong>Call strategically.</strong> Sometimes the best move is not to call.</li>
<li><strong>Defend when someone is hot.</strong> Discard safely when a player is one tile away.</li>
<li><strong>Play often.</strong> Muscle memory beats memorizing every hand.</li>
<li><strong>Host a lesson.</strong> <a href="girls-night-mahjong.html">Girls night mahjong</a> beats another dinner out.</li>
<li><strong>Get beautiful tiles.</strong> <a href="mahjong-tiles.html">TML pink, purple &amp; green</a> — code LOOKOUTMOUNTAIN.</li>
<li><strong>Follow @lookoutmountainmahjong.</strong> Daily tips on <a href="instagram-mahjong.html">Instagram</a>.</li>
<li><strong>Get Mahj'n.</strong> It's good for you. <a href="book-mahjong-lesson.html">Book a lesson</a>.</li>
</ol>
<p>More: <a href="share-mahjong.html">copy-paste texts to invite friends</a>.</p>""", priority="0.85", changefreq="weekly"),
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
    page("invite.html", "Invite Friends to Mahjong | Copy & Share", "Copy-paste mahjong invites for group chat, text & DM. Get Mahj'n with Lookout Mountain Mahjong.", "invite friends mahjong, mahjong party invite text, group chat mahjong", "Invite Friends to Get Mahj'n", """<p>Paste any message below into your group chat. Every path leads to <a href="book-mahjong-lesson.html">booking Mahjong 101</a>.</p>
<div class="viral-copy"><p class="viral-copy-label">Group chat classic</p><p>Who wants to learn mahjong?? 🀄 Mahj Jen &amp; Mahj Hen come teach us — tiles included. Get Mahj'n! lookoutmountainmahjong.com · @lookoutmountainmahjong</p></div>
<div class="viral-copy"><p class="viral-copy-label">Girls night pitch</p><p>Girls night idea: book a mahjong lesson instead of another dinner 🍷🀄 $125/person, 4–8 friends, they bring EVERYTHING.</p></div>
<div class="viral-copy"><p class="viral-copy-label">Greenbrier flex</p><p>These are the instructors who teach mahjong at THE GREENBRIER 🏔️🀄 We need to book Mahjong 101 ASAP.</p></div>
<div class="viral-copy"><p class="viral-copy-label">Instagram DM</p><p>Have you seen @lookoutmountainmahjong?? American mahjong — A Bam Good Time 🀄✨</p></div>
<div class="viral-copy"><p class="viral-copy-label">Short &amp; sweet</p><p>M is for Mahjong 🀄 @lookoutmountainmahjong</p></div>
<p>More viral copy: <a href="share-mahjong.html">share mahjong messages</a> · <a href="mahjong-tips.html">10 tips</a></p>""", priority="0.82", changefreq="weekly"),
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
    # ── Viral & trend pages ──
    page("why-everyones-getting-mahjn.html", "Why Everyone's Getting Mahj'n", "Why American mahjong is going viral — screen-free connection, Instagram, country clubs, The Greenbrier.", "why is mahjong popular, mahjong trend, mahjong viral 2026, everyone playing mahjong", "Why Everyone's Getting Mahj'n", """<p>American mahjong is the fastest-growing social board game in the South — and <a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a> are at the center of it on <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a>.</p>
<h2>Why Now?</h2>
<ul>
<li>Screen-free connection millennials &amp; Gen X crave</li>
<li>Beautiful <a href="pink-purple-green-mahjong.html">pink, purple &amp; green TML tiles</a></li>
<li>Perfect for <a href="girls-night-mahjong.html">girls night</a>, <a href="country-club-mahjong.html">country clubs</a>, and <a href="greenbrier-mahjong.html">luxury resorts</a></li>
<li>Easy to learn in one afternoon — <a href="mahjong-101.html">Mahjong 101</a></li>
</ul>
<p><em>Get Mahj'n... It's Good For You.</em> · <a href="share-mahjong.html">Share with friends</a></p>""", priority="0.88", changefreq="weekly"),
    page("viral-mahjong.html", "Viral Mahjong | The Trend Taking Over", "Viral mahjong on Instagram & TikTok — @lookoutmountainmahjong, Greenbrier, Mountain Mahjong.", "viral mahjong, mahjong tiktok, mahjong instagram trend", "Viral Mahjong", """<p>From Lookout Mountain to The Greenbrier — American mahjong is everywhere. Follow the viral story at <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a>.</p>
<p><a href="why-everyones-getting-mahjn.html">Why it's trending</a> · <a href="mahjong-tips.html">10 tips</a> · <a href="press.html">Press</a></p>""", priority="0.86", changefreq="weekly"),
    page("share-mahjong.html", "Share Mahjong | Group Chat Messages", "Copy-paste mahjong messages to share with friends. Get Mahj'n — Lookout Mountain Mahjong.", "share mahjong, mahjong group text, text friends mahjong", "Share Mahjong With Everyone You Know", """<p>American mahjong spreads by word of mouth. Copy any message:</p>
<div class="viral-copy"><p class="viral-copy-label">Text your neighbor</p><p>OK hear me out — what if we learned mahjong instead of book club this month? 🀄 There's a duo called Mahj Jen &amp; Mahj Hen who come teach you. $125/person.</p></div>
<div class="viral-copy"><p class="viral-copy-label">Work group</p><p>Team offsite idea that isn't another trust fall: mahjong lessons 🀄 Screen-free, actually fun, they bring the tiles.</p></div>
<div class="viral-copy"><p class="viral-copy-label">Family group</p><p>Mom wants mahjong lessons for her birthday — who's in? 4–8 people, they teach you the whole game in one afternoon.</p></div>
<div class="viral-copy"><p class="viral-copy-label">Social share line</p><p>Get Mahj'n... It's Good For You! 🀄 @lookoutmountainmahjong · Mountain Mahjong · A Bam Good Time</p></div>
<div class="viral-copy"><p class="viral-copy-label">Bachelorette pitch</p><p>Bach party idea that's NOT a bar crawl: hire mahjong instructors for the Airbnb 🀄✨ Classy, fun, everyone learns something.</p></div>
<div class="viral-copy"><p class="viral-copy-label">Lake house weekend</p><p>Lake house weekend agenda: Sat morning mahjong lesson on the dock 🀄☀️ Who's in for $125?</p></div>
<div class="viral-copy"><p class="viral-copy-label">Pickleball crossover</p><p>We did pickleball. Now we're doing mahjong. Same energy, better tiles 🀄</p></div>
<p>Full pack: <a href="viral-share-pack.html">viral share pack</a> · <a href="mahjong-captions.html">captions</a> · <a href="book-mahjong-lesson.html">Book</a></p>""", priority="0.84", changefreq="weekly"),
    page("instagram-mahjong.html", "Instagram Mahjong | @lookoutmountainmahjong", "Instagram mahjong — daily tips, tiles, Greenbrier, Get Mahj'n. Follow @lookoutmountainmahjong.", "instagram mahjong, mahjong instagram, lookoutmountainmahjong instagram", "Instagram Mahjong", "<p>Daily American mahjong on Instagram: tips, TML tiles, behind-the-scenes, and <em>A Bam Good Time</em>. <a href=\"lookoutmountainmahjong.html\">@lookoutmountainmahjong</a> · also on <a href=\"tiktok-mahjong.html\">TikTok</a>.</p>", priority="0.85"),
    page("tiktok-mahjong.html", "TikTok Mahjong | @lookoutmountainmahjong", "TikTok mahjong — viral American mah jongg content from Mountain Mahjong.", "tiktok mahjong, mahjong tiktok viral", "TikTok Mahjong", "<p>Follow <a href=\"lookoutmountainmahjong.html\">@lookoutmountainmahjong</a> on TikTok for mahjong tips, tiles &amp; event highlights.</p>"),
    page("pink-purple-green-mahjong.html", "Pink Purple Green Mahjong Tiles | TML", "Pink purple and green mahjong tiles from The Mahjong Line — the aesthetic driving the viral mahjong trend.", "pink purple green mahjong, aesthetic mahjong tiles, TML pink tiles", "Pink, Purple &amp; Green Mahjong", "<p>The tile aesthetic behind the viral mahjong movement. TML Ambassador code: <strong>LOOKOUTMOUNTAIN</strong>. <a href=\"the-mahjong-line.html\">The Mahjong Line</a> · <a href=\"mahjong-tiles.html\">tiles guide</a>.</p>"),
    page("aqua-mat-mahjong.html", "Aqua Mat Mahjong | TML Accessories", "TML aqua mat and mahjong accessories — Lookout Mountain Mahjong ambassador picks.", "aqua mat mahjong, mahjong mat, TML accessories", "Aqua Mat &amp; Mahjong Accessories", "<p>Certified <a href=\"the-mahjong-line.html\">TML ambassadors</a> — tiles, mats, and accessories. Code <strong>LOOKOUTMOUNTAIN</strong>.</p>"),
    page("southern-mahjong.html", "Southern Mahjong | The South's Favorite Game", "Southern mahjong culture — Lookout Mountain to Greenbrier, girls night to country clubs.", "southern mahjong, mahjong south, southern ladies mahjong", "Southern Mahjong", "<p>Mahjong is the South's social superpower. We teach across GA, TN, NC, AL &amp; beyond. <a href=\"girls-night-mahjong.html\">Girls night</a> · <a href=\"greenbrier-mahjong.html\">Greenbrier</a>.</p>"),
    page("screen-free-game-night.html", "Screen-Free Game Night | Mahjong", "Screen-free game night idea — American mahjong beats another Netflix night.", "screen free game night, social board games, offline games friends", "Screen-Free Game Night", "<p>Put down the phones. Pick up the tiles. Book <a href=\"mahjong-101.html\">Mahjong 101</a> for your friend group.</p>"),
    page("millennial-mahjong.html", "Millennial Mahjong", "Why millennials love American mahjong — social, aesthetic, strategic.", "millennial mahjong, gen y mahjong", "Millennial Mahjong", "<p>Millennials are driving the mahjong revival. Learn in one afternoon: <a href=\"beginner-mahjong.html\">beginner mahjong</a>.</p>"),
    page("empty-nester-mahjong.html", "Empty Nester Mahjong", "Empty nesters discovering American mahjong — new hobby, new friends.", "empty nester mahjong, retirement hobby mahjong", "Empty Nester Mahjong", "<p>The kids are gone — time to Get Mahj'n. <a href=\"mahjong-101.html\">Mahjong 101</a> is the perfect new chapter.</p>"),
    page("mother-daughter-mahjong.html", "Mother Daughter Mahjong", "Mother-daughter mahjong lessons — bond over tiles.", "mother daughter mahjong, mahjong with mom", "Mother-Daughter Mahjong", "<p>Book a private <a href=\"mahjong-101.html\">Mahjong 101</a> for mothers and daughters — a memory you'll replay forever.</p>"),
    page("vacation-mahjong.html", "Vacation Mahjong | Destination Lessons", "Vacation mahjong — Martha's Vineyard, beach houses, and destination events.", "vacation mahjong, beach mahjong, destination mahjong", "Vacation Mahjong", "<p>We travel to you: <a href=\"marthas-vineyard-mahjong.html\">Martha's Vineyard</a>, beach weeks, and family reunions.</p>"),
    page("holiday-mahjong-party.html", "Holiday Mahjong Party", "Holiday mahjong party — Thanksgiving, Christmas, New Year's gathering idea.", "holiday mahjong party, christmas mahjong, thanksgiving mahjong", "Holiday Mahjong Party", "<p>Skip the awkward small talk — teach the whole family mahjong. <a href=\"book-mahjong-lesson.html\">Book a holiday lesson</a>.</p>"),
    page("book-club-mahjong.html", "Book Club Mahjong | Switch It Up", "Book club bored? Try a mahjong lesson instead.", "book club mahjong, book club alternative", "Book Club Mahjong", "<p>When nobody finished the book — learn mahjong instead. <a href=\"girls-night-mahjong.html\">Girls night mahjong</a> $125/person.</p>"),
    page("charity-mahjong-event.html", "Charity Mahjong Event", "Charity mahjong fundraiser — philanthropy with tiles.", "charity mahjong, mahjong fundraiser, philanthropy mahjong", "Charity Mahjong Event", "<p>Philanthropy meets mahjong — popular with <a href=\"sorority-mahjong-parties.html\">sororities</a> and nonprofits. <a href=\"corporate-mahjong-events.html\">Corporate</a> too.</p>"),
    page("thread-and-ink-mahjong.html", "Thread & Ink Mahjong Apparel", "Thread & Ink mahjong apparel — tournament gear from Lookout Mountain Mahjong.", "thread and ink mahjong, mahjong apparel, mahjong shirt", "Thread &amp; Ink Mahjong", "<p>Mahjong apparel from the Lookout Mountain Mahjong shop. Visit the public shop at lookoutmountainmahjong.com/shop.html.</p>"),
    page("florida-mahjong.html", "Florida Mahjong Lessons", "Florida mahjong lessons — travel events and destination parties.", "florida mahjong, mahjong florida", "Florida Mahjong", "<p>We travel to Florida for private lessons, resorts, and seasonal events.</p>"),
    page("dallas-mahjong.html", "Dallas Mahjong Lessons", "Dallas Texas mahjong lessons and private events.", "dallas mahjong, mahjong dallas texas", "Dallas Mahjong", "<p>Dallas-Fort Worth private mahjong lessons — <a href=\"mahjong-lessons-near-me.html\">nationwide travel</a>.</p>"),
    page("charleston-sc-mahjong.html", "Charleston SC Mahjong", "Charleston South Carolina mahjong lessons.", "charleston sc mahjong, charleston south carolina mahjong", "Charleston, SC Mahjong", "<p>Lowcountry private lessons and events. <a href=\"southern-mahjong.html\">Southern mahjong</a>.</p>"),
    page("columbia-sc-mahjong.html", "Columbia SC Mahjong", "Columbia South Carolina mahjong lessons.", "columbia sc mahjong, columbia south carolina mahjong", "Columbia, SC Mahjong", "<p>South Carolina capital region events.</p>"),
    page("jacksonville-mahjong.html", "Jacksonville Mahjong", "Jacksonville FL mahjong lessons.", "jacksonville mahjong, mahjong jacksonville florida", "Jacksonville Mahjong", "<p>North Florida private mahjong events.</p>"),
    page("go-viral-mahjong.html", "Go Viral With Mahjong | Mountain Mahjong", "Go viral with American mahjong — Instagram, group chats, Greenbrier. Lookout Mountain Mahjong.", "go viral mahjong, mahjong social media", "Go Viral With Mahjong", """<p>The playbook: learn at <a href="mahjong-101.html">Mahjong 101</a> → post your tiles on Instagram → tag <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a> → invite friends with <a href="share-mahjong.html">share messages</a>.</p>
<p><a href="why-everyones-getting-mahjn.html">Why it's trending</a> · <a href="viral-mahjong.html">Viral mahjong</a> · <a href="get-mahjn.html">Get Mahj'n</a></p>""", priority="0.87", changefreq="weekly"),
    # ── More viral / lifestyle / share ──
    page("viral-share-pack.html", "Viral Mahjong Share Pack | Copy & Post", "Ultimate mahjong share pack — captions, texts, DMs & party pitches. @lookoutmountainmahjong", "viral mahjong share, mahjong captions, mahjong post ideas", "Viral Mahjong Share Pack", """<p>Everything to spread the mahjong gospel. Copy → paste → Get Mahj'n.</p>
<div class="viral-copy"><p class="viral-copy-label">Instagram caption</p><p>She got Mahj'n and never looked back 🀄✨ American mahjong with the best tiles, the best friends, and @lookoutmountainmahjong · #mahjong #getmahjn #americanmahjong #mountainmahjong</p></div>
<div class="viral-copy"><p class="viral-copy-label">Story sticker text</p><p>POV: you finally learned mahjong 🀄 link in bio</p></div>
<div class="viral-copy"><p class="viral-copy-label">WhatsApp</p><p>Ladies — mahjong lesson at my house? They bring ALL the tiles. $125 each, 6 of us, done in one afternoon. Who's in??</p></div>
<div class="viral-copy"><p class="viral-copy-label">Neighborhood group</p><p>Anyone want to learn mahjong as a cul-de-sac thing? Heard about Mahj Jen &amp; Mahj Hen — they travel and teach the whole game.</p></div>
<div class="viral-copy"><p class="viral-copy-label">TikTok hook</p><p>The tile game taking over your mom's group chat is American mahjong — and it's easier than you think 🀄</p></div>
<p><a href="mahjong-hashtags.html">Hashtags</a> · <a href="mahjong-captions.html">More captions</a> · <a href="share-mahjong.html">Share messages</a></p>""", priority="0.9", changefreq="weekly"),
    page("mahjong-captions.html", "Mahjong Instagram Captions", "50+ mahjong Instagram caption ideas — viral, funny, aesthetic. @lookoutmountainmahjong", "mahjong captions, mahjong instagram captions, funny mahjong captions", "Mahjong Captions for Instagram", """<ul>
<li>Get Mahj'n... It's Good For You 🀄</li>
<li>A Bam Good Time on and off the tiles</li>
<li>Currently accepting applications for my mahjong table</li>
<li>My personality is mahjong now</li>
<li>The Charleston changed me</li>
<li>Pink tiles, green envy 🀄💚</li>
<li>Booked the lesson. Learned the game. No regrets.</li>
<li>@lookoutmountainmahjong made me do it</li>
</ul>
<p>Full share pack: <a href="viral-share-pack.html">viral share pack</a></p>""", priority="0.85", changefreq="weekly"),
    page("mahjong-hashtags.html", "Mahjong Hashtags | Instagram & TikTok", "Best mahjong hashtags for Instagram and TikTok — go viral with American mah jongg.", "mahjong hashtags, mahjong tiktok hashtags, instagram mahjong hashtags", "Mahjong Hashtags", """<p><strong>Top hashtags:</strong> #mahjong #americanmahjong #mahjongg #getmahjn #mountainmahjong #lookoutmountainmahjong #mahjongtiles #tml #themahjongline #girlsnight #greenbrier #charleston #jokers #nmjl #boardgames #screenfree #southernliving</p>
<p>Tag <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a> — we repost the best tables.</p>""", priority="0.84"),
    page("trending-mahjong.html", "Trending Mahjong 2026", "Trending mahjong in 2026 — the social board game everyone's learning.", "trending mahjong, mahjong trend 2026, popular board games 2026", "Trending Mahjong", "<p>American mahjong is trending on Instagram, TikTok, and at luxury resorts. <a href=\"why-everyones-getting-mahjn.html\">Why everyone's getting Mahj'n</a>.</p>", priority="0.88", changefreq="weekly"),
    page("mahjong-aesthetic.html", "Mahjong Aesthetic | Pink Tiles & Tablescapes", "Mahjong aesthetic — pink purple green tiles, tablescapes, Instagram-worthy game nights.", "mahjong aesthetic, aesthetic mahjong, mahjong tablescape", "The Mahjong Aesthetic", "<p>The viral look: <a href=\"pink-purple-green-mahjong.html\">TML tiles</a>, linen napkins, champagne, and @lookoutmountainmahjong energy. <a href=\"girls-night-mahjong.html\">Host a night</a>.</p>"),
    page("quiet-luxury-mahjong.html", "Quiet Luxury Mahjong", "Quiet luxury mahjong — understated elegance, Greenbrier, country clubs.", "quiet luxury mahjong, old money mahjong, luxury mahjong", "Quiet Luxury Mahjong", "<p>No logos needed — just beautiful tiles and four friends. <a href=\"greenbrier-mahjong.html\">The Greenbrier</a> · <a href=\"country-club-mahjong.html\">country clubs</a>.</p>"),
    page("pickleball-and-mahjong.html", "Pickleball & Mahjong", "Done with pickleball? Try mahjong — the next social sport for your friend group.", "pickleball and mahjong, pickleball mahjong ladies", "Pickleball &amp; Mahjong", "<p>You've got the crew. You've got the driveway. Now get the tiles. <a href=\"mahjong-101.html\">Mahjong 101</a> for your pickleball group.</p>"),
    page("group-chat-mahjong.html", "Mahjong Group Chat", "Start a mahjong group chat — invite texts that actually get replies.", "mahjong group chat, start mahjong group", "Mahjong Group Chat", "<p>Drop this in the chat: <em>\"Who wants to learn mahjong?? 🀄 I found instructors who come to us — Mahj Jen &amp; Mahj Hen. $125/person.\"</em> More: <a href=\"viral-share-pack.html\">share pack</a>.</p>"),
    page("bridal-shower-mahjong.html", "Bridal Shower Mahjong", "Bridal shower mahjong party — unique shower idea.", "bridal shower mahjong, wedding shower mahjong", "Bridal Shower Mahjong", "<p>Skip the awkward games — teach the whole bridal party mahjong. <a href=\"girls-night-mahjong.html\">Private lesson</a> at the shower venue.</p>"),
    page("bachelorette-mahjong.html", "Bachelorette Party Mahjong", "Bachelorette mahjong party — classy alternative to bar crawls.", "bachelorette mahjong, bach party mahjong", "Bachelorette Mahjong Party", "<p>Classy. Memorable. Actually fun. Book <a href=\"mahjong-101.html\">Mahjong 101</a> for the bach weekend.</p>"),
    page("lake-house-mahjong.html", "Lake House Mahjong", "Lake house mahjong weekend — learn to play at the lake.", "lake house mahjong, lake weekend mahjong", "Lake House Mahjong", "<p>Lake weekends + mahjong = the perfect summer. We travel to your rental. <a href=\"vacation-mahjong.html\">Vacation mahjong</a>.</p>"),
    page("beach-house-mahjong.html", "Beach House Mahjong", "Beach house mahjong — coastal vacation activity.", "beach house mahjong, beach vacation mahjong", "Beach House Mahjong", "<p>Rainy beach day solved: mahjong lesson indoors. <a href=\"marthas-vineyard-mahjong.html\">Martha's Vineyard</a> · Florida · coast nationwide.</p>"),
    page("palm-beach-mahjong.html", "Palm Beach Mahjong", "Palm Beach Florida mahjong lessons and events.", "palm beach mahjong, mahjong palm beach florida", "Palm Beach Mahjong", "<p>Palm Beach private lessons and charity events. <a href=\"florida-mahjong.html\">Florida mahjong</a>.</p>"),
    page("naples-florida-mahjong.html", "Naples Florida Mahjong", "Naples FL mahjong — seasonal lessons and snowbird events.", "naples florida mahjong, naples mahjong", "Naples, Florida Mahjong", "<p>Southwest Florida snowbird season mahjong. <a href=\"florida-mahjong.html\">Florida</a>.</p>"),
    page("snowbird-mahjong.html", "Snowbird Mahjong", "Snowbird mahjong — Florida & Arizona seasonal mahjong groups.", "snowbird mahjong, winter mahjong florida", "Snowbird Mahjong", "<p>Seasonal residents — start your mahjong circle. We travel to FL, AZ &amp; coastal communities.</p>"),
    page("ladies-luncheon-mahjong.html", "Ladies Luncheon Mahjong", "Ladies luncheon mahjong — country club & garden club programming.", "ladies luncheon mahjong, luncheon and mahjong", "Ladies Luncheon Mahjong", "<p>Lunch + mahjong lesson = the ultimate ladies day. <a href=\"country-club-mahjong.html\">Country club</a> · <a href=\"junior-league-mahjong.html\">Junior League</a>.</p>"),
    page("junior-league-mahjong.html", "Junior League Mahjong", "Junior League mahjong fundraiser and social events.", "junior league mahjong, jl mahjong event", "Junior League Mahjong", "<p>Philanthropy + mahjong = sold-out events. <a href=\"charity-mahjong-event.html\">Charity mahjong</a>.</p>"),
    page("neighborhood-mahjong.html", "Neighborhood Mahjong Club", "Start a neighborhood mahjong club — we kickstart your group.", "neighborhood mahjong, cul de sac mahjong, street mahjong club", "Neighborhood Mahjong", "<p>One neighbor books <a href=\"mahjong-101.html\">Mahjong 101</a> — suddenly the whole street is playing. <a href=\"mahjong-club.html\">Start a club</a>.</p>"),
    page("best-friends-mahjong.html", "Best Friends Mahjong Trip", "Best friends mahjong weekend — trip idea with tiles.", "best friends mahjong, friends trip mahjong", "Best Friends Mahjong", "<p>Skip the spa — learn mahjong together. <a href=\"vacation-mahjong.html\">Destination lessons</a> · <a href=\"girls-night-mahjong.html\">girls night</a>.</p>"),
    page("retirement-mahjong-party.html", "Retirement Mahjong Party", "Retirement party mahjong — unique retirement celebration idea.", "retirement mahjong party, retirement mahjong gift", "Retirement Mahjong Party", "<p>Retire into mahjong. Book a lesson for the retirement party — they'll thank you forever.</p>"),
    page("50th-birthday-mahjong.html", "50th Birthday Mahjong Party", "50th birthday mahjong — milestone celebration with tiles.", "50th birthday mahjong, milestone birthday mahjong", "50th Birthday Mahjong", "<p>The milestone birthday that doesn't feel old — it feels fun. <a href=\"book-mahjong-lesson.html\">Book</a>.</p>"),
    page("mahjong-reels.html", "Mahjong Reels Ideas | Instagram & TikTok", "Mahjong reel ideas for Instagram and TikTok — go viral.", "mahjong reels, mahjong tiktok ideas, mahjong video ideas", "Mahjong Reel Ideas", """<ul>
<li>Tile reveal — pink, purple, green TML unboxing</li>
<li>Charleston explained in 30 seconds</li>
<li>POV: first time calling mahjong</li>
<li>Greenbrier tournament B-roll</li>
<li>Tag @lookoutmountainmahjong</li>
</ul>""", priority="0.83"),
    page("mahjong-meme.html", "Mahjong Memes & Funny Captions", "Funny mahjong memes and captions for group chat.", "mahjong meme, funny mahjong, mahjong jokes", "Mahjong Memes", """<ul>
<li>I'm not addicted to mahjong, I can stop anytime I want (after this hand)</li>
<li>The Charleston is just speed dating for tiles</li>
<li>My bank account vs my TML tile addiction</li>
<li>Sorry I'm late, I had mahjong</li>
</ul>
<p>Share: <a href="viral-share-pack.html">viral share pack</a></p>"""),
    page("richmond-mahjong.html", "Richmond VA Mahjong", "Richmond Virginia mahjong lessons.", "richmond mahjong, mahjong richmond va", "Richmond Mahjong", "<p>Richmond metro private lessons. <a href=\"mahjong-lessons-near-me.html\">Near me</a>.</p>"),
    page("wilmington-nc-mahjong.html", "Wilmington NC Mahjong", "Wilmington North Carolina mahjong.", "wilmington nc mahjong, wilmington mahjong", "Wilmington, NC Mahjong", "<p>Coastal NC private events.</p>"),
    page("austin-mahjong.html", "Austin Texas Mahjong", "Austin TX mahjong lessons and events.", "austin mahjong, mahjong austin texas", "Austin Mahjong", "<p>Austin private lessons — we travel Texas-wide from nationwide routing.</p>"),
    page("houston-mahjong.html", "Houston Mahjong Lessons", "Houston Texas mahjong private events.", "houston mahjong, mahjong houston", "Houston Mahjong", "<p>Houston metro mahjong parties and corporate events.</p>"),
    page("viral-mahjong-hub.html", "Viral Mahjong Hub | Everything Trending", "Master index of viral mahjong — share packs, captions, hashtags, trends. @lookoutmountainmahjong", "viral mahjong hub, mahjong viral index", "Viral Mahjong Hub", """<p><strong>Share &amp; spread:</strong> <a href="viral-share-pack.html">Share pack</a> · <a href="share-mahjong.html">Share messages</a> · <a href="invite.html">Invites</a> · <a href="mahjong-captions.html">Captions</a> · <a href="mahjong-hashtags.html">Hashtags</a> · <a href="mahjong-meme.html">Memes</a> · <a href="mahjong-reels.html">Reels</a></p>
<p><strong>Trend:</strong> <a href="why-everyones-getting-mahjn.html">Why everyone's getting Mahj'n</a> · <a href="trending-mahjong.html">Trending 2026</a> · <a href="viral-mahjong.html">Viral mahjong</a> · <a href="go-viral-mahjong.html">Go viral playbook</a></p>
<p><strong>Social:</strong> <a href="instagram-mahjong.html">Instagram</a> · <a href="tiktok-mahjong.html">TikTok</a> · <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a></p>
<p><strong>Book:</strong> <a href="book-mahjong-lesson.html">Book Mahjong 101</a> · <a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a></p>""", priority="0.92", changefreq="weekly"),
    # ── Mahjong keyword wave (pop for "mahjong" searches) ──
    mahjong_kw("mahjong-lessons.html", "Lessons", "Mahjong lessons for beginners and advanced players. Mahjong 101 $125, Mahjong 102 $115. We travel nationwide.", "mahjong lessons, mahjong classes, learn mahjong", "Mahjong Lessons", "<p>Professional <strong>mahjong lessons</strong> with certified TML Ambassadors. <a href=\"mahjong-101.html\">Mahjong 101</a> for beginners · <a href=\"mahjong-102.html\">102</a> for strategy · <a href=\"mahjong-lessons-near-me.html\">near me</a>.</p>", priority="0.97"),
    mahjong_kw("mahjong-events.html", "Events", "Mahjong events nationwide — corporate, sorority, country club, Greenbrier tournaments.", "mahjong events, mahjong event planning", "Mahjong Events", "<p>Private <strong>mahjong events</strong> for every occasion. <a href=\"corporate-mahjong-events.html\">Corporate</a> · <a href=\"sorority-mahjong-parties.html\">Sorority</a> · <a href=\"greenbrier-mahjong.html\">Greenbrier</a> · <a href=\"book-mahjong-lesson.html\">Book</a>.</p>", priority="0.92"),
    mahjong_kw("mahjong-party.html", "Party", "Book a mahjong party — private lesson at your home. 4–8 guests, $125/person, tiles included.", "mahjong party, mahjong party ideas, host mahjong party", "Mahjong Party", "<p>The ultimate <strong>mahjong party</strong> — we bring tiles, teach the game, send everyone home obsessed. <a href=\"girls-night-mahjong.html\">Girls night</a> · <a href=\"invite.html\">Invite friends</a>.</p>", priority="0.93"),
    mahjong_kw("what-is-mahjong.html", "Explained — What Is It?", "What is mahjong? American mah jongg explained — tiles, rules, NMJL card, four players.", "what is mahjong, what is mah jongg, mahjong meaning", "What Is Mahjong?", "<p><strong>Mahjong</strong> (mah jongg) is a four-player tile game using 152 tiles and the annual NMJL card. American mahjong uses jokers and the Charleston. Learn in one lesson: <a href=\"mahjong-101.html\">Mahjong 101</a>.</p>", priority="0.94"),
    mahjong_kw("play-mahjong.html", "Play — Learn Today", "Play mahjong today — book Mahjong 101 and play your first full game this week.", "play mahjong, play mah jongg, start playing mahjong", "Play Mahjong", "<p>Ready to <strong>play mahjong</strong>? No experience needed. <a href=\"mahjong-101.html\">Mahjong 101</a> takes you from zero to your first full game in one afternoon.</p>", priority="0.95"),
    mahjong_kw("mahjong-game.html", "Game — American Mah Jongg", "The mahjong game — American mah jongg rules, tiles, and how to win.", "mahjong game, mah jongg game, tile game mahjong", "The Mahjong Game", "<p>The <strong>mahjong game</strong> uses bams, cracks, dots, winds, dragons, flowers, and jokers. <a href=\"how-to-play-mahjong.html\">How to play</a> · <a href=\"mahjong-rules.html\">Rules</a>.</p>", priority="0.91"),
    mahjong_kw("mahjong-explained.html", "Explained for Beginners", "Mahjong explained simply — American mah jongg for first-timers.", "mahjong explained, mahjong for dummies, simple mahjong", "Mahjong Explained", "<p><strong>Mahjong explained</strong> in plain English. Book <a href=\"mahjong-101.html\">Mahjong 101</a> — we'll explain everything hands-on.</p>", priority="0.90"),
    mahjong_kw("teach-me-mahjong.html", "Teach Me", "Teach me mahjong — private Mahjong 101 lesson. Mahj Jen & Mahj Hen come to you.", "teach me mahjong, teach me mah jongg", "Teach Me Mahjong", "<p><em>Teach me mahjong!</em> — that's what <a href=\"mahjong-101.html\">Mahjong 101</a> is for. We bring tiles, you bring friends.</p>", priority="0.94"),
    mahjong_kw("mahjong-teacher.html", "Teacher", "Certified mahjong teacher — TML Ambassadors Mahj Jen & Mahj Hen.", "mahjong teacher, mahjong teachers near me", "Mahjong Teacher", "<p>Certified <strong>mahjong teachers</strong> — <a href=\"mahj-jen-mahj-hen.html\">Jenn Kline &amp; Ann Henley Perry</a>. <a href=\"book-mahjong-lesson.html\">Book</a>.</p>", priority="0.93"),
    mahjong_kw("mahjong-coach.html", "Coach", "Mahjong coach for strategy and tournament prep. Mahjong 102 $115/person.", "mahjong coach, mahjong coaching", "Mahjong Coach", "<p><strong>Mahjong coaching</strong> via <a href=\"mahjong-102.html\">Mahjong 102</a> — strategy, Siamese, tournament play.</p>", priority="0.88"),
    mahjong_kw("mahjong-tutor.html", "Tutor", "Private mahjong tutor — in-home lessons nationwide.", "mahjong tutor, private mahjong tutor", "Mahjong Tutor", "<p>Your private <strong>mahjong tutor</strong> comes to you. <a href=\"private-mahjong-lessons.html\">Private lessons</a> · <a href=\"mahjong-lessons-near-me.html\">Near me</a>.</p>", priority="0.90"),
    mahjong_kw("hire-mahjong-instructor.html", "Hire an Instructor", "Hire a mahjong instructor for your event, club, or home. Nationwide travel.", "hire mahjong instructor, hire mahjong teacher, mahjong instructor for hire", "Hire a Mahjong Instructor", "<p><strong>Hire a mahjong instructor</strong> — corporate, clubs, private homes, resorts. Email lookoutmountainmahjong@gmail.com · <a href=\"book-mahjong-lesson.html\">Book online</a>.</p>", priority="0.95"),
    mahjong_kw("certified-mahjong-instructor.html", "Certified Instructor", "Certified mahjong instructor — TML Ambassador certified. Mahj Jen & Mahj Hen.", "certified mahjong instructor, certified mah jongg teacher", "Certified Mahjong Instructor", "<p>Certified TML Ambassador <strong>mahjong instructors</strong>. <a href=\"mahj-jen-mahj-hen.html\">Meet the team</a>.</p>", priority="0.91"),
    mahjong_kw("best-mahjong-lessons.html", "Best Lessons", "Best mahjong lessons in the South — Lookout Mountain Mahjong, Greenbrier, nationwide.", "best mahjong lessons, best mahjong class", "Best Mahjong Lessons", "<p>Why we're among the <strong>best mahjong lessons</strong> — certified, traveled, Greenbrier-tested. <a href=\"mahjong-101.html\">Try Mahjong 101</a>.</p>", priority="0.92"),
    mahjong_kw("mahjong-for-beginners.html", "For Beginners", "Mahjong for beginners — Mahjong 101 from $125/person. No experience needed.", "mahjong for beginners, mahjong beginner class", "Mahjong for Beginners", "<p><strong>Mahjong for beginners</strong> starts with <a href=\"mahjong-101.html\">Mahjong 101</a>. Also: <a href=\"beginner-mahjong.html\">beginner guide</a> · <a href=\"what-is-mahjong.html\">what is mahjong</a>.</p>", priority="0.94"),
    mahjong_kw("american-mahjong-lessons.html", "American Mahjong Lessons", "American mahjong lessons — NMJL rules, certified instructors, nationwide.", "american mahjong lessons, american mah jongg lessons", "American Mahjong Lessons", "<p><strong>American mahjong lessons</strong> — not Chinese mahjong. We teach NMJL rules. <a href=\"learn-american-mahjong.html\">Learn more</a> · <a href=\"book-mahjong-lesson.html\">Book</a>.</p>", priority="0.96"),
    mahjong_kw("mah-jongg-lessons.html", "Mah Jongg Lessons", "Mah jongg lessons — spelled mah jongg, same great American tile game.", "mah jongg lessons, mah jongg classes, mah jongg near me", "Mah Jongg Lessons", "<p>Search <strong>mah jongg</strong>? Same game as mahjong. <a href=\"mahjong-lessons.html\">Mahjong lessons</a> · <a href=\"american-mah-jongg.html\">American mah jongg</a>.</p>", priority="0.95"),
    mahjong_kw("mahjongg-lessons.html", "Mahjongg Lessons", "Mahjongg lessons — learn American mahjongg with certified instructors.", "mahjongg lessons, mahjongg classes", "Mahjongg Lessons", "<p><strong>Mahjongg</strong> = mahjong = mah jongg. <a href=\"mahjong-101.html\">Book Mahjong 101</a> · <a href=\"mahjong-lessons-near-me.html\">Near me</a>.</p>", priority="0.88"),
    mahjong_kw("majong-lessons.html", "Majong Lessons", "Majong lessons — learn American mahjong (common spelling). Lookout Mountain Mahjong.", "majong lessons, majong classes, majong game", "Majong Lessons", "<p>Typed <strong>majong</strong>? You're in the right place. <a href=\"mahjong.html\">Mahjong lessons</a> with Mahj Jen &amp; Mahj Hen.</p>", priority="0.85"),
    mahjong_kw("mahjong-night.html", "Night — Host a Game Night", "Mahjong night — host the perfect game night at home.", "mahjong night, mah jongg night, game night mahjong", "Mahjong Night", "<p>Make it a <strong>mahjong night</strong> — book <a href=\"mahjong-101.html\">Mahjong 101</a> for your group. <a href=\"girls-night-mahjong.html\">Girls night</a> · <a href=\"neighborhood-mahjong.html\">Neighborhood</a>.</p>", priority="0.90"),
    mahjong_kw("local-mahjong.html", "Local — Find Lessons Near You", "Local mahjong lessons — Georgia, Tennessee, NC, AL, nationwide travel.", "local mahjong, local mah jongg, mahjong in my area", "Local Mahjong", "<p><strong>Local mahjong</strong> on Lookout Mountain + we travel. <a href=\"mahjong-lessons-near-me.html\">Lessons near me</a> · <a href=\"find-us.html\">All cities</a>.</p>", priority="0.92"),
    mahjong_kw("ladies-mahjong.html", "Ladies Mahjong", "Ladies mahjong groups — luncheons, clubs, and private lessons.", "ladies mahjong, women's mahjong, ladies mah jongg", "Ladies Mahjong", "<p><strong>Ladies mahjong</strong> is our specialty. <a href=\"ladies-luncheon-mahjong.html\">Luncheon</a> · <a href=\"country-club-mahjong.html\">Country club</a> · <a href=\"girls-night-mahjong.html\">Girls night</a>.</p>", priority="0.89"),
    mahjong_kw("mahjong-strategy.html", "Strategy", "Mahjong strategy — advanced tips, defensive play, hand selection.", "mahjong strategy, mah jongg strategy, win mahjong", "Mahjong Strategy", "<p>Level up your <strong>mahjong strategy</strong> with <a href=\"mahjong-102.html\">Mahjong 102</a>. <a href=\"mahjong-tips.html\">10 tips</a> · <a href=\"win-at-mahjong.html\">How to win</a>.</p>", priority="0.87"),
    mahjong_kw("mahjong-scoring.html", "Scoring", "Mahjong scoring in American mah jongg — how points work.", "mahjong scoring, mah jongg scoring, mahjong points", "Mahjong Scoring", "<p><strong>Mahjong scoring</strong> varies by hand on the NMJL card. We teach scoring in <a href=\"mahjong-101.html\">Mahjong 101</a>.</p>", priority="0.84"),
    mahjong_kw("mahjong-hands.html", "Hands — NMJL Card", "Mahjong hands on the NMJL card — winning combinations explained.", "mahjong hands, mah jongg hands, NMJL hands", "Mahjong Hands", "<p>Hundreds of <strong>mahjong hands</strong> on the annual NMJL card. Learn to read them: <a href=\"nmjl-card.html\">NMJL card guide</a> · <a href=\"mahjong-101.html\">101</a>.</p>", priority="0.86"),
    mahjong_kw("win-at-mahjong.html", "How to Win", "How to win at mahjong — strategy tips from certified instructors.", "how to win mahjong, win at mah jongg, mahjong winning tips", "How to Win at Mahjong", "<p>Want to <strong>win at mahjong</strong>? Start with fundamentals in <a href=\"mahjong-101.html\">101</a>, strategy in <a href=\"mahjong-102.html\">102</a>, tips in <a href=\"mahjong-tips.html\">10 tips</a>.</p>", priority="0.88"),
    mahjong_kw("buy-mahjong-tiles.html", "Buy Tiles", "Buy mahjong tiles — TML pink, purple, green. Ambassador code LOOKOUTMOUNTAIN.", "buy mahjong tiles, mahjong tiles for sale, best mahjong set", "Buy Mahjong Tiles", "<p><strong>Buy mahjong tiles</strong> from The Mahjong Line — code <strong>LOOKOUTMOUNTAIN</strong>. <a href=\"mahjong-tiles.html\">Tile guide</a> · <a href=\"the-mahjong-line.html\">TML</a>.</p>", priority="0.88"),
    mahjong_kw("mahjong-set.html", "Set — Tiles & Accessories", "Mahjong set — tiles, racks, cards, mats. TML ambassador recommendations.", "mahjong set, complete mahjong set, mah jongg set", "Mahjong Set", "<p>The perfect <strong>mahjong set</strong> starts with TML tiles. <a href=\"buy-mahjong-tiles.html\">Buy tiles</a> · code LOOKOUTMOUNTAIN.</p>", priority="0.87"),
    mahjong_kw("mahjong-accessories.html", "Accessories", "Mahjong accessories — mats, racks, cards, pushers. TML ambassador picks.", "mahjong accessories, mah jongg accessories, mahjong mat", "Mahjong Accessories", "<p><strong>Mahjong accessories</strong> including <a href=\"aqua-mat-mahjong.html\">aqua mats</a>. TML code LOOKOUTMOUNTAIN.</p>", priority="0.82"),
    mahjong_kw("mahjong-usa.html", "USA — Nationwide Lessons", "Mahjong USA — American mah jongg lessons nationwide from Lookout Mountain Mahjong.", "mahjong usa, mahjong united states, american mahjong usa", "Mahjong USA", "<p><strong>Mahjong</strong> is booming across the USA. We teach in GA, TN, NC, FL, TX &amp; travel nationwide. <a href=\"mahjong-lessons-near-me.html\">Near me</a>.</p>", priority="0.90"),
    mahjong_kw("mahjong-south.html", "South — Southern Mahjong", "Mahjong in the South — Georgia, Tennessee, Carolinas, Alabama, Florida.", "mahjong south, southern mah jongg, mahjong southeast", "Mahjong in the South", "<p><strong>Mahjong in the South</strong> — our home turf. <a href=\"southern-mahjong.html\">Southern mahjong</a> · <a href=\"georgia-mahjong.html\">Georgia</a> · <a href=\"tennessee-mahjong.html\">Tennessee</a>.</p>", priority="0.89"),
    mahjong_kw("mahjong-for-seniors.html", "For Seniors", "Mahjong for seniors — social, cognitive, fun. Beginner-friendly Mahjong 101.", "mahjong for seniors, senior mah jongg, retirement mahjong", "Mahjong for Seniors", "<p><strong>Mahjong for seniors</strong> — social connection and mental sharpness. Gentle, fun <a href=\"mahjong-101.html\">Mahjong 101</a> lessons.</p>", priority="0.86"),
    mahjong_kw("mahjong-learning.html", "Learning Center", "Mahjong learning — guides, lessons, tips, and classes.", "mahjong learning, learning mah jongg, mahjong education", "Mahjong Learning", "<p>Your <strong>mahjong learning</strong> hub: <a href=\"learn-american-mahjong.html\">Guide</a> · <a href=\"mahjong-101.html\">101</a> · <a href=\"mahjong-tips.html\">Tips</a> · <a href=\"mahjong-faq.html\">FAQ</a>.</p>", priority="0.91"),
    page(
        "mahjong-faq-extended.html",
        "Mahjong FAQ — 20 Common Questions",
        "Mahjong FAQ — pricing, rules, tiles, booking, beginners, Charleston, jokers, NMJL. Lookout Mountain Mahjong.",
        "mahjong faq, mahjong questions, mah jongg FAQ, mahjong help",
        "Mahjong FAQ — 20 Questions",
        """<h2>How much do mahjong lessons cost?</h2><p>Mahjong 101 is $125/person. Mahjong 102 is $115/person.</p>
<h2>What is American mahjong?</h2><p>Four players, 152 tiles, NMJL card, jokers, and the Charleston. <a href="what-is-mahjong.html">Full explanation</a>.</p>
<h2>Do I need my own mahjong tiles?</h2><p>No — we bring everything to every lesson.</p>
<h2>How long is a mahjong lesson?</h2><p>2–3 hours for Mahjong 101.</p>
<h2>How many people for mahjong?</h2><p>4–8 for lessons; 4 to play a standard game.</p>
<h2>Where do you teach mahjong?</h2><p>Lookout Mountain, GA + nationwide travel. <a href="mahjong-lessons-near-me.html">Cities</a>.</p>
<h2>Who are the mahjong instructors?</h2><p><a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a>, certified TML Ambassadors.</p>
<h2>Can you teach mahjong at my home?</h2><p>Yes — <a href="private-mahjong-lessons.html">private lessons</a> at your home, club, or venue.</p>
<h2>What mahjong tiles do you recommend?</h2><p>The Mahjong Line (TML) — code LOOKOUTMOUNTAIN. <a href="buy-mahjong-tiles.html">Buy tiles</a>.</p>
<h2>Do you host mahjong tournaments?</h2><p>Yes — <a href="greenbrier-mahjong.html">Greenbrier</a> and private events. <a href="mahjong-tournament.html">Tournaments</a>.</p>""",
        priority="0.90",
        schema={
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": "How much do mahjong lessons cost?", "acceptedAnswer": {"@type": "Answer", "text": "Mahjong 101 is $125/person. Mahjong 102 is $115/person."}},
                {"@type": "Question", "name": "What is American mahjong?", "acceptedAnswer": {"@type": "Answer", "text": "Four players, 152 tiles, the NMJL card, jokers, and the Charleston."}},
                {"@type": "Question", "name": "Do I need my own mahjong tiles?", "acceptedAnswer": {"@type": "Answer", "text": "No. Instructors bring tiles, tables, and NMJL cards."}},
                {"@type": "Question", "name": "Where do you teach mahjong?", "acceptedAnswer": {"@type": "Answer", "text": "Lookout Mountain, Georgia and nationwide travel."}},
                {"@type": "Question", "name": "Can you teach mahjong at my home?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Private lessons at homes, clubs, and venues."}},
            ],
        },
    ),
]


def build_schema(page: dict) -> dict:
    url = f"{BASE}/{page['file']}"
    graph = [ORG, {"@type": "WebPage", "@id": url, "url": url, "name": page["title"], "description": page["description"], "isPartOf": {"@id": f"{HOME}#website"}}]
    extra = page.get("schema")
    if extra:
        node = {**extra, "url": url}
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
    urls.append(f"- {BASE}/mahjong.html (primary mahjong keyword page)")
    urls.append(f"- {BASE}/mahjong-keyword-hub.html (mahjong search index)")
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
mahjong viral, get mahjn, a bam good time, instagram mahjong, tiktok mahjong, why everyone is getting mahjn, share mahjong, pink purple green tiles, greenbrier mahjong, mahj jen, mahj hen, southern mahjong, screen-free game night
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
