import turtle
def averageASCII(string):
    total = 0
    for letter in string:
        total += ord(letter)
    
    return int(total / len(string))
    
def merge(string1, string2):
    result = ""
    short_string = string1
    long_string = string2
    if len(string2) < len(string1):
        short_string = string2
        long_string = string1
    
    for i in range(len(short_string)):
        result += string1[i]+string2[i]
    
    if string1 != string2:
        result += long_string[len(short_string):len(long_string)]
        
    return result

def countUpperCaseLetters(string):
    result = 0
    for letter in string:
        if letter.isupper():
            result += 1
    return result


def drawBisected(size):
    t = turtle.Turtle()
    
    for count in range(6):
        for side in range(3):
            t.forward(size)
            t.left(360/3)
        t.right(360/6)
        