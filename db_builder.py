from pymongo import MongoClient
import csv

#connect to server on lisa
server = MongoClient('lisa.stuy.edu')

#open (or create) db
ourDB = c.('SecondTerm')

fObj = open("peeps.csv") 
d = csv.DictReader(fObj) #students dict

gObj = open("courses.csv")
g = csv.DictReader(gObj) #course dict
