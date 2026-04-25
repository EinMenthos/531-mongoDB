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

#filter
document_to_update = {"_id": ObjectId("69ec12a3f56b752f241c4bd6")}

#update
add_to_balance = {"$inc": {"balance": 1}}

#print original balance
pprint.pprint(accounts_collection.find_one(document_to_update))

#write exp to adds to the balance + what to change
result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Doc updated: " + str(result.modified_count))

#print updated balance
pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()

