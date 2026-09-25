import turtle

s = turtle.Screen()

me = turtle.Turtle()
me.speed(0)

def square(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)


def row(t, square_size, side_length):
    for i in range(square_size):
        square(t, side_length)
        t.forward(side_length)
        
        
def grid(t, square_size, side_length):
    for i in range(square_size):
        row(t, square_size, side_length)
        t.forward(-square_size * side_length)
        t.right(90)
        t.forward(side_length)
        t.left(90)


grid(me, 5, 60)
s.exitonclick()