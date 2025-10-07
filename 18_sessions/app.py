# Bogdan Sotnikov, Amy Shrestha, Haowen Xiao
# Software Dev
# October 2025

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)
# We did this assignment by first running it and seeing which comment does what. We predicted it before we ran anything though. THroughout the testing
# we figured out that the request.arg['username'] returns the username. We used that to return the input from the home page. 

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0                     #"home-rolled" module for basic exploration

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route("/") #, methods=['GET', 'POST']) #Gets input
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) # prints name of the file
    print("***DIAG: request obj ***")
    print(request) # prints out website link and method used ([GET])
    print("***DIAG: request.args ***")
    print(request.args) # prints out type of input argument
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username']) # returns an error
    print("***DIAG: request.headers ***")
    print(request.headers) # prints out user stats? browser stats?
    return render_template('login.html')


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) # prints the file name
    print("***DIAG: request obj ***")
    print(request) # prints the website link requested and which method used (GET)
    print("***DIAG: request.args ***")
    print(request.args) # prints the dictionary with the username and entered username args
    print("***DIAG: request.args['username']  ***")
    print(request.args['username']) # prints the entered username
    print("***DIAG: request.headers ***")
    print(request.headers) # prints status of the webiste
    return render_template('rseponse.html',
                           requestMethod=request[-1:request.rindex("[")],
                           username=request.args['username']) # response to a form submission, appears in /auth site

    
if __name__ == "__main__": #false if this file imported as module
    #app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run(port=5001)

