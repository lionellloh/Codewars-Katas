# https://www.codewars.com/kata/pyramid-slide-down/train/python


# def longest_slide_down(pyramid):
#     costs = []
#     sum = 0
#     for layer in pyramid:
#         c
#
#
#
#
#
#
#
# longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])



def factorial(n):
    sum = n
    for i in range(n-1, 0, -1):
        sum *=i

    return sum


print(factorial(5))


def longest_slide_down(pyramid):
    slide_lengths = [0]

    for i in range(len(pyramid)):
        new = []
        lookback = factorial(i)
        print("lookback: ", lookback)
        for i in range(number_of_values):
            for j in range(len(slide_lengths), len(slide_lengths) - lookback, -1):
                new.append(slide_lengths[j] +