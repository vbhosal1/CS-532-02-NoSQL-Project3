from bson.son import SON
from pymongo import MongoClient
from texttable import Texttable
t = Texttable()

client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]


def query4():
    print("List of top 10 best goalkeeper:")
    pipeline = [
        {
            u"$match": {
                u"player_positions": u"GK"
            }
        },
        {
            u"$project": {
                u"short_name": 1.0,
                u"Score": {
                    u"$avg": [
                        u"$gk_diving",
                        u"$gk_handling",
                        u"$gk_kicking",
                        u"$gk_reflexes"
                    ]
                }
            }
        },
        {
            u"$sort": SON([ (u"Score", -1) ])
        },
        {
            u"$limit": 10.0
        }
    ]

    cursor = collection.aggregate(
        pipeline,
        allowDiskUse = False
    )

    t.add_row(["Player Name", "Score"])

    try:
        for doc in cursor:
            t.add_row([doc['short_name'], doc['Score']])
    finally:
        client.close()
    print(t.draw())

