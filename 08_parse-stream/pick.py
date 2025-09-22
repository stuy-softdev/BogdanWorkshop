# Haowen Xiao, Bogdan Sotnikov
# Software Developers
# SoftDev
# K08 -- parse stream
# 2025-09-19
# time spent: 0.2

#We decided to use most of Haowen's code because it had no problem with organizing and sanitizing the code. Bogdans code had issues with
#the commas. We ended up using Bogdan's random code because Haowen didn't have a working one.

import random
# Open file, read it
file = open("handles-n-quacks", "r")
content = file.read()

# Replace the characters, then split it by new line. Purpose: Change into old format
splitter = content.replace("$$$", ",").replace("@@@", "\n").split('\n')
# Removes the class period
splitter = splitter[1:]

# Replace the characters
    

# This for loop is to clean the array, make it into key:value
# pop the commas first
# pop the anomalies second (DUCKIENAME, empty duckie, EMPTYSTRING)
t = 0
for i in range (len(splitter)):
    splitter[i - t] = splitter[i - t][2:]
    #pop out the commmas
    if ',' == splitter[i - t] or ', ' == splitter[i - t] or ' ' == splitter[i - t] or '' == splitter[i - t]:
        splitter.pop(i - t)
        t += 1
    #pop out EMPTYSTRING
    if 'EMPTYSTRING' in splitter[i - t]:
        splitter.pop(i-t)
        t += 1
    #pop out DUCKIENAME
    if 'DUCKIENAME' in splitter[i - t]:
        splitter.pop(i-t)
        t += 1
    #pop out empty duckienames
    if splitter[i-t][len(splitter[i-t]) - 1:] == ',':
        splitter.pop(i-t)
        t += 1

# Split it in the position theyre in, simple
d1 = {}
d2 = {}
d3 = {}
for i in range (len(splitter)):
    index = i % 3
    comma = splitter[i].index(',')
    if index == 1:
        d1[splitter[i][0:comma]] = splitter[i][comma+1:]
    elif index == 2:
        d2[splitter[i][0:comma]] = splitter[i][comma+1:]
    else:
        d3[splitter[i][0:comma]] = splitter[i][comma+1:]

print("Dictionary 1: Every user:duckie position if divided by 3, the remainder is equal to 1")
print(d1)
print('\n')
print("Dictionary 2: Every user:duckie position if divided by 3, the remainder is equal to 2")
print(d2)
print('\n')
print("Dictionary 3: Every user:duckie position if divided by 3, the remainder is equal to 0")
print(d3)

handle, dname = random.choice(list(d1.items()))
print("D1:\n")
print(f"{handle}:{dname}\n")
handle, dname = random.choice(list(d2.items()))
print("D2:\n")
print(f"{handle}:{dname}\n")
handle, dname = random.choice(list(d3.items()))
print("D3:\n")
print(f"{handle}:{dname}\n")





