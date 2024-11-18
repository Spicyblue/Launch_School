'''
Fibonacci Number Location By Length.
As we've seen in the last few exercises, the Fibonacci series is a computationally simple series.
However, the results grow at an incredibly rapid rate.
For example, the 100th Fibonacci number is 354,224,848,179,261,915,075 -- that's enormous,
especially considering that it takes six iterations just to find the first 2-digit Fibonacci number.
Write a function that calculates and returns the index of the first Fibonacci number
that has the number of digits specified by the argument.
The first Fibonacci number has an index of 1.
You may assume that the argument is always an integer greater than or equal to 2.
Since Python version 3.10.7, conversion of large integers to strings with more than 4300 digits raises an error.
Try to figure out a way to bypass this.
To bypass this limitation, we can use set sys.set_int_max_str_digits
from the sys module to a new upper limit.
First, we import the sys module, then we call sys.set_int_max_str_digits with
the maximum digits desired for string conversion.

In mathematical terms, this can be represented as:
    F(1) = 1
    F(2) = 1
    F(n) = F(n - 1) + F(n - 2)    (where n > 2) 

# Problem:
- Input:
Integer
- Output:
Integer

- Rules
    Explicit:
    Function computes the nth Fibonnacci number.
    The first Fibonacci number has an index of 1.
    The argument is always an integer greater than or equal to 2.
    Returns the index of the first Fibonacci number that has the number of digits specified by the argument

# Examples:
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

# Data structure
None

# Algorithm
    - High End 
        1. Get input.
        2. Set the maximum integer to string conversion.
        3. Set a counter to keep track of the index.
        4. Iterate through the recursion return values 
            - Convert  the return values to string and check if their length is less than the input.
            - if yes, increase counter till the right lenght is reached
        4. Return the counter.

# Code
'''

# Solution

import sys

already_calculated = {}
def fibonacci(number):

    if number <= 2:
        return 1
    elif number in already_calculated:
        return already_calculated[number]
    else:
        already_calculated[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return already_calculated[number]


def find_fibonacci_index_by_length(index):
    sys.set_int_max_str_digits(50_000)

    count = 0

    while len(str(fibonacci(count))) < index:
        count += 1
        print(fibonacci(count))

    return count

# code check
# print(find_fibonacci_index_by_length(2) == 7)
# print(find_fibonacci_index_by_length(3) == 12)
# print(find_fibonacci_index_by_length(10) == 45)
# print(find_fibonacci_index_by_length(16) == 74)
# print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)

# # Next example might take a little while on older systems
# print(find_fibonacci_index_by_length(10000) == 47847)

# Time take to write PEDAC and test/debug code is not available at the time being.

## LS Answer ##
# import sys

# def find_fibonacci_index_by_length(length):
#     sys.set_int_max_str_digits(50_000)
#     first = 1
#     second = 1
#     count = 2

#     while len(str(second)) < length:
#         first, second = second, first + second
#         count += 1

#     return count
