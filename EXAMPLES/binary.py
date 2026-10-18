"""
0 0
1 1
2 10
3 11
4 100
5 101
6 110
7 111
8 1000
9 1001
10 1010

1 bit: 2 nums
2 bit 4 nums
4 bits 8 nums
n bit 2^n

1010101
multiply 2^n times each (an acumulator)...
2^0+2^1+2^3+2^4....

total = 0
power = 0

go through string backwards
"""

def to_binary(n):
    result = ''
    while n > 0:
        print(n % 2, "-->", n//2)
        result += str(n % 2)
        n = n // 2
        
        
    return result[::-1]

def to_decimal(binary):
    total = 0
    power = 0
    for char in binary[::-1]:
        print(char, '* 2**', power)
        total = total + int(char) * 2 ** power
        power = power + 1
    
    return total

"""
1 * 2** 0
0 * 2** 1
1 * 2** 2
0 * 2** 3
1 * 2** 4
0 * 2** 5
1 * 2** 6
85
"""
# 100
print(to_decimal("100"))
print(to_binary(4))