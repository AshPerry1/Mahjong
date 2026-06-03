#!/usr/bin/env python3
"""Generate minimal hidden SEO pages — not linked from the public site."""
from pathlib import Path

BASE = "https://lookoutmountainmahjong.com"
HOME = f"{BASE}/"

PAGES = [
    {
        "file": "mahjong.html",
        "title": "Mahjong | American Mahjong Lessons — Lookout Mountain Mahjong",
        "description": "American mahjong lessons, Mahjong 101 & 102, Greenbrier tournaments, and private events with certified TML Ambassadors Mahj Jen and Mahj Hen.",
        "keywords": "mahjong, american mahjong, mah jongg, mountain mahjong, lookout mountain mahjong",
        "h1": "American Mahjong — Lookout Mountain Mahjong",
        "body": """<p><strong>Lookout Mountain Mahjong</strong> teaches <strong>American mahjong</strong> (mah jongg) nationwide — beginner lessons, private parties, corporate events, and luxury resort tournaments including The Greenbrier.</p>
<p>Certified TML Ambassadors <strong>Jenn Kline (Mahj Jen)</strong> and <strong>Ann Henley Perry (Mahj Hen)</strong> offer Mahjong 101 ($125/person) and Mahjong 102 ($115/person). We bring tiles, tables, and the NMJL card.</p>
<ul>
<li><a href="learn-american-mahjong.html">Learn American Mahjong</a></li>
<li><a href="mahjong-101.html">Mahjong 101</a></li>
<li><a href="mahjong-lessons-near-me.html">Mahjong lessons near me</a></li>
<li><a href="greenbrier-mahjong.html">Greenbrier mahjong</a></li>
<li><a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a></li>
</ul>""",
        "schema": {"@type": "WebPage", "name": "Mahjong | Lookout Mountain Mahjong"},
    },
    {
        "file": "m.html",
        "title": "M — Mahjong | Lookout Mountain Mahjong",
        "description": "M is for Mahjong. Lookout Mountain Mahjong — American mahjong lessons with Mahj Jen & Mahj Hen. Get Mahj'n.",
        "keywords": "mahjong, m mahjong, mountain mahjong, get mahjn",
        "h1": "M is for Mahjong",
        "body": """<p><strong>Mountain Mahjong</strong> with Mahj Jen &amp; Mahj Hen. American mahjong lessons, Greenbrier events, TML tiles.</p>
<p><a href="mahjong.html">Everything mahjong</a> · <a href="book-mahjong-lesson.html">Book a lesson</a></p>""",
    },
    {
        "file": "find-us.html",
        "title": "Find Lookout Mountain Mahjong Online",
        "description": "How to find Lookout Mountain Mahjong: mahjong lessons, Mahj Jen, Mahj Hen, Greenbrier, Instagram @lookoutmountainmahjong.",
        "keywords": "find lookout mountain mahjong, mahj jen, mahj hen, lookoutmountainmahjong",
        "h1": "Find Lookout Mountain Mahjong",
        "body": """<p>Search terms: mahjong, american mahjong, mahjong lessons near me, greenbrier mahjong, chattanooga mahjong, atlanta mahjong, mahj jen, mahj hen, jen kline mahjong, ann henley perry, mountain mahjong, TML tiles, mahjong 101.</p>
<p>Contact: lookoutmountainmahjong@gmail.com · (919) 247-3392 · Instagram @lookoutmountainmahjong</p>""",
    },
    {
        "file": "mahj-jen-mahj-hen.html",
        "title": "Mahj Jen & Mahj Hen | Jenn Kline & Ann Henley Perry",
        "description": "Meet Mahj Jen (Jenn Kline) and Mahj Hen (Ann Henley Perry), certified TML Ambassadors and co-founders of Lookout Mountain Mahjong.",
        "keywords": "mahj jen, mahj hen, jen kline mahjong, ann henley perry mahjong",
        "h1": "Mahj Jen &amp; Mahj Hen",
        "body": """<p><strong>Jenn Kline (Mahj Jen)</strong> and <strong>Ann Henley Perry (Mahj Hen)</strong> teach American mahjong from Lookout Mountain, Georgia to The Greenbrier and nationwide private events.</p>
<p>Mahjong 101: $125/person. Mahjong 102: $115/person.</p>""",
        "schema": {"@type": "WebPage", "name": "Mahj Jen and Mahj Hen"},
    },
    {
        "file": "lookout-mountain-mahjong.html",
        "title": "Lookout Mountain Mahjong | Mountain Mahjong",
        "description": "Official Lookout Mountain Mahjong — American mahjong lessons on Lookout Mountain, Georgia. Mountain Mahjong with Mahj Jen & Mahj Hen.",
        "keywords": "lookout mountain mahjong, mountain mahjong, lookout mountain georgia mahjong",
        "h1": "Lookout Mountain Mahjong",
        "body": """<p><strong>Lookout Mountain Mahjong</strong> is <strong>Mountain Mahjong</strong> — certified TML Ambassadors teaching American mahjong in Georgia, Tennessee, and nationwide.</p>""",
    },
    {
        "file": "mahjong-101.html",
        "title": "Mahjong 101 — Beginner Lesson | $125/person",
        "description": "Mahjong 101 beginner American mahjong lesson. Tiles, NMJL card, Charleston, and your first full game. $125/person with Mahj Jen & Mahj Hen.",
        "keywords": "mahjong 101, beginner mahjong class, learn mahjong 101",
        "h1": "Mahjong 101",
        "body": """<p>Complete beginner lesson — 2–3 hours, 4–8 players, $125/person. We bring tiles, tables, and the NMJL card.</p>
<p>Continue with <a href="mahjong-102.html">Mahjong 102</a> ($115/person).</p>""",
        "schema": {
            "@type": "Course",
            "name": "Mahjong 101",
            "offers": {"@type": "Offer", "price": "125", "priceCurrency": "USD"},
        },
    },
    {
        "file": "mahjong-102.html",
        "title": "Mahjong 102 — Advanced Strategy | $115/person",
        "description": "Mahjong 102 advanced American mahjong strategy, Siamese and Patio play, tournament skills. $115/person.",
        "keywords": "mahjong 102, advanced mahjong, mahjong strategy",
        "h1": "Mahjong 102",
        "body": """<p>Advanced strategy for players who completed Mahjong 101. $115/person.</p>""",
        "schema": {
            "@type": "Course",
            "name": "Mahjong 102",
            "offers": {"@type": "Offer", "price": "115", "priceCurrency": "USD"},
        },
    },
    {
        "file": "book-mahjong-lesson.html",
        "title": "Book a Mahjong Lesson | Lookout Mountain Mahjong",
        "description": "Book Mahjong 101 ($125) or Mahjong 102 ($115) with Mahj Jen & Mahj Hen. Email lookoutmountainmahjong@gmail.com or call (919) 247-3392.",
        "keywords": "book mahjong lesson, schedule mahjong class",
        "h1": "Book a Mahjong Lesson",
        "body": """<p><a href="mahjong-101.html">Mahjong 101</a> — $125/person (beginners)</p>
<p><a href="mahjong-102.html">Mahjong 102</a> — $115/person (advanced)</p>
<p>Email: lookoutmountainmahjong@gmail.com · Phone: (919) 247-3392</p>""",
    },
    {
        "file": "learn-american-mahjong.html",
        "title": "Learn American Mahjong | Beginner Guide",
        "description": "Learn American mahjong — tiles, NMJL card, jokers, Charleston, and how it differs from Chinese mahjong. Lookout Mountain Mahjong.",
        "keywords": "learn american mahjong, how to play american mahjong, mah jongg rules",
        "h1": "Learn American Mahjong",
        "body": """<p>American mahjong uses 152 tiles, jokers, the annual NMJL card, and the Charleston. Four players, endlessly replayable.</p>
<p>Book <a href="mahjong-101.html">Mahjong 101</a> to learn in one afternoon.</p>""",
    },
    {
        "file": "beginner-mahjong.html",
        "title": "Beginner Mahjong Lessons",
        "description": "Never played mahjong? Beginner American mahjong lessons with Mahj Jen & Mahj Hen. Mahjong 101 from $125/person.",
        "keywords": "beginner mahjong, mahjong for beginners, first time mahjong",
        "h1": "Beginner Mahjong",
        "body": """<p>Start with <a href="mahjong-101.html">Mahjong 101</a> or read <a href="learn-american-mahjong.html">Learn American Mahjong</a>.</p>""",
    },
    {
        "file": "mahjong-lessons-near-me.html",
        "title": "Mahjong Lessons Near Me | Lookout Mountain Mahjong",
        "description": "Mahjong lessons near you — Georgia, Tennessee, North Carolina, nationwide travel. Mahj Jen & Mahj Hen come to your home or event.",
        "keywords": "mahjong lessons near me, mahjong near me, mahjong instructor near me",
        "h1": "Mahjong Lessons Near Me",
        "body": """<p>We teach on Lookout Mountain, GA and travel nationwide. Cities: <a href="chattanooga-mahjong.html">Chattanooga</a>, <a href="atlanta-mahjong.html">Atlanta</a>, <a href="nashville-mahjong.html">Nashville</a>, <a href="charlotte-mahjong.html">Charlotte</a>, <a href="knoxville-mahjong.html">Knoxville</a>.</p>""",
    },
    {
        "file": "private-mahjong-lessons.html",
        "title": "Private Mahjong Lessons",
        "description": "Private American mahjong lessons at your home, club, or event. Lookout Mountain Mahjong travels nationwide.",
        "keywords": "private mahjong lessons, in home mahjong lesson",
        "h1": "Private Mahjong Lessons",
        "body": """<p>We come to you with tiles, tables, and instruction. 4–8 players ideal for <a href="mahjong-101.html">Mahjong 101</a>.</p>""",
    },
    {
        "file": "mahjong-tips.html",
        "title": "American Mahjong Tips",
        "description": "Mahjong tips from Lookout Mountain Mahjong — tiles, Charleston, jokers, and strategy for American mah jongg.",
        "keywords": "mahjong tips, american mahjong tips, mahjong strategy tips",
        "h1": "Mahjong Tips",
        "body": """<p>American mahjong tips: learn the NMJL card, pay attention during the Charleston, use jokers wisely, and play often. Book <a href="mahjong-101.html">Mahjong 101</a> for hands-on instruction.</p>""",
    },
    {
        "file": "mahjong-tiles.html",
        "title": "Mahjong Tiles | TML Pink Purple Green",
        "description": "TML mahjong tiles — pink, purple, and green sets. Lookout Mountain Mahjong is a certified TML Ambassador. Code LOOKOUTMOUNTAIN.",
        "keywords": "mahjong tiles, TML tiles, the mahjong line, pink purple green mahjong",
        "h1": "Mahjong Tiles — TML",
        "body": """<p>Certified ambassadors for The Mahjong Line (TML). Referral code: <strong>LOOKOUTMOUNTAIN</strong>.</p>""",
    },
    {
        "file": "greenbrier-mahjong.html",
        "title": "Greenbrier Mahjong | The Greenbrier Resort",
        "description": "Greenbrier mahjong tournaments and lessons at The Greenbrier Resort, West Virginia. Lookout Mountain Mahjong with Mahj Jen & Mahj Hen.",
        "keywords": "greenbrier mahjong, the greenbrier mahjong, greenbrier resort mahjong",
        "h1": "Greenbrier Mahjong",
        "body": """<p>American mahjong at <strong>The Greenbrier Resort</strong> in White Sulphur Springs, West Virginia. See also <a href="west-virginia-mahjong.html">West Virginia mahjong</a>.</p>""",
    },
    {
        "file": "west-virginia-mahjong.html",
        "title": "West Virginia Mahjong | The Greenbrier",
        "description": "West Virginia mahjong at The Greenbrier Resort with Lookout Mountain Mahjong.",
        "keywords": "west virginia mahjong, greenbrier mahjong wv",
        "h1": "West Virginia Mahjong",
        "body": """<p><a href="greenbrier-mahjong.html">Greenbrier mahjong</a> tournaments and lessons.</p>""",
    },
    {
        "file": "chattanooga-mahjong.html",
        "title": "Chattanooga Mahjong Lessons",
        "description": "Chattanooga and Lookout Mountain mahjong lessons. American mahjong 101 & 102 in TN and GA.",
        "keywords": "chattanooga mahjong, mahjong chattanooga, lookout mountain mahjong",
        "h1": "Chattanooga &amp; Lookout Mountain Mahjong",
        "body": """<p>Based on Lookout Mountain, Georgia — minutes from Chattanooga, Tennessee. Mahjong 101 from $125/person.</p>""",
    },
    {
        "file": "atlanta-mahjong.html",
        "title": "Atlanta Mahjong Lessons",
        "description": "Atlanta metro mahjong lessons and private events with Lookout Mountain Mahjong.",
        "keywords": "atlanta mahjong, mahjong atlanta, mahjong lessons atlanta",
        "h1": "Atlanta Mahjong",
        "body": """<p>We travel to the Atlanta metro for private lessons and events. See <a href="georgia-mahjong.html">Georgia mahjong</a>.</p>""",
    },
    {
        "file": "georgia-mahjong.html",
        "title": "Georgia Mahjong Lessons",
        "description": "Georgia mahjong lessons — Lookout Mountain, Atlanta, and statewide. Lookout Mountain Mahjong.",
        "keywords": "georgia mahjong, mahjong georgia",
        "h1": "Georgia Mahjong",
        "body": """<p>Home base on Lookout Mountain, Georgia. <a href="atlanta-mahjong.html">Atlanta</a> · <a href="chattanooga-mahjong.html">Chattanooga area</a>.</p>""",
    },
    {
        "file": "tennessee-mahjong.html",
        "title": "Tennessee Mahjong Lessons",
        "description": "Tennessee mahjong lessons — Chattanooga, Nashville, Knoxville. Lookout Mountain Mahjong.",
        "keywords": "tennessee mahjong, mahjong tennessee",
        "h1": "Tennessee Mahjong",
        "body": """<p><a href="chattanooga-mahjong.html">Chattanooga</a> · <a href="nashville-mahjong.html">Nashville</a> · <a href="knoxville-mahjong.html">Knoxville</a>.</p>""",
    },
    {
        "file": "nashville-mahjong.html",
        "title": "Nashville Mahjong Lessons",
        "description": "Nashville mahjong lessons and private events with Mahj Jen & Mahj Hen.",
        "keywords": "nashville mahjong, mahjong nashville",
        "h1": "Nashville Mahjong",
        "body": """<p>Private mahjong lessons and events in Nashville, TN.</p>""",
    },
    {
        "file": "knoxville-mahjong.html",
        "title": "Knoxville Mahjong Lessons",
        "description": "Knoxville and East Tennessee mahjong lessons. Lookout Mountain Mahjong.",
        "keywords": "knoxville mahjong, east tennessee mahjong",
        "h1": "Knoxville Mahjong",
        "body": """<p>East Tennessee mahjong — we travel from Lookout Mountain.</p>""",
    },
    {
        "file": "charlotte-mahjong.html",
        "title": "Charlotte Mahjong Lessons",
        "description": "Charlotte NC mahjong lessons and private events. Lookout Mountain Mahjong travels nationwide.",
        "keywords": "charlotte mahjong, mahjong charlotte nc",
        "h1": "Charlotte Mahjong",
        "body": """<p>Charlotte metro private lessons and corporate events.</p>""",
    },
    {
        "file": "marthas-vineyard-mahjong.html",
        "title": "Martha's Vineyard Mahjong",
        "description": "Martha's Vineyard private mahjong lessons and destination events with Lookout Mountain Mahjong.",
        "keywords": "martha's vineyard mahjong, marthas vineyard mahjong",
        "h1": "Martha&rsquo;s Vineyard Mahjong",
        "body": """<p>Destination private mahjong lessons on Martha&rsquo;s Vineyard.</p>""",
    },
    {
        "file": "corporate-mahjong-events.html",
        "title": "Corporate Mahjong Events | Team Building",
        "description": "Corporate mahjong team building events with Lookout Mountain Mahjong. American mahjong for offices and retreats.",
        "keywords": "corporate mahjong, mahjong team building, office mahjong event",
        "h1": "Corporate Mahjong Events",
        "body": """<p>Screen-free team building that actually connects people. We bring tiles and teach Mahjong 101.</p>""",
    },
    {
        "file": "sorority-mahjong-parties.html",
        "title": "Sorority Mahjong Parties",
        "description": "Sorority mahjong parties — bid day, philanthropy, and girls' events with Lookout Mountain Mahjong.",
        "keywords": "sorority mahjong, sorority mahjong party, greek life mahjong",
        "h1": "Sorority Mahjong Parties",
        "body": """<p>Bid day, philanthropy nights, and chapter events. Popular with Chi Omega and sororities nationwide.</p>""",
    },
    {
        "file": "girls-night-mahjong.html",
        "title": "Girls Night Mahjong Party",
        "description": "Girls night mahjong party — private lesson at your home. $125/person, 4–8 friends. Lookout Mountain Mahjong.",
        "keywords": "girls night mahjong, mahjong party, ladies mahjong night",
        "h1": "Girls Night Mahjong",
        "body": """<p>Book <a href="mahjong-101.html">Mahjong 101</a> for your group — we bring everything.</p>""",
    },
    {
        "file": "country-club-mahjong.html",
        "title": "Country Club Mahjong Events",
        "description": "Country club mahjong lessons and member tournaments with Lookout Mountain Mahjong.",
        "keywords": "country club mahjong, club mahjong event",
        "h1": "Country Club Mahjong",
        "body": """<p>Member intro days, ladies' programming, and club tournaments.</p>""",
    },
    {
        "file": "press.html",
        "title": "Press | Lookout Mountain Mahjong — Mahj Jen & Mahj Hen",
        "description": "Press and media contact for Lookout Mountain Mahjong. Stories about American mahjong, The Greenbrier, and @lookoutmountainmahjong.",
        "keywords": "mahjong press, mahjong news, jen kline mahjong, ann henley perry",
        "h1": "Press &amp; Media",
        "body": """<p><strong>Mountain Mahjong</strong> — Jenn Kline (Mahj Jen) and Ann Henley Perry (Mahj Hen), certified TML Ambassadors. Lookout Mountain, GA · travels nationwide.</p>
<p>Media: lookoutmountainmahjong@gmail.com · (919) 247-3392 · @lookoutmountainmahjong</p>""",
    },
    {
        "file": "invite.html",
        "title": "Invite Friends to Mahjong",
        "description": "Invite friends to learn American mahjong with Lookout Mountain Mahjong. Mahjong 101 private lessons.",
        "keywords": "invite friends mahjong, mahjong party invite",
        "h1": "Invite Friends to Mahjong",
        "body": """<p>Who wants to learn mahjong? Book Mahjong 101 — Mahj Jen &amp; Mahj Hen bring the tiles. lookoutmountainmahjong.com</p>""",
    },
    {
        "file": "get-mahjn.html",
        "title": "Get Mahj'n | Lookout Mountain Mahjong",
        "description": "Get Mahj'n... It's Good For You! American mahjong lessons with Mahj Jen & Mahj Hen. Lookout Mountain Mahjong.",
        "keywords": "get mahjn, get mahj'n, mahjong trend, mountain mahjong",
        "h1": "Get Mahj'n... It's Good For You",
        "body": """<p>The viral American mahjong movement — lessons, tiles, and tournaments with <a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a>. Follow @lookoutmountainmahjong.</p>""",
    },
    {
        "file": "a-bam-good-time.html",
        "title": "A Bam Good Time | Lookout Mountain Mahjong",
        "description": "A Bam Good Time — American mahjong with Lookout Mountain Mahjong. Mahj Jen & Mahj Hen, TML Ambassadors.",
        "keywords": "a bam good time, bam good time mahjong, mountain mahjong",
        "h1": "A Bam Good Time",
        "body": """<p><strong>Lookout Mountain Mahjong</strong> — <em>A Bam Good Time</em> on and off the tiles. Book <a href="mahjong-101.html">Mahjong 101</a>.</p>""",
    },
    {
        "file": "mountain-mahjong.html",
        "title": "Mountain Mahjong | Jenn Kline & Ann Henley Perry",
        "description": "Mountain Mahjong with Mahj Jen and Mahj Hen. American mahjong lessons, Greenbrier tournaments, @lookoutmountainmahjong.",
        "keywords": "mountain mahjong, mountain mahjong lessons, lookout mountain mahjong",
        "h1": "Mountain Mahjong",
        "body": """<p><strong>Mountain Mahjong</strong> is Lookout Mountain Mahjong — <a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a>, certified TML Ambassadors based on Lookout Mountain, Georgia.</p>""",
    },
    {
        "file": "american-mah-jongg.html",
        "title": "American Mah Jongg Lessons",
        "description": "American mah jongg lessons with certified instructors. NMJL card, jokers, Charleston — Lookout Mountain Mahjong.",
        "keywords": "american mah jongg, mah jongg lessons, mah jongg near me, mahjong jongg",
        "h1": "American Mah Jongg",
        "body": """<p>American <strong>mah jongg</strong> (mahjong) with the annual NMJL card. Learn with <a href="learn-american-mahjong.html">our beginner guide</a> or book <a href="mahjong-101.html">Mahjong 101</a>.</p>""",
    },
    {
        "file": "mahjong-instructor.html",
        "title": "Mahjong Instructor | Certified TML Ambassadors",
        "description": "Certified mahjong instructors Mahj Jen & Mahj Hen. TML Ambassadors teaching American mahjong nationwide.",
        "keywords": "mahjong instructor, mahjong teacher, certified mahjong instructor",
        "h1": "Mahjong Instructor",
        "body": """<p>Certified TML Ambassador instructors — <a href="mahj-jen-mahj-hen.html">Jenn Kline &amp; Ann Henley Perry</a>. Private and group lessons.</p>""",
    },
    {
        "file": "mahjong-class.html",
        "title": "Mahjong Class | Mahjong 101 & 102",
        "description": "Mahjong class for beginners and advanced players. Mahjong 101 $125, Mahjong 102 $115. Lookout Mountain Mahjong.",
        "keywords": "mahjong class, mahjong classes near me, mahjong lesson class",
        "h1": "Mahjong Class",
        "body": """<p><a href="mahjong-101.html">Mahjong 101</a> for beginners · <a href="mahjong-102.html">Mahjong 102</a> for strategy. We bring tiles and tables.</p>""",
    },
    {
        "file": "mahjong-tournament.html",
        "title": "Mahjong Tournament | Greenbrier & Private Events",
        "description": "Mahjong tournaments at The Greenbrier and private mini-tournaments nationwide. Lookout Mountain Mahjong.",
        "keywords": "mahjong tournament, mah jongg tournament, greenbrier mahjong tournament",
        "h1": "Mahjong Tournament",
        "body": """<p>Tournament play at <a href="greenbrier-mahjong.html">The Greenbrier</a> and private mini-tournaments. Prepare with <a href="mahjong-102.html">Mahjong 102</a>.</p>""",
    },
    {
        "file": "lookoutmountainmahjong.html",
        "title": "@lookoutmountainmahjong | Instagram Mahjong",
        "description": "lookoutmountainmahjong — Instagram & TikTok mahjong community. American mahjong tips, tiles, and events.",
        "keywords": "lookoutmountainmahjong, instagram mahjong, tiktok mahjong, mahjong viral",
        "h1": "@lookoutmountainmahjong",
        "body": """<p>Follow on Instagram &amp; TikTok for daily mahjong content. American mahjong lessons with Mahj Jen &amp; Mahj Hen.</p>""",
    },
    {
        "file": "birmingham-mahjong.html",
        "title": "Birmingham Mahjong Lessons",
        "description": "Birmingham Alabama mahjong lessons and private events. Lookout Mountain Mahjong travels statewide.",
        "keywords": "birmingham mahjong, mahjong birmingham alabama, alabama mahjong",
        "h1": "Birmingham Mahjong",
        "body": """<p>Private mahjong lessons in Birmingham and across Alabama. <a href="mahjong-lessons-near-me.html">Lessons near me</a>.</p>""",
    },
    {
        "file": "raleigh-mahjong.html",
        "title": "Raleigh Mahjong Lessons",
        "description": "Raleigh NC mahjong lessons and private events with Lookout Mountain Mahjong.",
        "keywords": "raleigh mahjong, mahjong raleigh nc, north carolina mahjong",
        "h1": "Raleigh Mahjong",
        "body": """<p>Raleigh and Triangle area private lessons. Also see <a href="charlotte-mahjong.html">Charlotte mahjong</a>.</p>""",
    },
    {
        "file": "the-mahjong-line.html",
        "title": "The Mahjong Line | TML Ambassador LOOKOUTMOUNTAIN",
        "description": "The Mahjong Line TML tiles — pink, purple, green. Lookout Mountain Mahjong ambassador code LOOKOUTMOUNTAIN.",
        "keywords": "the mahjong line, TML tiles, mahjong line tiles, LOOKOUTMOUNTAIN code",
        "h1": "The Mahjong Line — TML Ambassador",
        "body": """<p>Certified TML Ambassadors. Referral code: <strong>LOOKOUTMOUNTAIN</strong>. See <a href="mahjong-tiles.html">mahjong tiles</a>.</p>""",
    },
]

