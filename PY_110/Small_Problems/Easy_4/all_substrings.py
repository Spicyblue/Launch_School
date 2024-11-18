'''
All Substrings.
Write a function that returns a list of all substrings of a string.
Order the returned list by where in the string the substring begins.
This means that all substrings that start at index position 0 should come first, 
then all substrings that start at index position 1, and so on.
Since multiple substrings will occur at each position,
return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:

# Problem
- Input: 
String
- Output:
List of all substrings

- Rules
    Explicit:
    Returns a list of all substrings of a string
    Order the returned list by where in the string the substring begins.

    Implicit:

# Examples
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

# Data structure
List

# Algorithm
    - High End:
        1. Get input.
        2. Create a list to hold result.
        3. Create a start index begining at 0.
        4. Iterate through the string.
           - In the outer loop
                Create a stop index beginning at start + 1:
                    - In the inner loop:
                        - Using string indexing, access the string element from start to the stop index.
                        - Add element to list.
                        - Increase stop index by 1.
                - Increatse the start index by 1.
        5.Return list.

# Code
'''

# Solution
def substrings(string):

    result = []
    start = 0

    while start < len(string):
        stop = start + 1

        while stop < len(string) + 1: 
            sub_string = string[start : stop]
            result.append(sub_string)
            print(result)
            stop += 1

        start += 1

    return result

# code check
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

# Note!
# Time take to write PEDAC and test/debug code is 28 mins, 30 seconds.

# While loops can be tricky and so, my challenge here was trying to figure 
# the inner while loop syntax. How do i stop by 1 for every time start increases by 1..
# Well , now i know!.

## LS Answer ##
# def leading_substrings(string):
#     return [string[:idx + 1] for idx in range(len(string))]

# def substrings(string):
#     results = []
#     for idx in range(len(string)):
#         string_at_idx = string[idx:]
#         for substring in leading_substrings(string_at_idx):
#             results.append(substring)

#     return results

# Solution 2
# def leading_substrings(string):
#     return [string[:idx + 1] for idx in range(len(string))]

# def substrings(string):
#     return [
#         substring
#         for idx in range(len(string))
#         for substring in leading_substrings(string[idx:])
#     ]
