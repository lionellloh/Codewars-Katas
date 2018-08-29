def snail(arr_og):
    print(arr_og)


    output = []
    times = 0

    if arr_og == [[]]:
        return output
    # print(len(arr_og) ** 2)
    while len(output) < len(arr_og) ** 2:
        if times == 0:
            end = None
        else:
            end = -times
        arr = [sub_og[times: end] for sub_og in arr_og[times:end]]
        print("arr is", arr)
        for i in range(len(arr)):
            if i == 0:
                for j in range(len(arr[0])):
                    output.append(arr[0][j])

            elif i == len(arr) -1:
                print("z")
                output.extend(arr[i][::-1])
                for j in range(len(arr)-1, 1, -1):
                    print("j", j-1)
                    # temp = arr[j-1][0]
                    output.append(arr[j-1][0])
                    del arr[j-1][0]
            # if not first or last
            else:
                output.append(arr[i][-1])

        times += 1

    return output

arr = [[1,2,3,5],
         [8,9,4, 3],
         [7,6,5, 2],
       [7, 6, 5, 2]]
print(snail(arr))