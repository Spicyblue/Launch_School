'''
Fibonacci Numbers (Recursion).
The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers.
The first two Fibonacci numbers are 1 and 1.
The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on.
In mathematical terms, this can be represented as:
    F(1) = 1
    F(2) = 1
    F(n) = F(n - 1) + F(n - 2)    (where n > 2) 
Solve this using the recursion.

# Problem:
- Input:
Integer
- Output:
Integer

- Rules
    Explicit:
    Function computes the nth Fibonnacci number.
    The Fibonacci sequence starts with two 1s: F(1) = 1, F(2) = 1.
    Each subsequent number is the sum of the previous two numbers: F(n) = F(n-1) + F(n-2) for n > 2.

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
        2. Check if the input is less than 2, if yes, return 1. (base case)
        3. Return function(input - 1) + function(input - 2).


# Code
'''

# # Solution
def fibonacci(number):

    if number <= 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)

# code check
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True

# Time take to write PEDAC and test/debug code is 40 mins, 12 seconds.

# Took time to understand the recursion works and it can be applied to the Fibonnacci serries worked
# before being able to succesfully implement it.
# I still dont fully understand how it work especially
# with regards to the fibonacci sequence.
# Clearly would need more time with this before it become intuitive.

## LS Answer ##
# def fibonacci(n):
#     if n <= 2:
#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)