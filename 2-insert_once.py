import datetime
import os

from pymongo import MongoClient
from dotenv import load_dotenv

#dotenv setting variables:
#dotenv_path = ".env"
#dotenv.set_key =(dotenv_path, "MONGODB_URI", "mongodb+srv://myAtlasDBUser:myatlas-001@myatlasclusteredu.exvk4ak.mongodb.net")

#dotenv using OS variables. At OS, type at terminal:
#MONGODB_URI="mongodb+srv://myAtlasDBUser:myatlas-001@myatlasclusteredu.exvk4ak.mongodb.net"

#to view the variable at terminal, type:
#echo "$MONGODB_URI"

#load config from .env file (no need to create variables at terminal if it is saved at .env)
load_dotenv()
MONGODB_URI = os.environ.get("MONGODB_URI")

#or just type it here
#MONGODB_URI = 'mongodb+srv://myAtlasDBUser:myatlas-001@myatlasclusteredu.exvk4ak.mongodb.net'


#connect to mongodb cluster with mongoclient
client = MongoClient(MONGODB_URI)

#get reference to "bank" db. This is a little different from before
db = client["bank"]

#get reference to "bank"  collection
account_collection = db["accounts"]

new_account = {
    "account_holder": "Linus T.",
    "account_id": "MD123",
    "account_type": "checking",
    "balance": 123456,
    "last_updated":datetime.datetime.now(datetime.UTC),
}

#expression that inserts 'new_account' doc into acocunts collection
result = account_collection.insert_one(new_account)

document_id = result.inserted_id
print(f"_id of inserted doc: {document_id}")

client.close()
