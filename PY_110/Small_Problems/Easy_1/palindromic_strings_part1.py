'''
Palindromic Strings (Part 1).
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise.
A palindrome reads the same forwards and backwards.
For this problem, the case matters and all characters matter.

# Problem:
    - Input:
    String
    Output:
    Bool

    Explicit:
    - A plalindrome
    - All case matters

# Examples

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

# Data Structure
List Perhaps for indexing

# Algorithm
    - Get input.
    - Create an empty string.
    - Reverse input and assign to empty string.
    - Check if input and empty string are the same (case matters).
        -If True, return True.
        -If false, return False.
    
# Code
'''

# Solution
def is_palindrome(string):

    reverse_string = string[ : : -1]

    if string == reverse_string:
        return True
    
    return False

# code check
print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)
print(is_palindrome('Madam') == False)  # case matters
print(is_palindrome("madam i'm adam") == False) # all characters matter

# Note!
# Time take to write PEDAC and test/debug code is 7 mins, 10 seconds.

### LS Anwer ###

# def is_palindrome(s):
#     return s == s[::-1]