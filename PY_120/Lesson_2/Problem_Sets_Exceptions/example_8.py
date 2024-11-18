'''
Example 8.

Given the following global dictionary:

students = {'John': 25, 'Jane': 22, 'Doe': 30}
Write a Python function get_age(name) that takes a student's name as an argument and returns their age.
If the student's name isn't in the dictionary,
the function should return 'Student not found'.

'''

# Solution
students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):

    if name in students:
        return students[name]
    else:
        return 'Student     not found'

print(get_age('Jane'))
print(get_age('Doe'))
print(get_age('John'))
print(get_age('Hillary'))

## LS Solution ##
# def get_age(name):
#     try:
#         return students[name]
#     except KeyError:
#         return 'Student not found'
