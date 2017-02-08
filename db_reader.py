from pymongo import MongoClient
import csv

#connect to server on lisa
server = MongoClient('lisa.stuy.edu')
#server = MongoClient()
#open (or create) db

ourDB = server['SecondTerm']
students = ourDB.students.find()

def compAvg(d):
    total = 0.00
    for dic in d:
        for key in dic:
            total += int(dic[key])
    return total / len(d)

for student in students:
    #print compAvg(student["courses"])
    #print student["name"]
    print "name: %s, age: %s, average: %f" % (student["name"], student["id"], compAvg(student["courses"]))
