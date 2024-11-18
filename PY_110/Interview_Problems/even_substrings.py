'''
Even substrings.
Create a function that takes a string of digits as an argument and 
returns the number of even-numbered substrings that can be formed. 
For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', 
for a total of 6 substrings.
If a substring occurs more than once,
you should count each occurrence as a separate substring.

# Problem
- Input: 
String
- Output:
Integer

- Rules
    Explicit:
    - Returns the number of even-numbered substrings that can be formed.
    - If a substring occurs more than once, you should count each occurrence as a separate substring.

    Implicit:

# Examples
print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

# Data structure

# Algorithm
    High level
    1. Get all possible combination of the string.
    2. Select only the even combination.
    3. Get back the number of positive selection

    Low level:
        1. Get input.
        2. Create empty list to append to result.
        3. Iterate through the input:
            - Get the first number:
            - iterate through the rest of the input:
                - Get the next number.
                - Concantenate numbers together
                - Convert to integer and check if its odd (helper function)
                - If yes
                    - Add the Concantenated number to result.

        4. Return lenght of result.

# Code
'''

# Solution
def is_even(string):
    num = int(string)
    return num % 2 == 0

def even_substrings(string):
    result = []
    end = len(string)
   
    for start in range(end):
        for stop in range(start + 1, end + 1):
            substring = string[start: stop]

            if is_even(substring):
                result.append(substring)
    
    count = len(result)

    return count

# using list comprehension:
# def even_substrings(string):
#     end = len(string)
#     result = len([string[start : stop] for start in range(end) for stop in range (start + 1, end + 1) if is_even(string[start : stop])])

#     return result

# Code Check
print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

# Note!
# Time take to write PEDAC and test/debug code 12 mins 09 seconds

## LS Answer ##
# Not Available