# https://www.codewars.com/kata/55679d644c58e2df2a00009c/train/python

# For parsing of string 2

# string2 = "()[]<>"
#
# open = []
# close = []
# for i in range(0,len(string2),2):
#     open.append(string2[i])
#     close.append(string2[i+1])
#
#
# print("open:", open, "close:", close)
#
#
# # For validation of string 1
# string1 ="(Sensei [says] yes!)"
#
# seen = []


def is_balanced(string1, string2):
    opened, closed = [], []
    for i in range(0, len(string2), 2):
        opened.append(string2[i])
        closed.append(string2[i + 1])

    print(opened, closed)
    seen = []
    counter = 1
    for c in string1:
        if c in opened and c not in closed:
            seen.append(c)

        elif c in opened and c in closed:
            counter *= -1

        elif c in closed:
            if seen == []:
                return False
            elif opened.index(seen[-1]) == closed.index(c):
                seen.pop()

            else:
                return False

    if seen == [] and counter == 1:
        return True

    else:
        return False