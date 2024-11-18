'''
Fibonacci Numbers (Memoization).
Our recursive fibonacci function from the previous exercise isn't very efficient. 
It starts slowing down with an nth argument value somewhere around 35-60, depending on your system.
One way to improve the performance of our recursive fibonacci function (and other recursive functions) is to use memoization.
Memoization is an approach that involves saving a computed answer for future reuse,
instead of computing it from scratch every time it is needed.
In the case of our recursive fibonacci function, using memoization saves calls to fibonacci(nth - 2)
because the necessary values have already been computed by the recursive calls to fibonacci(nth - 1).
Hint: One approach to memoization is to use a lookup table, such as an object,
for storing and accessing previously computed values.
For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.
In mathematical terms, this can be represented as:
    F(1) = 1
    F(2) = 1
    F(n) = F(n - 1) + F(n - 2)    (where n > 2) 

Solve this using the recursion and memoization.

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
    - Use recursion and memoization.

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
        3. Check if the next recursive has already been calculated.
            -If yes, use this.
            -If not, store this.
        4. Return the recursion

# Code
'''

# Solution

already_calculated = {}
def fibonacci(number):

    if number <= 2:
        return 1
    elif number in already_calculated:
        return already_calculated[number]
    else:
        already_calculated[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return already_calculated[number]

# code check
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True

# Time take to write PEDAC and test/debug code is not available at the time being.

## LS Answer ##
# memo = {}
# def fibonacci(nth):
#     if nth <= 2:
#         return 1
#     elif nth in memo:
#         return memo[nth]
#     else:
#         memo[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
#         return memo[nth]

