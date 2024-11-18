"""
Given a list of strings, 
return a new list where the strings are sorted based on 
the highest number of adjacent consonants a string contains. 
If two strings contain the same highest number of adjacent consonants, 
they should retain their original order in relation to each other.
Consonants are considered adjacent if they are next to each other
in the same word or if there is a 
space between two consonants in adjacent words.

Problem
- Input: list of strings
- Output: a list of strings sorted according to the highest number
  of adjacent consonants

- Explict rules:
    - If two strings contain the same highest number of adjacent
    consonants, they should maintain their original relative order.
    - Adjacent consonants:
        - are next to each other in the same string.
        - can have a space between them in adjacent
        words.
- Implict rules:
    - Strings may contain single or multiple words.
    - Strings may not be empty.
    - Strings may have no adjacent consonants.
    - Strings should be sorted in descending order.
    - Case is not relevant.
    - Single consonants in a string do not affect sort order in
      comparison to strings with no consonants. Only adjacent
      consonants affect sort order.

Examples and Test Cases
- my_list = ['aa', 'baa', 'ccaa', 'dddaa']
- print(sort_by_consonant_count(my_list))
- # ['dddaa', 'ccaa', 'aa', 'baa']
- 
- my_list = ['can can', 'toucan', 'batman', 'salt pan']
- print(sort_by_consonant_count(my_list))
- # ['salt pan', 'can can', 'batman', 'toucan']
- 
- my_list = ['bar', 'car', 'far', 'jar']
- print(sort_by_consonant_count(my_list))
- # ['bar', 'car', 'far', 'jar']
- 
- my_list = ['day', 'week', 'month', 'year']
- print(sort_by_consonant_count(my_list))
- # ['month', 'day', 'week', 'year']
- 
- my_list = ['xxxa', 'xxxx', 'xxxb']
- print(sort_by_consonant_count(my_list))
- # ['xxxx', 'xxxb', 'xxxa']

Data structure:
- Our input and output are both lists,
  so at a minimum we will be working with lists in our solution.
Algorithm
- High leve Algorithm:
    - For each string in the input list, determine the highest number
    of adjacent consonants within that string.
    - Sort the input list based on the calculated highest number of
    consonants from step 1 above
    - Return the sorted list.

Helper function (Count Consonants: Algorithm)
- Remove the spaces from the "input string".
    - Use `string.split` combined with `string.join` to remove the
      spaces from the input string.
- Initialize a "maximum consonants count" to zero.
- Initialize an "adjacent consonants string" to an empty string.
- For each "letter" in the "input string":
    - Perhaps use a `for` loop to iterate through the string
    - If the "letter" is a consonant:
      - Use the `in` keyword to check whether a string of consonants
        includes the letter for that iteration
        - Concatenate it to the "adjacent consonants string".
    - If the "letter" is a vowel:
        - If the "adjacent consonants string" has a length
          greater than the current "maximum consonants count":
            - If the "adjacent consonants string" has a length
              greater than 1:
                - Set the "maximum consonants count" to the length
                  of the "adjacent consonants string".

        - Reset the "adjacent consonants string" to an empty string.

- Return the "maximum consonants count".

- For the main function:
    - Ensure correct order of arguments in the callback to `sort` to
      produce a descending order.

Code
"""
CONSONANT = 'bcdfghjklmnpqrstvwxyz'

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings

def count_max_adjacent_consonants(string):
    string = ''.join(string.split(' '))
    max_consonant_count = 0
    adjacent_consonants = ''

    for char in string:
        if char in CONSONANT:
            adjacent_consonants += char
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)
        else:
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)

            adjacent_consonants = ''

    return max_consonant_count

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) ==
    ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) ==
    ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) ==
    ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) ==
    ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) ==
    ['xxxx', 'xxxb', 'xxxa'])


