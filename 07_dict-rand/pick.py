# Jake, Sean, Bogdan
# The Snakes
# SoftDev
# K07 -- dictrand
# 2025-09-18
# time spent: 2hrs

import random

filename = "handles-n-quacks.csv"

def is_special(name):
    for ch in name:
        if ord(ch) > 122 or (ord(ch) < 65 and ord(ch) > 32):
            return True
            
    return False

with open(filename) as fn:
    # read csv file and removes heading
    data = fn.readlines()[1:]
    
    # initialize dictionary with nonempty handles
    # (handle:duckiename key:value pairs)
    gh = {}
    for row in data:
        datarow = row.split(',')
        if datarow[1] != '':
            gh[datarow[1]] = datarow[2][:-1]
            
    empty = {} # no duckiename or "EMPTYSTRING"
    default = {} # duckiename contains special chars or is "DUCKIENAME"
    good_name = {} # proper name
    
    for handle, dname in gh.items():
        if len(dname) == 0 or dname == 'EMPTYSTRING':
            empty[handle] = dname
            
        elif dname == 'DUCKIENAME' or is_special(dname):
            default[handle] = dname
        
        else:
            good_name[handle] = dname
            
    print("Dictionaries\n\n")
            
    print("Empty (no duckiename or \"EMPTYSTRING\"):\n")
    print(empty)
    print("\nDefault (duckiename contains special chars or is \"DUCKIENAME\"):\n")
    print(default)
    print("\nGoodname (proper name):\n")
    print(good_name)
    
    print("\nRandom pairs (handle:duckiename)\n\n")

    handle, dname = random.choice(list(empty.items()))
    print("Empty:\n")
    print(f"{handle}:{dname}\n")
    handle, dname = random.choice(list(default.items()))
    print("Default:\n")
    print(f"{handle}:{dname}\n")
    handle, dname = random.choice(list(good_name.items()))
    print("Goodname:\n")
    print(f"{handle}:{dname}\n")       
        
    
    
