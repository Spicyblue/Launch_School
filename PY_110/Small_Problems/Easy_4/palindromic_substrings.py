'''
Palindromic Substrings.
Write a function that returns a list of all palindromic substrings of a string.
That is, each substring must consist of a sequence of characters that reads the same forward and backward.
The substrings in the returned list should be sorted by their order of appearance in the input string.
Duplicate substrings should be included multiple times.
You may (and should) use the substrings function you wrote in the previous exercise.
For the purpose of this exercise, you should consider all characters and pay attention to case;
that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not.
In addition, assume that single characters are not palindromes.

# Problem
- Input: 
String
- Output:
List of all palindromic substrings

- Rules
    Explicit:
    The substrings in the returned list should be sorted by their order of appearance in the input string.
    Order the returned list by where in the string the substring begins.
    Consider all characters and pay attention to case;
    Multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.
    'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not.
    Implicit:


# Examples
print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

# Data structure
List

# Algorithm
    - High End:
        1. Get input.
        2. Create a list to hold result.
        3. Create a start index begining at 0
        4. Iterate through the string.
           - In the outer loop.
                Create a stop index beginning at start + 1.
                    - In the inner loop.
                        - Using string indexing, access the string element from start to the stop index (substring).
                        -  check if substring is a palindrome.
                             - if yes, append to list.
                        - Increase stop index by 1.
                - Increatse the start index by 1.
        5.Return list.

# Code
'''

# Solution

def is_palindrome(string):
    return len(string) > 1 and string[ : : -1] == string

def palindromes(string):

    result = []
    start = 0

    while start < len(string):
        stop = start + 1
        while stop < len(string) + 1: 
            sub_string = string[start : stop]
            if is_palindrome(sub_string):
                result.append(sub_string)
            stop += 1

        start += 1
        print(result)

    return result

# code check
# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True


# Note!
# Time take to write PEDAC and test/debug code is 7 mins, 30 seconds.

# Just needed to added a palindrome check to the original code.

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

# def is_palindrome(word):
#     return len(word) > 1 and word == word[::-1]

# def palindromes(s):
#     return [substring
#             for substring in substrings(s)
#             if is_palindrome(substring)]