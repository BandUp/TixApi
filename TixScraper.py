import atexit
from urllib import request
import json
from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from pprint import pprint


def schedule_scrape_job():
    """
    schedules scrape to happen every day at 3:00 AM
    """
    cron = BackgroundScheduler(daemon=True)
    cron.start()  # explicitly start cron jobs
    now = datetime.now()

    def parse_item(item):
        """
        Parse item and send data to db
        :param item: container for data from tix
        """
        # TODO: implement
        pprint(item)

    @cron.scheduled_job("interval", days=30, start_date=now.replace(day=now.day+1, hour=3))
    def scrape():
        """
        Scrape tix to get upcomming events
        """
        # load resource
        res = request.urlopen(os.getenv("TIX_URL", ""))

        # check charset
        encoding = res.info().get_content_charset('utf-8')

        # extract data
        data = json.loads(res.read().decode(encoding))

        for item in data:
            # TODO: take information from item and place in db
            parse_item(item)

    # hook cron shutdown to program exit so we don't leak memory
    atexit.register(lambda: cron.shutdown(wait=False))
