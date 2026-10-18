def ticket_price(age):
    if age < 12:
        return 5
    if age < 65:
        return 10
    return 7

def total_price(age, quantity):
    if quantity < 0:
        return 0 # guard
    return quantity * ticket_price(age)


def test():
    assert ticket_price(0) == 5
    assert ticket_price(5) == 5
    assert ticket_price(11) == 5
    assert ticket_price(12) == 10
    assert ticket_price(33) == 10
    assert ticket_price(64) == 10
    assert ticket_price(65) == 7
    assert ticket_price(100) == 7
    print("All ticket_price tests passed")
    
    assert total_price(4,0) == 0
    assert total_price(20,0) == 0
    assert total_price(65,0) == 0
    assert total_price(4, -5) == 0
    assert total_price(4,2) == 10
    assert total_price(20,2) == 20
    assert total_price(65,100) == 700
    assert total_price(20,100) == 1_000
    assert total_price(65,2) == 14
    print("All total_price tests passed")


def main():
    a = float(input("Age: "))
    q = int(input("Quantity: "))
    
    print("Total Cost: ", total_price(a, q))
    
test()
#main()