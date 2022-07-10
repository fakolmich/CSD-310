from pymongo import MongoClient
url= "mongodb+srv://admin:admin123@cluster0.dwrx5.mongodb.net/?retryWrites=true&w=majority"
client  = MongoClient(url)
db = client.pytech
print(db.list_collection_names)