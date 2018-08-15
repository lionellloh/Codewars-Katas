import math

def dbl_linear(n):
    x = math.floor(math.log(n+1,2))

    print(x)
    for i in range(x):
        

# testing(dbl_linear(10), 22)
# testing(dbl_linear(20), 57)
# testing(dbl_linear(30), 91)
# testing(dbl_linear(50), 175)

dbl_linear(10)