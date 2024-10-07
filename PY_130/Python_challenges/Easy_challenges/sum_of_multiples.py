import unittest
'''
Sum of Multiples.
Write a program that, given a natural number and a set of one or more other numbers,
can find the sum of all the multiples of the numbers in the set that are less than the first number.
If the set of numbers is not given, use a default set of 3 and 5.

For instance, if we list all the natural numbers up to,
but not including, 20 that are multiples of either 3 or 5,
we get 3, 5, 6, 9, 10, 12, 15, and 18.
The sum of these multiples is 78.
'''

# Solution
'''
PEDAC
Problem:
    Input: Integer
    output: Integers

    Exp: 
    - Valid natural numbers are integers above 0.
    - Sum of multiples do not include the natural numbers.
    - Do not include the natural number as multiples
    - Default sets of multiples are 3 and 5

    imp:
    - unittest test cases show that our we need a SumOfMultiples class that accept
      any argument passed to its constructor.
    - The class should have a sum_up_to classmethod to which takes
      in one argument and returns the sum of multiples based on the default set or sets passed.
    - The class should have a to classmethod to which takes
      one argument and returns the sum of multiples based on the default set or sets passed.

Examples:
Using unittest TestCase

Data Structure:
Class with class variables and methods.

Algorithm:
    Highend
    - Get the naturla number.
    - Find all its factors based on the sets.
    - Sum the factos.
    - Return the sum

    Lowend:
        - Define a class SumOfMultiples that accept variable number of arguments (*args)
        - Set self._sets_of_numbers to args if provided, otherwise to (3, 5)

        - Define a class method sum_up_to:
        - Accept parameter nat_num
        - Set cls._sets_of_numbers to (3, 5)
        - Call _get_sum_of_multiples with nat_num and cls._sets_of_numbers
        - Return the result

        - Define an instance method to:
        - Accept parameter nat_num
        - Call _get_sum_of_multiples with nat_num and self._sets_of_numbers
        - Return the result

        - Define a static method _get_sum_of_multiples:
        - Accept parameters numb and lst_of_sets_of_numbers
        - Set natural_num to numb
        - Create a list of multiples:
            - For each factor in lst_of_sets_of_numbers
                - For each number from 0 to natural_num (exclusive)
                    - Include number if it's divisible by the factor

            - Convert the set to a list and get the sum.
        - Return the sum.
'''

class SumOfMultiples:
    def __init__(self, *args ):
        self._sets_of_numbers = args if args else (3,5)
    
    @classmethod
    def sum_up_to(cls, nat_num):
        cls._sets_of_numbers = (3, 5)
        sum_of_multiples = cls._get_sum_of_multiples(nat_num, cls._sets_of_numbers)
        return sum_of_multiples

    def to(self, nat_num):
        sum_of_multiples = self._get_sum_of_multiples(nat_num, self._sets_of_numbers)
        return sum_of_multiples

    @staticmethod
    def _get_sum_of_multiples(numb, lst_of_sets_of_numbers):
        natural_num  = numb
        multiples_of_nat_num = list({numb 
                                    for factors in lst_of_sets_of_numbers
                                    for numb in range(natural_num)
                                    if numb % factors == 0})

        sum_of_multiples = sum(multiples_of_nat_num)
        return sum_of_multiples


class SumTest(unittest.TestCase):
    def test_sum_to_1(self):
        self.assertEqual(0, SumOfMultiples.sum_up_to(1))

    def test_sum_to_3(self):
        self.assertEqual(3, SumOfMultiples.sum_up_to(4))

    def test_sum_to_10(self):
        self.assertEqual(23, SumOfMultiples.sum_up_to(10))

    def test_sum_to_100(self):
        self.assertEqual(2_318, SumOfMultiples.sum_up_to(100))

    def test_sum_to_1000(self):
        self.assertEqual(233_168, SumOfMultiples.sum_up_to(1000))

    def test_configurable_7_13_17_to_20(self):
        self.assertEqual(51, SumOfMultiples(7, 13, 17).to(20))

    def test_configurable_4_6_to_15(self):
        self.assertEqual(30, SumOfMultiples(4, 6).to(15))

    def test_configurable_5_6_8_to_150(self):
        self.assertEqual(4419, SumOfMultiples(5, 6, 8).to(150))

    def test_configurable_43_47_to_10000(self):
        self.assertEqual(2_203_160, SumOfMultiples(43, 47).to(10_000))

if __name__ == "__main__":
    unittest.main()

# LS Solution ##
# class SumOfMultiples:
#     def __init__(self, *multiples):
#         self.multiples = multiples if multiples else (3, 5)

#     def to(self, num):
#         return sum(x for x in range(1, num) if self._any_multiple(x))

#     @classmethod
#     def sum_up_to(cls, num):
#         return cls().to(num)

#     def _any_multiple(self, num):
#         return any(num % multiple == 0 for multiple in self.multiples)

# ngl LS solution was more elegant!!!