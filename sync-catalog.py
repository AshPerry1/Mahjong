#!/usr/bin/env python3
"""Sync threadandink-catalog.json from Thread & Ink Co Shopify collections."""

import json
import urllib.request

BASE = "https://threadandinkco.com"
OUTPUT = "threadandink-catalog.json"
DEFAULT_FEATURED = {
    "handle": "mahj-long-sleeve-sweater",
    "eyebrow": "Featured on Instagram",
    "description": "The sweater we highlighted with Thread & Ink Co — soft cream knit with bold MAHJ lettering, perfect for tournament weekends at The Greenbrier.",
}
COLLECTIONS = [
    {
        "title": "Mahjong at The Greenbrier",
        "handle": "christmas",
        "image": "https://cdn.shopify.com/s/files/1/0146/4169/2720/collections/IMG_6782.jpg?v=1771887209",
        "categories": ["greenbrier"],
    },
    {
        "title": "Games, Golf and Mahjong",
        "handle": "games-and-mahjong",
        "image": "https://cdn.shopify.com/s/files/1/0146/4169/2720/collections/IMG_0512.jpg?v=1701112053",
        "categories": ["mahjong"],
    },
]
EXTRA_HANDLES = [
    "mahj-at-the-greenbrier-large-canvas-bag",
    "apres-mahj-pads",
]


def fetch_json(url):
    with urllib.request.urlopen(url) as response:
        return json.load(response)


def product_image(product):
    images = product.get("images") or []
    if images:
        return images[0]["src"]
    image = product.get("image")
    return image.get("src") if image else None


def load_existing_featured():
    try:
        with open(OUTPUT, encoding="utf-8") as handle:
            existing = json.load(handle)
        return existing.get("featured") or DEFAULT_FEATURED
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return DEFAULT_FEATURED


def main():
    products_by_handle = {}
    collection_counts = {}

    for collection in COLLECTIONS:
        data = fetch_json(f"{BASE}/collections/{collection['handle']}/products.json?limit=250")
        items = data.get("products", [])
        collection_counts[collection["handle"]] = len(items)

        for product in items:
            handle = product["handle"]
            price = product["variants"][0]["price"] if product.get("variants") else "0.00"
            entry = {
                "title": product["title"],
                "handle": handle,
                "price": price,
                "image": product_image(product),
                "url": f"{BASE}/products/{handle}",
            }

            if handle not in products_by_handle:
                products_by_handle[handle] = {
                    **entry,
                    "collections": [collection["title"]],
                    "categories": set(collection["categories"] + ["mahjong"]),
                }
            else:
                products_by_handle[handle]["collections"].append(collection["title"])
                products_by_handle[handle]["categories"].update(collection["categories"])
                products_by_handle[handle]["categories"].add("mahjong")
                if not products_by_handle[handle]["image"] and entry["image"]:
                    products_by_handle[handle]["image"] = entry["image"]

    for handle in EXTRA_HANDLES:
        if handle in products_by_handle:
            continue
        data = fetch_json(f"{BASE}/products/{handle}.json")
        product = data["product"]
        collection_title = "Mahjong at The Greenbrier"
        products_by_handle[handle] = {
            "title": product["title"],
            "handle": handle,
            "price": product["variants"][0]["price"],
            "image": product_image(product),
            "url": f"{BASE}/products/{handle}",
            "collections": [collection_title],
            "categories": {"greenbrier", "mahjong"},
        }

    products = []
    for handle, product in sorted(products_by_handle.items(), key=lambda item: item[1]["title"].lower()):
        primary_collection = product["collections"][0]
        if "Mahjong at The Greenbrier" in product["collections"]:
            primary_collection = "Mahjong at The Greenbrier"
        products.append({
            "title": product["title"],
            "handle": handle,
            "price": product["price"],
            "image": product["image"],
            "collection": primary_collection,
            "url": product["url"],
            "categories": sorted(product["categories"]),
        })

    catalog = {
        "featured": load_existing_featured(),
        "categories": [
            {"id": "all", "label": "All"},
            {"id": "greenbrier", "label": "Greenbrier"},
            {"id": "mahjong", "label": "Mahjong"},
        ],
        "collections": [
            {
                "title": collection["title"],
                "handle": collection["handle"],
                "image": collection["image"],
                "url": f"{BASE}/collections/{collection['handle']}",
                "count": collection_counts.get(collection["handle"], 0),
                "categories": collection["categories"],
            }
            for collection in COLLECTIONS
        ],
        "products": products,
    }

    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(catalog, handle, indent=2)
        handle.write("\n")

    print(f"Wrote {len(products)} products to {OUTPUT}")


if __name__ == "__main__":
    main()
