# UTF-16 String Value
# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument.
# The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-16 value of a character.)

# Solution

def utf16_value(utf16_string):
    string_value = 0
    for letter in utf16_string:
        string_value += ord(letter)

    return string_value

# using list comprehension
def utf16_value(utf16_string):
    value = [ord(letter) for letter in utf16_string]
    return sum(value)

print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)