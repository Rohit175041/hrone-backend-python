from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def connect_db():
    try:
        mongo_uri = os.getenv("MONGO_URI")
        db_name = os.getenv("DB_NAME")

        if not mongo_uri or not db_name:
            raise ValueError("Missing MONGO_URI or DB_NAME")

        client = MongoClient(mongo_uri)
        db = client[db_name]
        print(f"MongoDB connected to '{db_name}'")
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        exit(1)

# ✅ Global collections for direct import
_db = connect_db()
orders_col = _db["orders"]
products_col = _db["products"]