# Main site pages (included in sitemap only — never generated by this script)
PUBLIC_SITE = [
    ("", "weekly", "1.0"),
    ("shop.html", "weekly", "0.9"),
    ("faq.html", "monthly", "0.8"),
]


def render(page: dict) -> str:
    slug = page["file"]
    url = f"{BASE}/{slug}"
    schema = page.get("schema")
    schema_block = ""
    if schema:
        import json

        data = {"@context": "https://schema.org", **schema, "url": url}
        if data.get("@type") == "Course":
            data.setdefault("provider", {"@type": "Organization", "name": "Lookout Mountain Mahjong", "url": HOME})
        schema_block = f'\n    <script type="application/ld+json">\n    {json.dumps(data, indent=2)}\n    </script>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page["title"]}</title>
    <meta name="description" content="{page["description"]}">
    <meta name="keywords" content="{page["keywords"]}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{url}">
    <meta property="og:title" content="{page["title"]}">
    <meta property="og:description" content="{page["description"]}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}/Hero.png">
    <link rel="icon" href="/logo.png">{schema_block}
    <link rel="stylesheet" href="/seo.css">
</head>
<body>
    <!-- Crawler-only SEO page — not linked from the public website -->
    <article class="seo-page">
        <h1>{page["h1"]}</h1>
        {page["body"]}
        <p class="seo-home-link"><a href="{HOME}">Lookout Mountain Mahjong</a></p>
    </article>
</body>
</html>
"""


def write_sitemap(root: Path):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, freq, priority in PUBLIC_SITE:
        loc = HOME if not path else f"{BASE}/{path}"
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    for page in PAGES:
        priority = page.get("priority", "0.75")
        freq = page.get("changefreq", "monthly")
        lines.append("  <url>")
        lines.append(f"    <loc>{BASE}/{page['file']}</loc>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    (root / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def main():
    root = Path(__file__).parent
    for page in PAGES:
        (root / page["file"]).write_text(render(page), encoding="utf-8")
    write_sitemap(root)
    print(f"Wrote {len(PAGES)} hidden SEO pages + sitemap.xml")


if __name__ == "__main__":
    main()
