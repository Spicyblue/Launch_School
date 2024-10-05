import unittest
'''
Roman Numerals.
Write some code that converts modern decimal numbers into their Roman number equivalents.

The Romans wrote numbers using letters - I, V, X, L, C, D, M.
Notice that these letters have lots of straight lines and are hence easy to hack into stone tablets.

1  => I
10  => X
7  => VII
 
There is no need to be able to convert numbers larger than about 3000.
(The Romans themselves didn't tend to go any higher)

Wikipedia says: Modern Roman numerals ... are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero.

To see this in practice, consider the example of 1990.
In Roman numerals, 1990 is MCMXC:
1000=M
900=CM
90=XC

2008 is written as MMVIII:
2000=MM
8=VIII
'''

# Solution
'''
PEDAC
Problem:
    Input: Integers
    output: Strings

    Exp: 
    - Only accept numbers from 1 to 3000
    - Sequences must be of equall length.

    imp:
    - unittest test cases show that our we need RomanNumeral class which accepts
      integerss passed to the constructor.
    - The class should have a method to_roman which returns the roman numeral (string).

Examples:
Using unittest TestCase


Data Structure:
Class with instance variables and methods.
A dictionary and a list perhaps.

Algorithm:
    Highend
    - Get the number.
    - Convert the number its Roman numeral.
    - Return the number.


    Lowend:
        - Define a class RomanNumeral which has accepts integers using the RomanNumeral constructor. 
        - Set this to an instance _number.
        - Define an instance method to_roman.
        - Create an variable roman_numeral store the result of converting the roman numeral to string.
        - Create a variable rom_dict which is reference dictionary with roman numerals as keys
          and their corresponding integers as values from 1000, till 1.
          eg M = 1000, 900 = CM, C = 100 etc
        - Iterate through the dictionary key value pairs.
            - Using Divmod, pass each values of the dictiorary and the orignal number
            to get the after_division value and remainder(modulus).
            - if after_division value is > 0,
             multiply it by the current key and increment roman_numeral by this.
            - set the remainder to the be the next original number used by divmod

        - return roman_numeral
'''

class RomanNumeral:
    def __init__(self, number):
        self._number = number

    def to_roman(self):
        roman_numeral = ""
        to_convert = self._number
        
        rom_dct= {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

        for key, value in rom_dct.items():
            after_division, remainder = divmod(to_convert, value)
            if after_division > 0:
                roman_numeral += key * after_division
            to_convert = remainder

        return roman_numeral

import unittest
class RomanNumeralsTest(unittest.TestCase):
    def test_1(self):
        number = RomanNumeral(1)
        self.assertEqual(number.to_roman(), "I")
   
    def test_2(self):
        number = RomanNumeral(2)
        self.assertEqual(number.to_roman(), "II")

    def test_3(self):
        number = RomanNumeral(3)
        self.assertEqual(number.to_roman(), "III")

    def test_4(self):
        number = RomanNumeral(4)
        self.assertEqual(number.to_roman(), "IV")

    def test_5(self):
        number = RomanNumeral(5)
        self.assertEqual(number.to_roman(), "V")

    def test_6(self):
        number = RomanNumeral(6)
        self.assertEqual(number.to_roman(), "VI")

    def test_9(self):
        number = RomanNumeral(9)
        self.assertEqual(number.to_roman(), "IX")

    def test_27(self):
        number = RomanNumeral(27)
        self.assertEqual(number.to_roman(), "XXVII")

    def test_48(self):
        number = RomanNumeral(48)
        self.assertEqual(number.to_roman(), "XLVIII")

    def test_59(self):
        number = RomanNumeral(59)
        self.assertEqual(number.to_roman(), "LIX")

    def test_93(self):
        number = RomanNumeral(93)
        self.assertEqual(number.to_roman(), "XCIII")

    def test_141(self):
        number = RomanNumeral(141)
        self.assertEqual(number.to_roman(), "CXLI")

    def test_163(self):
        number = RomanNumeral(163)
        self.assertEqual(number.to_roman(), "CLXIII")

    def test_402(self):
        number = RomanNumeral(402)
        self.assertEqual(number.to_roman(), "CDII")

    def test_575(self):
        number = RomanNumeral(575)
        self.assertEqual(number.to_roman(), "DLXXV")

    def test_911(self):
        number = RomanNumeral(911)
        self.assertEqual(number.to_roman(), "CMXI")

    def test_1024(self):
        number = RomanNumeral(1024)
        self.assertEqual(number.to_roman(), "MXXIV")

    def test_3000(self):
        number = RomanNumeral(3000)
        self.assertEqual(number.to_roman(), "MMM")

if __name__ == "__main__":
    unittest.main()

## LS Solution ##
# class RomanNumeral:
#     def __init__(self, number):
#         self.number = number

#     ROMAN_NUMERALS = {
#         "M": 1000,
#         "CM": 900,
#         "D": 500,
#         "CD": 400,
#         "C": 100,
#         "XC": 90,
#         "L": 50,
#         "XL": 40,
#         "X": 10,
#         "IX": 9,
#         "V": 5,
#         "IV": 4,
#         "I": 1,
#     }

#     def to_roman(self):
#         roman_version = ""
#         to_convert = self.number

#         for key, value in self.ROMAN_NUMERALS.items():
#             multiplier, remainder = divmod(to_convert, value)
#             if multiplier > 0:
#                 roman_version += key * multiplier
#             to_convert = remainder

#         return roman_version