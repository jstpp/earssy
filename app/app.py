from flask import Flask, render_template, request, session
import mysql.connector
import feedparser

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'earssy_db'
app.config['MYSQL_PASSWORD'] = 'earssy_db'
app.config['MYSQL_DB'] = 'earssy_db'

#db = mysql.connector.connect(user=app.config['MYSQL_USER'], password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])
#cursor = db.cursor(dictionary=True, buffered=True)

rss_urls = ["https://feeds.bbci.co.uk/news/rss.xml",
            "https://www.polsatnews.pl/rss/swiat.xml"] # Temporary URLs for initial setup. Will be replaced by mysql database.

def get_context(rss_urls):
    context = {'channels': []}
    for url in rss_urls:
        context['channels'].append(feedparser.parse(url))
    return context

context = get_context(rss_urls)

@app.route("/", methods=['GET'])
def site_main():
    return render_template('index.html', **context)


@app.route("/profile", methods=['GET'])
def profile():
    return render_template('profile.html', **context)