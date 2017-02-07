from pymongo import MongoClient
import csv

#connect to server on lisa
server = MongoClient('lisa.stuy.edu')
#server = MongoClient()

#open (or create) db
ourDB = server['SecondTerm']

fObj = open("peeps.csv") 
d = csv.DictReader(fObj) #students dict

for student in d:
    student['courses'] = []   
    #print "student: ", student
    
    #you have to re-open this before ever itteration
    gObj = open("courses.csv")
    g = csv.DictReader(gObj) #course dict
    for course in g:
        #print "course: ", course
        if student['id'] == course['id']:
            student['courses'].append( { course['code']: course['mark'] } )
    #print "adding this student doc to db: ", student
    ourDB.students.insert_one( student )
