def add(x,y):
    return x + y

def print_add(x,y):
    print(x+y)
    
    
print(add(3,4))
print_add(3,4)

# print_add returns None even though I said it does not return anything
# the difference of these two functions is crutial to understand
# Most of the time programmers will use the top method for functions


# return leaves the funciton, anything else is never read
# most of the time we use return
# some t