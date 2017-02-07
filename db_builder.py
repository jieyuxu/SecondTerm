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
t = csv.DictReader(tObj) #teachers dict                                                                                                                                                                      
                                          
for teacher in t:
    teacher['students'] = []
    gObj = open("courses.csv")
    g = csv.DictReader(gObj) 
    
    for course in g:                                                                                                                                                                                                     
        for student in d:
            student['courses'] = []
                #print course                                                                                                                                                                                       
            if student['id'] == course['id']:
                student['courses'].append({ course['code'] : course['mark']})

        if course['code'] == teacher['code']:
            teacher['students'].append(student['name'])
                                             
        print student
        ourDB.students.insert_one( student )

    print teacher
    ourDB.teachers.insert_one( teacher )
