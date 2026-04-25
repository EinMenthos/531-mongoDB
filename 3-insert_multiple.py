import datetime
import os

from pymongo import MongoClient
from dotenv import load_dotenv

#dotenv setting variables:
#more info, check previous file

load_dotenv()
MONGODB_URI = os.environ.get("MONGODB_URI")


client = MongoClient(MONGODB_URI)
db = client.bank
account_collection = db.accounts

#this is different!!!
new_accounts = [
{
    "account_holder": "Linus T.",
    "account_id": "MD123",
    "account_type": "checking",
    "balance": 123456,
    "last_updated":datetime.datetime.now(datetime.UTC),
},
{
    "account_holder": "Ada L.",
    "account_id": "MD321",
    "account_type": "savings",
    "balance": 111111,
    "last_updated":datetime.datetime.now(datetime.UTC),
}
]


#also change here
result = account_collection.insert_many(new_accounts)

#and here
document_ids = result.inserted_ids
print("# of docs inserted: " + str (len(document_ids)))
print(f"_id of inserted doc: {document_ids}")



client.close()
