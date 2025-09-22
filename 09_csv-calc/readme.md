## K09: Divine Your Destiny!
### Due: `2025-09-25r` 08:00

### GOAL:
* Hone CSV i/o.
* Utilize random calls for more precise task.

### BACKGROUND:
In the notes&code repo is a CSV file containing information about occupations in the United States (courtesy of Mr. Brooks). Here is a snippet of two lines of the file:

```
    Legal,0.8
    "Education, training and library",6.1
```

The first item is the name of the occupation and the second is the percentage of the U.S. workforce it comprises. Note the quotation marks surrounding an occupation containing commas.

### TASK:
Step 0: Form a dynamic duo with your shoulder buddy. Effect pair programming mode.

1. Review last work.
1. Procure starter kit. Save locally and tell github to track. Configure directory in workshop, fit for submission. MMMC.
1. Develop and implement a python script that will...
   * read the given CSV file
   * build an appropriate dictionary from it. Make sure the percentages are stored as numbers.
1. Add a function that returns a randomly selected occupation where the results are weighted by the percentage given. For example, there should be a 6.1% chance that "Education, training and library" is returned.

   
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
path/to/my-workshop/$ tree 09_csv-calc
.
├── career_chooser.py
├── occupations.csv
└── readme.md
```


<br>


##### Related:
* [pydocs](https://docs.python.org/3.13/)  
* [pair pro](https://github.com/stuy-softdev/notes-and-code/blob/main/read/nyer_pp.pdf)
* [link](https://xkcd.com/519/)
* [link](https://www.officialasvab.com/)
* [link]()

