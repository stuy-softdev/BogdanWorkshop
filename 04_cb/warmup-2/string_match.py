def string_match(a, b):
    counter = 0
    for i in range(len(a)):
        if i < len(a) - 1 and a[i:i+2] == b[i:i+2]:
            counter += 1
    return counter

print(string_match('xxcaazz', 'xxbaaz')) # 3
print(string_match('abc', 'abc')) # 2
print(string_match('abc', 'axc')) # 0