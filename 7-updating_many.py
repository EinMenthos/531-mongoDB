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
select_accounts = {"account_type": "savings"}

#update. note that this variable does not exist, so we use "$set" to create it.
set_field = {"$set": {"minimum_balance": 100}}

#write expression that adds to the minimum balance field to each saving accounts and set its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Docs matched: " + str(result.matched_count))
print("Docs updated: " + str(result.modified_count))

pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()

