# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python
"""

I          1
V          5
X          10
L          50
C          100
D          500
M          1,000


"""

class RomanNumerals(object):
    denominations = [1, 4, 5, 10, 50, 100, 500, 1000]
    roman_numerals = ["I", "IV", "V", "X", "L", "C", "D", "M"]


    @classmethod
    def to_roman(cls, integer):
        roman_output = []
        for denomination in cls.denominations[::-1]:
            while integer >= denomination:
                integer -=denomination
                roman_numeral = cls.roman_numerals[cls.denominations.index(denomination)]
                print("integer: {}, roman_numeral: {}".format(integer,roman_numeral))
                roman_output.append(roman_numeral)

        return "".join(roman_output)

    @classmethod
    def from_roman(cls, roman_num):
        print("from_roman")
        integer = 0
        for c in roman_num:
            try:
                dem_index = cls.roman_numerals.index(c)
                integer += cls.denominations[dem_index]

            except:
                return "Roman numeral given is invalid"


        return integer





print(RomanNumerals.from_roman("CCCCLXXXXVIIII"))
print(RomanNumerals.to_roman(1990))