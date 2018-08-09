# https://www.codewars.com/kata/529b418d533b76924600085d/train/python

print("HELLO")

def to_underscore(string):
    # your code here
    output = []
    string = str(string)
    for pos in range(len(string)):
        if string[pos].isupper():
            if pos != 0:
                output.append('_')
                output.append(string[pos].lower())

            else:
                output.append(string[pos].lower())

        else:
            output.append(string[pos])


    return "".join(output)


print(to_underscore("TestControllerLuck"))



