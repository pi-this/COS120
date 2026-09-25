"""ALL PROBLEMS BELOW REQUIRE AT LEAST ONE LOOP!
ONLY PROBLEM L01-12 REQUIRES YOU TO WRITE YOUR SOLUTION USING FUNCTIONS"""
# 
# L01-01 write code to print out the numbers 0-7.
def main_01():
    for i in range(7+1):
        print(i)



# L01-02 write code to print out the numbers 1 to 8
def main_02():
    for i in range(1, 8+1):
        print(i)



# L01-03 write code to print out the numbers 1 to 50
def main_03():
    for i in range(1, 50+1):
        print(i)
        

# # L01-04 write code to print out the numbers 50 to 1
def main_04():
    for i in range(50, 1-1, -1):
        print(i)
        
        
# L01-05 write code that will print the integers from 4 to 44 by 4's
def main_05():
    for i in range(4, 44+1, 4):
        print(i)
        

# L01-06 write code that will print the integers from 44 to 4 by -4's
def main_06():
    for i in range(44, 4-1, -4):
        print(i)
        
# L01-07 write code that will SUM the integers from 1 to 12 and print the result
def main_07():
    result = 0 # I don't want to use the word sum as a variable due to it already being a python function
    for i in range(1, 12+1):
        result += i
    print(result)
        
   
# L01-08 write code that will multiply the integers from 1 to 8 and print the result
def main_08():
    result = 1
    for i in range(1, 8+1):
        result *= i
    
    print(result)
    
     
     
# L01-09 write code to print out the following, using a for loop inside of a for loop
"""
1 Nina
2 Nina
3 Nina
1 Omar
2 Omar
3 Omar
1 Priya
2 Priya
3 Priya
"""
def main_09():
    for x in ["Nina", "Omar", "Priya"]:
        for y in range(1,3+1):
            print(y, x)
            
            
# L01-10 modify the above code to allow the user to enter the range of numbers they wish to print out. Keep the names the same. 
def main_10():
    starting = int(input("Enter starting number: "))
    ending = int(input("Enter ending number: "))
    for x in ["Nina", "Omar", "Priya"]:
        for y in range(starting,ending+1):
            print(y, x)
    
    
# L01-11 write code that will print the following multiplication facts
"""
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8

3 x 2 = 6
3 x 3 = 9
3 x 4 = 12

4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
"""

def main_11():
    for x in range(2, 4+1):
        for y in range(2, 4+1):
            print(f"{x} x {y} = {x*y}")
        

# L01-12 modify the above code so that the multiplication facts starting and ending values may be passed in as parameters to the function that you will then call
def main_12():
    def showMultFacts(start, end):
        for x in range(start, end+1):
            for y in range(start, end+1):
                print(f"{x} x {y} = {x*y}")
        
    showMultFacts(2, 6)



# L01-13 write code to use the turtle module to draw a series of equilateral triangles right next to each other
def main_13():
    import turtle
    
    def triangle(t, size=50):
        sides = 3
        for i in range(sides):
            t.forward(size)
            t.left(360/sides)
        t.forward(size)
    
    
    me = turtle.Turtle()
    me.speed(0)
    me.hideturtle()
    
    for i in range(5):
        triangle(me)
        
    


# L01-14 write code to use the turtle to draw a set of "steps" made of squares. Make use of the drawSquare function we wrote in class, and looping in the code that draws the set of squares illustrated below
def main_14():
    import turtle
    
    
    def drawSquare(t, size=50):
        sides = 4
        for i in range(4):
            t.forward(size)
            t.left(360/sides)
            
        t.forward(size)
    
    
    me = turtle.Turtle()
    me.speed(0)
    me.hideturtle()
    
    for x in range(3, 2-1, -1):
        for y in range(x):
            drawSquare(me)
            
            print(x, y)
            
        me.up()
        me.goto(50,50)
        me.down()
        
    me.up()
    me.goto(100,100)
    me.down()
    
    drawSquare(me)
        
    

main_01()
print( "\n\n\n\n\n" )
main_02()
print( "\n\n\n\n\n" )
main_03()
print( "\n\n\n\n\n" )
main_04()
print( "\n\n\n\n\n" )
main_05()
print( "\n\n\n\n\n" )
main_06()
print( "\n\n\n\n\n" )
main_07()
print( "\n\n\n\n\n" )
main_08()
print( "\n\n\n\n\n" )
main_09()
print( "\n\n\n\n\n" )
main_10()
print( "\n\n\n\n\n" )
main_11()
print( "\n\n\n\n\n" )
main_12()
print( "\n\n\n\n\n" )
main_13()
print( "\n\n\n\n\n" )
main_14()
print( "\n\n\n\n\n" )






