def make_chocolate(small, big, goal):
    # small = 1 kilo
    # big = 5 kilo
    # use big bars > use small bar
    goal = goal - big * 5
    if goal > small:
        return -1
    elif goal == small:
        return small
    else:
        return small - goal

print(make_chocolate(4, 1, 9)) # 4
print(make_chocolate(4, 1, 10)) # -1
print(make_chocolate(4, 1, 7)) # 2