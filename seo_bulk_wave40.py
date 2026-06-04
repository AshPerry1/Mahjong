# -*- coding: utf-8 -*-
"""Booking & Near Me Wave — lessons, private teachers, tournaments nationwide."""
from __future__ import annotations

from generate_bulk_city_data import STATE_META
from seo_bulk_wave40_booking_cities_data import WAVE40_BOOKING_CITIES
from seo_bulk_waves import _occasion, _rule

BOOKING_HUB = "mahjong-booking-near-me-hub.html"

STATE_SLUGS = {
    "AL": ("alabama", "Alabama"),
    "AK": ("alaska", "Alaska"),
    "AZ": ("arizona", "Arizona"),
    "AR": ("arkansas", "Arkansas"),
    "CA": ("california", "California"),
    "CO": ("colorado", "Colorado"),
    "CT": ("connecticut", "Connecticut"),
    "DE": ("delaware", "Delaware"),
    "FL": ("florida", "Florida"),
    "GA": ("georgia", "Georgia"),
    "HI": ("hawaii", "Hawaii"),
    "ID": ("idaho", "Idaho"),
    "IL": ("illinois", "Illinois"),
    "IN": ("indiana", "Indiana"),
    "IA": ("iowa", "Iowa"),
    "KS": ("kansas", "Kansas"),
    "KY": ("kentucky", "Kentucky"),
    "LA": ("louisiana", "Louisiana"),
    "ME": ("maine", "Maine"),
    "MD": ("maryland", "Maryland"),
    "MA": ("massachusetts", "Massachusetts"),
    "MI": ("michigan", "Michigan"),
    "MN": ("minnesota", "Minnesota"),
    "MS": ("mississippi", "Mississippi"),
    "MO": ("missouri", "Missouri"),
    "MT": ("montana", "Montana"),
    "NE": ("nebraska", "Nebraska"),
    "NV": ("nevada", "Nevada"),
    "NH": ("new-hampshire", "New Hampshire"),
    "NJ": ("new-jersey", "New Jersey"),
    "NM": ("new-mexico", "New Mexico"),
    "NY": ("new-york", "New York"),
    "NC": ("north-carolina", "North Carolina"),
    "ND": ("north-dakota", "North Dakota"),
    "OH": ("ohio", "Ohio"),
    "OK": ("oklahoma", "Oklahoma"),
    "OR": ("oregon", "Oregon"),
    "PA": ("pennsylvania", "Pennsylvania"),
    "RI": ("rhode-island", "Rhode Island"),
    "SC": ("south-carolina", "South Carolina"),
    "SD": ("south-dakota", "South Dakota"),
    "TN": ("tennessee", "Tennessee"),
    "TX": ("texas", "Texas"),
    "UT": ("utah", "Utah"),
    "VT": ("vermont", "Vermont"),
    "VA": ("virginia", "Virginia"),
    "WA": ("washington", "Washington"),
    "WV": ("west-virginia", "West Virginia"),
    "WI": ("wisconsin", "Wisconsin"),
    "WY": ("wyoming", "Wyoming"),
}


def _booking_city_page(mahjong_kw, row: tuple) -> dict:
    near_slug, label, st, state_page, city_page, state_near = row
    stem = near_slug.replace("-lessons-near-me.html", "")
    desc = (
        f"Book mahjong lessons near {label} — private teacher comes to you. "
        "Mahjong 101 $125 · nationwide travel · Lookout Mountain Mahjong."
    )
    body = (
        f"<p><strong>Mahjong lessons near {label}</strong> — certified TML Ambassadors "
        f"<a href=\"mahj-jen-mahj-hen.html\">Mahj Jen &amp; Mahj Hen</a> travel to your home, "
        "club, resort, or event. We bring tiles, tables, and NMJL cards.</p>"
        f'<p><a href="{city_page}">{label} mahjong</a> · '
        f'<a href="{state_near}">Lessons near me in {st}</a> · '
        f'<a href="{state_page}">{st} statewide</a></p>'
        f'<p class="seo-inline-cta"><strong>Book now:</strong> '
        f'<a href="/book-mahjong-lesson.html">Schedule Mahjong 101</a> · '
        f'<a href="hire-mahjong-instructor.html">Hire instructor</a> · '
        f'<a href="private-mahjong-teacher-home-visit.html">Teacher comes to you</a> · '
        f'<a href="{BOOKING_HUB}">Booking hub</a></p>'
    )
    return mahjong_kw(
        near_slug,
        f"Mahjong Lessons Near {label} | Book Now",
        desc,
        f"mahjong lessons near me {stem}, book mahjong lessons {label.lower()}, mahjong teacher {stem}",
        f"Mahjong Lessons Near {label}",
        body,
    )


