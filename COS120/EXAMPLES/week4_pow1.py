"""
Write a function that accepts the size of a "square" as a parameter.
The function should then draw a square made up of '*' characters.
For instance:
>>> drawCharSquare(5)
*****
*****
*****
*****
*****
"""

def drawCharSquare(n):
    for row in range(n):
        for i in range(n):
            print('*', end='')
        print()
            
drawCharSquare(5)
drawCharSquare(10)