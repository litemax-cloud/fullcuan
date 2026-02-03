"""Scheduler that triggers scraper -> post pipeline using APScheduler for bot_masterslot333."""
import os
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler
from src.bot.telegram_bot import post_payload, get_sample_payload
from src.utils.logger import get_logger

load_dotenv()
log = get_logger('scheduler')
interval = int(os.getenv('UPDATE_INTERVAL_MIN', '30'))

def job():
    try:
        payload = get_sample_payload()
        post_payload(payload, with_image=True)
    except Exception as e:
        log.exception('Job failed: %s', e)

if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_job(job, 'interval', minutes=interval)
    log.info('Scheduler started with interval %s minutes', interval)
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        log.info('Scheduler stopped.')
