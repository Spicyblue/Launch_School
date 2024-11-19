'''
Concatenate Strings.
Use reduce to concatenate a list of strings into a single string.
'''

# Solution

from functools import reduce
lst = ["This ", 'is ', 'a ', 'single ', 'string']
single_string = reduce(lambda str1, str2: str1 + str2, lst)
print(single_string)

## LS Solution ##
# Solution 1
# from functools import reduce
# concatenated = reduce(lambda x, y: x + y, ["Launch", " ", "School", " ", "is", " ", "great"])

# Solution 2
# from functools import reduce
# def concatenate(x, y):
#     return x + y
# concatenated = reduce(concatenate, ["Launch", " ", "School", " ", "is", " ", "great"])
