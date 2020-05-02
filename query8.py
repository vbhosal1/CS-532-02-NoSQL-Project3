from pymongo import MongoClient
from bson.son import SON
from texttable import Texttable
t = Texttable()

client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]

"""players that offer best value for money(value divided by rating)
    also only for players that have rating greater than 80 and that do not have null values for value_eur"""
def query8():
    cursor = collection.aggregate( [ { "$match": { "overall": { "$gt" : 80.0 } } }, { "$match": {"value_eur": { "$gt" : 1000 }} }, { "$project": { "short_name": 1,"overall": 1, "value_eur": 1, "value_for_money": { "$divide": [ "$value_eur", "$overall" ] }   } },{ "$sort": { "value_for_money": 1} }, {"$limit": 20} ] )
    i=1

    t.add_row([" ", "Name", "Value in eur", "Performance rating"])

    try:
        for doc in cursor:
            t.add_row([i, doc['short_name'], doc['value_eur'] ,doc['overall']])
            i=i+1

    finally:
        client.close()

    print(t.draw())