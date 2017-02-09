import atexit
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler


def schedule_scrape_job():
    """
    schedules scrape to happen every day at 3:00 AM
    """
    cron = BackgroundScheduler(daemon=True)
    cron.start() # explicitly start cron jobs
    now = datetime.now()

    @cron.scheduled_job("interval", days=1, start_date=now.replace(day=now.day+1, hour=3))
    def scrape():
        """
        Scrape tix to get upcomming events
        """
        print("Hello")

    atexit.register(lambda: cron.shutdown(wait=False))
