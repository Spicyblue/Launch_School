'''
Fibonacci Numbers (Procedural).
The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers.
The first two Fibonacci numbers are 1 and 1.
The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on.
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
        2. Check if the input is less than 2, if yes, return 1.
        3. Initialize the first two numbers of the fibonacci_series.
        4. Iterate through the input starting from 3.
            - Calculate the next Fibonacci number as the sum of first and second.
            - Update first number to the value of second number.
            - Update second number to the value of the new Fibonacci number.
        5. Return recond number which is the last number in the fibonacci_series.

# Code
'''

# # Solution
def fibonacci(number):

    if number < 3:
        return 1

    first_number =  1
    second_number = 1

    for _ in range(3, number + 1):

        fibonacci_series = first_number + second_number

        first_number = second_number

        second_number = fibonacci_series

        print('Fibonacci number is' ,fibonacci_series)

    return fibonacci_series

# code check
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

# Time take to write PEDAC and test/debug code is 16 mins, 45 seconds.

# Took time to understand the logic of how the Fibonnacci serries worked before being able to succesfully implement it.

## LS Answer ##
# def fibonacci(nth):
#     if nth <= 2:
#         return 1

#     previous, current = 1, 1
#     for _ in range(3, nth + 1):
#         previous, current = current, previous + current

#     return current