# count vowels
# 9/28/2026
# 9:29 AM
# Wesley Chastain

def count_vowels(string):
    result = 0
    # loop each character in string and add one if vowel
    """
    # two ways I can go through a string with loop:
    
    # 1st way:
    for index in range(len(string)):
        print(string[index])
       
    # 2nd way:
    for char in string:
        print(char)
        
    """
    """
#     for index in range(len(string)):
#         if string[index].lower() in "aeiou":
#             result += 1

# the other way...
    """
    
    for char in string:
        if char.lower() in "aeiou":
            result += 1

    
        

        
    return result



            