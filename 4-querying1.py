import os
import pprint

from pymongo import MongoClient
from dotenv import load_dotenv

#import objectID from bson package (part of pymongo distr) to enable querying by objectID
from bson.objectid import ObjectId

load_dotenv()
MONGODB_URI = os.environ.get("MONGODB_URI")

client = MongoClient(MONGODB_URI)
db = client.bank
accounts = db.accounts

#query by objectID
document_to_find = {"_id": ObjectId("69ec12a3f56b752f241c4bd6")}

#write an expression to retrieve the doc matching the query constraints 
result = accounts.find_one(document_to_find)
pprint.pprint(result)

client.close()
