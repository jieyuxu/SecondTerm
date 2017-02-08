from pymongo import MongoClient
import csv
#connect to server on lisa
server = MongoClient('lisa.stuy.edu')
#server = MongoClient()
#open (or create) db
ourDB = server['SecondTerm']
fObj = open("peeps.csv")

d = csv.DictReader(fObj) #students dict

tObj = open("teachers.csv")
t = csv.DictReader(tObj)
                                                                                                                                                                                                      
for student in d:
    student['courses'] = []
    #print course   
    gObj = open("courses.csv")
    g = csv.DictReader(gObj) 
                                                                                                                                                                                        
    for course in g: 

        if student['id'] == course['id']:
            student['courses'].append({ course['code'] : course['mark']})
        
    for teacher in t:
        teacher['students'] = []
                
        #print course['code'], teacher['code']
        if course['code'] == teacher['code']:
            teacher['students'].append(student['name'])
            print teacher
                                             
        #print student
        #ourDB.students.insert_one( student )

    print teacher
    #ourDB.teachers.insert_one( teacher )

