# https://www.codewars.com/kata/57680d0128ed87c94f000bfd/train/python

# Write a function that determines whether a string is a valid guess in a Boggle board, as per the rules of Boggle. A Boggle board is a 2D array of individual characters, e.g.:
#
# [ ["I","L","A","W"],
#   ["B","N","G","E"],
#   ["I","U","A","O"],
#   ["A","S","R","L"] ]

import math

def find_word(board, word):
    # write your code here

    for i in range(len(board)):
        if board[i].index(char):
            row = i
            col = board[i].index(char)

            indexes.append((word[i], row, col))

    # Find the first character of the word
    for i in range(len(word)):

        char = word[i]

        # initialise a list that stores the indexes of the found character
        indexes = []

        # traverse the rows in the matri






    return False

