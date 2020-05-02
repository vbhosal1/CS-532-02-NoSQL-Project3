import sys
from pymongo import MongoClient
from bson.son import SON
import query1 as q1
import query2 as q2
# import query3 as q3
import query4 as q4
import query5 as q5
import query6 as q6
import query7 as q7
import query8 as q8
import query9 as q9



client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]


def menu(ch):
        if ch==1:
            q1.query1()
        elif ch==2:
            q2.query2()
        elif ch==3:
            q4.query4()
        elif ch==4:
            q5.query5()
        elif ch==5:
            q6.query6()
        elif ch==6:
            q7.query7()
        elif ch==7:
            q8.query8()
        elif ch==8:
            q9.query9()
        elif ch==0:
            sys.exit()
        elif ch==99:
            print("1. \n2. \n3. \n4. \n5. \n6. \n7. \n8. \n9.\n99. Menu\n")

        else:
            print("Invalid input")



print("\nWelcome to world soccer infotainment wizard!\n")
print("1. \n2. \n3. \n4. \n5. \n6. \n7. \n8. \n9.\n")
s=1
while 1:
    s = int(input("Choose Operation: "))
    menu(s)




