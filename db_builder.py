from pymongo import MongoClient
import csv

#connect to server on lisa
server = MongoClient('lisa.stuy.edu')
#server = MongoClient()

#open (or create) db
ourDB = server['SecondTerm']

fObj = open("peeps.csv") 
d = csv.DictReader(fObj) #students dict

gObj = open("courses.csv")
g = csv.DictReader(gObj) #course dict

for student in d:
    gObj = open("courses.csv")
    g = csv.DictReader(gObj)
    for course in g:
        if student['id'] == course['id']:
            student[ course['code'] ] = course['mark']
    print student
    ourDB.students.insert_one( student )
