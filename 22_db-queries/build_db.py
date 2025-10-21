# Jake Liu, Bogdan Sotnikov, Joyce Lin, Naomi Kurian
# Lost and Found
# k22:...but Where Are They?
# 10/16/2025
# time spent: 1hr

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events



#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# creates a clean slate basically so that when you run the code it doesn't create duplicates in the tables or throw an error due to duplciate tables
# better way of doing this would be if not exist for the tables and adding something into the code to check for duplicate values before adding but this works too
c.execute("DROP TABLE IF EXISTS roster;")
c.execute("DROP TABLE IF EXISTS courses;")

# creates table for students
command = "CREATE TABLE roster(name TEXT, age INTEGER, id INTEGER);"  # first command creates table (adds the columns and the value types)
c.execute(command) # executes everything in command string with sqlite; will only take one command at a time
with open("students-beeg.csv", "r") as file:
    # uses dictreader to process the csv file into rows with the very first one acting as a header (which essentially becomes the index for each value per row)
    reader = csv.DictReader(file)
    for row in reader:
        command = f"INSERT INTO roster VALUES (\"{row['name']}\", {row['age']}, {row['id']});" # inserts each value into the table in the order that you first dictated when creating the table
        c.execute(command)    # run SQL statement

# creates table for courses
# basically same thing as the table for students but with different values
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);"
c.execute(command)
with open("courses-beeg.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        command = f"INSERT INTO courses VALUES (\"{row['code']}\", {row['mark']}, {row['id']});"
        c.execute(command)    # run SQL statement

c.execute("SELECT name FROM roster;") #getting all the names from roster
names = [name[0] for name in c.fetchall()] #accessing string values in tuples and putting into a list
print("Students: ", names) #printing list of student names

c.execute("SELECT code FROM courses;") #getting course names from courses
course_list = []
for course in c.fetchall(): #adding each unique course name to list
    if not course[0] in course_list: #checking for repitition
        course_list += course  #adding the tuple to the list results in the adding of its string elements so [] not needed
print("Courses: ", course_list) #printing list of courses

c.execute("SELECT name FROM roster WHERE age > 50;") #getting all the names from roster where age > 50
names = [name[0] for name in c.fetchall()] #accessing string values in tuples and putting into a list
print("Students over 50: ", names) #printing list of student names

c.execute("SELECT code, mark FROM courses WHERE id = 3;") #getting courses and grades for specific student/id (id = 3)
grades = []
for grade in c.fetchall(): #adding each grade to list
    grades += [grade[0] + ": " + str(grade[1])] #associating course with grade--[] needed to make string before adding to list
print("Grades for student with id = 3", grades) #printing list of courses and grades

c.execute("SELECT name, id FROM roster WHERE id IN (SELECT id FROM courses WHERE code = 'bio');") #getting names of students with ids that match those associated with bio course
students = []
for kid in c.fetchall(): #adding each kid to list
    students += [kid[0] + ": id = " + str(kid[1])] #associating id with kid
print("Students in bio", students) #printing list of students in bio
#==========================================================

db.commit() #save changes
db.close()  #close database
