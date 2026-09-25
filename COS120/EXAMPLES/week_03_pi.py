import turtle, math, random


def dart_board(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

def throw_dart(t, x, y, color):
    t.goto(x, y)
    t.dot(3, "blue")

def main():
    screen = turtle.Screen()
    screen.tracer(0)
    scale = 100
    bob = turtle.Turtle()
    
    dart_board(bob,scale)
    bob.up()
    bob.speed(0)
    darts_inside = 0
    darts_total = 100
    
    for i in range(darts_total):
        x = random.random()
        y = random.random()
        distance = math.hypot(x, y)
        
        if distance <= 1:
            darts_inside = darts_inside + 1
            throw_dart(bob, x*scale, y*scale, "blue")

        
    
    screen.update()
    print('darts total', darts_total)
    print('darts inside', darts_inside)
    print('there, pi must be', darts_inside/darts_total * 4)
    screen.exitonclick()
    
    
    
main()