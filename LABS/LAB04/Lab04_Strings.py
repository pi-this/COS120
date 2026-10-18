# L04-01
def print_chars_indexed(text):
    for letter in range(len(text)):
        print(text[letter])
        
"""
>>> %Run -c $EDITOR_CONTENT
>>> print_chars_indexed("right")
r
i
g
h
t
>>> 
"""


# L04-02
def print_chars(text):
    for letter in text:
        print(letter)
        

# L04-03
def first_middle_last(text):
    first = text[0]
    middle = text[len(text) // 2]
    last = text[len(text)-1]
    return first+middle+last

"""
>>> first_middle_last("James")
'Jms'
"""

# L04-04
def middle_three(text):
    # assume text has an odd length of at least 3
    # middle = text[len(text) // 2] therefore to get the 3 middle characters
    # I subtract and add from both sides
    return text[(len(text) // 2)-1:(len(text) // 2)+2]
    

"""
>>> %Run Lab04_Strings.py
>>> middle_three("JhonDipPeta")
'Dip'
>>> middle_three("JaSon")
'aSo'
>>>
"""


# L04-05
def reverse_string(text):
    return text[::-1]

"""
>>> %Run Lab04_Strings.py
>>> reverse_string("PYnative")
'evitanYP'
>>>
"""

# L04-06
def print_prefixes(text):
    new_text = ""
    for letter in text:
        new_text += letter
        print(new_text)
        
"""
>>> %Run Lab04_Strings.py
>>> print_prefixes("right")
r
ri
rig
righ
right
>>> 
"""

# L04-07
def print_in_reverse(text):
    new_text = ""
    for letter in text:
        new_text = letter + new_text
        print(new_text)
        
"""
>>> %Run Lab04_Strings.py
>>> print_in_reverse("hello")
h
eh
leh
lleh
olleh
>>>
"""

# L04-08
def my_length(text):
    amount = 0
    for number in text:
        amount += 1
    return amount

"""
>>> %Run Lab04_Strings.py
>>> my_length("")
0
>>> my_length("1234")
4
>>>
"""

# L04-09
def change_case(ch):
    if ord(ch) < 65:
        # 65 is the decimal value of 'A'
        # if the value is smaller than 'A' then it must not be a letter
        return ch
    if ord(ch) < 97:
        # 97 is the decimal value of 'a'
        # the value IS a letter, but it is smaller than 'a', this means that
        # it can NOT be an lowercase letter
        return chr(ord(ch)+32) # turn uppercase to lowercase
    return chr(ord(ch)-32) # turn lowercase to uppercase


# L04-10
def lower_case(text):
    new_text = ""
    for letter in text:
        if ord(letter) < 97: # if the value is NOT lowercase then change_case
            new_text += change_case(letter)
        else:
            new_text += letter
    return new_text

"""
>>> %Run Lab04_Strings.py
>>> lower_case("123 HeLlo BOB #$% abcD")
'123 hello bob #$% abcd'
>>>
"""

# L04-11

# (a)
def string_to_ascii_codes(text):
    code = ""
    for letter in text:
        code += str(ord(letter)).zfill(3)
        # the above code gives the same result as this:
        # new_text += "0"+str(ord(letter))
    return code

# (b)
def ascii_codes_to_string(code):
    text = ""
    string = ""
    amount = 0
    # loop through all of the numbers
    for number in code:
        amount += 1
        string += str(number)
        
        if amount == 3:
            text += chr(int(string))
            string = ""
            amount = 0
        
    return text


# L04-12

def my_find(sub, text):
    new_text = ""
    for i in range(len(text)):
        if text[i:len(sub)+i] == sub:
            return i
    return -1
#         new_text += text[i]
#         if text[i] == " ":
#             if sub in new_text:
#                 return i-3
#         if i == len(text)-1:
#             if sub in new_text:
#                 return i-2
#             else:
#                 return -1


my_find("all", "best of all")