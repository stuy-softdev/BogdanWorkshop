# Bogdan Sotnikov, Amy Shrestha, Ethan Cheung
# Software Developers 2.0
# October 2025

'''
We just took our code for a flask server and made it only run the
render template from the last assignment. We changed the path for
the stylesheet in the html file to accomodate the new directories
and names.
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

app = Flask(__name__)    #create Flask object

@app.route("/")
def index():
    return render_template('index.html')

    
if __name__ == "__main__":
    app.run(port=5001)

