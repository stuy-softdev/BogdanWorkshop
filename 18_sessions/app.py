# Bogdan Sotnikov, Amy Shrestha, Haowen Xiao
# Software Dev
# October 2025

'''
In our model, the root of the page acts as a redirector and never displays directly. It redirects the user to either login or
auth based on whether it can find a username. Auth stores the username in session, and logout removes it. You can go back to
login from the logout page, and you can log out from the response page.
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
from flask import redirect

app = Flask(__name__)    #create Flask object

app.secret_key = b'blfkbflbjfl'

@app.route("/", methods=['GET', 'POST']) #Gets input
def index():
    if 'username' in session:
        return redirect('/auth?username='+session["username"]+'&sub1=Submit')
    return app.redirect('/login')
    

@app.route("/login")
def disp_loginpage():
    return render_template('login.html')

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return render_template('logout.html')

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    session['username'] = request.args['username']
    return render_template('response.html',
                           requestMethod=request.method,
                           username=session['username']) # response to a form submission, appears in /auth site

    
if __name__ == "__main__": #false if this file imported as module
    #app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run(port=5001)

