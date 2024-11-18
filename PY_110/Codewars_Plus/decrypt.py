'''
Available at https://www.codewars.com/kata/58693136b98de0e4910001ab/train/python
Level = 6kyu

Decrypt.
You'll be given a string of random characters (numbers, letters, and symbols).
To decode this string into the key we're searching for:

(1) count the number occurences of each ascii lowercase letter, and
(2) return an ordered string, 26 places long, corresponding to the number of occurences for each corresponding letter in the alphabet.

For example:
'$aaaa#bbb*cc^fff!z' gives '43200300000000000000000001'
   ^    ^   ^  ^  ^         ^^^  ^                   ^
  [4]  [3] [2][3][1]        abc  f                   z
  
'z$aaa#ccc%eee1234567890' gives '30303000000000000000000001'
 ^  ^   ^   ^                    ^ ^ ^                    ^
[1][3] [3] [3]                   a c e                    z

Remember, the string returned should always be 26 characters long, and only count lowercase letters.
Note: You can assume that each lowercase letter will appears a maximum of 9 times in the input string.


# Problem
- Input: 
String
- Output:
String

- Rules
    Explicit:
    - Return an ordered string, 26 places long, corresponding to the number of occurences for each corresponding letter in the alphabet.
    - You can assume that each lowercase letter will appears a maximum of 9 times in the input string

    Implicit:
    - Return 0 for lowercase alphabet not occuring.

# Examples
print(decrypt('$aaaa#bbb*ccfff!z') == '43200300000000000000000001')
print(decrypt('z$aaa#ccc%eee1234567890') == '30303000000000000000000001')

# Data structure
Dictionary

# Algorithm
    High level
    1. Count all the alpbaets occuring in the string
    2. Get them returned back by order of the alphabet.

    Low level:
        1. Get input.
        2. Create a dictionary with all the alpbaets and set them to zero.
        3. Iterate through the input:
            - Check if the current character is lowercase:
                - If yes,increase its dictionary value by 1
                - repeat for all characters in the string.

        4. Sort the dictionary by the key and get its values as strings.
            - Use a list comprehension.
            - Join the string together.

        5. Return the result.

# Code
'''

# Solution
def decrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_dict = {letter : 0  for letter in alphabet}
    
    for char in string:
        if char.islower():
            alpha_dict[char] += 1

    result = "".join([str(count) for _, count in sorted(alpha_dict.items())])

    return result

# other solution:
# def decrypt(test_key):
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     s = ''
#     for n in alpha:
#         s += str(test_key.count(n))
#     return s


# Code Check
print(decrypt('$aaaa#bbb*ccfff!z') == '43200300000000000000000001')
print(decrypt('z$aaa#ccc%eee1234567890') == '30303000000000000000000001')

# Note!
# Time take to write PEDAC and test/debug code 14 mins 21 seconds

## LS Answer ##
# Not Available