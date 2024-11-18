import unittest
'''
Scrabble Score.
Write a program that, given a word, computes the Scrabble score for that word.

Letter Values
You'll need the following tile scores:

Letter                          Value
A, E, I, O, U, L, N, R, S, T    1
D, G                            2
B, C, M, P                      3
F, H, V, W, Y                   4
K                               5
J, X                            8
Q, Z                            10

How to Score
Sum the values of all the tiles used in each word.
For instance, lets consider the word CABBAGE which has the
following letters and point values:

3 points for C
1 point for each A (there are two)
3 points for B (there are two)
2 points for G
1 point for E

Thus, to compute the final total (14 points), we count:
3 + 2*1 + 2*3 + 2 + 1
=> 3 + 2 + 6 + 3
=> 5 + 9
=> 14
'''

# Solution
'''
PEDAC
Problem:
    Input: String
    output: Integer

    Exp: 
    - Only accept string with letters and returns integers.
    - Each letter has a point.
    - Score is calculated by adding all the points in the letters.

    imp:
    - unittest test cases show that our we need Scrabble class which
      accepts string arguments passed to the constructor.
    - Whitespaces do not count, so we need to strip them off.
    - None value types should return 0.
    - The class should have a score match which returns the score.
    - There shoould be a class calculate_score which accept a string and retuns the calculated score.
 
Examples:
Using unittest TestCase

Data Structure:
Class with instance variables and methods.
Dicttionary with key as letters and value as letter value

Algorithm:
    Highend
    - Get the words
    - Calculate the score based on the value of each letter in the word.
    - Return the score.


    Lowend:
        - Define a class Scrabble which accepts a string using the Scrabble constructor. 
        - Check if arguments passed as string is of None type, if yes, set to empty string,
          else strip all whitespaces in string.
        - Convert string to uppercase.
        - Set this to an instance variable _word.
        - Create a scrabble_dict with letters as keys and values as letter values.
        - Define an instance method score which accepts only self.
        - Set a total score to 0.
        - Iterate through the _word:
            - For each letter, check if it is a key in scrabble_dict:
                - If yes, increment total score by the scrabble_dict value.
            - Repeat for all letters.
        - Return the total_score.
'''

class Scrabble:
    ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SCRABLE_VALUES = {
            key: 2 if key in 'DG' 
            else 3 if key in 'BCMP' 
            else 4 if key in 'FHVWY' 
            else 5 if key in 'K' 
            else 8 if key in 'J,X' 
            else 10 if key in 'QZ' 
            else 1 for key in ALPHABETS}

    def __init__(self, word = ''):
        if word == None:
            word = ''
        self._word = word.upper().strip()
        
    def score(self):
        score = 0

        for letter in self._word:
            if letter in self.SCRABLE_VALUES:
                score += self.SCRABLE_VALUES[letter]

        return score

    @classmethod
    def calculate_score(cls, word):
        new_scrabble = Scrabble(word)
        return new_scrabble.score()
        
class ScrabbleTest(unittest.TestCase):
    def test_empty_word_scores_zero(self):
        self.assertEqual(0, Scrabble("").score())

    def test_whitespace_scores_zero(self):
        self.assertEqual(0, Scrabble(" \t\n").score())

    def test_nil_scores_zero(self):
        self.assertEqual(0, Scrabble(None).score())

    def test_scores_very_short_word(self):
        self.assertEqual(1, Scrabble("a").score())

    def test_scores_other_very_short_word(self):
        self.assertEqual(4, Scrabble("f").score())

    def test_simple_word_scores_the_number_of_letters(self):
        self.assertEqual(6, Scrabble("street").score())

    def test_complicated_word_scores_more(self):
        self.assertEqual(22, Scrabble("quirky").score())

    def test_scores_are_case_insensitive(self):
        self.assertEqual(41, Scrabble("OXYPHENBUTAZONE").score())

    def test_convenient_scoring(self):
        self.assertEqual(13, Scrabble.calculate_score("alacrity"))

if __name__ == "__main__":
    unittest.main()

## LS Solution ##
# class Scrabble:
#     POINTS = {
#         "AEIOULNRST": 1,
#         "DG": 2,
#         "BCMP": 3,
#         "FHVWY": 4,
#         "K": 5,
#         "JX": 8,
#         "QZ": 10,
#     }

#     def __init__(self, word):
#         self.word = word if word else ""

#     def score(self):
#         letters = [letter for letter in self.word.upper() if letter.isalpha()]

#         total = 0
#         for letter in letters:
#             for all_letters, point in self.POINTS.items():
#                 if letter in all_letters:
#                     total += point
#                     break

#         return total

#     @classmethod
#     def calculate_score(cls, word):
#         return cls(word).score()