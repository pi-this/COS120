def sum_numbers(n):
    result = 0
    for i in range(10+1):
        result = result + i
    print("local variables", n, i, result)
    return result
    
def main():
    a = 10
    b = sum_numbers(a)
    print(b)
    


main()