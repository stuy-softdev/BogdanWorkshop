# Amy Shrestha, Bogdan Sotnikov, Haowen Xiao
# Software Developers
# SoftDev
# K11 -- softserve
# 2025-09-28
# time spent: 0.5

'''
We first inferred on what each part of the code did. Then, we ran the code
once and clicked on the link that appeared because I seemed to have seen
this before, and it opened up a website with the words "No hablo queso!"
Seeing that it this, we then commented out each section of the code to
see how each line affects the result.

Prediction:
We think the code will create a website that runs the function hello_world
and print "No hablo queso!" on it.

'''

from flask import Flask
app = Flask(__name__)          # creates object of Flask class

@app.route("/")                # links the app to a website route
def hello_world():
    print(__name__)            # prints __main__ in console/shell
    return "No hablo queso!"   # prints text in website app created

app.run()                      # runs the app and the function hello_world
                
