'''
Is It Prime?
A prime number is a positive number that is evenly divisible only by itself and 1.
Thus, 23 is prime since its only divisors are 1 and 23.
However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24.
Note that the number 1 is not prime.

Write a function that takes a positive integer as an argument and returns true if the number is prime,
false if it is not prime.
You may not use any of Python's add-on packages to solve this problem.
Your task is to programmatically determine whether a number is prime without relying on functions that already do that for you.

# Problem:
- Input:
Integer
- Output:
Integer

- Rules
    Explicit:
    A prime number is only divisible by 1 and itself
    

# Examples:
print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True

# Data structure
None

# Algorithm
    - High End 
        1. Get input.
        2. If input is 1, return False as 1 cannot be a prime number.
        3. Interate through the all the sequence avalible for the input after 1 (from  2) till end (but not including the number).
            - If any resulting number can divide the input, return False
        4. Return False

# Code
'''

# Solution
def is_prime(number):

    if number == 1:
        return False

    for nums in range(2, number):
        if number % nums == 0:
            return False
    
    return True

# code check
print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True


# Time take to write PEDAC and test/debug code is 2 mins, 45 seconds.

## LS Answer ##
# def is_prime(number):
#     if number == 1:
#         return False

#     for divisor in range(2, number):
#         if number % divisor == 0:
#             return False

#     return True

# Solution 2
# import math

# def is_prime(number):
#     if number == 1:
#         return False

#     for divisor in range(2, int(math.sqrt(number)) + 1):
#         if number % divisor == 0:
#             return False

#     return True

