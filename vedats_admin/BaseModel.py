from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import click

import os
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 
# MongoDB setup
password = os.getenv("PASSWORD")
username = os.getenv("USERNAME")
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.tduqnwp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["Official"]

class Poet:
    collection = db["Poet"]

    @classmethod
    def is_poet_in_db(cls, poet):
        poet_find = cls.collection.find_one({"name": poet})
        return poet_find is not None  
    
    @classmethod 
    def get_poet_id(cls, poet):
        poet_find = cls.collection.find_one({"name": poet})
        return poet_find['_id']
    
    @classmethod
    def add(cls, poet):
        poet_insert = cls.collection.insert_one({"name":poet})
        return [poet_insert.inserted_id, f'Poet "{poet}" added!']
    
class Poem:
    collection_poem = db["Poem"]
    collection_poet = db["Poet"]
    @classmethod
    def add(cls, poem, poet):
        if cls.poem_not_in_db(poem):
            if Poet.is_poet_in_db(poet):
                poem_insert = cls.collection_poem.insert_one({"poet_id":Poet.get_poet_id(poet),
                                                            "title": "",
                                                            "poem":poem})
                if poem_insert.inserted_id:
                    return f'Poet exists, poem added, id: {poem_insert.inserted_id}'
            else: 
                [poet_id, poet_m] = Poet.add(poet)
                poem_insert = cls.collection_poem.insert_one({"poet_id":ObjectId(poet_id),
                                                "title": "",
                                                "poem":poem})
                if poem_insert.inserted_id:
                    return f'{poet_m}, poem added, id:{poem_insert.inserted_id}'               
                
        else:
            return f"Poem({poem[0:30]}) is in the database"

    @classmethod
    def poem_not_in_db(cls, poem):
        poem_find = cls.collection_poem.find_one({"poem": poem})
        return poem_find is None 

