'''
Write a function that takes a string as an argument and returns that string with every occurrence of a "number word"
 -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- 
 converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

# Problem:
- Input:
String
- Output:
String
- Rules
    Explicit:
    Convert number words to digit characeter.

# Examples:
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

# Data structure
Dictionary but ended up using a match case.

# Algorithm
    - High End 
        1. Get input.
        2. Create a checker for converting words to digits
        3. Create a emtpy list for storing result.
        4. Split input into list.
        5. Iterate through the list.
            - If the element is number-word, return the digits.
            - If not, return the same element.
            - Add to result to the empty list.
            - Repeat for all items in the list.

        6. Join the result with space and return the new list
    
# Code
'''

# Solution
def number_word_to_digit(string_input):

    match string_input:
            case "zero":
                return '0'
            case "one":
                return '1'
            case "two":
                return '2'
            case "three":
                return '3'
            case "four":
                return '4'
            case "five":
                return '5'
            case "six":
                return '6'
            case "seven":
                return '7'
            case "eight":
                return '8'
            case "nine":
                return '9'
            case _:
                return string_input

def word_to_digit(message):

    message_lst = message.split(' ')
    final_message = [number_word_to_digit(word) for word in message_lst]
    returned_message = ' '.join(final_message)

    return returned_message

# code check
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")

# Time take to write PEDAC and test/debug code is 11 mins, 45 seconds.

## LS Answer ##
# NUM_WORDS = {
#     'zero':  '0',
#     'one':   '1',
#     'two':   '2',
#     'three': '3',
#     'four':  '4',
#     'five':  '5',
#     'six':   '6',
#     'seven': '7',
#     'eight': '8',
#     'nine':  '9',
# }

# def word_to_digit(sentence):
#     words = sentence.split()
#     processed_words = [NUM_WORDS.get(word, word) for word in words]
#     return ' '.join(processed_words)
