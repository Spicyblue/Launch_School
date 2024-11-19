import unittest
'''
Series
Write a program that will take a string of digits and return all
the possible consecutive number series of a specified length in that string.

For example, the string "01234" has the following 3-digit series:

012
123
234
Likewise, here are the 4-digit series:

0123
1234
Finally, if you ask for a 6-digit series from a 5-digit string, you should throw an error.

'''

# Solution
'''
PEDAC
Problem:
    Input: string
    output: list

    Exp: 
    - Valid inputs are strings.
    - Returns a list of consecutive number series based on a specific length.
    - If the specific lenght is longer than the string, throw and error

    imp:
    - unittest test cases show that our we need a Series class that accept string arguments passed to its constructor.
    - The class should have a slices method to which takes in one argument and returns the list of consecutive number having same length as the argument.

Examples:
Using unittest TestCase

Data Structure:
Class with class variables and methods.

Algorithm:
    Highend
    - Get the string number input.
    - Get the slices required.
    - Return all possible combination of the slices in a list.

    Lowend:
        - Define a class Series that accept a string number when passed as an argument.
        - Set self._number to string number.

        - Define a instance method slices that accepts one argument.
        - Set this to _slice_lenght
        - create an empty list _slice_lst = []
        - check if slice_lenght > self._number:
            if yes, raise a ValueError
        - Iterate from idx to len(self._number - slice_lenght):
            - get the slice from current index : current idex + slice_lenght
            - Convert each string to integer and convert to a list.
            - Add list to _slice_lst. 
            - Repeat till all possible list is gotten.
        - Return _slice_lst.
'''

class Series:

    def __init__(self, string_number):
        self._number = string_number

    def slices(self, slice_lenght):
        slice_lst = []
        end = len(self._number) - slice_lenght + 1

        if slice_lenght > len(self._number):
            raise ValueError

        for idx in range(end):
            sliced_value = self._number[idx : idx + slice_lenght]
            slice_lst.append([int(digit) for digit in sliced_value])

        return slice_lst


class SeriesTest(unittest.TestCase):
    def test_simple_slices_of_one(self):
        series = Series("01234")
        self.assertEqual([[0], [1], [2], [3], [4]], series.slices(1))

    def test_simple_slices_of_one_again(self):
        series = Series("92834")
        self.assertEqual([[9], [2], [8], [3], [4]], series.slices(1))

    def test_simple_slices_of_two(self):
        series = Series("01234")
        self.assertEqual([[0, 1], [1, 2], [2, 3], [3, 4]], series.slices(2))

    def test_other_slices_of_two(self):
        series = Series("98273463")
        expected = [[9, 8], [8, 2], [2, 7], [7, 3], [3, 4], [4, 6], [6, 3]]
        self.assertEqual(expected, series.slices(2))

    def test_simple_slices_of_two_again(self):
        series = Series("37103")
        self.assertEqual([[3, 7], [7, 1], [1, 0], [0, 3]], series.slices(2))

    def test_simple_slices_of_three(self):
        series = Series("01234")
        self.assertEqual([[0, 1, 2], [1, 2, 3], [2, 3, 4]], series.slices(3))

    def test_simple_slices_of_three_again(self):
        series = Series("31001")
        self.assertEqual([[3, 1, 0], [1, 0, 0], [0, 0, 1]], series.slices(3))

    def test_other_slices_of_three(self):
        series = Series("982347")
        expected = [[9, 8, 2], [8, 2, 3], [2, 3, 4], [3, 4, 7]]
        self.assertEqual(expected, series.slices(3))

    def test_simple_slices_of_four(self):
        series = Series("01234")
        self.assertEqual([[0, 1, 2, 3], [1, 2, 3, 4]], series.slices(4))

    def test_simple_slices_of_four_again(self):
        series = Series("91274")
        self.assertEqual([[9, 1, 2, 7], [1, 2, 7, 4]], series.slices(4))

    def test_simple_slices_of_five(self):
        series = Series("01234")
        self.assertEqual([[0, 1, 2, 3, 4]], series.slices(5))

    def test_simple_slices_of_five_again(self):
        series = Series("81228")
        self.assertEqual([[8, 1, 2, 2, 8]], series.slices(5))

    def test_simple_slice_that_blows_up(self):
        series = Series("01234")
        with self.assertRaises(ValueError):
            series.slices(6)

    def test_more_complicated_slice_that_blows_up(self):
        slice_string = "01032987583"
        series = Series(slice_string)
        with self.assertRaises(ValueError):
            series.slices(len(slice_string) + 1)

if __name__ == "__main__":
    unittest.main()

# LS Solution ##
# class Series:
#     def __init__(self, number_string):
#         self.number_string = number_string

#     def slices(self, length):
#         if length > len(self.number_string):
#             raise ValueError("Slice length is greater than string length")

#         numbers = [int(char) for char in self.number_string]
#         return [numbers[idx : idx + length] for idx in range(len(numbers) - length + 1)]

