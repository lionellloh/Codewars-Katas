# https://www.codewars.com/kata/decimal-to-any-rational-or-irrational-base-converter/python

import math


def recur(n, base):

    log_result = int(math.log(n, base))
    print(log_result, base)
    remainder = n - (base ** log_result)


    return remainder, log_result


def converter(n, decimals=0, base = math.pi):
    output = list()
    while n > base:
         n, place = recur(n, base)
         output.append((place, n))

    return output



print(converter(20,0, 3))


