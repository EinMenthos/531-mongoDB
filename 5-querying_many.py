import os
import pprint

from pymongo import MongoClient
from dotenv import load_dotenv

#import objectID from bson package (part of pymongo distr) to enable querying by objectID
from bson.objectid import ObjectId

load_dotenv()
MONGODB_URI = os.environ.get("MONGODB_URI")

client = MongoClient(MONGODB_URI)
db = client["bank"]
accounts = db["accounts"]

#query by objectID
documents_to_find = {"balance": {"$gt": 4700}}

#write an expression to retrieve the doc matching the query constraints 
cursor = accounts.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()

print ("# of docs found: " + str(num_docs))

client.close()
