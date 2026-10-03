from random import randint
"""
Write a function printAdditionTable(n)
that prints the N-by-N addition table,
one sum per line, in the format shown below.
N is passed as a parameter. You must use one
for loop nested inside another.
"""

def printAdditionalTable(n):
    for x in range(1, n+1):
        for y in range(1, n+1):
            print(x, "+", y, "=", x+y)
            
def L02_01():
    printAdditionalTable(3)
    
"""
Write a function productPThroughN(p, n)
that computes and returns the product of
P through N, inclusive. Assume P < N. Both
P and N are parameters, e.g. productPThroughN(3, 5)
is 3 * 4 * 5 => 60.
"""

def productPThroughN(p, n):
    result = 1
    for i in range(p, n+1):
        result *= i
        
    return result

def L02_02():
    print(productPThroughN(3, 5))
    print(productPThroughN(1, 5))
    

"""
Write a function sumPThroughN(p, n) that
computes and returns the sum of P through
N, inclusive. Assume P < N. Both P and N are
parameters, e.g. sumPThroughN(3, 5) is 3 + 4 + 5 => 12.
"""

def sumPThroughN(p, n):
    result = 0
    for i in range(p, n+1):
        result += i
        
    return result

def L02_03():
    print(sumPThroughN(3, 5))
    print(sumPThroughN(1, 5))
    
    
"""
Write a function sumOfProducts(n)
that, given N as a parameter, computes
and returns the sum of the products of 1
through N by 1 through N. For N = 3 that is
1*1 + 1*2 + 1*3 + 2*1 + 2*2 + 2*3 + 3*1 + 3*2 + 3*3.
Another way to think of it: add up every cell of an N-by-N
multiplication table. Use one for loop nested inside another.
Do not print the table — return only the sum.
"""

def sumOfProducts(n):
    result = 0
    for x in range(1, n+1):
        for y in range(1, n+1):
            result += x*y
    return result

def L02_04():
    print(sumOfProducts(3))
    print(sumOfProducts(4))
    
    
"""
Write a function printRandomNumbers(n)
that prints N random integers, each in
the range 1 to 100. N is passed as a parameter.
Before you start, import random and use help(random)
to spend a few minutes exploring the module.
"""


def printRandomNumbers(n):
    for numbers in range(n):
        print(randint(1, 100))

def L02_05():
    printRandomNumbers(5)
    
    
"""
Below is code that has already been compiled.
Predict exactly what will appear in the Thonny
shell when demoCalls() is called, and write your
prediction down. Then copy the code into a Thonny
code window and run it. Did you get what you expected?
Why or why not?

from math import *

def demoCalls():
    sqrt(16)
    print(sqrt(16))
    x = sqrt(16)
    print(x)
    y = sqrt(16) * sqrt(25)
    print(y)

The code above will output:
4
4
20

After running the code I was close, but I forgot that the
numbers would be floats instead of integers:
4.0
4.0
20.0
"""

def demoCalls():
    sqrt(16)
    print(sqrt(16))
    x = sqrt(16)
    print(x)
    y = sqrt(16) * sqrt(25)
    print(y)


"""
Now enter the code below exactly as
it appears and run testmySQRT().
Shouldn't the results be much like part (a)?
Why aren't they? Why does None print?
What does the error message mean?

This throws an error because None is assignmed to the function.
For this to function properly I need to add return result at the end
which assigns the variable result to the function.
"""

def mySQRT(n, iters):
    result = 1
    for i in range(iters):
        result = 1/2 * (result + n/result)
    return result

def testmySQRT():
    mySQRT(16, 2)
    print(mySQRT(16, 100))
    x = mySQRT(16, 100)
    print(x)
    y = mySQRT(16, 100) * mySQRT(25, 100)
    print(y)
    
"""
Modify your repaired mySQRT so that it
prints the square root instead of returning it,
and run testmySQRT() again. What happens, and why?
Why is it better for a function to return the value
it calculates than to print it directly? Which version
gives the more flexible, more useful abstraction?
When you are done, repair mySQRT one last time so that
it returns the value.
"""

def mySQRT(n, iters):
    result = 1
    for i in range(iters):
        result = 1/2 * (result + n/result)
    print(result)

