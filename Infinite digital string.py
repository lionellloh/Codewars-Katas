# https://www.codewars.com/kata/the-position-of-a-digital-string-in-a-infinite-digital-string


# Split a string into parts of n character/digit(s)
def split_string(input, n):
    old_n = 0
    output = list()
    for n in range(n, len(input), n):
        output.append(input[old_n : n])
        old_n = n

    remainder = len(input)%n
    print(len(input))
    if remainder != 0:
        output.append(input[-(remainder +1): ])


    return output


print(split_string("Singaporeuniversityoftech", 6))


def breakdown(string):
    for i in range(len(string)):
        components = split_string(string, i+1)
        for pos in range(len(components)):
            num_str = components[pos]
            if num_str[-1] == '9':
                pass

            else:
                
