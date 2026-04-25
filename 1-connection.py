from pymongo import MongoClient

#MONGODB_URI = "mongodb+srv://tariwu_db_user:BusPbYnX4jNsAfE9@cluster0.zfsqucr.mongodb.net/?appName=Cluster0"
MONGODB_URI = 'mongodb+srv://myAtlasDBUser:myatlas-001@myatlasclusteredu.exvk4ak.mongodb.net'


client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)

client.close()
