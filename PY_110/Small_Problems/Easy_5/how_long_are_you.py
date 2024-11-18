'''
How Long Are You?.
Write a function that takes a string as an argument and returns a
list that contains every word from the string,
with each word followed by a space and the word's length.
If the argument is an empty string or if no argument is passed,
the function should return an empty list.
You may assume that every pair of words in the string will be separated by a single space.

# Problem
- Input: 
String
- Output:
List

- Rules
    Explicit:
    Return an empty list if empty string argument is passed.
    Every pair of words in the string will be separated by a single space.

    Implicit:

# Examples

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True

# Data structure
List

# Algorithm
    - High End:
        1. Get input and set default argument to empty string.
        2. Check if string is empty and return an empty list.
        3. Split word into a list.
        4. Create a new list to hold result.
        5. Iterate through item in the split word:
            - concantenate item + space, + item lenght as strings.
            - Repeat for all item.
        6. Return list.
        
# Code
'''

# Solution
def word_lengths(string = ''):

    if string == '':
        return []

    list_word = string.split(' ')
    result = []

    for item in list_word:
        output = item + " " + str(len(item))
        result.append(output)

    return result

# code check
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True

# Note!
# Time take to write PEDAC and test/debug code is 7 mins, 54 seconds.
# Should have just used the f string and list comprehension.

## LS Answer ##
# def word_lengths(string=''):
#     if not string:
#         return []

#     return [f"{word} {len(word)}"
#             for word in string.split()]
#
# Defintely a smart solution