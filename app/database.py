from pymongo import MongoClient

# Initialize MongoDB client and connect to the database
client = MongoClient("mongodb://localhost:27017")
db = client.Client_data

# Define collections used in the application
users_collection = db.get_collection("users")
linked_ids_collection = db.get_collection("linked_ids")
