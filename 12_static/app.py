# Clyde 'Thluffy' Sinclair
# SoftDev
# Sep 2025

# DEMO
# basics of /static folder
from flask import Flask
app = Flask(__name__)

@app.route("/")             # bind the root route to this function. Ie serve this function's return value when the root route is requested.
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-restart of web server upon code change
    app.run()
