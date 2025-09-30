# Amy Shrestha, Bogdan Sotnikov, Haowen Xiao
# Software Developers
# SoftDev
# K11 -- softserve
# 2025-09-28
# time spent: 0.1

'''
Same as before, we know everything will run the same as v0 since it has the
same code, and we will look at how the extra lines of code affect the original
code by commenting it out and then uncommenting it. In addition, since there
are already comments, we will look at those as well to see what each part of the
code does.

Prediction:
It will run the same as the code in v3, because __name__ will
equal __main__.
'''

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route

def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
