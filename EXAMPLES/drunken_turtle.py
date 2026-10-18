# drunken turtle
import turtle
import random
t = turtle.Turtle()


def drunken_turtle(turtle_object, amount):
    for count in range(amount):
        random_angle = random.randint(0,360)
        random_distance = random.randint(0,100)
        random_direction = random.randint(1,2)
        
        if random_direction == 1:
            turtle_object.forward(random_distance)
        elif random_direction == 2:
            turtle_object.backward(random_distance)
        if random_direction == 1:
            turtle_object.left(random_angle)
        elif random_direction == 2:
            turtle_object.right(random_angle)
            
    
drunken_turtle(t, random.randint(50,150))