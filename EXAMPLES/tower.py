import turtle


def rectangle(t, w, h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        
        
def main():
    width = 200.0
    screen = turtle.Screen()
    bob = turtle.Turtle()
    for j in range(10, 0, -1):
        bob.penup()
        bob.goto(-width/2,j*20) # where do I start the next one?
        bob.pendown()
        rectangle(bob, width, 20)
        width = width * 0.8
    screen.exitonclick()
    
main()