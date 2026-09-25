name = input("Name ? ")

john_hours = int(input("Hours? "))
john_hourly_rate = float(input("Hourly Rate? "))

with_holding = john_hours * john_hourly_rate
fica = .07

calculated_wage = with_holding - (fica * with_holding)




print("Name: ", name)
print("calcuated wage", "$"+round(calculated_wage))

"""

POW1:  You have been asked by your manager to write a
program to calculate the wages for an employee
(let's call him John Smith).
Hours for John Smith are 38, hourly rate is 16.75
and FICA withholding is calculated as 7% of the
calculated wage.  The program should declare
appropriate variables, and calculate and print
appropriate output (make it detailed, including
employee name, hours worked, hourly rate, withholding
and calculated wage).
POW2:  Modify the POW1 solution so it is totally dynamic - that is, no variable is hardcoded but is assigned values via input statements so that the results from each run may differ.
As you can see from the icon, this is not an assignment.  These are problems we will
solve in class this week as an introduction to initial programming concepts.
"""