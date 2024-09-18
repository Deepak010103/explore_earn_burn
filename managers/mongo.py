from pymongo import MongoClient
from config import CONFIG

class Mongo:
    client = MongoClient(CONFIG.get("MONGO_URI"))
    db = client[CONFIG.get('DB')]

    @classmethod
    def get_users(cls):
        users = cls.db['users']
        records = users.find()
        
        records = [{
            "reference_id":record.get("reference_id"),
            "user_id":record.get("user_id"),
            "provider":record.get("provider"),
            "last_webhook_update":record.get("last_webhook_update"),
            "created_at":record.get("created_at"),
            "active":record.get("active")
        } for record in records]
        
        return records
    
    @classmethod
    def push_queue(cls,event):
        queue = cls.db['queue']
        result = queue.insert_one(event)
        print(result)
        return str(result.inserted_id)

