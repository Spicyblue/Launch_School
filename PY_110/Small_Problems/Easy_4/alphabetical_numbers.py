'''
Alphabetical Numbers.
Write a function that takes a list of integers between 0 and 19 and 
returns a list of those integers sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, 
thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

# Problem
- Input: 
list of integers
- Output:
Sorted list of integers

- Rules
    Explicit:
    Sorted based on the english word for each number.
    Implicit:

# Examples

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)

# Prints True

# Data structure
Dictionary and list

# Algorithm
    - High End:
        1. Get input.
        2. Create a helper function that return the string name of the integers.
            - Use a dictionary for this.
        3. Sort the input based on the string name returned.
        4. Return the sorted output.

# Code
'''

# Solution
def get_number_word(num):

    number_word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 
                        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 
                        'thirteen', 'fourteen', 'fifteen', 'sixteen', 
                        'seventeen', 'eighteen', 'nineteen'
                        ]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    numbers_dict = dict(zip(numbers, number_word_list))

    return numbers_dict[num]

def alphabetic_number_sort(lst):
    return sorted(lst, key = get_number_word)

#Code Check
input_list = [5, 4, 3, 2, 1, 0, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)

# Note!
# Time take to write PEDAC and test/debug code is 13 mins, 58 seconds.

## LS Answer ##
# NUMBER_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five',
#                 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
#                 'twelve', 'thirteen', 'fourteen', 'fifteen',
#                 'sixteen', 'seventeen', 'eighteen', 'nineteen']

# def word_for_number(num):
#     return NUMBER_WORDS[num]

# def alphabetic_number_sort(numbers):
#     return sorted(numbers, key=word_for_number)
