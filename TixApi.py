import os

from flask import Flask
from dotenv import load_dotenv, find_dotenv
import TixScraper

app = Flask(__name__)

# get .env folder
load_dotenv(find_dotenv())


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/events')
def events():
    return "not implemented"


if __name__ == '__main__':
    TixScraper.schedule_scrape_job()
    myPort = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=myPort)
