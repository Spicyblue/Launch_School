'''
Letter Swap.
Given a string of words separated by spaces,
write a function that swaps the first and last letters of every word.
You may assume that every word contains at least one letter,
and that the string will always contain at least one word.
You may also assume that each string contains nothing but words and spaces,
and that there are no leading, trailing, or repeated spaces.

# Problem
    - Input: String of words
    String
    - Output: 
    String of words

    Rules:
    - Explicit:
    Every word contains at least one letter
    String will always contain at least one word.
    Each string contains nothing but words and spaces
    There are no leading, trailing, or repeated spaces.
    
    dictionary that shows the number of words of different sizes.

# Examples
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True


# Data Structure:
String

# Algorithm
    -High level
        1. Enter string Input.
        2. Split string into a list of word.
        3. Create an empty list.
        4. for each word in list of word.
            - if lenght of word is 2:
                - reverse the words.
                - append to empyty list.
            - if lenght of word is more than two.
                - concantenate the last element in word + the words till the the second to the last element + the first element.
                - append to the empty list.
        5. join the elements in the list to strings with spaces between each element.
        6. return the rew string.

# Code 
'''

# Solution
def swap(string):

    if len(string) == 1:
        return string

    words = string.split(' ')

    result = []

    if len(words) == 1:
        for word in words:
            result = word[-1] + word[1 : -1] + word[0]
        return result

    if len(words) >= 2:
        for word in words:
            if len(word) == 1:
                result.append(word)

            if len(word) == 2:
                reverse_word = word [ : : -1]
                result.append(reverse_word)
            
            if len(word) > 2:
                reverse_word = word[-1] + word[1 : -1] + word[0]
                result.append(reverse_word)
                
        result = " ".join(result)

        return result

# code check
print(swap('Oh what a wonderful day it is')
       == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a") 

# Note!
# Time take nto write PEDAC and test/debug code is 29 mins, 45 seconds.
# Spent much more time than i needed on the logic.. Could do better!!

## LS Answer ##

# def swap(words):
#     words_list = words.split()

#     for idx in range(len(words_list)):
#         words_list[idx] = swap_first_last_characters(words_list[idx])

#     return ' '.join(words_list)

# def swap_first_last_characters(word):
#     if len(word) == 1:
#         return word

#     return word[-1] + word[1:-1] + word[0]

# LS answer was probably more elegant than mine!!