"""Sample scraper for a fictional RTP source.

Replace this module's `scrape_from_html` with real parsing logic using BeautifulSoup.
The functions here return the canonical JSON payload used by the app.
"""
import datetime

def scrape_sample():
    now = datetime.datetime.now().isoformat()
    payload = {
        "timestamp": now,
        "source": "sample-site",
        "games": [
            {"rank":1,"name":"Gates of Olympus 1000™","provider":"Pragmatic Play","rtp":"92.6%","note":"High Multiplier Potential"},
            {"rank":2,"name":"Mahjong Ways 2™","provider":"PG Soft","rtp":"92.1%","note":"Stable Pattern Phase"},
            {"rank":3,"name":"Starlight Princess 1000™","provider":"Pragmatic Play","rtp":"91.8%","note":"Fast Volatility Cycle"}
        ],
        "notes": "BET TERKECIL KE BESAR | 400PERAK UP TO 4.000 RIBU",
        "refined_at": now
    }
    return payload

def scrape_from_html(html_text):
    # TODO: parse real HTML with BeautifulSoup and return canonical payload
    return scrape_sample()
