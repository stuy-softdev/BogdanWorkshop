## K15: Template for Success!
### Due: `2025-10-03f 08:00`

### DISCOVERIES, QUESTIONS, COMMENTS, CONCERNS
* You can assign multiple values to a key by assigning an array as its value in the dictionary
* I wonder if there's a way to make the site reload when the template changes, because stopping and starting it to change the template was kind of tedious

### GOAL:
* Gain working knowledge of Jinja2 templating engine.
* Deepen understanding of how Flask app components work with one another.

### TASK:
Your Trio Mission:

_Step 0: Come together. "Form like Voltron." Learn each others' names. Introduce Duckies..._

1. Peruse your last few work submissions with an eye toward...
   * assessing each others' coding styles, workflow preferences
   * taking only the best (cleanest, most expressive, most robust) code forward
   * deepening your understanding of anything covered thus far

1. Write a Flask app with an `/wdywtbwygp` route, which will use a template to generate an HTML page with
   * an appropriate title,
   * a descriptive heading,
   * TNPG+roster,
   * and a tablified version of the occupations data, along with
   * a randomly selected occupation shown at the top (each page refresh should yield a newly-chosen occupation).
1. Read the "egoless programming" excerpt. Discuss with teammates. (Outside class.)
1. *Grow your codebase* to incorporate this functionality:
   * For each occupation, find a link that would be helpful to get started in that field.
   * Add that link to the `occupations.csv` file.
   * Include the link in your python dictionary (_Note: you'll have to store the percentage and the link as values attached to each name._)
   * Configure your app to publish each link alongside its occupation. (You know, to help your users on their way to their new job.)
1. Stretch/flex goal if you want it... wave team flag to signal readiness :)

   
--- 

#### Specifications/Guidelines:
* NOTE ANYTHING NOTABLE as you go.
* __Design first.__ Conceive a plan with your partner. __KtS are your friends.__
* __Develop jointly.__ Once finished, store identical code in each of your respective workshops.
* Team name must portend greatness.
* Comment liberally in-line. Speak to your future self and/or future teammates.
* Each teammate must be able to explain any aspect of your code. Ponder the implications...
* Note anything notable in `notes.txt` in app's root directory. Include section labelled `EGO` for any responses you would like to *share*...
* _PLAN FIRST_ so as to maximize your valuable time. Re-use code where possible. (Do not carry forward garbage...)
* _Reminder:_ include heading as comment in your html and python files.
* PROTIP: When designing a new jinja2 template, a Devo-proven approach is writing a static html file first, tuning it until it looks correct, then making a copy and stripping the copy down to its template bones.

<br>

##### DELIVERABLES:
* Section in readme for DISCOVERIES, QUESTIONS/COMMENTS/CONCERNS
* Block comment in source code explaining approach.
* Identical source code and supporting files in each teammates' work repo, as shown below. (notes file excepted)

```
path/to/myworkshop/$ tree 15_tempwork
.
├── app.py
├── data
│   └── occupations.csv
├── notes.txt
├── readme.md
└── templates
    └── tablified.html
```


<br>


##### Related:
* [jinja2 docs](https://jinja.palletsprojects.com/en/3.1.x/templates/)
* [link](https://xkcd.com/)
* [link]()


