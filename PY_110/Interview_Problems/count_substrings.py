'''
Count substrings.
Create a function that takes two string arguments and returns
the number of times that the second string occurs in the first string.
Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.
You may assume that the second argument is never an empty string.

# Problem
- Input: 
String
- Output:
Integer

- Rules
    Explicit:
    - Overlapping strings don't count.

    Implicit:
    - empty string return 0.

# Examples
print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

# Data structure
None

# Algorithm
    High level
    1. Get back the number of times the substring apprears in the string.

    Low level:
        1. Get input.
        2. Set counter to 0.
        3. check the number of times the substring appears in the string
            - set counter to this number.
        4. Return counter.

# Code
'''

# Solution
def count_substrings(string, substring):
   count = string.count(substring)
   print(count)
   
   return count

# code check
print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

# Note!
# Time take to write PEDAC and test/debug code 5 mins 21 seconds

## LS Answer ##
# Not Available