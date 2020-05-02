from bson.son import SON
from pymongo import MongoClient
from texttable import Texttable
t = Texttable()

client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]



def query6():
            print("Worst players who should resign")
            cursor = collection.find( { "$and": [ {"age": { "$gt": 30}}, {"overall": { "$lt": 55} } ] } )
            i = 1
            try:
                t.add_row(["Player name","Age","Overall_Rating"])
                for doc in cursor:
                    t.add_row([doc['short_name'],doc['age'],doc['overall']])
                    i = i+1
                print(t.draw())

            finally:
                client.close()
