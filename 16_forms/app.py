# Bogdan Sotnikov, Amy Shrestha, Haowen Xiao
# Software Developers
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


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will NOT.

TASK: Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST']) #Gets input
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #prediction: prints the route; outcome: name of the file
    print("***DIAG: request obj ***")
    print(request) #prediction: prints path to the request; outcome: prints out website link and method used ([GET])
    print("***DIAG: request.args ***")
    print(request.args) #prediction: prints arguments of the request; prints out type of input argument
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username']) #prediction: gets username for request. maybe person who runs the program?; outcome: the website returns an error and doesn't print. maybe because there is no input for username?
    print("***DIAG: request.headers ***")
    print(request.headers) #prediction: get header of the request; outcome: prints out user stats? browser stats?
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) # prediction: prints file name; outcome: prints the file name
    print("***DIAG: request obj ***")
    print(request) # prediction: prints out website link and method used, maybe [GET]; outcome: prints the website link requested and which method used (GET)
    print("***DIAG: request.args ***")
    print(request.args) # prediction: prints input of the form; outcome: prints the dictionary with the username and entered username args
    print("***DIAG: request.args['username']  ***")
    print(request.args['username']) # prediction: prints the inputted username; outcome: prints the entered username
    print("***DIAG: request.headers ***")
    print(request.headers) # prediction: prints all the headers of /auth path; outcome: prints status of the webiste
    return request.args['username'] # response to a form submission, appears in /auth site



    
if __name__ == "__main__": #false if this file imported as module
    #app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run(port=5001)
