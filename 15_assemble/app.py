# Amy Shrestha, Bogdan Sotnikov, Haowen Xiao
# Software Developers
# SoftDev
# K15 -- assemble
# 2025-10-01
# time spent: 2.0

'''
After borrowing our code from our previous assignments, we planned the process and read the
instructions. Knowing that we needed to use knowledge from previous assignments, we opened up
relevant files on our computer too. We also made sure to read the Jinja2 documentation for ideas
on how to use the engine as well as how to use it to develop our plan.

Then, we got started on our code. We first created all the necessary files then worked on finalizing
the html file, where we experimented with Jinja2's code, then adding the necessary parts of the
lab, making sure we used html code to create our title, heading, TNPG+roster onto the website. However,
we had to refresh some of our knowledge on creating tables in html, so we looked into that before
editing our html file to create tables using our Python values. Also, we searched for ways to
use for loops in dictionaries in the Jinja2 documentation, where we found our current code. After
completing step 2, we read the "egoless programming" excerpt before going onto adding links to our
csv file.

Although we had trouble adding links, we found a very expansive network of occupations for each
field on the occupational outlook handbook in the US bureau of labor's website, where we quickly
searched up each field and added links to them. At first, we used the Numbers app on our computers
but found out that it couldn't be saved as a csv file anymore. After a long time troubleshooting,
we found we could edit the csv file properly in Microsoft Excel, so we transferred our work onto
there. Finally, we edited our Python code to properly parse both the percentage and link as a
dictionary as a value inside the main dictionary key:value pair of the occupations:value as
well as edit our route, before finally using render_template to pass in the necessary values.

'''

from flask import Flask, render_template
import random

app = Flask(__name__)            # create instance of class Flask


# Open file, read it
file = open("data/occupations.csv", "r")
content = file.read()

# split the string by newlines into a list, remove extra items (total, empty lines, etc.)
splitter = content.split("\n")
# remove first row of titles and last rows with total and extra newline
splitter = splitter[1:-2]

string = ""

# turn the list into a dictionary by splitting by last comma
d = {}
weighted_l = []

for i in range(len(splitter)):
    # find where the comma splitting percentage and link is
    comma = splitter[i].rindex(',')
    
    # find where the comma splitting occupation and percentage is
    secondcomma = splitter[i].rfind(',', 0, comma)
    
    # create each dictionary key:value with type casting to convert string into a float
    occupation = splitter[i][0:secondcomma].replace("\"", "")
    percentage = float(splitter[i][secondcomma+1:comma])
    weblink = splitter[i][comma+1:].strip()
    
    # create key:value pair in dictionary
    d[occupation] = {"percentage":percentage, "link":weblink}
    
    # create weighted list with percentages of weights
    weighted_l.append(percentage)

file.close()
print(d)

# set website page to http://127.0.0.1:8080/wdywtbwygp
@app.route("/wdywtbwygp")
def occ_print():
    # randomly choose one key value from the weighted list
    job = random.choices(list(d.keys()), weights = weighted_l)[0]

    # access value of key item from dictionary
    rate = d[job]["percentage"]
    
    # access the correct link
    link = d[job]["link"]
    
    # use the template called tablified.html to format page
    return render_template('tablified.html', title="Occupations",
                           dictionary=d, job1=job, rate1=rate, link1=link)


if __name__ == "__main__":
    app.debug = True
    app.run(port=8080)