def testmySQRT():
    mySQRT(16, 2)
    print(mySQRT(16, 100))
    x = mySQRT(16, 100)
    print(x)
    y = mySQRT(16, 100) * mySQRT(25, 100)
    print(y)
    
    
    
    
    
"""
Write a function sumFirst100Evens() that computes
and returns the sum of the first 100 even numbers.
How do you know the answer is correct?

I know the answer is correct because I debugged it and printed the
result then i. I saw that both times the numbers were counting up
by 2s.
"""

def sumFirst100Evens():
    result = 0
    for i in range(1, 200+1):
        if i % 2 == 0:
            result += i
    return result
        
print(sumFirst100Evens())
print('lab problem 100 evens')
    
    
    
"""
Write a function sumFirst50Odds() that computes and
returns the sum of the first 50 odd numbers.
How do you know the answer is correct?

I knew this one was correct because I checked by adding a print
statement to print i and found that every number was odd.
I als odid it the same way I did the last one, but instead changed 100
to 50 and changed the == to !==.
"""
def sumFirst50Odds():
    result = 0
    for i in range(1, 100+1):
        if i % 2 != 0:
            result += i
    return result
    
print(sumFirst50Odds())
    
"""
Write a function averageFirst100Odds()
that computes and returns the average
of the first 100 odd numbers. How do you
know the answer is correct?

I know this one is correct because I printed i under the if statement
and found no even numbers as it printed a test print.
"""

def averageFirst100Odds():
    result = 0
    for i in range(1, 200+1):
        if i % 2 != 0:
            result += i
    return result/100
    
print(averageFirst100Odds())

"""
Write a function printThreeTimes1()
that uses a loop to print exactly this,
and nothing more:
"""
def printThreeTimes1():
    for i in range(3):
        print("in the loop")
        
#printThreeTimes1()
        
"""
Then write five more functions, printThreeTimes2()
through printThreeTimes6(), that produce the same
output using a different loop each time. Your six
versions must satisfy all of the following:
•   Use several different forms of range() — do not
count 0 to 3 by 1s or 1 to 4 by 1s in every version.
•   At least one version must count by a step other than 1.
•   At least one version must use negative numbers.
•   At most two versions may loop over a list.
"""

def printThreeTimes2():
    for i in range(7, 1, -2): # step other than 1
        print(i)
        print("in the loop")
        
#printThreeTimes2()
        
def printThreeTimes3():
    for q in range(-15, -45, -10): # negative numbers
        print("in the loop")
        
def printThreeTimes4():
    for h in range(15, 1, -5):
        print("in the loop")

def printThreeTimes5():
    for y in range(0, 5, 2):
        print("in the loop")
def printThreeTimes6():
    for x in ["in", "the", "loop"]: # loop over a list
        print("in the loop")
        
#printThreeTimes3()
#printThreeTimes4()
#printThreeTimes5()
#printThreeTimes6()

#testmySQRT()
        
"""
Solve these using only iteration and the printing techniques
above. Do not use string multiplication or string
concatenation — you have not covered them yet.
They would make these problems easier, which is
exactly why they are off limits here.

L02-11. (10 points) Write a
function printTriangle() that
prints the figure below, using
nested for loops.
"""

def printTriangle(n):
    for x in range(1, n+1):
        for y in range(1, x+1):
            print('*', end='')
        print()

printTriangle(5)
        
"""
Write a function printInvertedTriangle()
that prints the figure below, using nested for loops.
"""
    
def printInvertedTriangle(n):
    for x in range(n, 0, -1):
        for y in range(1, x+1):
            print('*', end='')
        print()
    
printInvertedTriangle(5)
"""
Write a function printPyramid() that prints
the figure below, using nested for loops.
This one is challenging at this stage —
think about how you would draw it by hand,
one line at a time. Remember that a loop can
print spaces as well as visible characters.
"""
def printPyramid(n):
    for x in range(n, 0, -1):
        for y in range(1, x):
            print(' ', end='')
        for z in range(((n-x+1)*2)-1):
            print('*', end='')
        print()
    
    
#     for x in range(1,n+1):
#         for y in range(0,n,1):
#             print('*', end='')
#         print()
#printPyramid(7)
L02_01()
L02_02()
L02_03()  
L02_04()
L02_05()
    
    
    

    
