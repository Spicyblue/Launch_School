'''
Sequence Count.
Create a function that takes two integers as arguments.
The first argument is a count, and the second is the
starting number of a sequence that your function will create.
The function should return a list containing the same number of elements as the count argument.
The value of each element should be a multiple of the starting number.

# Problem
- Input: 
integer
- Output:
list

- Rules
    Explicit:
    The first argument is a count.
    The second is the starting number of a sequence that your function will create. 
    The function should return a list containing the same number of elements as the count argument.
    The value of each element should be a multiple of the starting number.
    The starting number can be any integer.
    If the count is 0, the function should return an empty list.

# Examples
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Create a range and define its argument.
            - Start is the value of the start argument.
            - stop is the value of the count argument + 1.
            - multiply the number in the sequence by start argument.
        3. Convert range to list and return it.
        4. Use list comprehension for 1 - 4.

# Code
'''

# Solution
def sequence(count, start):
    return [start * num for num in range(1 , count + 1)]

# Code Check
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

# Note!
# Time take to write PEDAC and test/debug code is 8 mins, 58 seconds.

## LS Answer ##
# def sequence(count, start_num):
#     return [start_num * num for num in range(1, count + 1)]