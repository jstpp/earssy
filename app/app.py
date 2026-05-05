from flask import Flask, render_template, request, session
import feedparser

app = Flask(__name__)

@app.route("/", methods=['GET'])
def site_main():
    rss_url = "https://feeds.bbci.co.uk/news/rss.xml" # Temporary URL for initial setup. Will be replaced by mysql database.
    context = feedparser.parse(rss_url)

    return render_template('index.html', **context)