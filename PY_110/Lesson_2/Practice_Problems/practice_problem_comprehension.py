#**********************************************************************#
# Practice Problems: Comprehensions
# In the last assignment, we did a deep-dive on comprehensions.
# The best way to gain a thorough understanding of comprehensions
# is by putting them into practice.

# If any of these problems seem hard at first,
# take the time to break them down and remember to focus on the
# structure of the collection object  and what the code should do with it.
# For code that requires you to write a comprehension,
# it's sometimes easier to begin by writing a for loop,
# then refactoring the code into a comprehension.

# Practice Problem 1
# Consider the following nested dictionary:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# Compute and display the total age of the family's male members.
# Try working out the answer two ways: first with an ordinary loop,
# then with a comprehension.
# The result should be 444.

# Answer
# using a forloop and a list
total_male_age = []
for _, value in munsters.items():
    if value['gender'] == 'male':
        total_male_age.append(value['age'])

print(sum(total_male_age))

# using a list comprehension
total_male_age_2 = sum(
    [ value['age'] for _, value in munsters.items()
    if value['gender'] == 'male']
    )

print(total_male_age_2)

# or
# using a for loop and incrementing integer return value
total_males_age = 0
for member in munsters.values():
    if member['gender'] == 'male':
        total_males_age += member['age']

print(total_males_age)

# using a list comprehension
all_male_ages = [member['age'] for member in munsters.values()
                               if member['gender'] == 'male']
print(sum(all_male_ages))

#**********************************************************************#
# Show Solution
# Practice Problem 2
# Given the following data structure, return a new list
# with the same structure, but with the values in each sublist
# ordered in ascending order. Use a comprehension if you can.
# (Try using a for loop first.)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# Expected resultCopy Code
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
# The string values should be sorted as strings
# while the numeric values should be sorted as numbers.

# Answer
new_lst = []
for items in lst:
    new_lst.append(sorted(items, reverse= False))
print(new_lst)

# using list comprehensions
newer_list = [sorted(members, reverse= False) for members in lst]
print(newer_list)

# Practice Problem 3
# Given the following data structure, return a new list with
# the same structure, but with the values in each sublist
# ordered in ascending order as strings
# (that is, the numbers should be treated as strings).
# Use a comprehension if you can. (Try using a for loop first.)

lst_1 = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Expected result
# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

# Answer
new_lst_1 = []
for elements in lst_1:
    new_lst_1.append(sorted(elements, reverse= False, key = str))
print(new_lst_1)

# using list comprehensions
newer_list_1 = [sorted(members, reverse= False, key = str) for members in lst]
print(newer_list_1)

#**********************************************************************#
# Practice Problem 4
# Given the following data structure,
# write some code that defines a dictionary where
# the key is the first item in each sublist, and the value is the second.

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]
# Expected result
# # Pretty printed for clarity
# {
#     'a': 1,
#     'b': 'two',
#     'sea': {c: 3},
#     'D': ['a', 'b', 'c']
# }

# Answer
lst_dct = {element[0]: element[1] for element in lst }
print(lst_dct)

#**********************************************************************#
# Practice Problem 5
# Given the following data structure,
# sort the list so that the sub-lists are ordered based
# on the sum of the odd numbers that they contain.
# You shouldn't mutate the original list.


lsttt = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# Note that the first sublist has the odd numbers 1 and 7;
# the second sublist has odd numbers 1, 5, and 3;
# and the third sublist has 1 and 3.
# Since (1 + 3) < (1 + 7) < (1 + 5 + 3),
# the sorted list should look like this:
# Expected result.
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]
# Try to use a comprehension in your solution.

# Answer
def sum_of_odd_numbers(sublist):
    odd_numbers = [num for num in sublist if num % 2 == 1]
    return sum(odd_numbers)

new_sorted_list = sorted(lsttt, key=sum_of_odd_numbers)
print(new_sorted_list)

#**********************************************************************#
# Practice Problem 6
# Given the following data structure,
# return a new list identical in structure to the original but,
# with each number incremented by 1.
# Do not modify the original data structure. Use a comprehension.

lst_dict_new = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
# Expected result
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# Answer
def increment_values(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}

new_list = [increment_values(value) for value in lst_dict_new]
print(new_list)
print(lst_dict_new)

#**********************************************************************#
# Practice Problem 7
# Given the following data structure return a new list
# identical in structure to the original,
# but containing only the numbers that are multiples of 3.

lst_main = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
# The returned list should look like this:
# Expected resultCopy Code
# [[], [3, 12], [9], [15, 18]]
# Try to use a comprehension for this.
# However, we recommend first trying it without comprehensions.

# Answer
# Using loop and selection
multiples_of_3a = []

