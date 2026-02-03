# bot_masterslot333 - RTP Auto Text Telegram Bot (Starter, Ready-to-deploy)

This repository is a **ready-to-run starter** for a Telegram bot that auto-posts RTP slot updates
to a Telegram group/chat. The project is intentionally minimal, modular, and safe to deploy.

**Project name:** bot_masterslot333

## What's included
- `src/` Python source (scraper, formatter, generator, bot, scheduler)
- `Dockerfile` for containerized deployment
- GitHub Actions CI workflow (lint & tests)
- `.env.example` for local configuration
- `requirements.txt` with needed packages
- `CODEOWNERS`, `CONTRIBUTING.md`, `SECURITY.md`
- Example tests and a simple Pillow-based poster generator (no external API)

## Quick local run
1. Copy `.env.example` -> `.env` and fill values (TELEGRAM_TOKEN, TELEGRAM_CHAT_ID etc).
2. Create and activate virtualenv:
   ```
   python -m venv .venv
   source .venv/bin/activate   # windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Try a single post (uses sample payload):
   ```
   python -m src.bot.telegram_bot --postnow
   ```
4. Start scheduler (runs periodic jobs):
   ```
   python -m src.scheduler
   ```

## Deployment
- Build Docker image and deploy (Render, Railway, VPS, etc.). Provide environment variables via service secrets.
- Do **not** commit `.env` or tokens.

## Notes
- Replace `src.scraper/source_site.py` with real scraping logic for your source site.
- `src/generator/text2image.py` renders a simple poster using Pillow; replace fonts/assets for a better look.
