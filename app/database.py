import os
from pymongo import MongoClient

# Retrieve the MongoDB URI from environment variables
MONGO_URL = os.getenv('MONGO_URI')

# Initialize the MongoDB client with the retrieved URI
client = MongoClient(MONGO_URL, tls=True)

# Access the 'url_shortener' database
db = client.url_shortener

# Access the 'urls' collection within the 'url_shortener' database
urls_collection = db.urls
