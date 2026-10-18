# COS 120 - Midterm Lab Exam
import math
import random
import turtle

def MT_01(d):
    r = d/2
    a = math.pi*r**2
    
    return a

print('MT-01')
print(MT_01(1))
print(MT_01(2))
print(MT_01(10))
print('\n\n')

def MT_02(a, b, c):
    matches = 0
    if a == b and b == c:
        # (7, 7, 7)
        matches = 3
    elif a == b:
        # (7, 7, ?)
        matches = 2
    elif b == c:
        # (?, 7, 7)
        matches = 2
    elif a == c:
        # (7, ?, 7)
        matches = 2
    else:
        matches = 0
        # (7, ?, ?)
        # (?, 7, ?)
        # (?, ?, 7)
        # (?, ?, ?)
        
    return matches

print('MT-02')
print(MT_02(7, 7, 7))
print(MT_02(7, 7, 1))
print(MT_02(1, 7, 1))
print(MT_02(1, 7, 7))
print(MT_02(1, 7, 13))
print('\n\n')


def MT_03(low, high):
    # low <= high (assume this)
    len_run = 0
    sum_run = 0
    avg_run = 0
    for i in range(low, high+1):
        len_run += 1
        sum_run += i
    avg_run = sum_run/len_run
    print("Length of run is",len_run)
    print("Sum of run is",sum_run)
    print("Average of run is",avg_run)

print('MT-03')
MT_03(4, 9)
print()
MT_03(1, 5)
print('\n\n')


def MT_04(text):
    # sums the integer value of each digit
    digit_sum = 0
    for ch in text:
        if ch.isdigit():
            digit_sum += int(ch)
    return digit_sum

print('MT-04')
print(MT_04('3hello2joe1today!'))
print(MT_04('fourscore03and21seven0years9'))
print('\n\n')


def MT_05(text, letter):
    new_letters = ""
    new_text = ""
    for ch in text:
        if ch == letter:
            new_letters += ch
        else:
            new_text += ch
    new_text += new_letters
    return new_text

print('MT-05')
print(MT_05('', 'a'))
print(MT_05('The cake is a lie', 'a'))
print(MT_05("Roads? Where we're going, we don't need... roads.", 'e'))
print(MT_05('Alabama', 'a'))
print('\n\n')


def MT_06(h, w, c):
    result = ""
    for current_height in range(1, h+1):
        for current_width in range(1, w+1):
            if (current_height > 1 and current_height < h) and (current_width > 1 and current_width < w):
                # if the current_height and current_width are inside the center of the square (not on the border)
                # then add a space
                result += " "
            else:
                # otherwise add the c variable
                result += c
        # output the result line
        print(result)
        # reset the result value to prepare for the new line
        result = ""
            

print('MT-06')
MT_06(5, 10, 'o')
print()
MT_06(3, 5, 't')

print('\n\n')


def MT_07(t, max_wander_segments, max_distance):
    # assume t is at the center of the screen when the function is called
    
    segments = random.randint(1, max_wander_segments)
    
    for num in range(segments):
        t.right(random.randint(0, 360))
        t.forward(random.randint(0, max_distance))

def test_MT_07():
    emma = turtle.Turtle()
    MT_07(emma, 30, 50)

test_MT_07()

def MT_08(a, b):
    # ignore case in both strings
    # if both are not same length or a percentage cannot be calculated, return 0
    correct = 0
    a = a.lower()
    b = b.lower()
    
    if len(a) != len(b):
        return 0
    
    for ch in range(len(a)):
        if a[ch] == b[ch]:
            correct += 1
    
    # I cannot simply return correct at the end
    # this is because if I don't do it here it will give me a runtime error
    # ...from dividing by 0
    if correct == 0:
        return 0
    
    total = len(b)
    grade = round((correct / total) * 100, 2)
    
    return grade
    

print('MT-08')
print(MT_08('AABCE', 'AABCE'))
print(MT_08('AABCE', 'aabce'))
print(MT_08('AAbCEDEDTFTFTTTtFFFFAEDEbCD','ACBCEDEDTFfFTTTTFFFFZEDEBcD'))
print(MT_08('AABCE', 'AABCEQ'))
print(MT_08('AABCEDE', 'AABCEE'))
print(MT_08('', ''))
print('\n\n')