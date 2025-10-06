## K17: Take and Give
### Due: `2025-10-07t 08:00`


### TASK:
Your Trio Mission: 

_Step 0: Come together. "Form like Voltron." Learn each others' names. Introduce Duckies, fetch KtS..._

__Write a Flask app__ to echo to a site visitor their input via an HTML form. Use provided code as starting point.

Your app's response should be
* visible to your visitor as a rendered page in the browser,
* produced via template,
* include username entered,
* include request method used,
* include your greeting to this person, and
* showcase your clearest breakdown of the differences between a GET and POST request (generalizations welcome, but give treatment specifically to handling these in the context of a Flask app, using the shared codebase you all started from)

Also:
  - Display team name and roster on landing page and response page.

<br>

#### Specifications/Guidelines:
* Use Q&A forum liberally.
* *Simplicity is divine.*
* Note anything notable in `notes.txt` in app's root directory.
*  _Reminder:_ include heading as comment in your html and python files.
* Stretch goal: Can you make your code work with any of these in your decorator(s)?
  - `methods=['GET']`
  - `methods=['POST']`
  - `methods=['GET', 'POST']`
  
<br>

##### DELIVERABLES:
* Section in notes.txt for DISCOVERIES, QUESTIONS/COMMENTS/CONCERNS
* Identical source code and supporting files in each teammates' work repo, as shown below.
* In heading, replace name with TNPG+roster.

```
path/to/myworkshop$ tree 17_form-resp
.
├── app.py
├── notes.txt
└── templates
    ├── login.html
    └── response.html
```

<br>

##### Related:
* [pydocs](https://docs.python.org/3.13/)  
* [you will NOT need all of this; focus on the zones with bits you recognize](https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask)
* [teamwork how you teamwork](https://www.youtube.com/watch?v=2M3cyCFWChg)

<br>

*PROTIP: Use Ctrl+click or Cmd-click to open links in a new tab.*
