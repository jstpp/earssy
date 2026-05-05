from flask import Flask, render_template, request, session
import feedparser

app = Flask(__name__)

@app.route("/", methods=['GET'])
def site_main():
    rss_urls = ["https://feeds.bbci.co.uk/news/rss.xml",
                "https://www.polsatnews.pl/rss/swiat.xml"] # Temporary URLs for initial setup. Will be replaced by mysql database.

    context = {'channels': []}

    for url in rss_urls:
        context['channels'].append(feedparser.parse(url))

    return render_template('index.html', **context)