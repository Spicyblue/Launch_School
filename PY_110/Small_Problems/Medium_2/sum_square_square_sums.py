'''
Sum Square - Square Sum
Write a function that computes the difference between the square of the sum of the first count positive integers
and the sum of the squares of the first count positive integers.

# Problem
- Input: 
Integer
- Output:
Integer

- Rules
    Explicit:
    - Computes the square of the sum of the first count positive integers.
    - Computes the sum of the squares of the first count positive integer.

    Implicit:

# Examples
print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True


# Data structure
List

# Algorithm
    - High End:
        1. Get input.
        2. Get the square of the sum of the first count positive integer.
        3. Get the sum of the square of the first count positive integer.
        4. Return the value of step 2 minus step 3.

# Code
'''

# Solution
def square_of_sum_of_first_count(number):
    sum_of_count = sum([num for num in range(number + 1)])
    return sum_of_count ** 2

def sum_of_square_of_first_Count(number):
    square_of_count = sum([num**2 for num in range(number + 1)])
    return square_of_count

def sum_square_difference(num):
    square_of_sum = square_of_sum_of_first_count(num)
    sum_of_square = sum_of_square_of_first_Count(num)
    return square_of_sum - sum_of_square

# code check
print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

# Note!
# Time take to write PEDAC and test/debug code is 14 mins, 19 seconds.

## LS Answer ##
# def sum_square_difference(count):
#     sum_ = sum(range(1, count + 1))

#     sum_of_squares = 0
#     for i in range(1, count + 1):
#         sum_of_squares += i**2

#     return sum_**2 - sum_of_squares