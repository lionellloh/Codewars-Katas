def lowest_common_multiple(list):
    biggest = max(list)
    while True:
        fulfiled = 0
        print("biggest:", biggest)
        for e in list:
            if fulfiled == len(list):
                print("BIGGEST IS", biggest)
            if biggest // e == 0:
                fulfiled +=1

            else:
                biggest += 1
                break

def multiple_or_not(list):
    for i in


print(lowest_common_multiple([1, 4, 5, 7]))