'''
Longest Sentence.
Write a program that prints the longest sentence in a string based on the number of words.
Sentences may end with periods (.), exclamation points (!), or question marks (?).
You should treat any sequence of characters that are not spaces
or sentence-ending characters as a word.
Thus, -- should count as a word. Log the longest sentence and its word count.
Pay attention to the expected output, and be sure you preserve the punctuation from the end of the sentence.
Note that this problem is about manipulating and processing strings.
As such, every detail about the string matters (e.g., case, punctuation, tabs, spaces, etc.).

'''

# Solution
'''
PEDAC
problem:
    Exp: 
    - Prints the longest sentence in a string based on the number of words
    - Sentences may end with periods (.), exclamation points (!), or question marks (?).
    - Words are sequence of characters that are not spaces or sentence-ending characters.
    - Any sequence of characters that are not spaces or sentence-ending characters as a word.
    - Double spaced characters should count as a word.
    - Log the longest sentence and its word count.
    - Preserve the punctuation from the end of the sentence.
    
    Imp:
    - Do not alter the original string.
    - Keep all formats together.

Examples:
See test cases

Data Structure:
list

Algorithm:
    High end.
    1. Go over the whole input string.
    2. Get the longest sentences available in the string.
    3. Verify it is the longest sentence based on word count, not string lenght.
    4. Return the longest sentence and its word count.

    Short end:
    - Get input.
    - Set a max_sentence variable to store longest sentence.
    - Set an initial_sentence variable to store checked sentence.
    - set a max_sentence_counter to store the lenght of the longest string
    - Iterate through the string:
        - Check if the character starts with a space (for new sentences).
            - If yes, pass.
        - Increment inital_sentence by characters.
        - Check if the current character is a sentence ender (.!?)
        - if yes,
            - Strip all trailing and leading spaces and split the inital_sentence into seperated words and save in a variable called initial_word_count.
            - Check if the lenght of the initial_word_count is greater or equall to max_word_count.
            - if yes:
                - join the list of words in initial_word_count with spaces and set to inital_sentence.
                - Set max_sentence to inital_sentence.
                - Set max_word_count to the initial_word_count.
                - reset inital_sentence to '' (an empty string).
        - reset inital_sentence to '' (an empty string).
    - Return the max_sentence and max_word_count based on the test outputs.

'''
def longest_sentence(string):
    max_sentence = ''   #
    inital_sentence = ''
    max_word_count = 0
    sentence_ender = '.!?'

    for char in string:
        inital_sentence += char
        if char in sentence_ender:
            initial_word_count = inital_sentence.strip().split()
            if len(initial_word_count) >= max_word_count:
                inital_sentence = ' '.join(initial_word_count)
                max_sentence = inital_sentence
                max_word_count = len(initial_word_count)
                inital_sentence = ''
            else:
                inital_sentence = ''

    print(f"{max_sentence}\n")
    print(f"The longest sentence has {max_word_count} words \n")
        
long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

longest_sentence("Where do you think you're going? What's up, Doc?")
# Where do you think you're going?
#
# The longest sentence has 6 words.

longest_sentence("To be or not to be! Is that the question?")
# To be or not to be!
#
# The longest sentence has 6 words.

## LS Solution ##
# import re

# def longest_sentence(text):
#     sentences = re.findall(r'\w.*?[.!?]', text)

#     longest = max(sentences, key=lambda s: len(s.split()))

#     print(longest + "\n")
#     print(f"The longest sentence has {len(longest.split())} words.\n")

# The chief point of interest in this solution is this statement:
# sentences = re.findall(r'\w.*?[.!?]', text)
# We take advantage of the findall function from the re module.
# The solution leverages the lazy quantifier (*?) to restrict the match to the shortest possible string: a single sentence. Given the pattern, a match:

# \w - starts with any word character
# .*? - may contain any number of characters in the middle (even zero characters)
# [.!?] - ends when the first ., !, or ? after the starting word character is reached

