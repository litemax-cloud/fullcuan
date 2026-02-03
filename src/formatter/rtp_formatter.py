"""Convert canonical payload to Telegram-friendly Markdown text for bot_masterslot333."""
def format_payload(payload):
    lines = []
    lines.append('*RTP SLOT — bot_masterslot333 Update*')
    lines.append('')
    games = payload.get('games', [])
    for g in games:
        lines.append(f"{g.get('rank')}. *{g.get('name')}*\nProvider: {g.get('provider')}\nRTP: {g.get('rtp')} | {g.get('note')}")
        lines.append('')
    lines.append('—————————————')
    lines.append(payload.get('notes',''))
    lines.append('')
    lines.append(f"_Last refined: {payload.get('refined_at')}_")
    text = '\n'.join(lines)
    return text
