def xyz_there(string):
    for i in range(len(string)):
        if (i < len(string) - 2) and (string[i:i+3] == "xyz"):
            if ((i != 0) and string[i-1] != ".") or i == 0:
                return True
    return False


print(xyz_there('abcxyz')) # True
print(xyz_there('abc.xyz')) # False
print(xyz_there('xyz.abc')) # True
