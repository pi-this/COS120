def remove_duplicates(string):
    result = ""
    for char in string:
        if char not in result:
            result = result + char
    return result

def remove_matches(string, remove_string):
    result = ""
    for ch in string:
        if not ch in remove_string:
            result += ch
    return result


def create_key(password):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    password = remove_duplicates(password)
    split_index = alphabet.index(password[-1])
    topalpha = remove_matches(alphabet[:split_index],password)
    botalpha = remove_matches(alphabet[split_index:],password)
    
    return password + botalpha + topalpha

def encrypt3(string, key):
    code = ""
    string = string.lower()
    string = string.replace(" ", "")
    for char in string:
        index = ord(char)-ord("a")
        code = code + key[index]
    return code

def decrypt3(code, key):
    plain = ""
    for char in code:
        index = key.index(char)
        plain += chr(ord("a") + index)
    return plain

def main():
    command = ""
    while command != "Q":
        text = input("Enter Text: ")
        password = input("Enter Password: ")    
        command = input("[E]ncrypt, [D]ecrypt or [Q]uit: ")
        key = create_key(password)
        print("Substitution Key is",key)
        print()
        if command == "E":
            print(encrypt3(text, key))
        if command == "D":
            print(decrypt3(text, key))

# main()


def test():
    assert remove_duplicates("Benn") == "Ben"
    assert remove_duplicates("Ben") == "Ben"
    assert remove_duplicates("") == ""
    assert remove_duplicates("aaaaaaaabbbbbcc") == "abc"
    print("remove duplicates worked!")
    
    assert remove_matches("abcdef", "cd") == "abef"
    assert remove_matches("abcdefcdcd", "cd") == "abef"
    assert remove_matches("", "cd") == ""
    assert remove_matches("dc", "cd") == ""
    assert remove_matches("2 workers", "iuz2") == " workers"
    print("remove matches worked!")
    
    assert create_key("topsecret") == "topsecruvwxyzabdfghijklmnq"
    print("Create Key Works")

#test()
main()