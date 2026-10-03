"""
Shipping Cost
An online store charges $7 for shipping.
Orders of $50 or more receive free shipping.
Rewards members receive free shipping on orders
of $25 or more.

Write a function called shipping_cost()
that accepts the order total and whether the customer
is a rewards member and returns the shipping cost.

Write a main() function that asks the user for their
order total and whether they are a rewards member.
Accept "y" or "yes" as indicating a rewards member.
Call shipping_cost() and display the result.
"""

def shipping_cost(total,is_member):
    
    return 0 if total >= 50 or (total >= 25 and is_member) else 7

def main():
    # ask for the total
    order_amount = float(input("Order Total:"))
    # get membership status
    status = input("Member (y/n): ")
    
    # if y or ys, call shipping_cost with true
    # else call with false
    
    if status == "y" or status == "yes":
        s = shipping_cost(order_amount, True)
    else:
        s = shipping_cost(order_amount, False)
        
    # print shipping cost
    print("Shippping Cost = ", s)
    
    
main()