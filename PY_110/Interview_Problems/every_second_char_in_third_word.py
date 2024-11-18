'''
Every second letter.
Create a function that takes a string argument and 
returns a copy of the string with every second character in every third word converted to uppercase.
Other characters should remain the same.

# Problem
- Input: 
String
- Output:
String

- Rules
    Explicit:
    - Returns a copy of the string with every second character in every third word converted to uppercase
    - Other characters should remain the same.

    Implicit:

# Examples
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

# Data structure
List

# Algorithm:
    High Level:
    1. Make list of every word in the sentence.
    2. Get every third word in list.
    3. Make every second letter captial in the third word.
    4. Add the changes to the list.
    5. Get back the new sentence.

    Low level:
        1. Get input.
        2. Split string input into list.
        3. Iterate through the list.
            - Check if the current item is the 3rd position (2nd index) in the list:
            - If yes, create an empty string to store the new wierd words:
                - Interate through the elements in the list:
                - Check if the index is odd:
                    - If yes, convert to uppercase and add to string:
                    - Else, just add the letter.
                - Use the new string to reassigned the current element in the list
                - Repeat until the last element in the list.
        4. Join the list with space and return it. 

# Code
'''

# Solution

def get_wierd_word(string):
    result = ''

    for idx in range(len(string)):
        if idx % 2 == 1:
            result += string[idx].upper()
        else:
            result += string[idx]

    return result

def to_weird_case(string):
    string_lst = string.split(' ')

    for index, word in enumerate(string_lst):
        if (index + 1) % 3 == 0: # Necessary because in the problem description, index starts from 1,
                                 # not 3 (so zero index becomes the first, the first becomes the second. 
                                 # The second becomes the third. etc)
            string_lst[index] = get_wierd_word(word)
    
    result = ' '.join(string_lst)

    return result

# code check
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

# Note!
# Time take to write PEDAC and test/debug code 22 mins 41 seconds

# other solutions
# def to_weird_case(string):
#     # Split the string into words
#     words = string.split()

#     # Iterate over the words
#     for i in range(2, len(words), 3):  # Start at the third word (index 2) and iterate every third word
#         word = words[i]
#         # Convert every second character in the word to uppercase
#         modified_word = ''.join(
#             [char.upper() if (idx % 2 != 0) else char for idx, char in enumerate(word)]
#         )
#         # Update the word in the list
#         words[i] = modified_word

#     # Join the words back into a single string
#     result = ' '.join(words)

#     return result

# original = 'Lorem Ipsum is simply dummy text of the printing world'
# expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
# print(to_weird_case(original) == expected)

# original = 'It is a long established fact that a reader will be distracted'
# expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
# print(to_weird_case(original) == expected)

# print(to_weird_case('aaA bB c') == 'aaA bB c')

# original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
# expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
# print(to_weird_case(original) == expected)

## LS Answer ##
# Not Available
