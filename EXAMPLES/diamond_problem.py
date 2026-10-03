# center
def diamond(n):
    if n % 2 == 0:
        # guard: if it is even
        print("Must be odd!")
        return
        # we don't want our whole function to be in an if statement
        # just return
    
    for i in range(1,n+1,2):
        print(('*'*i).center(n))
    
    for i in range(n-2,0,-2):
        print(('*'*i).center(n))
    

diamond(20)