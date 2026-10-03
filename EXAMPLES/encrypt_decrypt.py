# Challenge:
# CEASAR CIPHER
# only letters...
# if it gets past z go back to a
def encrypt1(offset, plain_text): 

    cipher_text = "" 

    for char in plain_text: 

        value = ord(char) 

        new_char = chr(value + offset) 

        cipher_text += new_char 

    return cipher_text 

     

def decrypt1(offset, cipher_text): 

    plain_text = "" 

    for char in cipher_text: 

        value = ord(char) 

        new_char = chr(value - offset) 

        plain_text += new_char 

    return plain_text

 

 

# message = "Benjamin" 
# 
# cipher_text = encrypt1(7, message) 
# 
# print(message,'=>',cipher_text)
# 
# plain_text = decrypt1(7, cipher_text) 
# 
# print(cipher_text,'=>',plain_text)


key = "qwertyuiopasdfghjklzxcvbnm"

def encrypt3(string, key):
    code = ""
    string = string.lower()
    string = string.replace(" ", "")
    for char in string:
        index = ord(char) - ord('a') # ord('a') == 97
        code = code + key[index]
        
    return code


def decrypt3(code, key):
    plain = ""
    for char in code:
        index = key.index(char)
        plain += chr(ord("a") + index)
        
        
    return plain

print(encrypt3("bad", key))
print(decrypt3("wqr", key))



# Transportation cipher

def encrypt2(plain_text):
    even_letters = ''
    odd_letters = ''
    
    for i in range(len(plain_text)):
        if i % 2 == 0:
            # that means it is even
            even_letters += plain_text[i]
        # otherwise
        else:
            # it must be odd letters
            odd_letters += plain_text[i]
    
    
    cipher_text = odd_letters+even_letters
    return cipher_text

def decrypt2(cipher_text):
    plain_text = ""
    # divide each by 2 then take the first letter
    # of each one
    halfway = len(cipher_text) // 2
    odds = cipher_text[:halfway]
    evens = cipher_text[halfway:]
    
    for i in range(halfway):
        plain_text = plain_text + evens[i] + odds[i]
    if len(evens) > len(odds):
        plain_text = plain_text + evens[-1]
    
        
    return plain_text


message = "Today is my birthday!" 
cipher_text = encrypt2(message)
#print(message, '=>', cipher_text)

plain_text = decrypt2(cipher_text)
#print(cipher_text, '=>', plain_text)



def remove_spaces(text):
    result = ""
    for char in text:
        if char != " ":
            result += char
    return result

#print(remove_spaces("There should be no spaces in this string."))