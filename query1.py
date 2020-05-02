from bson.son import SON
from pymongo import MongoClient
from texttable import Texttable
t = Texttable()


client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]



def query1():

    cursor = collection.distinct("nationality")
    nationality = []
    try:
        for doc in cursor:
            nationality.append(doc)
    finally:
        client.close()

    name = input("Enter nationality:")

    pipeline = [
        {"$match":{"nationality":name}},
        {"$group":{"_id":"$short_name", "Nation":{"$first":"$nationality"}, 
        "Overall":{"$first":"$overall"}}}, 
        {"$sort":{"Overall":-1}},
        {"$limit":10}
    ]

    cursor1 = collection.aggregate(
        pipeline, 
        allowDiskUse = False
    )

    t.add_row(["Player Name", "Performance rating"])
    try:
        for doc1 in cursor1:
            t.add_row([doc1['_id'],doc1['Overall']])
    finally:
        client.close()
    print(t.draw())

