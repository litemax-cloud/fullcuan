"""bot_masterslot333 - Telegram poster CLI & helper functions.

Usage:
  python -m src.bot.telegram_bot --postnow
  python -m src.bot.telegram_bot --status
"""
import os
import json
import argparse
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
CACHE_FILE = os.getenv('CACHE_FILE', './data/cache.json')

API_BASE = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def send_message(text, parse_mode='Markdown'):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print('TELEGRAM_TOKEN or CHAT_ID not set; skipping send.')
        return None
    resp = requests.post(f"{API_BASE}/sendMessage", json={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True
    })
    try:
        return resp.json()
    except Exception:
        return {"ok": False, "status_code": resp.status_code, "text": resp.text}

def send_photo(photo_path, caption=None):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print('TELEGRAM_TOKEN or CHAT_ID not set; skipping send_photo.')
        return None
    with open(photo_path, 'rb') as f:
        files = {'photo': f}
        data = {'chat_id': CHAT_ID}
        if caption:
            data['caption'] = caption
        resp = requests.post(f"{API_BASE}/sendPhoto", data=data, files=files)
        try:
            return resp.json()
        except Exception:
            return {"ok": False, "status_code": resp.status_code, "text": resp.text}

def load_cache():
    p = Path(CACHE_FILE)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding='utf8'))
    except Exception:
        return {}

def save_cache(data):
    p = Path(CACHE_FILE)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf8')

def post_payload(payload, with_image=True):
    # payload is canonical dict
    from src.formatter.rtp_formatter import format_payload
    from src.generator.text2image import render_poster

    text = format_payload(payload)
    # compare cache
    cache = load_cache()
    last = cache.get('last_payload')
    if last == payload:
        print('No change since last payload; skipping post.')
        return
    if with_image:
        img = render_poster(payload, out_path='./data/latest_poster.png')
        r = send_photo(img, caption=text)
    else:
        r = send_message(text)
    cache['last_payload'] = payload
    cache['last_post_ts'] = __import__('time').time()
    save_cache(cache)
    print('Posted:', r)
    return r

def get_sample_payload():
    # For demo/testing: reuse scraper sample
    from src.scraper.source_site import scrape_sample
    return scrape_sample()

def cmd_postnow():
    payload = get_sample_payload()
    post_payload(payload, with_image=True)

def cmd_status():
    cache = load_cache()
    print('Cache:', cache)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--postnow', action='store_true')
    parser.add_argument('--status', action='store_true')
    args = parser.parse_args()
    if args.postnow:
        cmd_postnow()
    if args.status:
        cmd_status()
