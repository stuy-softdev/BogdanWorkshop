# Amy Shrestha, Bogdan Sotnikov
# Software Developers
# SoftDev
# K09 -- csv calc
# 2025-09-22
# time spent: 

import random
# Open file, read it
file = open("occupations.csv", "r")
content = file.read()

splitter = content.split("\n")
splitter = splitter[1:-2]


# Split it in the position theyre in, simple
d = {}
for i in range (len(splitter)):
    print(splitter[i])
    comma = splitter[i].rindex(',')
    d[splitter[i][0:comma]] = splitter[i][comma+1:]

print(d)

handle, dname = random.choice(list(d.items()))
print("D1:\n")
print(f"{handle}:{dname}\n")






