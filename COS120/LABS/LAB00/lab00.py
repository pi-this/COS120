"""
1) Write a program that allows the user to enter their first name,
then their last name. Print the following output:
Lab Problem 00_01
Enter your first name: Joe
Enter your last name: Smith
Hello Joe
Hello Joe!
Joe Hello!
Joe Joe Joe Joe
Joe Smith
Smith, Joe

"""


# Lab 00_01
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Hello "+first_name)
print("Hello "+first_name+"!")
print(first_name+" Hello!")

print((first_name+" ")*4)
print(first_name+" "+last_name)
print(last_name+", "+first_name)



"""
2) Write a program that allows the user
to enter their Earth weight in pounds.
Using the surface-gravity ratios in parentheses,
display what that person would weigh on the Moon
(0.17), Mercury (0.38), Venus (0.91), Saturn (1.06)
and Jupiter (2.34), in the following format:
Lab Problem 00_02
Your Earth weight: 185
Your Moon weight: 31.450000000000003
Your Mercury weight: 70.3
Your Venus weight: 168.35
Your Saturn weight: 196.10000000000002
Your Jupiter weight: 432.9

"""

print()
# Lab 00_02
earth = float(input("Your Earth weight: "))
moon = .17
mercury = .38
venus = .91
saturn = 1.06
jupiter = 2.34
print("Your Moon weight: "+str(earth*moon))
print("Your Mercury weight: "+str(earth*mercury))
print("Your Venus weight: "+str(earth*venus))
print("Your Saturn weight: "+str(earth*saturn))
print("Your Jupiter weight: "+str(earth*jupiter))

print()

"""
3) Write a program that accepts the amount of
money a person has available, and then accepts
as input the current price of one Bitcoin.
Print out the number of Bitcoins the person
could purchase with the amount of money entered.
Lab Problem 00_03
How much money do you have available to gamble in Bitcoin: 4500
What is Bitcoin’s current price in USD: 7231.35
You could be the sorry owner of 0.6222904436930863 Bitcoins
"""

# Lab 00_03

money = float(input("How much money do you have available to gamble in Bitcoin: "))
price = float(input("What is Bitcoin's current price in USD: "))
print(f"You could be the sorry owner of {money/price} Bitcoins")
print()

"""

4)You recorded the following miles driven and gallons of
gas used for your car in three logbook entries:
Entry 1:  234 miles, 10 gallons
Entry 2:  360 miles, 15 gallons
Entry 3:  200 miles, 10 gallons
Write a program with these three sets of values hard-coded (no input).
Calculate the MPG for each entry, then calculate the average of those
three MPG values, and output the following:
Lab Problem 00_04
For entry 1 your MPG is 23.4
For entry 2 your MPG is 24.0
For entry 3 your MPG is 20.0
Your average MPG for the three logbook entries is 22.46666666666667
(Before you write the code for this one, think out or write in brief
English phrases the steps you will use to solve the problem.  Follow
these steps, using a calculator, to solve the problem manually.  Now
translate this algorithm into Python code.)
"""


# Lab 00_04

entry1 = 23.4
entry2 = 24.0
entry3 = 20.0


print(f"Your average MPG for the three logbook entries is {(entry1+entry2+entry3)/3}") 


"""
5) Given the number of elapsed seconds as an input,
turn the number of elapsed seconds into elapsed days,
hours, minutes and seconds and display these values:
Lab Problem 00_05
Enter the total seconds you wish to convert to days,
hours, minutes and seconds: 923000
Days: 10
Hours: 16
Minutes: 23
Seconds: 20
(Before you write the code for this one, think out
or write in brief English phrases the steps you will
use to solve the problem.  Follow these steps, using a
calculator, to solve the problem manually.
Now translate this algorithm into Python code.)
"""

# Lab 00_05
# Come back to this one later. It works, but there must be a better way. It is way too redundant.
seconds = int(input("Enter the total seconds you wish to convert to days, hours, minutes and seconds: "))
days = ((seconds//60)//60)//24
hours = ((seconds//60)//60)%24
minutes = (seconds//60)%60
seconds = seconds%60
print()
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
print()

"""
6) Write a program that will compute
the area of a circle. Prompt the user
to enter the radius and print a nice
message back to the user with the answer.
Area = 3.14159 * radius ** 2 (2.13.8)
"""
# Additional #6


# look at this one...
radius = float(input("Enter the radius: "))
area = 3.141592653589793238462 * radius ** 2
print(f"The area of your circle is {area}")

print()

"""
Write a program that will compute the area of a rectangle.
Prompt the user to enter the width and height of the rectangle.
Print a nice message with the answer. Area = width * height (2.13.9)
"""

width = int(input("Enter width of rectangle: "))
height = int(input("Enter height of rectangle: "))

area = width * height

print(f"The area of your rectangle is {area}")

print()

"""
8) Write a program that will convert degrees
Celsius to degrees Fahrenheit.
Fahrenheit = Celsius * (9/5) + 32
"""

celsius = float(input("Enter celsius degrees: "))
fahrenheit = celsius * (9/5) + 32
print(f"{celsius} degrees celsius is the equal to {fahrenheit} degrees fahrenheit.")



