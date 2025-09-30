# Amy Shrestha, Bogdan Sotnikov, Haowen Xiao
# Software Developers
# SoftDev
# K11 -- softserve
# 2025-09-28
# time spent: 0.15

'''
Same as before, we know everything will run the same as v0 since it has the
same code, and we will look at how the extra lines of code affect the original
code by commenting it out and then uncommenting it.

Prediction:
Instead of printing "Debug mode: off" it will print "Debug mode: on"
and I think the website will not show you the print statement.
'''

from flask import Flask
app = Flask(__name__)                 # create instance of class Flask

@app.route("/")                       # assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   # where will this go?
    return "No hablo queso!"

app.debug = True
app.run()
