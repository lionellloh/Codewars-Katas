def fibo(n):
    if n == 0:
        output = 0


    elif n == 1:
        output = 1


    else:
        output = fibo(n-1) + fibo(n-2)

    return output


print(fibo(6))
print(fibo(7))


def perimeter(n):
    output = [0, 1]
    for i in range(n):
        output.append(output[-1] + output[-2])


    return(sum(output) * 4)

print(perimeter(100))