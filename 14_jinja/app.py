# Bogdan Sotnikov, Ethan Saldanha
# 1% of gamblers
# Sep 30 2025

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
Prediction: It'll throw an error because it can't find render_template if it isn't imported.
Outcome: Internal server error

Q1:
Prediction: http://127.0.0.1:5000/my_foist_template
Outcome: yes

Q2:
Prediction: When the template is run, render_template will replace "foo" with "fooooo" and "collection" with the list initialised earlier.
Outcome: yes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
#                              (log prediction BEFORE executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: What URL shall you use to load this page?
#         Self-assess: Can all of your teammates confidently predict?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument?
    #                                  Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
