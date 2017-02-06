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
    student = student.update({'courses':[]})    
    print student
    print "whats in student"
    print student
    for course in g:
        print course
        if student['id'] == course['id']:
            student[courses] = student[courses].append({ course['code'] : course['mark']})
    ourDB.students.insert_one( student )
