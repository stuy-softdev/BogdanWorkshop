# Amy Shrestha, Bogdan Sotnikov, Haowen Xiao
# Software Developers
# SoftDev
# K10 -- teardown
# 2025-09-25
# time spent: 1.0

'''
DISCO:
- I found that when we stop running the program the website disappears.
- It seems that __name__ stands for __main__.
- When we comment out app.run() the webpage still works, but it seems to be
supported by Thonny, as it prints an additional line: "Running the app with
options chosen by Thonny. See Help for details."
- When we didn't return a value for the function hello_world, the website
shows an "Internal Server Error" and a TypeError is raised.
- Commenting out "print(__name__)" does not affect the actual run of the app/website.
- Without the hello_world() function, the app fails to run, saying that
app.run() is an invalid syntax (SyntaxError).
- Commenting out "@app.route("/")" or the "@" still creates a website domain but when
we open it, it says the URL was not found. So most likely it's used to connect
it to a proper website URL.
- It seems in order to initialize app, we need the syntax "Flask(__name__)" and
not a single part can be omitted.

QCC:
0. Flask seems like a submodule of flask.
1. What does the @ symbol do and is it necessary?
2. What is Flask used for?
3. What significance does printing __name__ have?
4. Where does the route "/" connect to exactly and can we change the website route?
5. Why does the function hello_world() run if it isn't called yet?
 ...

INVESTIGATIVE APPROACH:
We first inferred on what each part of the code did. Then, we ran the code
once and clicked on the link that appeared because I seemed to have seen
this before, and it opened up a website with the words "No hablo queso!"
Seeing that it this, we then commented out each section of the code to
see how each line affects the result.

ERRORS:
- TypeError:
[2025-09-28 22:09:59,494] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/Users/amy/Library/Python/3.10/lib/python/site-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/Users/amy/Library/Python/3.10/lib/python/site-packages/flask/app.py", line 920, in full_dispatch_request
    return self.finalize_request(rv)
  File "/Users/amy/Library/Python/3.10/lib/python/site-packages/flask/app.py", line 939, in finalize_request
    response = self.make_response(rv)
  File "/Users/amy/Library/Python/3.10/lib/python/site-packages/flask/app.py", line 1212, in make_response
    raise TypeError(
TypeError: The view function for 'hello_world' did not return a valid response. The function either returned None or ended without a return statement.
--> occurred bc we didn't return a value for the function hello_world

- Not Found:
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
--> occurred on the website bc we didn't have '@app.route("/")'

- SyntaxError:
Traceback (most recent call last):
  File "/Users/amy/Desktop/wkshp_1/10_teardown/app.py", line 76
    app.run()                                # Q5: Where have you seen similar constructs in other languages?
    ^^^
SyntaxError: invalid syntax
--> occurred because there was no function hello_world

- NameError:
Traceback (most recent call last):
  File "/Users/amy/Desktop/wkshp_1/10_teardown/app.py", line 76, in <module>
    @app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
NameError: name 'app' is not defined
--> occurred because we didn't have 'app = Flask(__name__)'

- TypeError:
Traceback (most recent call last):
  File "/Users/amy/Desktop/wkshp_1/10_teardown/app.py", line 80, in <module>
    app = Flask()                    # Q0: Where have you seen similar syntax in other langs?
TypeError: Flask.__init__() missing 1 required positional argument: 'import_name'
--> occurred bc we didn't include the __name__ argument in Flask's object creation

- NameError:
Traceback (most recent call last):
  File "/Users/amy/Desktop/wkshp_1/10_teardown/app.py", line 87, in <module>
    app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?
NameError: name 'Flask' is not defined
--> occurred bc we didn't have 'from flask import Flask'
'''
from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?
                                         # Using Java to create classes.

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
                                         # Maybe the origin terminal or the place where the file is in.
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
                                         # It will print to the route that the app is in, and it will print whatever __name__ is.
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?
                                         # This will appear in the place where the route is and I know because the function will return it as a string.

app.run()                                # Q5: Where have you seen similar constructs in other languages?
                                         # Perhaps in Python creation of a class, or maybe in Java.


