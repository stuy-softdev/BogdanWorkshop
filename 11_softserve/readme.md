## K11: Would You Like Fries With That?
### Due: `2025-09-29m` 08:00

### GOAL:
* Serve a webpage using Flask.
* Gain working knowledge of python virtual environments.
* Prune/tune/robustify codebase.

### TASK:
As a trio...
1. In a new folder in your workshop, save a copy of the flask starter kit, versions 0-4.
1. As a team, for each version, one at a time...
   - Read (for understanding!) through each file.
   - **Note anything notable.**
   - Predict expected behaviors.
   - "Spin up" your website on the loopback interface (a.k.a. "localhost"|127.0.0.1) and reconcile behavior with prediction.
   - Repeat for each successive version.
   - Record your responses as comments in each python file.
1. Once your team has done this, write a flask app to flush the output of your occupation-chooser to a webpage:
   - Do this as simply as possible. (A team planning discussion will be in order...)
   - Show a newly-selected occupation upon each reload.
   - Display the list of occupations.
   - Display TNPG+roster at top of served page.
   - PROTIP: Versioning will help. Start with something simple, save a copy as soon as it works, add more features –  then *"lather/rinse/repeat"*. You are welcome/encouraged to save your backups in this work folder, along with CSV file.

---

#### Specifications/Guidelines:
* NOTE ANYTHING NOTABLE as you go.
* In a block comment near the top of your file, summarize/explain your team's approach. Pay special attention to clarity of your weighted probabilities explanation.
* Each run of your script should produce new random selections.
* __Design first.__ Conceive a plan with your partner. __KtS are your friends.__
* __Develop jointly.__ Once finished, store identical code in each of your respective workshops.
* Team name must portend greatness.
* Comment liberally in-line. Speak to your future self and/or future teammates.
* Each teammate must be able to explain any aspect of your code. Ponder the implications...
* Include proper heading. Note team name and roster.

<br>

##### DISCOVERIES, QUESTIONS/COMMENTS/CONCERNS
* In v3's app.py, turning debug mode on creates a loading website
page, not an error page or a completely loaded page. Also, because it's loading, none of the print statements print anything into the
console yet, and that also means that the function hello_world() only
runs after the page has loaded. When debug mode was turned on, it instead printed "OK" in the console.
* Changing the name of the function still runs it in the app.
* When we try returning __name__ instead of a string, it prints __main__ on the website.
* The line '@app.route("/")' checks directly for the next line of code, and I think it runs it (so it needs to be a function or a blank line of code).
* What does it mean in v4's app.py that the if statement will be true
if the file is not imported?
* How do we use debug mode to debug the code?
* What is the usage of __name__ in the code?


##### DELIVERABLES:
* Section in readme for DISCOVERIES, QUESTIONS/COMMENTS/CONCERNS
* Block comment in source code explaining approach.
* Identical source code and supporting files in each teammates' work repo, as shown below.

```
path/to/your/workshop$ tree 11_serve
.
├── app.py
├── occupations.csv
├── readme
├── v0
│   └── app.py
├── v1
│   └── app.py
├── v2
│   └── app.py
├── v3
│   └── app.py
└── v4
    └── app.py
```


<br>


##### Related:
* [flask primary docs](https://flask.palletsprojects.com/en/stable/)
* [pydocs on virtual environments](https://docs.python.org/3/library/venv.html)
* [pydocs](https://docs.python.org/3.13/)  
* [link](https://xkcd.com/)
* [link]()
