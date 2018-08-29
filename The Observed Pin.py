# https://www.codewars.com/kata/the-observed-pin

def get_pins(observed):
    keypad_relation = {
        1: [2,4],
        2: [1,3,5],
        3: [2,6],
        4: [1,5,7],
        5: [2,4,6,8],
        6: [3,5,9],
        7: [4,8],
        8: [5,7,9,0],
        9: [6,8],
        0: [8]
    }

    output = []
    possibilities = []

    def accum(current_string, new_string):

        return current_string + new_string


    for i in range(len(observed)):
        possibility = keypad_relation[int(observed[i])]
        possibility.append(int(observed[i]))

        possibilities.append(possibility)



    return possibilities

print(get_pins("1352"))
