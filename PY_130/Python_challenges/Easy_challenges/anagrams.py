import unittest
'''
Anagrams.
Write a program that takes a word and a list of possible anagrams 
and selects the correct sub-list that contains the anagrams of the word.

For example, given the word "listen" and a list of candidates like
"enlists", "google", "inlets", and "banana",
the program should return a list containing "inlets".
Please read the test suite for the exact rules of anagrams.
'''

# Solution
'''
PEDAC
Problem:
    Input: string, list
    output: list

    Exp: 
    - Only accept string and list.
    - Returns a sublist with string elements.

    imp:
    - unittest test cases show that our we need Anagram class which
      accepts string arguments passed to the constructor.
    - The class should have a method match which accepts
      a list of strings which returns a sublist of anagrams.
    - If no anagrams are found, returns an empty list.

Examples:
Using unittest TestCase


Data Structure:
Class with instance variables and methods.
list

Algorithm:
    Highend
    - Get the words
    - Check which are words in the list are anagrams of the main word.
    - Return a sublist containing only those anagrams present.

    Lowend:
        - Define a class Anagram which has accepts a string using the Anagram constructor. 
        - Convert the argument passed to lowercases using casefold and set this to an instance _word.
        - Define an instance method match which accept list objects.
        - Set the list object to the instance variable (or just a variable) possible_anagrams.
        - Create an instance_variable or variable called anagrams is list to hold true anagrams.
        - Iterate through each element in possible_anagrams.
            - Check if the current element is not the same as 
               the _word and sorting both the current element and _word returns True.
                - If yes, append current element to anagram
            - Repeat for all elemets in the list.
        - Return the anagram sublist.
'''

class Anagram:
    def __init__(self, word):
        self._word = word.casefold()

    def match(self, lst_of_anagrams):
        possible_anagrams = lst_of_anagrams
        anagrams = []
        
        for word in possible_anagrams:
            if word.casefold() != self._word and (self.sorted_string(self._word) == self.sorted_string(word)):
                print(word)
                anagrams.append(word)

    def sorted_string(self, string):
        return "".join(sorted(string.lower()))

class TestAnagram(unittest.TestCase):
    def test_no_matches(self):
        detector = Anagram("diaper")
        self.assertEqual([], detector.match(["hello", "world", "zombies", "pants"]))

    def test_detect_simple_anagram(self):
        detector = Anagram("ant")
        anagrams = detector.match(["tan", "stand", "at"])
        self.assertEqual(["tan"], anagrams)

    def test_detect_multiple_anagrams(self):
        detector = Anagram("master")
        anagrams = detector.match(["stream", "pigeon", "maters"])
        self.assertEqual(sorted(["maters", "stream"]), sorted(anagrams))

    def test_does_not_confuse_different_duplicates(self):
        detector = Anagram("galea")
        self.assertEqual([], detector.match(["eagle"]))

    def test_identical_word_is_not_anagram(self):
        detector = Anagram("corn")
        anagrams = detector.match(
            ["corn", "dark", "Corn", "rank", "CORN", "cron", "park"]
        )
        self.assertEqual(["cron"], anagrams)

    def test_eliminate_anagrams_with_same_checksum(self):
        detector = Anagram("mass")
        self.assertEqual([], detector.match(["last"]))

    def test_eliminate_anagram_subsets(self):
        detector = Anagram("good")
        self.assertEqual([], detector.match(["dog", "goody"]))

    def test_detect_anagram(self):
        detector = Anagram("listen")
        anagrams = detector.match(["enlists", "google", "inlets", "banana"])
        self.assertEqual(["inlets"], anagrams)

    def test_multiple_anagrams(self):
        detector = Anagram("allergy")
        anagrams = detector.match(
            ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]
        )
        self.assertEqual(sorted(["gallery", "largely", "regally"]), sorted(anagrams))

    def test_anagrams_are_case_insensitive(self):
        detector = Anagram("Orchestra")
        anagrams = detector.match(["cashregister", "Carthorse", "radishes"])
        self.assertEqual(["Carthorse"], anagrams)

if __name__ == "__main__":
    unittest.main()

## LS Solution ##
# class Anagram:
#     def __init__(self, word):
#         self.word = word.lower()

#     def match(self, word_list):
#         return [
#             ana
#             for ana in word_list
#             if ana.lower() != self.word and self._is_anagram(ana, self.word)
#         ]

#     def _sorted_letters(self, string):
#         return "".join(sorted(string.lower()))

#     def _is_anagram(self, word1, word2):
#         return self._sorted_letters(word1) == self._sorted_letters(word2)
