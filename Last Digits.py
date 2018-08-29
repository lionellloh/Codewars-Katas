# https://www.codewars.com/kata/last-digits-of-n-2-equals-equals-n/train/python


def green(n):
    print(n)
    i = 1
    x = 1
    accepted_chars = ['0', '1', '5', '6']
    seen = []
    while (x <= n):
        # print(i)
        for saw in seen:
            if saw in str(i) or str(i)[-1] in accepted_chars:
                squared = i**2
                squared_string = str(squared)
                squared_length = len(str(squared))

                if squared_string[squared_length - len(str(i)):] == str(i):
                    x += 1
                    seen.append(str(i))
                    print(seen)

        i+=1

    return i-1

print(green(3))