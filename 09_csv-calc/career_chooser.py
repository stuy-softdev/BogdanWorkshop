# Amy Shrestha, Bogdan Sotnikov
# Software Developers
# SoftDev
# K09 -- csv calc
# 2025-09-22
# time spent: 0.4

import random
# Open file, read it
file = open("occupations.csv", "r")
content = file.read()

# split the string by newlines into a list, remove extra items (total, empty lines, etc.)
splitter = content.split("\n")
splitter = splitter[1:-2]


# turn the list into a dictionary by splitting by last comma
d = {}
weighted_l = []
for i in range(len(splitter)):
    #print(splitter[i])
    comma = splitter[i].rindex(',')
    # create each dictionary key:value with type casting to convert string into a float
    d[splitter[i][0:comma]] = float(splitter[i][comma+1:])
    # add key items to weighted list
    for f in range(int(float(splitter[i][comma+1:])*10)):
        key1 = splitter[i][0:comma]
        weighted_l.append([key1])

print(d)

# randomly choose one key value from the weighted dictionary
handlei = random.randrange(len(weighted_l))
handle = weighted_l[handlei]

# access value of key item from dictionary
dname = d.get(str(handle))

print("\nRandom Item:")
print(f"{handle}: {dname}\n")








