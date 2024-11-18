#**********************************************************************#
# Practice Problems: Nested Data Structures
# Let's get some practice dealing with nested data structures.
# Your eyes may feel a bit crossed after this assignment.
# We recommend trying to work each problem one step at a time.
# That is, if you need to access a value that is deeply nested in an object,
# try to get to that value one step at a time.
# For instance, consider this code:

# lst = [[1, [2, [3, 4]]], 5]
# If you want to access the value 3,
# first look at what lst[0] returns ([1, [2, [3, 4]]]).
# Seeing that 3 is in the second element of lst[0],
# take a look at lst[0][1] ([2, [3, 4]]).
# Once again, 3 is in the second element,
# so we now look at lst[0][1][1] ([3, 4]).
# Finally, we can see that 3 is the first element of lst[0][1][1],
# so we can access it with lst[0][1][1][0].

#**********************************************************************#
# Practice Problem 1
# For each object shown below,
# demonstrate how you would access the letter g.

lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

# Answer

print(lst1[2][1][3])

print(lst2[1]['third'][0])

print(lst3[2]['third'][0][0])

print(dict1['b'][1])

print(''.join(list(dict2['3rd'].keys())))
#or
print(list(dict2['3rd'].keys())[0])

#**********************************************************************#
# Practice Problem 2
# For each of these collection objects,
# demonstrate how you would change the value 3 to 4.


lst_1 = [1, [2, 3], 4]

lst_2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

dict_1 = {'first': [1, 2, [3]]}

dict_2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}

# Answer
lst_1[1][1] = 4
print(lst_1)

lst_2[2] = 4
print(lst_2)

dict_1['first'][2][0] = 4
print(dict_1)

dict_2['a']['a'][2] = 4
print(dict_2)

#**********************************************************************#
# Practice Problem 3
# Given the following code, what will the final values of a and b be?
# Try to answer without running the code.

value_1 = 2
value_2 = [5, 8]
lst = [value_1, value_2]

lst[0] += 2
lst[1][0] -= value_1

print(lst)

# Answer
# The coude will output [4,[3, 8]].
# The value of a didn't change since we don't reference a at any point.
# The code lst[0] += 2 modifies the list lst, but not a.
# In effect, we are assigning a new value to that index of the list
# so that instead of lst[0] containing 2, the value obtained from a,
# it now contains 4.

#**********************************************************************#
# Practice Problem 4
# One of the most frequently used real-world string operations is that
# of "string substitution," where we take a hard-coded string and
# modify it with various parameters from our program.
# Given the object shown below,
# print the name, age, and gender of each family member:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# Each output line should follow this pattern:
# (name) is a (age)-year-old (male or female).
# Expected OutputCopy Code
# Herman is a 32-year-old male.
# Lily is a 30-year-old female.
# Grandpa is a 402-year-old male.
# Eddie is a 10-year-old male.
# Marilyn is a 23-year-old female.

# Answer
def family_profile(family_dictionary):

    for key, value in family_dictionary.items():
        name = key
        age = value['age']
        gender = value['gender']

        print(f'{name} is a {age}-year-old {gender}')

family_profile(munsters)
#or
for names, info in munsters.items():
    print(f"{names} is a {info['age']}-year-old {info['gender']}.")
    