import unittest
'''
Perfect Number.
The Greek mathematician Nicomachus devised a classification scheme for natural numbers (1, 2, 3, ...),
identifying each as belonging uniquely to the categories of abundant, perfect, or deficient
based on a comparison between the number and the sum of its positive divisors.
For instance, the positive divisors of 15 are 1, 3, and 5.
This sum is known as the Aliquot sum.

Perfect numbers have an Aliquot sum that is equal to the original number.
Abundant numbers have an Aliquot sum that is greater than the original number.
Deficient numbers have an Aliquot sum that is less than the original number.

Examples:
6 is a perfect number since its divisors are 1, 2, and 3, 
and 1 + 2 + 3 = 6.
28 is a perfect number since its divisors are 1, 2, 4, 7, and 14
and 1 + 2 + 4 + 7 + 14 = 28.
15 is a deficient number since its divisors are 1, 3, and 5 
and 1 + 3 + 5 = 9 which is less than 15.
24 is an abundant number since its divisors are 1, 2, 3, 4, 6, 8,and 12 
and 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36 which is greater than 24.

Prime numbers 7, 13, etc. are always deficient since their only divisor is 1.
Write a program that can tell whether a number is perfect, abundant, or deficient.

'''

# Solution
'''
PEDAC
Problem:
    Input: Integer
    output: String

    Exp: 
    - Only accept Integers and returns a string.
    - Output can be 'perfect', 'abundant' or 'deficient'
    - This is calculated from the aliquot sum

    imp:
    - unittest test cases show that our we need a PerfectNumber class which
      accepts integer arguments passed to its constructor.
    - None value types should return 0.
    - The class should have a classify which returns the type of number.
    - The class should have a method fail for handling numbers < 0, which raises a ValueError.
 
Examples:
Using unittest TestCase

Data Structure:
Class with classmethods and static methods.


Algorithm:
    Highend
    - Get the number.
    - Get its aliquot sum.
    - Get the total of its aliquot sum.
    - Return the type of number based on this.


    Lowend:
        - Define a class PerfectNumber with a class method that takes one argument, an integer.
        - Check if the number is greater than zero, if not, raise a ValueError.
        - Within the class method, create a variable aliquot_num set to an empty list.
        - Iterate through the all numbers from 1 till the last number before _number:
            - check if the current number is a positive divisor of _number. 
                - If yes, add the number to aliquot_num
            repeat for all number

        - Use the helper function (static method)
        below to get the type of number and assign it to a variable number_type
            - helper function (get_type_of_num)
            - A helper function which accpets a list of integers and a number
            - Check if the sum of the list of integers is equall to number:
                if yes, return 'perfect'
            - Check if the sum of the list of integers is greater than the number:
                if yes, return 'abundant' 
            - else, return 'deficient'.

        - return number type.
'''

class PerfectNumber:

    @classmethod
    def classify(cls, num):
        number = cls.fail(num)
        aliquot_num = [num for num in range(1, number) if number % num == 0]
        type_of_num = cls.get_type_num(aliquot_num,number)

        return type_of_num

    @staticmethod
    def get_type_num(lst_of_num, number):
        aliquot_sum = sum(lst_of_num)

        if aliquot_sum ==  number:
            return 'perfect'
        elif aliquot_sum > number:
            return 'abundant'
        else:
            return 'deficient'
    
    @classmethod
    def fail(cls, number):
        if number < 1:
            raise ValueError("Input must be a positive integer")
        else:
            return number

class PerfectNumberTest(unittest.TestCase):
    def test_initialize_perfect_number(self):
        try:
            PerfectNumber.classify(-1)
            self.fail("Expected exception not raised")
        except ValueError as e:
            self.assertEqual(str(e), "Input must be a positive integer")

    def test_classify_deficient(self):
        result = PerfectNumber.classify(13)
        self.assertEqual(result, "deficient")

    def test_classify_perfect(self):
        result = PerfectNumber.classify(28)
        self.assertEqual(result, "perfect")

    def test_classify_abundant(self):
        result = PerfectNumber.classify(12)
        self.assertEqual(result, "abundant")

if __name__ == "__main__":
    unittest.main()


## LS Solution ##
# class PerfectNumber:
#     @classmethod
#     def classify(cls, number):
#         if number < 1:
#             raise ValueError("Input must be a positive integer")

#         sum_of_factors = cls._sum_of_factors(number)

#         if sum_of_factors == number:
#             return "perfect"
#         elif sum_of_factors > number:
#             return "abundant"
#         else:
#             return "deficient"

#     @staticmethod
#     def _sum_of_factors(number):
#         factors = [
#             possible_divisor
#             for possible_divisor in range(1, number)
#             if number % possible_divisor == 0
#         ]
#         return sum(factors)
