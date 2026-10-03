def dollars_cents(c):
    # if 150 cents how many cents and dollars it is.
    dollars = c // 100
    cents = c % 100
    return dollars, cents
    

"""
>>> dollars_cents(150)
(1, 50)
>>> dollars, cents = dollars_cents(250)
>>> dollars
2
>>> cents
50
"""