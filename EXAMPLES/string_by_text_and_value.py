

def remove_vowels1(string):
    total_text = ""
    for i in range(len(string)):
         if not string[i].lower() in "aeiou":
            total_text += string[i]
    return total_text
            
        
# looping through the string by value


def remove_vowels2(string):
    total_text = ""
    for letter in string:
        if not letter.lower() in "aeiou":
            total_text += letter
    return total_text
        

# looping through the string by text

def test():
    assert remove_vowels1("Isaac") == "sc"
    assert remove_vowels1("Hello World!%()") == "Hll Wrld!%()" 
    assert remove_vowels1("12345") == "12345"
    assert remove_vowels1("") == ""
    
    assert remove_vowels2("Isaac") == "sc", print("You did this wrong!")
    assert remove_vowels2("Hello World!%()") == "Hll Wrld!%()"
    assert remove_vowels2("12345") == "12345"
    assert remove_vowels2("") == ""
    print("All tests passed!")
    
    
    



test()