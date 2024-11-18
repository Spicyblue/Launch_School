'''
Reverse a String.
You have a function that is supposed to reverse a string passed as an argument.
However, it's not producing the expected output. Explain the bug, and provide a solution.
'''

# # Current code
# def reverse_string(string):
#     for char in string:
#         string = char + string

#     return string

# print(reverse_string("hello") == "olleh")

'''
Issue with the current code:
Within the forloop, for every iteration, we are concantenating the value of string object
refereced by the temporary variable `char` to the current value of `string`
and using the new string object returned to reassign `string`.

To solve this, due to the immutable nature of string,
we can create a new variable `result` to hold the string object after each iteration
and concantenate the string object referenced by `char` to result.
'''

# fixed code 
def reverse_string(string):
    result = ''
    for char in string:
        result =  char + result
        print(result)

    return result

print(reverse_string("hello") == "olleh")

# Note!
# Time take to debug code is 4 mins, 12 seconds.
# Took more time to write the reason for the error but didnt include it.

## LS Answer ##
# def reverse_string(string):
#     reversed_str = ""
#     for char in string:
#         reversed_str = char + reversed_str

#     return reversed_str

# print(reverse_string("hello") == "olleh")  # True

# Solution 2
# def reverse_string(string):
#     return string[::-1]

# print(reverse_string("hello") == "olleh")  # True

