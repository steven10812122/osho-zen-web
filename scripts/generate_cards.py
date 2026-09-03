#!/usr/bin/env python3
"""Batch-generate card images via the free Pollinations.ai image API.

Usage:
  python3 scripts/generate_cards.py --out prompts/test_output --only ccard1.jpg,fcard1.jpg
  python3 scripts/generate_cards.py --out assets/cards            # full 79-card run

Reads scripts/_prompts_data.json (produced from prompts/card-image-prompts.md),
combines each card's prompt with the shared art-direction style block, and
downloads one image per card from image.pollinations.ai (no API key needed).
"""
import argparse
import json
import time
import urllib.parse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(HERE, "_prompts_data.json")


def load_data():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def build_url(prompt, seed, width=512, height=768, model="sana"):
    q = urllib.parse.quote(prompt)
    return (
        f"https://image.pollinations.ai/prompt/{q}"
        f"?width={width}&height={height}&nologo=true&model={model}&seed={seed}"
    )


def fetch(url, dest, retries=6, timeout=120):
    backoff = 8
    for attempt in range(1, retries + 1):
        try:
            result = subprocess.run(
                ["curl", "-sS", "-w", "\n%{http_code}", "--max-time", str(timeout), "-o", dest, url],
                capture_output=True, text=True,
            )
            status = result.stdout.strip().splitlines()[-1] if result.stdout else ""
            is_real_image = False
            if result.returncode == 0 and status == "200" and os.path.getsize(dest) > 0:
                with open(dest, "rb") as f:
                    head = f.read(16)
                is_real_image = head.startswith(b"\xff\xd8\xff") or head.startswith(b"\x89PNG")
            if is_real_image:
                return True
            body_snippet = ""
            if os.path.exists(dest) and os.path.getsize(dest) < 2000:
                with open(dest, "rb") as f:
                    body_snippet = f.read(200).decode("utf-8", "replace")
                os.remove(dest)
            print(f"  attempt {attempt} failed: http={status} {result.stderr.strip()} {body_snippet}", file=sys.stderr)
            if status == "429" or "rate_limit" in body_snippet or "429" in body_snippet:
                print(f"  rate-limited, backing off {backoff}s", file=sys.stderr)
                time.sleep(backoff)
                backoff = min(backoff * 2, 90)
                continue
        except Exception as e:
            print(f"  attempt {attempt} failed: {e}", file=sys.stderr)
        time.sleep(4)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="output directory for generated images")
    ap.add_argument("--only", default=None, help="comma-separated filenames to limit to (e.g. ccard1.jpg,fcard1.jpg)")
    ap.add_argument("--delay", type=float, default=2.0, help="seconds to sleep between requests")
    ap.add_argument("--seed-offset", type=int, default=0, help="add to each card's seed, to regenerate with a different look")
    ap.add_argument("--override-prompt", default=None, help="use this exact prompt instead of the JSON one (still gets art_direction appended); only valid with a single --only file")
    ap.add_argument("--no-art-direction", action="store_true", help="don't append the shared art_direction block (override-prompt already includes everything needed)")
    ap.add_argument("--skip-existing", action="store_true", help="skip any card whose output file already exists")
    args = ap.parse_args()

    data = load_data()
    art_direction = data["art_direction"].replace("\n", " ")
    cards = data["cards"]

    if args.only:
        wanted = set(x.strip() for x in args.only.split(","))
        cards = [c for c in cards if c["file"] in wanted]

    if args.override_prompt:
        if len(cards) != 1:
            print("--override-prompt requires exactly one file in --only", file=sys.stderr)
            sys.exit(1)
        cards[0]["prompt"] = args.override_prompt

    os.makedirs(args.out, exist_ok=True)

    print(f"Generating {len(cards)} card(s) into {args.out}/")
    for i, card in enumerate(cards, start=1):
        dest = os.path.join(args.out, card["file"])
        if args.skip_existing and os.path.exists(dest) and os.path.getsize(dest) > 0:
            print(f"[{i}/{len(cards)}] {card['file']} — skipping (already exists)")
            continue
        if args.no_art_direction:
            full_prompt = card["prompt"]
        else:
            full_prompt = f"{card['prompt']} {art_direction}"
        seed = (hash(card["file"]) % 100000) + args.seed_offset
        url = build_url(full_prompt, seed)
        print(f"[{i}/{len(cards)}] {card['file']} — {card['title']}")
        ok = fetch(url, dest)
        if not ok:
            print(f"  FAILED: {card['file']}", file=sys.stderr)
        time.sleep(args.delay)

    print("Done.")


if __name__ == "__main__":
    main()
