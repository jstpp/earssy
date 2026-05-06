from include import db as database
import mysql.connector
import feedparser

def get_context(rss_urls, app):
    context = {'channels': []}

    db = database.get_db(app)
    cursor = db.cursor(dictionary=True, buffered=True)
    cursor.execute(''' INSERT INTO USERS (USER_ID, username, password) VALUES (1, "jean", "1234") ''')
    cursor.execute(''' SELECT * FROM USERS ''')
    result = cursor.fetchall()

    if(len(result)>0):
        print(result)
    else:
        print("0")
        
    for url in rss_urls:
        context['channels'].append(feedparser.parse(url))
    return context