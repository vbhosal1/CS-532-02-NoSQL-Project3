from pymongo import MongoClient
from bson.son import SON
from texttable import Texttable
t = Texttable()

client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]


"""teams that perform best in the selected skill.
    by adding the skill points of all players per team
"""

def query7():
        name = input("Which skill: ")

        pipeline = [
            {
                u"$group": {
                    u"_id": u"$club",
                    u"total": {
                        u"$sum": u"$"+name
                    }
                }
            },
            {
                u"$sort": SON([ (u"total", -1) ])
            },
            {
                u"$limit": 5.0
            }
        ]
        cursor = collection.aggregate(
            pipeline
        )
        i = 1

        t.add_row([" ", "Team Name"])
        try:
            for doc in cursor:
                t.add_row([i, doc['_id']])
                i = i+1

        finally:
            client.close()

        print(t.draw())