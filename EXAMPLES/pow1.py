import math
import turtle

"""
Write a python program that accepts the two non-hypotenuse
side lengths of a right triangle as input.  Call these a and b.
Write a function that will calculate the hypotenuse given a and b and return it.
Now write a function that will plot a,b and c (the hypotenuse) using turtle graphics.
Assume default screen coordinates, with the turtle starting at 0,0.  Plot a parallel to the x axis,
and b parallel to the y axis.  Close the triangle by drawing the hypotenuse.   Write your program as a
main function that uses the two functions described above to carry out the program requirements.
You may accept your inputs for a and b in the main function.
"""

"""
hypotenuse
return sqrt (a**2 + b**2)
"""

def hypotenuse(x, y):
    return math.sqrt(x**2 + y**2)


def plot(t, base, height):
    t.forward(base)
    t.left(90)
    t.forward(height)
    t.goto(0,0)
    


def main():
    a = float(input("a please: "))
    b = float(input("b please: "))
    little_guy = turtle.Turtle()
    plot(little_guy, a*20, b*20)
    
    little_guy.up()
    little_guy.goto(-10, 10)
    little_guy.hideturtle()
    little_guy.write(round(hypotenuse(a, b),1))
    
    
    
    
    
    

    


main()