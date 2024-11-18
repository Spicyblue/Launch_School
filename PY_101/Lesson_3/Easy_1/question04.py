# Using the following string, print a string that contains the same value, 
# but using all lowercase letters except for the first character, which should be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

# using method hunting
print(munsters_description.capitalize())

# using indexing and slicing method.
munsters_description_new = munsters_description[0].capitalize() + munsters_description[1:].lower()
print(munsters_description_new)

# using a for loop in a function
def capitalized_first_word(word_string):
    result = ''

    for index, char in enumerate(word_string):
        if index == 0:
            result += char.upper()
        else:
            result += char.lower()

    return result

print(capitalized_first_word(munsters_description))

# using a while loop in a function
def capitalize_only_first_word(word_input):
    final_word = ''
    index = 0

    while index < len(word_input):
        if index == 0:
            final_word += word_input[index].upper()
        else:
            final_word += word_input[index].lower()
        
        index += 1
    
    return final_word

print(capitalize_only_first_word(munsters_description))
