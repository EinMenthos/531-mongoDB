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
document_to_delete = {"_id": ObjectId("69ec12a3f56b752f241c4bd6")}

# search the doc to delete
print("search doc to delete...")
pprint.pprint(accounts_collection.find_one(document_to_delete))


#write the expression to delete the doc
result = accounts_collection.delete_one(document_to_delete)

#search for the doc after delete
print("still there???")
pprint.pprint(accounts_collection.find_one(document_to_delete))

print("Docs deleted: " + str(result.deleted_count))

client.close()

