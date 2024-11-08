
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['pdf_pipeline']
collection = db['pdf_summaries']

def update_mongo(metadata, summary, keywords):
    document = {
        "metadata": metadata,
        "summary": summary,
        "keywords": keywords
    }
    collection.insert_one(document)
