from bson.son import SON
from pymongo import MongoClient
from texttable import Texttable
t = Texttable()

client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]

def query2():
    name = input("Enter the name of player whose weak skills you need to find:")

    pipeline1 = [

        {
            u"$match": {
                u"short_name": u"" + name
            }
        },
        {
            u"$group": {
                u"_id": u"$long_name",
                u"overall": {
                    u"$first": u"$overall"
                },
                u"pace": {
                    u"$first": u"$pace"
                },
                u"shooting": {
                    u"$first": u"$shooting"
                },
                u"passing": {
                    u"$first": u"$passing"
                },
                u"dribbling": {
                    u"$first": u"$dribbling"
                },
                u"defending": {
                    u"$first": u"$defending"
                },
                u"physic": {
                    u"$first": u"$physic"
                },
                u"lowest": {
                    u"$first": {
                        u"$min": [
                            u"$pace",
                            u"$shooting",
                            u"$passing",
                            u"$dribbling",
                            u"$defending",
                            u"$physic"
                        ]
                    }
                }
            }
        },
        {
            u"$sort": SON([(u"overall", -1)])
        },
        {
            u"$limit": 10
        }
    ]

    cursor1 = collection.aggregate(
        pipeline1,
        allowDiskUse=False
    )

    t.add_row(["Player Name", "Pace", "Shoorting", "Passing", "Dribbbling", "Defending", "Physic"])
    try:
        for doc in cursor1:
            a = doc['lowest']
            if (a == doc['pace']):
                print("\nLacking in Pace.\n")
            elif (a == doc['shooting']):
                print("\nLacking in shooting.\n")
            elif (a == doc['passing']):
                print("\nLacking in passing.\n")
            elif (a == doc['dribbling']):
                print("\nLacking in dribbling.\n")
            elif (a == doc['defending']):
                print("\nLacking in defending.\n")
            elif (a == doc['physic']):
                print("\nLacking in physic.\n")
            t.add_row([doc['_id'], doc['pace'], doc['shooting'], doc['passing'], doc['dribbling'], doc['defending'], doc['physic']])
    finally:
        client.close()
    print(t.draw())

