# Jake Liu, Bogdan Sotnikov, Joyce Lin, Naomi Kurian
# Lost and Found
# k21: All Your Database are belong to us
# 10/15/2025
# time spent: 30 mins

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
command = "CREATE TABLE roster(name TEXT, age INTEGER, userid INTEGER);"  # first command creates table (adds the columns and the value types)
c.execute(command) # executes everything in command string with sqlite; will only take one command at a time
with open("students.csv", "r") as file:
    # uses dictreader to process the csv file into rows with the very first one acting as a header (which essentially becomes the index for each value per row)
    reader = csv.DictReader(file)
    for row in reader:
        command = f"INSERT INTO roster VALUES (\"{row['name']}\", {row['age']}, {row['id']});" # inserts each value into the table in the order that you first dictated when creating the table
        c.execute(command)    # run SQL statement

# creates table for courses
# basically same thing as the table for students but with different values
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);"
c.execute(command)
with open("courses.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        command = f"INSERT INTO courses VALUES (\"{row['code']}\", {row['mark']}, {row['id']});"
        c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
