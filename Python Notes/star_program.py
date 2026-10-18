def triangle_1(size):
    for i in range(1, size+2, 2):
            
        for j in range(i):
            print("*", end="")
        print()


def triangle_2(size):
    for i in range(1, size+2, 2):
        print(" "*(size-i), end="")
            
        for j in range(i):
            print("*", end="")
        print()


def triangle_3(size):
    # size = layers
    x = size
    for i in range(1,size+3,2):
        x -= 1
        print(" "*x, end="")
        for k in range(i):
            print("*", end="")
        print()
        
def triangle_4(size):
    # size = layers
    result = ""
    spaces = ""
    amount = 0
    for i in range(1,size+5,2):
        amount += 1
        spaces = " "*(size-amount)
        result = "*"*i
        print(spaces+result)
        

            
            
"""
OOOO*
OOO***
OO*****
O*******
*********

OO*
O***
*****

2 to 0


OOOO*
OOO***
OO*****
O*******
*********

4 to 0

OOOOO*
OOOO***
OOO*****
OO*******
O*********
***********

5 to 0
"""