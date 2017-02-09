import os

from flask import Flask
# import TixScraper

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/events')
def events():
    return "not implemented"


if __name__ == '__main__':
    # TixScraper.schedule_scrape_job()
    port = int(os.environ.get('PORT', 5000))
    app.run()
