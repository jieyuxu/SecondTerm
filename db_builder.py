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
    gObj = open("courses.csv")                                                                                                                                                                              
    g = csv.DictReader(gObj)                                                                                                                                                                                
                                                                                                                                                                                                             
    #print student.keys()                                                                                                                                                                                   
                                                                                                                                                                                                             
    for course in g:                                                                                                                                                                                        
                                                                                                                                                                                                             
         #print course                                                                                                                                                                                       
        if student['id'] == course['id']:                                                                                                                                                                   
             student['courses'].append({ course['code'] : course['mark']})                                                                                                                                   
                                                                                                                                                                                                             
    #print student                                                                                                                                                                                           
    ourDB.students.insert_one( student )      
