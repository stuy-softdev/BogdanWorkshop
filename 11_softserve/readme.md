## K11: Would You Like Fries With That?
### Due: `2025-09-29m` 08:00

### GOAL:
* Serve a webpage using Flask.
* Gain working knowledge of python virtual environments.
* Prune/tune/robustify codebase.

#### DISCOVERIES, QUESTIONS, COMMENTS, CONCERNS
Flask prints after running. The return outputs to the page that flask opens.

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
