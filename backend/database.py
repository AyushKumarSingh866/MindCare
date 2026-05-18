import asyncio
import uuid

class MockCursor:
    def __init__(self, data):
        self.data = data
        
    def sort(self, key, direction):
        if key == "created_at":
            self.data.sort(key=lambda x: x.get(key, 0), reverse=(direction == -1))
        return self
        
    def limit(self, limit_val):
        self.data = self.data[:limit_val]
        return self
        
    async def to_list(self, length=None):
        return self.data

class MockCollection:
    def __init__(self):
        self.data = []
        
    async def find_one(self, query):
        for item in self.data:
            match = True
            for k, v in query.items():
                if item.get(k) != v:
                    match = False
                    break
            if match:
                return dict(item)
        return None
        
    async def insert_one(self, doc):
        doc["_id"] = str(uuid.uuid4())
        self.data.append(dict(doc))
        class Result:
            inserted_id = doc["_id"]
        return Result()
        
    def find(self, query):
        results = []
        for item in self.data:
            match = True
            for k, v in query.items():
                if item.get(k) != v:
                    match = False
                    break
            if match:
                results.append(dict(item))
        return MockCursor(results)
        
    def aggregate(self, pipeline):
        match_query = pipeline[0]["$match"]
        group_id = pipeline[1]["$group"]["_id"]
        # simplified aggregation for stats
        results = {}
        for item in self.data:
            match = True
            for k, v in match_query.items():
                if item.get(k) != v:
                    match = False
                    break
            if match:
                val = item.get(group_id[1:]) if group_id.startswith("$") else item.get(group_id)
                results[val] = results.get(val, 0) + 1
        
        final_res = [{"_id": k, "count": v} for k, v in results.items()]
        return MockCursor(final_res)

class MockDB:
    def __init__(self):
        self.users = MockCollection()
        self.predictions = MockCollection()

db = MockDB()

async def connect_to_mongo():
    print("Using Mock In-Memory MongoDB for local testing")

async def close_mongo_connection():
    print("Closed Mock MongoDB")

def get_database():
    return db
