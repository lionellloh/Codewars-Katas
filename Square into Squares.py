# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python

import math
output = []
def decompose(n):
    output = []

    x = n -1
    print("x is", x)
    output.append(x)
    remainder = n**2 - x**2
    print("remainder is: ", remainder)
    if remainder**(1/2) ==  math.ceil(remainder**(1/2)):
        output.insert(0, int(remainder**(1/2)))
        return sorted(output)

    else:
        next_input = math.ceil(remainder**(1/2))
    print("next input is: ", next_input)

    output.extend(decompose(next_input))

    if remainder <= 0 or x > 1000:
        return(sorted(output))

    else:
        return sorted(output)


print(decompose(50))