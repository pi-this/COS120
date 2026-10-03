def combos():
    flavors = ['vanilla', 'mint chocolate chip', 'cookie dough']
    toppings = ["m & m's", "sprinkles", "caramel"]
    
    # How might I return every possible combination?
    # I need a loop inside of a loop
    
    for flavor in flavors:
        for topping in toppings:
            print(flavor, topping)
            

def encrypt(offset, string):
    # the way we do this is by using ascii values
    code = "" # this will be an accumulator: therefore it must be empty
    for char in string:
        value = ord(char)
        code += chr(value + offset)
    return code

    
    """
    >>> %Run combos_and_encrypt_decrypt.py
    >>> encrypt(1, "Ben")
    'Cfo'
    >>> 
    """

def decrypt(offset, string):
    pass