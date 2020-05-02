from bson.son import SON
from pymongo import MongoClient
from texttable import Texttable
t = Texttable()

client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]

def query5():
    print("List of players which the club ready to sell:")
    print('\n')

    club= input("Club name:")
    pipeline = [
        {
            u"$match": {
                u"overall": {
                    u"$lt": 60.0
                },
                u"club": u""+club
            }
        }, 
        {
            u"$project": {
                u"short_name": 1.0,
                u"age": 1.0,
                u"nationality": 1.0,
                u"club": 1.0,
                u"player_position": 1.0,
                u"overall": 1.0,
                u"player_positions": 1.0,
                u"Average": {
                    u"$avg": [
                        u"$pace",
                        u"$shooting",
                        u"$passing",
                        u"$dribbling",
                        u"$defending",
                        u"$physic"
                    ]
                },
                u"GKavg": {
                    u"$avg": [
                        u"$gk_diving",
                        u"$gk_handling",
                        u"$gk_kicking",
                        u"$gk_reflexes",
                        u"$gk_speed"
                    ]
                }
            }
        }, 
        {
            u"$sort": SON([ (u"overall", 1) ])
        }
    ]

    cursor = collection.aggregate(
            pipeline,
            allowDiskUse = False
            )

    t.add_row(["Name", "Age", "Nationality", "Club", "Performance rating", "Position", "Average skill points"])

    try:
        for doc in cursor:
            if(doc['player_positions'] == 'GK'):
                t.add_row([doc['short_name'], doc["age"], doc['nationality'], doc['club'], doc['overall'], doc['player_positions'], doc['GKavg']])
            else:
                t.add_row([doc['short_name'], doc["age"], doc['nationality'], doc['club'], doc['overall'], doc['player_positions'], doc['Average']])
                 
    finally:
     client.close()

    print(t.draw())

