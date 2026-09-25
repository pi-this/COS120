import turtle 

 

def square(t, size, filled): 

    if filled: 

        t.begin_fill() 

    for i in range(4): 

        t.forward(size) 

        t.right(90) 

    if filled: 

        t.end_fill() 

 

def row(t, count, size, first_filled): 

    filled = first_filled 

    for i in range(count): 

        square(t, size, filled) 

        t.forward(size)        # move to the next square 

        filled = not filled    # switch between filled and empty 

 

def grid(t, count, size): 

    first_black = True 

    for i in range(count): 

        row(t, count, size, first_black) 

        first_black = not first_black    # next row starts with the opposite 

 

        # go back to the start of the row, then down one square 

        t.back(count * size) 

        t.right(90) 

        t.forward(size) 

        t.left(90) 

 

def main(): 

    screen = turtle.Screen() 

    bob = turtle.Turtle() 

    bob.speed(10)               # fastest 

    count = int(input("Squares per side: ")) 

    grid(bob, count, 60) 

    screen.exitonclick() 

 

main() 