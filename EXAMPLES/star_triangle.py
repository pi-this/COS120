def triangle(levels):
    for level in range(1, levels+1):
        print('level', level, '|',end="")
        for space in range(levels-level):
            print(' ', end="")
        for star in range(level+level-1):
            print('*', end="")
        print()

triangle(7)
print()
triangle(3)

"""
1. **
2. *,/,//,%
3. +, -
4. <=


7 > 4 and 7 > 8 or 7 > 8
"""
# coding competition 4 hours (extra credit)