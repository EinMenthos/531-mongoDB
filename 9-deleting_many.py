import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)
db = client.bank
accounts_collection = db.accounts

#filter by objectid
documents_to_delete = {"balance": {"$lt": 2000}}

# search the doc to delete
print("search doc to delete...")
pprint.pprint(accounts_collection.find_one(documents_to_delete))


#write the expression to delete the doc. IF IT IS EMPTY, THE DB will be ERASED!
result = accounts_collection.delete_many(documents_to_delete)

#search for the doc after delete
print("still there???")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print("Docs deleted: " + str(result.deleted_count))

client.close()

