import unittest
'''
Octal.
Implement octal to decimal conversion.
Given an octal input string, your program should produce a decimal output.
Treat invalid input as octal 0.
Note that the only valid digits in an octal number are 0, 1, 2, 3, 4, 5, 6, and 7.

Note: Implement the conversion yourself.
Don't use any built-in or library methods that perform the necessary conversions for you.
In this exercise, the code necessary to perform the conversion is what we're looking for.

About Octal (Base-8)

Octal use a base-8 system. A number 233 in base 8 can be understood as a linear combination of powers of 8:

The rightmost digit gets multiplied by 80 = 1
The next digit gets multiplied by 81 = 8
The digit after that gets multiplied by 82 = 64
The digit after that gets multiplied by 83 = 512
...
The n_th_ digit gets multiplied by 8n-1.
All of these values are then summed.
Thus:

233 # octal
= 2*8^2 + 3*8^1 + 3*8^0
= 2*64  + 3*8   + 3*1
= 128   + 24    + 3
= 155

'''

# Solution
'''
PEDAC
Problem:
    Input: Strings
    output: Integer

    Exp: 
    - Valid digits in an octal number are 0, 1, 2, 3, 4, 5, 6, and 7.
    - Treat invalid input as octal 0. (ie inputs with 8 and 9)
    - Do not use any built-in library or methods

    imp:
    - unittest test cases show that our we need a Octal class which accepts string arguments passed to its constructor.
    - If alphabets or any 8, 9 are passed as argument, consider it to ebe octal 0.
    - The class should have method to_decimal which calculats the decimal conversio of octals.
    - if a string starts with 0, remove the 0 and return a new string without 0.
 
Examples:
Using unittest TestCase

Data Structure:
Class with instance variables and methods.


Algorithm:
    Highend
    - Get the octal string input.
    - Validate the input.
    - calculate the decimal eqivalent of the input.
    - Return the value.


    Lowend:
        - Define a class Octal which accepts a string using the PerfectNumber constructor. 
        - Define a class contant OCTAL and set to 8.
        - Check if number is valid:
            - If valid set string to instance varible _octal_numb.
            - If ninvlaid, set '0' to instance varible _octal_numb

        - Define an instance method to_decimal.
        - Set a variable octal_to_decimal to 0.
        - Get the len of the string.
        - Iterate through the string from 0 till end of the string, strating from the last vaue.
            - set an adder_variable to muntiply (OCTAL^current (len of string -1 idx) * value at current index.
            - increment octal_to_decimal by added
            - Repeat till the last number.
        - Return octal_to_decimal.

        @staticmethod
        Helperfunction (is_valid_octal):
        - Def function which accept string:
        - check is string is alphanumber or 8,9 in string:
            - If yes, return "0"
        - check if string startswith '0':
            - if yes, right string all spaces and 0 and set the return string to a clean_octal.
            - return clean_octal
        - All all check is valid, return string as is.
'''

class Octal:
    OCTAL = 8

    def __init__(self, octal_string):
        self._octal_numb = self.is_valid_octal(octal_string)

    def to_decimal(self):
        octal_to_decimal = 0
        len_of_octal = len(self._octal_numb)

        for idx in range(0, len_of_octal):
            octal_adder = int(self._octal_numb[idx]) * (8 ** (len_of_octal - 1 - idx))
            octal_to_decimal +=  octal_adder

        return octal_to_decimal

    @staticmethod
    def is_valid_octal(octal_string):
        NONE_OCTALS =['8', '9']
        try:
            int(octal_string)
        except ValueError:
            return '0'
        
        for num in octal_string:
            if num in NONE_OCTALS:
                return '0'
        if octal_string.startswith('0'):
            clean_octal = octal_string.lstrip(' 0')
            return clean_octal

        return octal_string

test = Octal('17')
print(test.to_decimal())

class OctalTest(unittest.TestCase):
    def test_octal_1_is_decimal_1(self):
        self.assertEqual(1, Octal("1").to_decimal())

    def test_octal_10_is_decimal_8(self):
        self.assertEqual(8, Octal("10").to_decimal())

    def test_octal_17_is_decimal_15(self):
        self.assertEqual(15, Octal("17").to_decimal())

    def test_octal_11_is_decimal_9(self):
        self.assertEqual(9, Octal("11").to_decimal())

    def test_octal_130_is_decimal_88(self):
        self.assertEqual(88, Octal("130").to_decimal())

    def test_octal_2047_is_decimal_1063(self):
        self.assertEqual(1063, Octal("2047").to_decimal())

    def test_octal_7777_is_decimal_4095(self):
        self.assertEqual(4095, Octal("7777").to_decimal())

    def test_octal_1234567_is_decimal_342391(self):
        self.assertEqual(342391, Octal("1234567").to_decimal())

    def test_invalid_octal_is_decimal_0(self):
        self.assertEqual(0, Octal("carrot").to_decimal())

    def test_8_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("8").to_decimal())

    def test_9_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("9").to_decimal())

    def test_6789_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("6789").to_decimal())

    def test_abc1z_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("abc1z").to_decimal())

    def test_valid_octal_formatted_string_011_is_decimal_9(self):
        self.assertEqual(9, Octal("011").to_decimal())

    def test_234abc_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("234abc").to_decimal())

if __name__ == "__main__":
    unittest.main()

## LS Solution ##
# class Octal:
#     def __init__(self, number):
#         self.number = number

#     def to_decimal(self):
#         if not self._valid_octal(self.number):
#             return 0

#         digits = [int(digit) for digit in reversed(self.number)]
#         decimal_number = 0

#         for exponent, digit in enumerate(digits):
#             decimal_number += digit * (8**exponent)

#         return decimal_number

#     def _valid_octal(self, num):
#         return all(char.isdigit() and "0" <= char <= "7" for char in num)
