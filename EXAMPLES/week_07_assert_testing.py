def is_passing(score):
    return score >= 60

def test():
    assert is_passing(87) == True
    assert is_passing(44) == False
    assert is_passing(60) == True
    assert is_passing(0) == False
    

    
    
    print("is_passing passed all tests")

def main():
    s = float(input("Enter a score: "))
    print("Passing: ", is_passing(s))
    
test()    
#main()

    