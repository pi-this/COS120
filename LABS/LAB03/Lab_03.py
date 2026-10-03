# is this what it wants me to do?
def print_rectangle(rows, cols, chars):
    for i in range(rows):
        print(cols*chars)

"""
>>> print_rectangle(3, 10, '#')
##########
##########
##########
>>> print_rectangle(2, 2, '*')
**
**
"""

def diamond(n):
    
    if n % 2 == 0:
        # n is even
        return "Not an odd number of rows!"
    spaces = n
    star_count = 1
    for i in range(int(n/2)):
        print((spaces*' ')+"*"*star_count)
        spaces -= 1
        star_count += 2
    
    for i in range(int(n/2)+2):
        print((spaces*' ')+"*"*star_count)
        spaces += 1
        star_count -= 2
        
"""
>>> %Run Lab_03.py
>>> diamond(6)
'Not an odd number of rows!'
>>> diamond(5)
     *
    ***
   *****
  *******
   *****
    ***
     *
>>> 
"""
#L03-L03
def school_stage_linear(age):
    if age >= 1 and age <= 3:
        return "Nursery"
    if age >= 4 and age <= 5:
        return "Preschool"
    if age >= 6 and age <= 11:
        return "Elementary"
    if age >= 12 and age <= 13:
        return "Middle School"
    if age >= 14 and age <= 18:
        return "High School"

    return "Invalid age!"

def school_stage_nested(age):
    if age >= 1 and age <= 3:
        print("Nursery")
    else:
        if age >= 4 and age <= 5:
            print("Preschool")
        else:  
            if age >= 6 and age <= 11:
                print("Elementary")
            else: 
                if age >= 12 and age <= 13:
                    print("Middle School")
                else:
                    
                    if age >= 14 and age <= 18:
                        print("High School")
                    else:
                        print("Invalid age!")
    
                    

def school_stage_elif(age):
    if age >= 1 and age <= 3:
        print("Nursery")
    elif age >= 4 and age <= 5:
        print("Preschool")
    elif age >= 6 and age <= 11:
        print("Elementary")
    elif age >= 12 and age <= 13:
        print("Middle School")
    elif age >= 14 and age <= 18:
        print("High School")
    else:
        print("Invalid age!")
    
    
def rock_paper_scissors(player1, player2):
    if player1 == "rock":
        if player2 == "rock":
            print("tie")
        elif player2 == "paper":
            print("paper covers rock")
        elif player2 == "scissors":
            print("rock dulls scissors")
        else:
            print("Invalid input!")
    elif player1 == "paper":
        if player2 == "rock":
            print("paper covers rock")
        elif player2 == "paper":
            print("tie")
        elif player2 == "scissors":
            print("scissors cuts paper")
        else:
            print("Invalid input!")
    elif player1 == "scissors":
        if player2 == "rock":
            print("rock dulls scissors")
        elif player2 == "paper":
            print("scissors cuts paper")
        elif player2 == "scissors":
            print("tie")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

#L03-06 (b)
def test_rock_paper_scissors():
    for player1 in ["rock", "paper", "scissors", "fault"]:
        for player2 in ["rock", "paper", "scissors", "fault"]:
            rock_paper_scissors(player1, player2)
        
def calc_auto_premium(age, num_doors, gender):
    if age < 21:
        if num_doors == 2:
            print("High Risk")
            premium = 2_500
        else:
            print("Semi-High Risk")
            premium = 1_900
            
        if gender == "F":
            premium *= 2/3
        elif gender == "M":
            premium *= 2
    else:
        if num_doors == 2:
            print("Medium Risk")
            premium = 1_500
        else:
            print("Low Risk")
            premium = 800
    return premium

  
# L03-08

def count_characters(text):
    # upper case, lower case, digits, other characters
    upper, lower, digits, other = 0, 0, 0, 0
    for letter in text:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        elif letter.isdigit():
            digits += 1
        else:
            other += 1
        
    return upper, lower, digits, other
    # return a tuple


def main():
    enter_string = input("Enter a string: ")
    upper = count_characters(enter_string)[0]
    lower = count_characters(enter_string)[1]
    digits = count_characters(enter_string)[2]
    other = count_characters(enter_string)[3]
    
    print(f"Upper case letters: {upper}")
    print(f"Lower case letters: {lower}")
    print(f"Digits: {digits}")
    print(f"Other characters: {other}")
    