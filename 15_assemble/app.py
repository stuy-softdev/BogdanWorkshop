# Amy Shrestha, Bogdan Sotnikov, Haowen Xiao
# Software Developers
# SoftDev
# K11 -- softserve
# 2025-10-01
# time spent: 0.5


'''
We took our code for the last assignment that tasked us with displaying the dictionary. This time, we modified the code to
parse the csv into a dictionary, where the values corresponding to each of the keys are arrays of the rate and the link.
For the links, we chose a database available on the website of the Department of Labor, where, conveniently, there was a
section for each of the industries mentioned in the original csv. We amended the template to take the keys and values from the
dictionary and create a table out of them.
'''

from flask import Flask, render_template
import random

app = Flask(__name__)            # create instance of class Flask


# Open file, read it
file = open("data/occupations.csv", "r")
content = file.read()

# split the string by newlines into a list, remove extra items (total, empty lines, etc.)
splitter = content.split("\n")
splitter = splitter[1:-2]

# turn the list into a dictionary by splitting by last comma
d = {}
weighted_l = []
for i in range(len(splitter)):
    #print(splitter[i])
    comma2 = splitter[i].rindex(',')
    comma1 = splitter[i][0:comma2].rindex(',')
    # create each dictionary key:value with type casting to convert string into a float
    d[splitter[i][0:comma1].replace("\"", "")] = [splitter[i][comma1+1:comma2], splitter[i][comma2+1:]]
    
    # create list with percentages of weights
    weighted_l.append(float(splitter[i][comma1+1:comma2]))

@app.route("/wdywtbwygp")
def occ_print():
    # randomly choose one key value from the weighted list
    job = random.choices(list(d.keys()), weights = weighted_l)[0]

    # access value of key item from dictionary
    rate = d.get(str(job))
    
    return render_template('tablified.html', title="Occupations", dictionary = d, randJob = job, randRate = rate)


if __name__ == "__main__":
    #app.debug = True
    app.run(port=8080)
