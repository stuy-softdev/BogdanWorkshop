# Amy Shrestha, Bogdan Sotnikov, Haowen Xiao
# Software Developers
# SoftDev
# K11 -- softserve
# 2025-09-28
# time spent: 0.5


'''
Our team decided to borrow the code from our previous assignment, 08_stream-proc in order
to read a CSV file, and create a dictionary separated by newlines and commas. To do that,
we opened, read and split the file with newlines to create a list of strings of each line. Then,
we sliced out the unnecessary data (first line, last line, extra newline) before looping over
each list item to then create a dictionary key:value pair for each list item. In addition to that,
we created a list of weighted values by adding in the value for each dictionary item. Finally,
to choose a weighted pair of key:value from the dictionary, we used the random.choices() method's
weighted parameter to choose a key value from the dictionary, which we then used to get the corresponding
value for that key. This would work because from 3.7 and onwards, Python dictionaries are ordered.

We combined this career_chooser code with flask by simply adding in the import flask statement, the
object creation statement 'app = Flask(__name__)' and made sure to create a new function
that was able to return the items necessary for the task, putting it right under the line
'@app.route("/").' Then, we simply used HTML code to create stylized headings and line breaks, before
adding in the if statement from the flask code.
'''

from flask import Flask
import random

app = Flask(__name__)            # create instance of class Flask


# Open file, read it
file = open("occupations.csv", "r")
content = file.read()

# split the string by newlines into a list, remove extra items (total, empty lines, etc.)
splitter = content.split("\n")
splitter = splitter[1:-2]


# turn the list into a dictionary by splitting by last comma
d = {}
weighted_l = []
for i in range(len(splitter)):
    #print(splitter[i])
    comma = splitter[i].rindex(',')
    
    # create each dictionary key:value with type casting to convert string into a float
    d[splitter[i][0:comma].replace("\"", "")] = float(splitter[i][comma+1:])
    
    # create weighted list with percentages of weights
    weighted_l.append(float(splitter[i][comma+1:]))

@app.route("/")
def occ_print():
    # randomly choose one key value from the weighted list
    job = random.choices(list(d.keys()), weights = weighted_l)[0]

    # access value of key item from dictionary
    rate = d.get(str(job))
    string = "<h2>Roster:</h2>Amy Shrestha, Bogdan Sotnikov, Haowen Xiao<br><h2>TNPG:</h2>Software Developers<br><br><h2>List of Occupations: </h2>" + str(d) + f"<br><br><h2>Random Item:</h2> {job}: {rate}"
    return string

if __name__ == "__main__":
    app.debug = True
    app.run()