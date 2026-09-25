import turtle

sn = turtle.Screen()

emma = turtle.Turtle()
emma.pensize(10)

size = float(input("What size to your prefer? "))

def square(trtl, sl):
    for side in range(4):
        trtl.forward(sl)
        trtl.left(90)
        print('heading', trtl.heading())
        print('position', trtl.position())
        print('side', side)


jordan = turtle.Turtle()
jordan.pensize(10)

square(emma, size)
jordan.forward(size*2)
square(jordan, size)


sn.exitonclick()