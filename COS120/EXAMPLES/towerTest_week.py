import turtle


def rect(t, width, height):
    for i in range(2):
        t.forward(width)
        t.right(-90)
        t.forward(height)
        t.right(-90)
        
        
def main():
    bob = turtle.Turtle()
    w = 200
    h = 50
    
    for l in range(3):
        rect(bob, w, h)
        #bob.goto()
    
    
main()