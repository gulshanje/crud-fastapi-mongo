from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
connection = MongoClient(os.getenv("mongoClient"))