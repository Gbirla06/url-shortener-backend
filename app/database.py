import os
from pymongo import MongoClient

MONGO_URL = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URL, tls=True)

db = client.url_shortener
urls_collection = db.urls
