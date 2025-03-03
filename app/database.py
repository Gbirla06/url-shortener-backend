from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "url_shortener"

client = AsyncIOMotorClient(MONGO_URI)  # Async MongoDB connection
database = client[DB_NAME]
urls_collection = database["urls"]