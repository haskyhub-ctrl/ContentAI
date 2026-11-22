#!/usr/bin/env python3
"""Export an X post / X Article (incl. code blocks) to markdown via api.fxtwitter.com.

Usage: python3 tools/x_export.py <x.com status URL> [-o out.md]
Only public content; no login needed. Stdlib only.
"""
import argparse, json, re, sys, urllib.request


def fetch(url):
    m = re.search(r"(?:x|twitter)\.com/([^/]+)/status/(\d+)", url)
    if not m:
        sys.exit("Not an X status URL")
    api = f"https://api.fxtwitter.com/{m.group(1)}/status/{m.group(2)}"
    req = urllib.request.Request(api, headers={"User-Agent": "contentai-export/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["tweet"]


def article_md(art):
    content = art.get("content") or {}
    em = content.get("entityMap") or []
    items = em.items() if isinstance(em, dict) else enumerate(em)
    by_key = {}
    for idx, e in items:
        by_key[str(idx)] = e  # block entityRanges reference the list index
    out = [f"# {art.get('title', '')}\n"]
    for b in content.get("blocks", []):
        t = (b.get("text") or "").strip()
        if b.get("type") == "atomic":
            for rng in b.get("entityRanges", []):
                e = by_key.get(str(rng.get("key")))
                data = (e or {}).get("value", {}).get("data", {})
                if "markdown" in data:
                    out.append(data["markdown"].strip() + "\n")
        elif t:
            out.append(("## " + t if b.get("type", "").startswith("header") else t) + "\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    tw = fetch(a.url)
    parts = [f"Source: {a.url}\nAuthor: @{tw['author']['screen_name']}\n"]
    if tw.get("text"):
        parts.append(tw["text"] + "\n")
    if tw.get("article"):
        parts.append(article_md(tw["article"]))
    md = "\n".join(parts)
    if a.out:
        open(a.out, "w").write(md)
        print("Saved", a.out)
    else:
        print(md)


if __name__ == "__main__":
    main()
