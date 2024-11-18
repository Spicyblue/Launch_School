'''
Next prime sum.
Create a function that takes a list of integers as an argument. 
The function should determine the minimum integer value that can be appended
to the list so the sum of all the elements equal the closest prime number
that is greater than the current sum of the numbers. 
For example, the numbers in [1, 2, 3] sum to 6.
The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

Notes:
The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.

# Problem
- Input: 
String
- Output:
Integer

- Rules
    Explicit:
    - The list will always contain at least 2 integers.
    - All values in the list must be positive (> 0).
    - The function gets the minimum integer value that can be appended to the list
    so the sum of all the elements equal the closest prime number that is
    greater than the current sum of the numbers.

    Implicit:

# Examples
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

# Data structure
None

# Algorithm
    High level
    1. Get all sum of the list
    2. Define what a prime number is
    3. Find the minimum number than must be added to give a prime.
    4. Get that number.

    Low level:
        1. Get input.
        2. Get the sum of a input and add one to it.
        3. Get a counter and set to one.
        4. Define a prime number.
            - Helper function
            - Iterate from 2 to the last number before the input:
                - Check if the input is divisble by that any number in the sequence:
                    - If yes, return Fasle
                - If not, return True.
        4. Check if the sum is a a prime number:
            - If not, increase the sum by 1.
            - Increase counter by 1.
            - Repeat untill a prime number is reached.
        5. Return the counter,

# Code
'''

# Solution
def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    
    return True

def nearest_prime_sum(lst):
    current_sum  = sum(lst) + 1
    counter = 1
    
    while not is_prime(current_sum):
        current_sum += 1
        counter += 1

    return counter

# Code Check
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37
# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

# Note!
# Time take to write PEDAC and test/debug code 18 mins 21 seconds

# Now i have a mini function for checking prime numbers.

## LS Answer ##
# Not Available