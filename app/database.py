from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.Client_data

users_collection = db.get_collection("users")
linked_ids_collection = db.get_collection("linked_ids")
