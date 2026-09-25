def add_two(x, y):
    print(x, "+",y,"=",x+y)

# # all we do in lab next week will be for loops
# print(list(range(1,10,4))) # (start, end, step)
# add_two(4,5)
# 
# # control + 3 for commenting


for i in range(4):
    for j in range(4):
        add_two(i, j)