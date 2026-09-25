import turtle

sn = turtle.Screen()

emma = turtle.Turtle()
emma.pensize(10)

def polygon(trtl, ns, sl):
    for side in range(ns):
        trtl.forward(sl)
        trtl.left(360/ns)
        print('heading', trtl.heading())
        print('position', trtl.position())
        print('side', side)



sides = int(input("Enter sides --> "))
length = float(input("Enter side length --> "))


polygon(emma, sides, length)


sn.exitonclick()
