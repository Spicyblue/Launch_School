# Clean up the words
# Given a string that consists of some words and an assortment of non-alphabetic characters,
# write a function that returns that string with all of the non-alphabetic characters replaced by spaces. 
# If one or more non-alphabetic characters occur in a row, you should only have one space in the result 
# (i.e., the result string should never have consecutive spaces).

# Solution

def clean_up(string_input):
    new_string = ""

    for index, char in enumerate(string_input):
        if char.isalpha():
            new_string += char
        elif index == 0 or new_string[-1] != ' ':
            new_string += " "

    return new_string


print(clean_up("---what's my +*& line?") == " what s my line ")
