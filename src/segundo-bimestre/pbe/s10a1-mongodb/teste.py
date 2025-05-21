
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dielme:1234@cluster0.g8uqx.mongodb.net/"
client = MongoClient(uri, server_api=pymongo.server_api.ServerApi(
   version="1", strict=True, deprecation_errors=True))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)