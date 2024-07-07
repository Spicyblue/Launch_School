# **********************************************************************#
# Practice Problem 1
# Given the tuple:
# How would you count the number of occurrences of "banana" in the tuple?

fruits = ("apple", "banana", "cherry", "date", "banana")
print('*'* 70)

# Answer
print(fruits.count('banana'))

#**********************************************************************#
# Practice Problem 2
# Consider the set:

numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers))
# What is the set's length? Try to answer without running the code.

# Answer
# Set lenght is 5. Sets have unique values.

# **********************************************************************#
#Practice Problem 3
# Given two sets:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# How would you obtain a set that contains all the unique
# values from both sets?

# Answer
# Union of two sets. The union method or the | operator
# can be used to get all unique values from both sets.
new_set = a|b
print(new_set)

# **********************************************************************#
# Practice Problem 4
# Given the following code, what would the output be?
# Try to answer without running the code.

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)

# Answer
# The code creates a dictionary where the names
# are keys and their positions in the original list are the values.
# outputs
# {
#   'Fred': 0,
#   'Barney': 1,
#   'Wilma': 2,
#   'Betty': 3,
#   'Pebbles': 4,
#   'Bambam': 5
# }

# **********************************************************************#
# Practice Problem 5
# Calculate the total age given the following dictionary:

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}
# Answer
age_values = list(ages.values())
total_age = sum([numbers for numbers in age_values])
print(total_age)
# or
total_age = sum(ages.values())
print(total_age)

# **********************************************************************#
# Practice Problem 6
# Determine the minimum age from the above ages dictionary.

# Answer
new_ages = min(list(ages.values()))
print(new_ages)
# or
min_age = min(ages.values())
print(min_age)

# **********************************************************************#
# Practice Problem 7
# What would the following code output?
# Try to answer without running the code.

words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)

# Answer
# The code will output `[bear]`.
# While iterating through the list object referenced by `words`,
# We have a selection criteria that checks if any elements within
# the list has length greater than 3.
# Elements that pass this check gets appended to
# the new list referenced by `selected_words`.


# Practice Problem 8
# **********************************************************************#
# Given the following string, create a dictionary that represents
# the frequency with which each letter occurs.
# The frequency count should be case-sensitive:

statement = "The Flintstones Rock"
# The output should resemble the following:
# # Pretty printed for clarity
# {
#     'T': 1,
#     'h': 1,
#     'e': 2,
#     'F': 1,
#     'l': 1,
#     'i': 1,
#     'n': 2,
#     't': 2,
#     's': 2,
#     'o': 2,
#     'R': 1,
#     'c': 1,
#     'k': 1
# }
# Your program may output the pairs in a different order.

def string_dictionary(string_input):
    string_dictionary = {}
    string_input = string_input.replace(" ", "")

    for char in string_input:
        string_dictionary[char] = string_input.count(char)

    return string_dictionary

print(string_dictionary(statement))

# LS  Answer #
char_freq = {}
statement = statement.replace(' ', '')
for char in statement:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)

# check if both solution are equall and they both are.
print(string_dictionary(statement) == char_freq)

# **********************************************************************#
# Practice Problem 9
# What is the return value of the list comprehension below?
# Try to answer without running the code.

print([num for num in [1, 2, 3] if num > 1])

# Answer
# The list comprehension outputs [2, 3], a new list object.

# **********************************************************************#
# Practice Problem 10
# What does the following code print and why?

dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

# Answer
# The coode outputs ('b': 'bear').
# Caling the `popitem` dictionary method on the varialble `dictionary`
# which references a dictionary object returns the
# last dictionary key-value pair added to `dictionary`
# as a tupple. This only applies to Python 3.7 and above.

# **********************************************************************#
# Practice Problem 11
# What does the following code return? Try to answer without running the code
lst = [1, 2, 3, 4, 5]
print(lst[:2])

# Answer
# This code outputs [1, 2]. Using slicing sythax,
# we access the list objects referenced by lst from index 0 to 1,
# and return the elements in those positions which is then printed out.

# **********************************************************************#
# Practice Problem 12
# What would be the output of the below code?
# Try to answer without running the code.

frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# Answer:
# Code will raise an error.
# Frozen sets are immutable and thus new elements
# cannot be added to a frozenset.
# The add method, which is used to add elements to a regular set,
# does not exist for frozenset objects. Attempting to use it will
# result in the mentioned AttributeError.
# If you need to perform an operation that
# modifies a set you should use a regular set instead.