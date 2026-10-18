def xyz_there(s):
    for i in range(len(s)):
        if s[i:i+3] == "xyz" and s[i-1] != ".":
            return True
    return False



# Examples:
print(xyz_there('abcxyz'))    # True
print(xyz_there('abc.xyz'))   # False
print(xyz_there('xyz.abc'))   # True
print(xyz_there('.xyzxyz'))   # True