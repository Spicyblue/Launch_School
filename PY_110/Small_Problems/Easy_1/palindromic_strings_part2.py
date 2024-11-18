'''
Palindromic Strings (Part 2).
Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. 
This time, however, your function should be case-insensitive,
 and should ignore all non-alphanumeric characters. 
If you wish, you may simplify things by calling the
is_palindrome function you wrote in the previous exercise.

# Problem:
    - Input:
    String
    - Output:
    Bool

    - Explicit:
    A plalindrome
    Case dosent matter, only alphanumerics matter

# Examples

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# Data Structure
List Perhaps for indexing

# Algorithm
    - Get input.
    - Create an empty string to hold the clean new string.
    - Clean the input string by removing all characters than are not alphanumeric and assing to empty string.
    - Reverse the cleaned string.
    - Check if reversed cleaned string and cleaned strings are the same.
        -If True, return True.
        -If false, return False.
    
# Code
'''

# Solution
def is_real_palindrome(string):
    # clean the input string
    new_string = ''

    for char in string:
        if char.isalnum():
            new_string += char.casefold()
    
    reversed_new_string = new_string[ : : -1]

    if new_string == reversed_new_string:
        return True
    
    return False

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# Note!
# Time take to write PEDAC and test/debug code is 5 mins, 10 seconds.
# Reason because I had the same code from the previous exercise.

# ## LS Answer ##
# def is_palindrome(s):
#     return s == s[::-1]

# def is_real_palindrome(s):
#     cleaned_string = ''
#     for char in s:
#         if char.isalnum():
#             cleaned_string += char.casefold()
    
#     print(cleaned_string)

#     return is_palindrome(cleaned_string)
