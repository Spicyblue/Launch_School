# Starting with the string:
munsters_description = "The Munsters are creepy and spooky."

#print the string with the case of all letters swapped:
"tHE mUNSTERS ARE CREEPY AND SPOOKY."
# That is, lowercase letters are converted to uppercase, and uppercase letters are converted to lowercase"

# method hunthing
print(munsters_description.swapcase())

# using a forloop in a function
def switch_letter_case(word_string):
    result = ""

    # is.upper() returns a boolen True if string is upper.. This is not the same as upper() which converts to uppercase.
    for char in word_string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()

    return result

print(switch_letter_case(munsters_description))

# using a while loop in a function
def switch_alphabet_case(words):
    final_word = ""
    index = 0

    while index < len(words):
        if words[index].islower():
            final_word += words[index].upper()
        else:
            final_word += words[index].lower()
        
        index += 1
    
    return final_word

print(switch_alphabet_case(munsters_description))