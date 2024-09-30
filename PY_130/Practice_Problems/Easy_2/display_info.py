'''
Display Info.
Write a function display_info that takes a positional-only parameter data,
and keyword-only parameters reverse and uppercase.
'''

# Solution

def display_info(string,/,*, reverse = False, uppercase = False):
    if reverse and uppercase:
        return string[::-1].upper()
    elif reverse:
        return string[::-1]
    elif uppercase:
        return string.upper()
    else:
        return string

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC

## LS Solution ##
# def display_info(data, /, *, reverse=False, uppercase=False):
#     if reverse:
#         data = data[::-1]
#     if uppercase:
#         data = data.upper()
#     return data