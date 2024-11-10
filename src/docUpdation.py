# docUpdation.py
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['pdf_pipeline']
collection = db['pdf_summaries']

def update_mongo(metadata, summary, keywords, processing_time):
    document = {
        "metadata": metadata,
        "summary": summary,
        "keywords": keywords,
        "processing_time": processing_time
    }
    collection.insert_one(document)
    print(f"Document for {metadata['name']} inserted successfully.")
