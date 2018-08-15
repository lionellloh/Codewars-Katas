# https://www.codewars.com/kata/555b1890a75b930e63000023/train/python



def combos(n):
    output = [[n]]
    for i in range(n):
        temp = i+1
        combo = (n-temp) * 1
