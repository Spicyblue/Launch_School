# The End Is Near But Not Here
# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.
#Further Exploration
# Our solution ignored two edge cases since we explicitly stated that you didn't have to handle them: strings that contain no words or just one word.
# Suppose we need a function that retrieves the middle word of a phrase/sentence. 
# What edge cases need to be considered? How would you handle those edge cases without ignoring them?
# Write a function that returns the middle word of a phrase or sentence. It should handle all of the edge cases you thought of

# Solution

def penultimate(string_input):
    words = string_input.split()
    return words[-2]

#These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

# Further exploration
def get_middle_word(string_literal):
    words = string_literal.split()
    middle_index = len(words) // 2
    if len(words) == 0:
        return "Empty string"
    elif len(words) == 1:
        return words[0]
    elif len(words) % 2 == 1:
        return words[middle_index]
    else:
        return words[middle_index - 1], words[middle_index]


print(get_middle_word('')) # 'Empty String'
print(get_middle_word('last word')) # ('last', 'word')
print(get_middle_word('Launch School is great for software engineering!')) # 'great'
print(get_middle_word('Manchester United are champions of the league')) # 'chhampions'