def bulk_pages_booking_near_me_wave(city, page, mahjong_kw) -> list:
    out: list = []

    out.append(
        page(
            BOOKING_HUB,
            "Book Mahjong Lessons Near Me | Private Teachers & Tournaments",
            "Book mahjong lessons near you — private teachers travel nationwide. Mahjong 101, tournaments, Greenbrier prep.",
            "book mahjong near me, mahjong lessons near me, hire mahjong teacher, book mahjong instructor",
            "Book Mahjong — Lessons Near Me Nationwide",
            """<p><strong>Book Lookout Mountain Mahjong</strong> when you search <em>mahjong lessons near me</em>, 
<em>hire a mahjong teacher</em>, or <em>private mahjong instructor</em>. We travel to your city — home, country club, resort, or tournament.</p>
<h2>Book a Lesson</h2>
<p><a href="book-mahjong-lesson.html">★ Book Mahjong 101</a> ($125/person) · <a href="mahjong-102.html">Mahjong 102</a> ($115) · 
<a href="booking-mahjong-hub.html">Booking guide</a> · Email lookoutmountainmahjong@gmail.com · (919) 247-3392</p>
<h2>Near Me</h2>
<p><a href="mahjong-lessons-near-me.html">Mahjong lessons near me</a> · <a href="find-mahjong-instructor-near-me.html">Find instructor near me</a> · 
<a href="mahjong-teacher-near-me.html">Mahjong teacher near me</a> · <a href="mahjong-coach-near-me.html">Coach near me</a> · 
<a href="mahjong-tutor-near-me.html">Tutor near me</a> · <a href="cities-mahjong-hub.html">All cities</a> · <a href="states-mahjong-hub.html">All states</a></p>
<h2>Private Teacher Comes to You</h2>
<p><a href="private-mahjong-teacher-home-visit.html">Teacher home visit</a> · <a href="mahjong-instructor-comes-to-you.html">Instructor comes to you</a> · 
<a href="travel-to-you-mahjong.html">We travel to you</a> · <a href="private-mahjong-lessons.html">Private lessons</a> · 
<a href="hire-mahjong-instructor.html">Hire instructor</a></p>
<h2>Tournaments &amp; Prep</h2>
<p><a href="book-mahjong-tournament-coach.html">Book tournament coach</a> · <a href="greenbrier-tournament-booking.html">Greenbrier tournaments</a> · 
<a href="mahjong-tournament-prep-booking.html">Tournament prep</a> · <a href="greenbrier-mahjong-hub.html">Greenbrier hub</a></p>
<h2>By State</h2>
<p><a href="mahjong-lessons-near-me-georgia.html">Georgia</a> · <a href="mahjong-lessons-near-me-tennessee.html">Tennessee</a> · 
<a href="mahjong-lessons-near-me-north-carolina.html">North Carolina</a> · <a href="mahjong-lessons-near-me-florida.html">Florida</a> · 
<a href="mahjong-lessons-near-me-texas.html">Texas</a> · <a href="mahjong-lessons-near-me-california.html">California</a> · 
<a href="southeast-mahjong-hub.html">Southeast hub</a></p>""",
            priority="0.96",
        )
    )

    out.append(
        page(
            "mahjong-lessons-near-me-hub.html",
            "Mahjong Lessons Near Me | Every State & City",
            "Mahjong lessons near me — book private teachers in every state. Lookout Mountain Mahjong travels nationwide.",
            "mahjong lessons near me hub, mahjong near me nationwide, book mahjong near me",
            "Mahjong Lessons Near Me — Nationwide",
            """<p>Search <strong>mahjong lessons near me</strong>? Pick your state or city — we book private lessons and events everywhere we travel.</p>
<p><a href="mahjong-booking-near-me-hub.html">★ Book mahjong hub</a> · <a href="book-mahjong-lesson.html">Book now</a> · 
<a href="hire-mahjong-instructor.html">Hire instructor</a></p>
<p><a href="mahjong-lessons-near-me-georgia.html">GA</a> · <a href="mahjong-lessons-near-me-tennessee.html">TN</a> · 
<a href="mahjong-lessons-near-me-north-carolina.html">NC</a> · <a href="mahjong-lessons-near-me-south-carolina.html">SC</a> · 
<a href="mahjong-lessons-near-me-alabama.html">AL</a> · <a href="mahjong-lessons-near-me-florida.html">FL</a> · 
<a href="mahjong-lessons-near-me-texas.html">TX</a> · <a href="mahjong-lessons-near-me-california.html">CA</a> · 
<a href="mahjong-lessons-near-me-new-york.html">NY</a> · <a href="states-mahjong-hub.html">All states</a></p>""",
            priority="0.95",
        )
    )

    out.append(
        page(
            "book-private-mahjong-teacher-hub.html",
            "Book a Private Mahjong Teacher | Home & Event Visits",
            "Book a private mahjong teacher — certified instructors travel to your home, club, or resort nationwide.",
            "book private mahjong teacher, private mahjong instructor, mahjong teacher for hire",
            "Book a Private Mahjong Teacher",
            """<p><strong>Book a private mahjong teacher</strong> — Mahj Jen &amp; Mahj Hen bring tiles, tables, and the NMJL card to you.</p>
<ul>
<li><a href="private-mahjong-teacher-home-visit.html">Home visit lessons</a></li>
<li><a href="mahjong-instructor-comes-to-you.html">Instructor comes to you</a></li>
<li><a href="hire-mahjong-instructor.html">Hire for events</a></li>
<li><a href="book-mahjong-country-club.html">Country club booking</a></li>
<li><a href="book-mahjong-resort.html">Resort &amp; hotel events</a></li>
</ul>
<p><a href="book-mahjong-lesson.html">Book Mahjong 101</a> · <a href="mahjong-booking-near-me-hub.html">Near me hub</a></p>""",
            priority="0.94",
        )
    )

    out.append(
        page(
            "book-mahjong-tournament-hub.html",
            "Book Mahjong for Tournaments | Coach & Greenbrier Prep",
            "Book mahjong tournament coaching — Greenbrier prep, NMJL strategy, private tournament lessons.",
            "book mahjong tournament, mahjong tournament coach, greenbrier mahjong booking",
            "Book Mahjong — Tournaments & Prep",
            """<p><strong>Book tournament mahjong coaching</strong> with instructors who teach at <a href="greenbrier-mahjong.html">The Greenbrier</a>.</p>
<p><a href="book-mahjong-tournament-coach.html">Tournament coach</a> · <a href="mahjong-tournament-prep-booking.html">Tournament prep</a> · 
<a href="greenbrier-tournament-booking.html">Greenbrier booking</a> · <a href="greenbrier-prep-mahjong.html">Greenbrier prep</a> · 
<a href="mahjong-tournament.html">Tournaments</a></p>
<p><a href="book-mahjong-lesson.html">Book a lesson</a> · <a href="mahjong-102.html">Mahjong 102 strategy</a></p>""",
            priority="0.93",
        )
    )

    for abbr, (slug, name) in STATE_SLUGS.items():
        state_page, hub_page = STATE_META[abbr]
        near_file = f"mahjong-lessons-near-me-{slug}.html"
        body = (
            f"<p><strong>Mahjong lessons near me in {name}</strong> — book certified instructors "
            f"who travel to your home, club, or event anywhere in {name}.</p>"
            f'<p><a href="{state_page}">{name} mahjong</a> · <a href="{hub_page}">{name} hub</a> · '
            f'<a href="cities-mahjong-hub.html">Cities nationwide</a></p>'
            f'<p><a href="book-mahjong-lesson.html">Book Mahjong 101</a> · '
            f'<a href="hire-mahjong-instructor.html">Hire instructor</a> · '
            f'<a href="private-mahjong-teacher-home-visit.html">Private teacher visit</a> · '
            f'<a href="{BOOKING_HUB}">Booking near me hub</a></p>'
        )
        out.append(
            page(
                near_file,
                f"Mahjong Lessons Near Me {name} | Book Private Teacher",
                f"Mahjong lessons near me {name} — book private teacher, home visits, tournaments. Nationwide travel.",
                f"mahjong lessons near me {slug}, book mahjong lessons {name.lower()}, mahjong teacher {slug}",
                f"Mahjong Lessons Near Me — {name}",
                body,
                priority="0.91",
            )
        )

    priority_metros = [
        ("chattanooga-lessons-near-me.html", "Chattanooga", "TN", "tennessee-mahjong.html", "chattanooga-mahjong.html"),
        ("atlanta-lessons-near-me.html", "Atlanta", "GA", "georgia-mahjong.html", "atlanta-mahjong.html"),
        ("nashville-lessons-near-me.html", "Nashville", "TN", "tennessee-mahjong.html", "nashville-mahjong.html"),
        ("charlotte-lessons-near-me.html", "Charlotte", "NC", "north-carolina-mahjong.html", "charlotte-mahjong.html"),
        ("raleigh-lessons-near-me.html", "Raleigh", "NC", "north-carolina-mahjong.html", "raleigh-mahjong.html"),
        ("birmingham-lessons-near-me.html", "Birmingham", "AL", "alabama-mahjong.html", "birmingham-mahjong.html"),
        ("savannah-lessons-near-me.html", "Savannah", "GA", "georgia-mahjong.html", "savannah-mahjong.html"),
        ("dallas-lessons-near-me.html", "Dallas", "TX", "texas-mahjong.html", "dallas-mahjong.html"),
        ("houston-lessons-near-me.html", "Houston", "TX", "texas-mahjong.html", "houston-mahjong.html"),
        ("austin-lessons-near-me.html", "Austin", "TX", "texas-mahjong.html", "austin-mahjong.html"),
        ("miami-lessons-near-me.html", "Miami", "FL", "florida-mahjong.html", "miami-mahjong.html"),
        ("tampa-lessons-near-me.html", "Tampa", "FL", "florida-mahjong.html", "tampa-mahjong.html"),
        ("orlando-lessons-near-me.html", "Orlando", "FL", "florida-mahjong.html", "orlando-mahjong.html"),
        ("denver-lessons-near-me.html", "Denver", "CO", "colorado-mahjong.html", "denver-mahjong.html"),
        ("phoenix-lessons-near-me.html", "Phoenix", "AZ", "arizona-mahjong.html", "phoenix-mahjong.html"),
        ("chicago-lessons-near-me.html", "Chicago", "IL", "illinois-mahjong.html", "chicago-mahjong.html"),
        ("boston-lessons-near-me.html", "Boston", "MA", "massachusetts-mahjong.html", "boston-mahjong.html"),
        ("new-york-lessons-near-me.html", "New York", "NY", "new-york-mahjong.html", "new-york-mahjong.html"),
        ("los-angeles-lessons-near-me.html", "Los Angeles", "CA", "california-mahjong.html", "los-angeles-mahjong.html"),
        ("san-francisco-lessons-near-me.html", "San Francisco", "CA", "california-mahjong.html", "san-francisco-mahjong.html"),
        ("seattle-lessons-near-me.html", "Seattle", "WA", "washington-state-mahjong.html", "seattle-mahjong.html"),
        ("portland-lessons-near-me.html", "Portland", "OR", "oregon-mahjong.html", "portland-mahjong.html"),
        ("las-vegas-lessons-near-me.html", "Las Vegas", "NV", "nevada-mahjong.html", "las-vegas-mahjong.html"),
        ("richmond-lessons-near-me.html", "Richmond", "VA", "virginia-mahjong.html", "richmond-mahjong.html"),
        ("louisville-lessons-near-me.html", "Louisville", "KY", "kentucky-mahjong.html", "louisville-mahjong.html"),
        ("new-orleans-lessons-near-me.html", "New Orleans", "LA", "louisiana-mahjong.html", "new-orleans-mahjong.html"),
        ("memphis-lessons-near-me.html", "Memphis", "TN", "tennessee-mahjong.html", "memphis-mahjong.html"),
        ("knoxville-lessons-near-me.html", "Knoxville", "TN", "tennessee-mahjong.html", "knoxville-mahjong.html"),
        ("greenville-sc-lessons-near-me.html", "Greenville SC", "SC", "south-carolina-mahjong.html", "greenville-sc-mahjong.html"),
        ("charleston-sc-lessons-near-me.html", "Charleston SC", "SC", "south-carolina-mahjong.html", "charleston-sc-mahjong.html"),
        ("lookout-mountain-lessons-near-me.html", "Lookout Mountain", "GA", "georgia-mahjong.html", "lookout-mountain-georgia-mahjong.html"),
    ]
    for near_slug, label, st, state_page, city_page in priority_metros:
        st_slug = STATE_SLUGS.get(st, ("", ""))[0]
        state_near = f"mahjong-lessons-near-me-{st_slug}.html" if st_slug else "mahjong-lessons-near-me.html"
        out.append(_booking_city_page(mahjong_kw, (near_slug, label, st, state_page, city_page, state_near)))

    for row in WAVE40_BOOKING_CITIES:
        out.append(_booking_city_page(mahjong_kw, row))

    intents = [
        ("private-mahjong-teacher-home-visit", "Private Teacher Home Visit", "private mahjong teacher home visit — instructor comes to your house", '<p><strong>Private mahjong teacher home visit</strong> — we bring everything. <a href="book-mahjong-lesson.html">Book</a> · <a href="travel-to-you-mahjong.html">Travel</a>.</p>'),
        ("mahjong-instructor-comes-to-you", "Instructor Comes to You", "mahjong instructor comes to you — nationwide private lessons", '<p>Your <strong>mahjong instructor comes to you</strong> — no studio required. <a href="hire-mahjong-instructor.html">Hire</a>.</p>'),
        ("find-mahjong-instructor-near-me", "Find Instructor Near Me", "find mahjong instructor near me — book certified teacher", '<p><strong>Find a mahjong instructor near me</strong> — <a href="mahjong-lessons-near-me.html">Near me index</a> · <a href="certified-mahjong-instructor.html">Certified</a>.</p>'),
        ("mahjong-teacher-near-me", "Mahjong Teacher Near Me", "mahjong teacher near me — book private lessons", '<p><strong>Mahjong teacher near me</strong> — TML Ambassadors Mahj Jen &amp; Mahj Hen. <a href="mahjong-teacher.html">Teachers</a>.</p>'),
        ("mahjong-coach-near-me", "Mahjong Coach Near Me", "mahjong coach near me — strategy and tournament prep", '<p><strong>Mahjong coach near me</strong> — <a href="mahjong-coach.html">Coach</a> · <a href="mahjong-102.html">102</a>.</p>'),
        ("mahjong-tutor-near-me", "Mahjong Tutor Near Me", "mahjong tutor near me — private in-home tutoring", '<p><strong>Mahjong tutor near me</strong> — <a href="mahjong-tutor.html">Tutor</a> · <a href="private-mahjong-lessons.html">Private</a>.</p>'),
        ("book-mahjong-instructor-near-me", "Book Instructor Near Me", "book mahjong instructor near me — schedule nationwide", '<p><strong>Book mahjong instructor near me</strong> — email lookoutmountainmahjong@gmail.com · <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("schedule-mahjong-lesson-near-me", "Schedule Lesson Near Me", "schedule mahjong lesson near me — Mahjong 101 booking", '<p><strong>Schedule mahjong near me</strong> — $125/person · <a href="mahjong-101.html">101</a>.</p>'),
        ("hire-mahjong-teacher-near-me", "Hire Teacher Near Me", "hire mahjong teacher near me — events and home lessons", '<p><strong>Hire mahjong teacher near me</strong> — <a href="hire-mahjong-instructor.html">Hire guide</a>.</p>'),
        ("book-mahjong-tournament-coach", "Book Tournament Coach", "book mahjong tournament coach — prep for NMJL tournaments", '<p><strong>Book a tournament coach</strong> — <a href="mahjong-tournament.html">Tournaments</a> · <a href="greenbrier-prep-mahjong.html">Greenbrier prep</a>.</p>'),
        ("mahjong-tournament-prep-booking", "Tournament Prep Booking", "mahjong tournament prep booking — private coaching before events", '<p><strong>Tournament prep booking</strong> — <a href="mahjong-102.html">Mahjong 102</a> · <a href="book-mahjong-tournament-hub.html">Tournament hub</a>.</p>'),
        ("greenbrier-tournament-booking", "Greenbrier Tournament Booking", "greenbrier tournament booking mahjong — book Mahj Jen & Mahj Hen", '<p><strong>Greenbrier tournament booking</strong> — <a href="greenbrier-mahjong.html">Greenbrier</a> · <a href="jen-kline-greenbrier-mahjong.html">Mahj Jen</a>.</p>'),
        ("book-mahjong-for-tournament", "Book for Tournament", "book mahjong for tournament — group prep sessions", '<p><strong>Book mahjong for your tournament</strong> — club or charity event. <a href="charity-mahjong-event.html">Charity</a>.</p>'),
        ("book-mahjong-country-club", "Book Country Club", "book mahjong country club — private teacher at your club", '<p><strong>Book mahjong at your country club</strong> — <a href="country-club-mahjong.html">Country club</a>.</p>'),
        ("book-mahjong-resort", "Book Resort Mahjong", "book mahjong resort — instructor at hotel or resort", '<p><strong>Book resort mahjong</strong> — <a href="resort-mahjong.html">Resort</a> · <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("book-mahjong-corporate-event", "Book Corporate Event", "book mahjong corporate event — team building with instructor", '<p><strong>Book corporate mahjong</strong> — <a href="corporate-mahjong-events.html">Corporate</a>.</p>'),
        ("book-mahjong-bachelorette", "Book Bachelorette", "book mahjong bachelorette — private teacher for wedding weekend", '<p><strong>Book bachelorette mahjong</strong> — <a href="bachelorette-mahjong.html">Bachelorette</a>.</p>'),
        ("book-mahjong-bridal-shower", "Book Bridal Shower", "book mahjong bridal shower — instructor-led shower activity", '<p><strong>Book bridal shower mahjong</strong> — <a href="bridal-shower-mahjong.html">Bridal shower</a>.</p>'),
        ("book-mahjong-girls-night", "Book Girls Night", "book mahjong girls night — private teacher for your group", '<p><strong>Book girls night mahjong</strong> — <a href="girls-night-mahjong.html">Girls night</a>.</p>'),
        ("book-mahjong-sorority", "Book Sorority Event", "book mahjong sorority — philanthropy and bid day", '<p><strong>Book sorority mahjong</strong> — <a href="sorority-mahjong-parties.html">Sorority</a>.</p>'),
        ("book-mahjong-snowbird", "Book Snowbird Season", "book mahjong snowbird — Florida winter lessons", '<p><strong>Book snowbird mahjong</strong> — <a href="snowbird-mahjong.html">Snowbird</a> · <a href="florida-mahjong-hub.html">Florida</a>.</p>'),
        ("book-mahjong-vacation-rental", "Book Vacation Rental", "book mahjong vacation rental — teacher at beach house", '<p><strong>Book vacation rental mahjong</strong> — <a href="vacation-mahjong.html">Vacation</a>.</p>'),
        ("book-mahjong-lessons-online", "Book Lessons (Schedule)", "book mahjong lessons — schedule by email phone nationwide", '<p><strong>Book mahjong lessons</strong> — lookoutmountainmahjong@gmail.com · (919) 247-3392 · <a href="booking-mahjong-hub.html">Hub</a>.</p>'),
        ("mahjong-lessons-at-my-house", "Lessons at My House", "mahjong lessons at my house — private teacher home visit", '<p><strong>Mahjong at my house</strong> — <a href="private-mahjong-lessons.html">Private</a> · <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("in-home-mahjong-instructor", "In-Home Instructor", "in home mahjong instructor — book teacher to your address", '<p><strong>In-home mahjong instructor</strong> — nationwide. <a href="hire-mahjong-instructor.html">Hire</a>.</p>'),
        ("mobile-mahjong-lessons", "Mobile Mahjong Lessons", "mobile mahjong lessons — we come to your location", '<p><strong>Mobile mahjong lessons</strong> — we drive to you. <a href="travel-to-you-mahjong.html">Travel</a>.</p>'),
        ("traveling-mahjong-teacher", "Traveling Mahjong Teacher", "traveling mahjong teacher — book instructor who travels", '<p><strong>Traveling mahjong teacher</strong> — <a href="mahjong-usa.html">USA wide</a>.</p>'),
        ("book-mahjong-teacher-nationwide", "Book Teacher Nationwide", "book mahjong teacher nationwide — any city we travel", '<p><strong>Nationwide mahjong teacher booking</strong> — <a href="mahjong-lessons-near-me-hub.html">Near me hub</a>.</p>'),
        ("certified-mahjong-instructor-near-me", "Certified Instructor Near Me", "certified mahjong instructor near me — TML ambassadors", '<p><strong>Certified instructor near me</strong> — <a href="certified-mahjong-instructor.html">Certified</a> · <a href="tml-ambassador-mahjong.html">TML</a>.</p>'),
        ("best-mahjong-lessons-near-me", "Best Lessons Near Me", "best mahjong lessons near me — top rated private teachers", '<p><strong>Best mahjong lessons near me</strong> — <a href="best-mahjong-lessons.html">Best lessons</a>.</p>'),
        ("affordable-mahjong-lessons-near-me", "Affordable Lessons Near Me", "affordable mahjong lessons near me — Mahjong 101 pricing", '<p><strong>Affordable lessons</strong> — $125/person includes gear. <a href="mahjong-party-cost.html">Pricing</a>.</p>'),
        ("beginner-mahjong-lessons-near-me", "Beginner Lessons Near Me", "beginner mahjong lessons near me — Mahjong 101 booking", '<p><strong>Beginner lessons near me</strong> — <a href="beginner-mahjong.html">Beginner</a> · <a href="mahjong-101.html">101</a>.</p>'),
        ("group-mahjong-lessons-near-me", "Group Lessons Near Me", "group mahjong lessons near me — 4-8 players book together", '<p><strong>Group lessons near me</strong> — ideal 4–8 players. <a href="mahjong-101.html">101</a>.</p>'),
        ("private-mahjong-class-near-me", "Private Class Near Me", "private mahjong class near me — book your group", '<p><strong>Private class near me</strong> — <a href="private-mahjong-lessons.html">Private</a>.</p>'),
        ("mahjong-instructor-for-hire-near-me", "Instructor for Hire Near Me", "mahjong instructor for hire near me — book events", '<p><strong>Instructor for hire</strong> — <a href="hire-mahjong-instructor.html">Hire</a>.</p>'),
        ("book-mahjong-lesson-today", "Book Lesson Today", "book mahjong lesson today — same-week scheduling when available", '<p><strong>Book today</strong> — email lookoutmountainmahjong@gmail.com · <a href="book-mahjong-lesson.html">Book page</a>.</p>'),
        ("book-mahjong-this-weekend", "Book This Weekend", "book mahjong this weekend — private party scheduling", '<p><strong>Book this weekend</strong> — girls night, shower, club event. <a href="events-mahjong-hub.html">Events</a>.</p>'),
        ("mahjong-teacher-for-party", "Teacher for Party", "mahjong teacher for party — book instructor for your event", '<p><strong>Teacher for your party</strong> — <a href="mahjong-party.html">Party</a> · <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("mahjong-teacher-for-club", "Teacher for Club", "mahjong teacher for club — country club and league booking", '<p><strong>Teacher for your club</strong> — <a href="country-club-mahjong.html">Club</a>.</p>'),
        ("mahjong-teacher-for-retirement", "Teacher for Retirement", "mahjong teacher retirement community — book senior-friendly lessons", '<p><strong>Retirement community lessons</strong> — <a href="retirement-community-mahjong.html">Retirement</a>.</p>'),
        ("book-mahjong-charity-tournament", "Book Charity Tournament", "book mahjong charity tournament — fundraiser with instructor", '<p><strong>Charity tournament booking</strong> — <a href="charity-mahjong-event.html">Charity</a>.</p>'),
        ("book-mahjong-league-night", "Book League Night", "book mahjong league night — upgrade your league with a pro", '<p><strong>League night booking</strong> — <a href="mahjong-league.html">League</a>.</p>'),
        ("book-mahjong-hoa-event", "Book HOA Event", "book mahjong hoa event — neighborhood instructor visit", '<p><strong>HOA event booking</strong> — <a href="hoa-mahjong.html">HOA</a>.</p>'),
        ("book-mahjong-church-event", "Book Church Event", "book mahjong church event — fellowship hall lessons", '<p><strong>Church event booking</strong> — <a href="church-mahjong.html">Church</a>.</p>'),
        ("book-mahjong-senior-center", "Book Senior Center", "book mahjong senior center — instructor-led beginner class", '<p><strong>Senior center booking</strong> — <a href="senior-center-mahjong.html">Senior center</a>.</p>'),
        ("mahjong-near-me-open-now", "Mahjong Near Me Open", "mahjong near me open now — book upcoming lesson dates", '<p>Check availability — <a href="book-mahjong-lesson.html">Book</a> · Instagram <a href="lookoutmountainmahjong.html">@lookoutmountainmahjong</a>.</p>'),
        ("mahjong-lessons-near-me-now", "Lessons Near Me Now", "mahjong lessons near me now — schedule private teacher", '<p><strong>Lessons near me now</strong> — <a href="mahjong-booking-near-me-hub.html">Booking hub</a>.</p>'),
        ("where-to-book-mahjong-lessons", "Where to Book Lessons", "where to book mahjong lessons — official Lookout Mountain booking", '<p><strong>Where to book</strong> — <a href="book-mahjong-lesson.html">Official book page</a> · <a href="booking-mahjong-hub.html">Hub</a>.</p>'),
        ("who-teaches-mahjong-near-me", "Who Teaches Near Me", "who teaches mahjong near me — Mahj Jen and Mahj Hen", '<p><strong>Who teaches near you</strong> — <a href="mahj-jen-mahj-hen.html">Mahj Jen &amp; Mahj Hen</a> travel nationwide.</p>'),
    ]
    for slug, title, desc, body in intents:
        out.append(_occasion(mahjong_kw, slug, title, desc, body))

    rules = [
        ("how-to-book-mahjong-lesson.html", "How to Book", "how to book mahjong lesson — email phone pricing", '<p>Email lookoutmountainmahjong@gmail.com · (919) 247-3392 · <a href="book-mahjong-lesson.html">Book</a> · <a href="first-mahjong-lesson.html">First lesson</a>.</p>'),
        ("mahjong-lesson-pricing-booking.html", "Lesson Pricing", "mahjong lesson pricing booking — 101 and 102 rates", '<p><a href="mahjong-101.html">101 $125</a> · <a href="mahjong-102.html">102 $115</a> · <a href="mahjong-party-cost.html">Party cost</a>.</p>'),
        ("travel-fee-mahjong-booking.html", "Travel Fee", "travel fee mahjong booking — out of area lessons", '<p>We travel nationwide — <a href="travel-to-you-mahjong.html">Travel policy</a> · <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("minimum-players-mahjong-booking.html", "Minimum Players", "minimum players mahjong booking — group size 4-8", '<p>Ideal <strong>4–8 players</strong> for Mahjong 101 — <a href="mahjong-101.html">101</a>.</p>'),
        ("what-is-included-mahjong-booking.html", "What Is Included", "what is included mahjong booking — tiles tables cards", '<p>We bring <strong>tiles, tables, NMJL cards</strong> — <a href="mahjong-101.html">101</a>.</p>'),
        ("cancellation-policy-mahjong-booking.html", "Cancellation Policy", "cancellation policy mahjong booking — contact to reschedule", '<p>Contact us to reschedule — lookoutmountainmahjong@gmail.com.</p>'),
        ("deposit-mahjong-booking.html", "Deposit", "deposit mahjong booking — confirm your date by email", '<p>Confirm dates by email — <a href="book-mahjong-lesson.html">Book</a>.</p>'),
        ("gift-certificate-mahjong-booking.html", "Gift Certificate", "gift certificate mahjong booking — lesson gift experience", '<p><a href="mahjong-gift-experience.html">Gift experience</a> · <a href="gifts-mahjong-hub.html">Gifts</a>.</p>'),
        ("corporate-invoice-mahjong-booking.html", "Corporate Invoice", "corporate invoice mahjong booking — business events", '<p><a href="corporate-mahjong-events.html">Corporate events</a> · email for invoice.</p>'),
        ("tournament-coaching-rates.html", "Tournament Coaching Rates", "tournament coaching rates mahjong — book prep sessions", '<p><a href="book-mahjong-tournament-coach.html">Tournament coach</a> · <a href="mahjong-102.html">102</a>.</p>'),
    ]
    for slug, title, desc, body in rules:
        out.append(_rule(mahjong_kw, slug, title, desc, body))

    return out
