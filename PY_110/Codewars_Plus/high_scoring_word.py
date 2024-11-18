'''
Available at https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
Level = 6kyu

Highest scoring word.
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

# Problem
- Input: 
String
- Output:
String

- Rules
    Explicit:
    - You need to return the highest scoring word as a string.
    - If two words score the same, return the word that appears earliest in the original string.
    - All letters will be lowercase and all inputs will be valid.

    Implicit:

# Examples
print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')
print(high('aa b') == 'aa')
print(high('b aa') == 'b')
print(high('bb d') == 'bb')
print(high('d bb') == 'd')
print(high("aaa b") == "aaa")

# Data structure
List

# Algorithm
    High level
    1. Covert words to list.
    2. Sort them based on the score.
    3. Get the first word with the highest score.

    Low level:
        1. Get input.
        2. Split input into a list.
        3. Sort the list based on the character point of the letters.
        4. Return the first word in the sorted result.

# Code
'''

# Solution
def high(string):
    string_lst = string.split(' ')
    result = sorted(string_lst, key = get_string_score, reverse= True)

    return result[0]

    
def get_string_score(string_input):
    count = 0

    for char in string_input:
        count += (ord(char) - 96)

    return count
        

# other solution:
# def high(string):
#     string_list = string.split(' ')
#     max_count = 0
#     result = ''

#     for idx in range(len(string_list)):
#         word = string_list[idx]
#         count = 0
#         for char in word:
#             count += (ord(char) - 96)

#         if count > max_count:
#             max_count = count
#             result = word

#     return result

# Code Check
print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')
print(high('aa b') == 'aa')
print(high('b aa') == 'b')
print(high('bb d') == 'bb')
print(high('d bb') == 'd')
print(high("aaa b") == "aaa")


# Note!
# Time take to write PEDAC and test/debug code 11 mins 07 seconds

## LS Answer ##
# Not Available