for no_of_list in lst_main:
    sublist = []
    for objects in no_of_list:
        if objects % 3 == 0:
            sublist.append(objects)

    multiples_of_3a.append(sublist)

print(multiples_of_3a)

# or

multiples_of_3b = []

for sublist in lst_main:
    new_sublist = [num for num in sublist if num % 3 == 0]
    multiples_of_3b.append(new_sublist)

print(multiples_of_3b)

# or

def divisible_by_3(sublist):
    return [num for num in sublist if num % 3 == 0]

multiples_of_3c = [divisible_by_3(sublist) for sublist in lst_main]
print(multiples_of_3c)

# or

multiples_of_3b = [[num for num in sublist if num % 3 == 0]
                   for sublist in lst_main]
print(multiples_of_3b)

#**********************************************************************#
# Practice Problem 8
# Given the following data structure, write some code to
# return a list that contains the colors of the fruits
# and the sizes of the vegetables.
# The sizes should be uppercase
# and the colors should be capitalized.

dict1_fruits = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}
# The return value should look like this:
# Expected result
# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

# Answer
fruit_info = []
for value in dict1_fruits.values():
    if value['type'] == 'fruit':
        inner_list = []
        for element in value['colors']:
            color = element.capitalize()
            inner_list .append(color)
        fruit_info.append(inner_list)

    elif value['colors'] and value['type'] == 'vegetable':
        size = value['size'].upper()
        fruit_info.append(size)

print(fruit_info)

# or

def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()

new_fruit_info = [transform_item(item) for item in dict1_fruits.values()]
print(new_fruit_info)

#**********************************************************************#
# Practice Problem 9
# This problem may prove challenging.
# Try it, but don't stress about it.
# If you don't solve it in 20 minutes, you can look at the answer.
# Given the following data structure,
# write some code to return a list that contains only
# the dictionaries where all the numbers are even.

lst_dict_1 = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
# Expected result
# [{e: [8], f: [6, 10]}]

# Answer

def check_even_values(dictionary):
    return all(all(num % 2 == 0 for num in value)
               for value in dictionary.values())

new_lst_2 = [elements for elements in lst_dict_1
            if check_even_values(elements)]
print(new_lst_2)

# or

def all_even(dictionary):
    for values in dictionary.values():
        if not all([num % 2 == 0 for num in values]):
            return False

    return True

new_lst_3 = [val for val in lst_dict_1 if all_even(val)]
print(new_lst_3)

#**********************************************************************#
# Practice Problem 10
# A UUID (Universally Unique Identifier) is a type of identifier often
# used to uniquely identify items, even when some of those items were
# created on a different server or by a different application.
# That is, without any synchronization, two or more computer systems
# can create new items and label them with a UUID with no significant
# risk of stepping on each other's toes.
# It accomplishes this feat through massive randomization.
# The number of possible UUID values is approximately 3.4 X 10E38,
# which is a huge number. The chance of a conflict, a "collision",
# is vanishingly small with such a large number of possible values.
# Each UUID consists of 32 hexadecimal characters
# (the digits 0-9 and the letters a-f) represented as a string.
# The value is typically broken into 5 sections in an 8-4-4-4-12 pattern
# e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.
# Note that our description of UUIDs
# is a simplified description of how UUIDs are formed.
# There are several UUID versions, each with some non-random characteristics
# in some of the bits. These different versions can play a
# part in certain applications.
# Write a function that takes no arguments and
# returns a string that contains a UUID.

# Answer
import random

def generate_user_uuid():
    hex_chars = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)

new_uuid = generate_user_uuid()
print(new_uuid)

#**********************************************************************#

# Practice Problem 11
# The following dictionary has list values that contains strings.
# Write some code to create a list of every vowel
# (a, e, i, o, u) that appears in the contained strings,
# then print it.

dict1_messages = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# print(list_of_vowels)
# # ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
# Start by trying to write this using nested loops.

# Answer
VOWELS = 'aeiou'
string_of_vowels = ""
vowel_list = []

for value in dict1_messages.values():
    for words in value:
        for character in words:
            if character in VOWELS:
                string_of_vowels += character
                vowel_list.append(character)

all_vowels = list(string_of_vowels)
print(all_vowels)
print(vowel_list)

# Extra Challenge:
# Once your nested loop code works,
# try to refactor the code so it uses a single list comprehension.
# You can print the resulting list outside of the comprehension.)

# Answer

the_vowels = [char for value in dict1_messages.values()
                for word in value
                for char in word if char in VOWELS]

print(the_vowels)

# or
chars = []
for key in dict1_messages:
    for word in dict1_messages[key]:
        for char in word:
            if char in VOWELS:
                chars.append(char)
print(chars)
