        """Render a simple poster image using Pillow for bot_masterslot333.

        Produces a PNG with title and list items. Replace fonts/assets as needed.
"""
        from PIL import Image, ImageDraw, ImageFont
        import textwrap
        from pathlib import Path

        def render_poster(payload, out_path='latest_poster.png', width=640, height=720):
            title = f"RTP SLOT — {payload.get('refined_at','')}"
            games = payload.get('games', [])
            lines = [title, '']
            for g in games:
                lines.append(f"{g.get('rank')}. {g.get('name')} — {g.get('rtp')} | {g.get('provider')}")
            lines.append('')
            lines.append(payload.get('notes',''))

            # Create image
            img = Image.new('RGB', (width, height), color=(18, 24, 33))
            draw = ImageDraw.Draw(img)

            try:
                font_title = ImageFont.truetype('DejaVuSans-Bold.ttf', 20)
                font_body = ImageFont.truetype('DejaVuSans.ttf', 14)
            except Exception:
                font_title = ImageFont.load_default()
                font_body = ImageFont.load_default()

            y = 16
            padding = 16
            for i, line in enumerate(lines):
                if not line:
                    y += 8
                    continue
                wrap = textwrap.wrap(line, width=40)
                for sub in wrap:
                    if i == 0:
                        draw.text((padding, y), sub, font=font_title, fill=(255, 215, 0))
                        y += font_title.getsize(sub)[1] + 6
                    else:
                        draw.text((padding, y), sub, font=font_body, fill=(230, 230, 230))
                        y += font_body.getsize(sub)[1] + 4
                y += 2

            out = Path(out_path)
            out.parent.mkdir(parents=True, exist_ok=True)
            img.save(out)
            return str(out)
