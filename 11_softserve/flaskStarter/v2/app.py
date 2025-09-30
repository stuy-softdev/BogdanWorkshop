# Amy Shrestha, Bogdan Sotnikov, Haowen Xiao
# Software Developers
# SoftDev
# K11 -- softserve
# 2025-09-28
# time spent: 0.1

'''
Same as before, we know everything will run the same as v0 since it has the
same code, and we will look at how the extra lines of code affect the original
code by commenting it out and then uncommenting it.

Prediction:
Again, will probably do the same exact thing as the v0 app, only
this time, it will print an extra statement before printing __main__.

'''

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go?
    return "No hablo queso!"

app.run()

