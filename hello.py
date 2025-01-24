from pymongo import MongoClient

try:
    # Create a MongoDB client
    uri = "mongodb://root:example@localhost:27017/"
    client = MongoClient(uri)
    print("Connected successfully!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    exit(1)

