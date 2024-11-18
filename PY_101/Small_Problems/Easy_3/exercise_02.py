# ddaaiillyy ddoouubbllee
# Write a function that takes a string argument and 
# returns a new string that contains the value of the original string
# with all consecutive duplicate characters collapsed into a single character.

# Solution

def crunch(string):
    if not string:
        return string
    
    new_string = string[0]
    for char in string:
        if char != new_string[-1]:
            new_string += char

    return new_string

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

# Quite an intresting logic
