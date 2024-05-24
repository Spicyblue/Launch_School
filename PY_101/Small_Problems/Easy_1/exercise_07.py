# Short Long Short
# Write a function that takes two strings as arguments, 
# determines the length of the two strings, 
# and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again.
# You may assume that the strings are of different lengths.

# Solution

def short_long_short(string1, string2):
    word = ""
    if len(string1) > len(string2):
        word = string2 + string1 + string2
    else:
        word = string1 + string2 + string1
    
    return word

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")