"""
1)  Write a function sumExponents that will accept a parameter, call it n, and the maximum exponent to
which n is to be raised, call it x.  Calculate the sum of n to all of the exponents from 1 to x, (e.g.
sumExponents(2,4) would return the sum of 2**1 +  2**2  +  2**3  +  2**4,  or 30).  Write and call a main
function that calls and displays the results for at least 4 different test cases for sumExponents.

2) Write a function that will calculate the volume of a sphere, given the radius of the sphere.
The formula for calculating the volume is V = 4/3 × π × r**3.  Write a main function that will call
and display the results for at least 4 test cases.

"""


def sumExponents(n,x):
    sumtotal = 0
    # accurmulating sums start with 0, acumulating products start with 1
    for i in range(1, x+1):
        sumtotal = sumtotal + n**(i)
    return sumtotal

def main():
    print(sumExponents(2,4))
    print(sumExponents(2,5))
    print(sumExponents(3,4))
    print(sumExponents(3,5))
    print(sumExponents(2,3))

main()