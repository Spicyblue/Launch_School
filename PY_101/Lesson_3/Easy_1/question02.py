# How can you determine whether a given string ends with an exclamation mark (!)? 
# Write some code that prints True or False depending on whether the string ends with an exclamation mark.

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

# method hunting
print(str1.endswith('!'))
print(str2.endswith('!'))

# using a function that checks the last index in a string.
def check_string(string_input):
    if string_input[len(string_input)-1] == '!':
        return True
    else:
        return False

print(check_string(str1))
print(check_string(str2))