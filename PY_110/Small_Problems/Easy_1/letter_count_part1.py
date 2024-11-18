'''
Letter Counter (Part 1).
Write a function that takes a string consisting of zero or more space-separated words
and returns a dictionary that shows the number of words of different sizes.
Words consist of any sequence of non-space characters.

# Problem
    - Input: 
    String
    - Output: 
    Dictionary (Key is length of string and value is numbeer of time it occurs )

    Rules:
    - Explicit:
    String consisting of zero or more space-separated words
    Dictionary that shows the number of words of different sizes.

    - Implicit:
    - Empty string returns empty dictionary

# Examples
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# Data Structure:
Dictionary

# Algorithm
    -High level
        1. Enter string Input.
        2. Split string into list of words.
        3. Create empty dictionary.
        4. Iterate through the word in the list of words.
            - set the len of each word to be a key used to determine the key for the dictionary.
            - If the key exist, increase its value by 1.
            - if the key doesnt exist, create a new key and assign it a value of 1.
        5. Can also use dicionary comprehension for step 3 and 4.
        6. Return new dictionary.

# Code 
'''

# Solution
def word_sizes(string):
    if len(string) == 0:
        return {}

    words  = string.split() 
    str_dict  = {}

    for word in words:
        word_length = len(word)
        if word_length in str_dict:
            str_dict[word_length] += 1
        else:
            str_dict[word_length] = 1
      
    return str_dict

# using dictionaray comprehension
def word_sizes_comp(str):
    words = string.split()
    length_counts = {len(word): 0 for word in words}
    
    for word in words:
        length_counts[len(word)] += 1
    
    return(length_counts)

# code check
string = 'Four score and seven.'
print(word_sizes_comp(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes_comp(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes_comp(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes_comp(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

# Note!
# Time take to write PEDAC and test/debug code is 27 mins, 45 seconds.

## LS Answer ##

# def word_sizes(words):
#     words_list = words.split()
#     counts = {}

#     for word in words_list:
#         word_size = len(word)
#         if word_size not in counts:
#             counts[word_size] = 0

#         counts[word_size] += 1

#     return counts
