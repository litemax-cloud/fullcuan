from src.scraper.source_site import scrape_sample, scrape_from_html
def test_scrape_sample():
    p = scrape_sample()
    assert 'games' in p
    assert isinstance(p['games'], list)
    assert p['games'][0]['name'].startswith('Gates')
def test_scrape_from_html():
    html = '<html><body>dummy</body></html>'
    p = scrape_from_html(html)
    assert p['source'] == 'sample-site'
