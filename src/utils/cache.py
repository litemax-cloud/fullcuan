import json
from pathlib import Path

def load_cache(path='./data/cache.json'):
    p = Path(path)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding='utf8'))
    except Exception:
        return {}

def save_cache(data, path='./data/cache.json'):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf8')
