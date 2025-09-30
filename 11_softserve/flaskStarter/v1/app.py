# Amy Shrestha, Bogdan Sotnikov, Haowen Xiao
# Software Developers
# SoftDev
# K11 -- softserve
# 2025-09-28
# time spent: 0.2

'''
Same as before, we know everything will run the same as v0 since it has the
same code, and we will look at how the missing line of code changes the terminal
output as well as the website output

Prediction:
Does the same exact thing as the v0 app, only that it doesn't print __main__
in the console/shell because it is missing a print(__name__).

'''

from flask import Flask
app = Flask(__name__)            # create instance of class Flask

@app.route("/")                  # assign fxn to route
def hello_world():
    return "No hablo queso!"     # prints text onto website

app.run()

