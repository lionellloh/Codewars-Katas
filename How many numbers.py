# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python



# print(is_increasing(122))

# def find_all(sum_dig, digs):
    # def is_increasing(i):
    #     breakdown = [int(x) for x in list(str(i))]
    #     for j in range(len(breakdown) - 1, 0, -1):
    #         # print(j, j -1)
    #         if breakdown[j] - breakdown[j - 1] < 0:
    #             return False
    #
    #     return True
    #
    # # start = 10 ** (digs-1)
    # start = 0
    # for power in range(digs):
    #     start += 10** power
    #
    # print(start)
    #
    # end = 10 **(digs)
    #
    # fulfiled = []
    # for i in range(start, end):
    #     if is_increasing(i):
    #         if sum([int(x) for x in list(str(i))]) == sum_dig:
    #
    #             fulfiled.append(i)
    #
    # if fulfiled == []:
    #     return []
    #
    # return[len(fulfiled), min(fulfiled), max(fulfiled)]






# Current number is a string arg
def dfs(current_number, current_sum, digs, sum_dig, perms):
    # reached the max depth
    total = current_sum
    if len(current_number) == digs:
        if total == sum_dig:
            perms.append(int(current_number))
        return

    # Current numbers + new number exceeded the required sum of digits
#     total = sum([int(x) for x in list(current_number)])

    r = int(current_number[-1])
    for i in range(r, 10):
        if i + total > sum_dig:
            continue

        dfs(current_number + str(i), current_sum+i, digs, sum_dig, perms)



def find_all(sum_dig, digs):
    perms = []
    for i in range(1, 10):
        if i > sum_dig:
            continue
        dfs(str(i), i, digs, sum_dig, perms)

    if len(perms) == 0:
        return []

    return [len(perms), min(perms), max(perms)]

print(find_all(40, 6))