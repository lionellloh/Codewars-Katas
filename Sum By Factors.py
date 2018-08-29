# https://www.codewars.com/kata/sum-by-factors/train/python

def prime(x):
    # check that number is greater that 1
    if x > 1:
        for i in range(2, x + 1):
            # check that only x and 1 can evenly divide x
            if x % i == 0 and i != x and i != 1:
                return False
        else:
            return True
    else:
        return False

def sum_for_list(lst):
    result = {}
    for num in lst:
        for i in range(2, abs(num)+1):
            # check that it is a factor
            if num//i == num/i:
                if prime(i):
                    if i in result:
                        result[i].append(num)

                    else:
                        result[i] = [num]

    output = [[k, sum(v)] for k,v in result.items()]


    return sorted(output)


print(sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100]))



