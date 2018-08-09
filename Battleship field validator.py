# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

def count_linked_tups(tup, count, locations):
    possibilities = [(tup[0] + 1, tup[1]), (tup[0] - 1, tup[1]), (tup[0], tup[1] + 1), (tup[0], tup[1] - 1)]

    print("possibilities: ", possibilities)
    for pos in possibilities:
        if pos in locations:
            print("new loc: ", pos)
            print("count", count)
            count += 1
            locations.remove(pos)
            count_linked_tups(pos, count, locations)


        else:
            print("ELSE COUNT:", count)
            break

    print("HERE HERE")
    return(count)



def validateBattlefield(field):
    # write your magic here
    locations = []
    for r in range(len(field)):
        # print(field[r])
        for c in range(len(field[r])):

            # print("row: {}, col: {}".format(r,c))
            if field[r][c] == 1:
                locations.append((r,c))

    print(locations)
    print(len(locations))

    # seen = {"row" = [], "col" = []}
    battleship_count = [4,3,2,1]


    for tup in locations:
        print("initial loc", tup)
        locations.remove(tup)
        size_of_ship = count_linked_tups(tup, 1, locations)
        print("size of ship")
        print(size_of_ship)
        battleship_count[size_of_ship-1] -= 1

    print("Battleship count")
    print(battleship_count)













field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


validateBattlefield(field)