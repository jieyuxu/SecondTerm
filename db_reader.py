from pymongo import MongoClient
import csv

#connect to server on lisa
server = MongoClient('homer.stuy.edu')
#server = MongoClient()

#open (or create) db
ourDB = server['SecondTerm']

students = ourDB.students.find()

for student in students:
    
    print student
    
