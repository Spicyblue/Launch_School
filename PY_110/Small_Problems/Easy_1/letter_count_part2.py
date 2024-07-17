'''
Letter Counter (Part 2).
Write a function that takes a string consisting of zero or more space-separated words
and returns a dictionary that shows the number of words of different sizes.
Words consist of any sequence of non-space characters.
Modify the function above to exclude non-letters when determining word size.
For instance, the word size of "it's" is 3, not 4.

# Problem
    - Input: 
    string
    - Output: 
    Dictionary (Key is length of string and value is numbeer of time it occurs )

    Rules:
    - Explicit:
    String consisting of zero or more space-separated words
    Remove all signs and symbols
    Dictionary that shows the number of words of different sizes.
    - Implicit:
    Empty string returns empty dictionary

# Examples
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

# Data Structure:
Dictionary

# Algorithm
    -High level
        1. Enter string Input
        2. Clean string by removing all signs/symbols
        2. Split cleaned string into list of words and store
        3. Create empty dictionary
        4. Iterate through the word in the list
            - set the len of each word to be a key used to determine the key for the dictionary-
            - If the key exist, increase its value by 1
            - else, create a new key 
        5. Can also use dicionary comprehension for step 3 and 4
        6. Return new dictionary

# Code 
'''

# Solution
def remove_symbols(string):

    result = ""

    for char in string:
        if char.isalnum() or char.isspace():
            result += char

    return result

def word_sizes(string):
    if len(string) == 0:
        return {}

    clean_string = remove_symbols(string)

    words = clean_string.split(' ')
    size_counts = {len(word): 0 for word in words}
    
    for word in words:
        size_counts[len(word)] += 1
    
    return size_counts

# code check
string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

# Note!
# Time take to write PEDAC and test/debug code is 7 mins, 45 seconds.
# Since it was a refatoring of an already exisitng code.

## LS Answer ##

# def remove_non_letters(string):
#     result = ""
#     for char in string:
#         if char.isalpha():
#             result += char

#     return result

# def word_sizes(words):
#     words_list = words.split()
#     counts = {}

#     for word in words_list:
#         clean_word = remove_non_letters(word)

#         clean_word_size = len(clean_word)
#         if clean_word_size == 0:
#             continue

#         if clean_word_size not in counts:
#             counts[clean_word_size] = 0

#         counts[clean_word_size] += 1

#     return counts