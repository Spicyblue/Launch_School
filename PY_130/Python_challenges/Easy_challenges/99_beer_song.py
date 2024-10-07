import unittest
'''
Beer Song.
Write a program that can generate the lyrics of the 99 Bottles of Beer song. 
See the test suite for the entire song.

'''

# Solution
'''
PEDAC
Problem:
    Input: Integer
    output: String

    Exp: 
    - Valid digits are integers above 0.
    - Alwasy starts from the integer input and down.

    imp:
    - unittest test cases show that our we need a BeerSong class 
      which doesnt accept any argument passed to its constructor.
    - The class should have a verse classmethod to which takes in one argument
      and return the verse of the beersong.
    - The class should have a verses classmethod to which takes in two argument
      and return the verse of the beersong.
    - The class should have a lyrics classmethod to which takes no argument 
      and the whole verses of the beersong.
 
Examples:
Using unittest TestCase

Data Structure:
Class with class variables and methods.

Algorithm:
    Highend
    - Get the verse required.
    - Construct the verse.
    - Return the verse

    Lowend:
        - Define a class method verse:
        - Accept parameter start_verse
        - Call _get_verse with start_verse and return the result

        - Define a class method verses:
        - Accept parameters start_verse and end_verse
        - Call _get_verse with start_verse and end_verse, return the result

        - Define a class method lyrics:
        - Call _get_verse with 99 and 0, return the result

        - Define a static method _get_verse:
        - Accept parameters start_verse and end_verse (default to None)
        - Set _start_verse to start_verse
        - Set _end_verse to end_verse if provided, otherwise to _start_verse
        - Define verse_0 and verse_1 as default verses
        - Initialize requested_verse as an empty string
        - Iterate from _start_verse down to _end_verse (inclusive):
            - If verse is 0, add verse_0 to requested_verse
            - If verse is 1, add verse_1 to requested_verse
            - Otherwise, add a dynamically generated verse to requested_verse
            - Add a newline character between verses (except for the last one)
        - Return requested_verse

'''
class BeerSong:
    @classmethod
    def verse(cls, start_verse):
        return cls._get_verse(start_verse)

    @classmethod
    def verses(cls, start_verse, end_verse):
        return cls._get_verse(start_verse, end_verse)

    @classmethod
    def lyrics(cls):
        return cls._get_verse(99, 0)

    @staticmethod
    def _get_verse(start_verse, end_verse = None):
        _start_verse = start_verse
        _end_verse = end_verse if end_verse is not None else start_verse

        verse_0 = ("No more bottles of beer on the wall, no more bottles of beer.\n"
            "Go to the store and buy some more, 99 bottles of beer on the wall.\n")
        verse_1 = ("1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take it down and pass it around, no more bottles of beer on the wall.\n")

        requested_verse = ''
        for verse in range(_start_verse, _end_verse - 1, -1):
            if verse == 0:
                requested_verse += verse_0
            elif verse == 1:
                requested_verse += verse_1
            else:
                requested_verse += (f"{verse} bottles of beer on the wall, {verse} bottles of beer.\n"
                f"Take one down and pass it around, {verse - 1} bottle{'s' if verse - 1 != 1 else ''} of beer on the wall.\n")
            
            if verse != _end_verse:
                requested_verse += "\n"

        return requested_verse

class BeerSongTest(unittest.TestCase):
    def test_the_first_verse(self):
        expected = (
            "99 bottles of beer on the wall, 99 bottles of beer.\n"
            "Take one down and pass it around, 98 bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, BeerSong.verse(99))

    def test_another_verse(self):
        expected = (
            "3 bottles of beer on the wall, 3 bottles of beer.\n"
            "Take one down and pass it around, 2 bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, BeerSong.verse(3))

    def test_verse_2(self):
        expected = (
            "2 bottles of beer on the wall, 2 bottles of beer.\n"
            "Take one down and pass it around, 1 bottle of beer on the wall.\n"
        )
        self.assertEqual(expected, BeerSong.verse(2))

    def test_verse_1(self):
        expected = (
            "1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take it down and pass it around, no more bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, BeerSong.verse(1))

    def test_verse_0(self):
        expected = (
            "No more bottles of beer on the wall, no more bottles of beer.\n"
            "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, BeerSong.verse(0))

    def test_a_couple_verses(self):
        expected = (
            "99 bottles of beer on the wall, 99 bottles of beer.\n"
            "Take one down and pass it around, 98 bottles of beer on the wall.\n"
            "\n"
            "98 bottles of beer on the wall, 98 bottles of beer.\n"
            "Take one down and pass it around, 97 bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, BeerSong.verses(99, 98))

    def test_a_few_verses(self):
        expected = (
            "2 bottles of beer on the wall, 2 bottles of beer.\n"
            "Take one down and pass it around, 1 bottle of beer on the wall.\n"
            "\n"
            "1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take it down and pass it around, no more bottles of beer on the wall.\n"
            "\n"
            "No more bottles of beer on the wall, no more bottles of beer.\n"
            "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, BeerSong.verses(2, 0))

    def test_the_whole_song(self):
        expected = """\
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.

97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.

96 bottles of beer on the wall, 96 bottles of beer.
Take one down and pass it around, 95 bottles of beer on the wall.

95 bottles of beer on the wall, 95 bottles of beer.
Take one down and pass it around, 94 bottles of beer on the wall.

94 bottles of beer on the wall, 94 bottles of beer.
Take one down and pass it around, 93 bottles of beer on the wall.

93 bottles of beer on the wall, 93 bottles of beer.
Take one down and pass it around, 92 bottles of beer on the wall.

92 bottles of beer on the wall, 92 bottles of beer.
Take one down and pass it around, 91 bottles of beer on the wall.

91 bottles of beer on the wall, 91 bottles of beer.
Take one down and pass it around, 90 bottles of beer on the wall.

90 bottles of beer on the wall, 90 bottles of beer.
Take one down and pass it around, 89 bottles of beer on the wall.

89 bottles of beer on the wall, 89 bottles of beer.
Take one down and pass it around, 88 bottles of beer on the wall.

88 bottles of beer on the wall, 88 bottles of beer.
Take one down and pass it around, 87 bottles of beer on the wall.

87 bottles of beer on the wall, 87 bottles of beer.
Take one down and pass it around, 86 bottles of beer on the wall.

86 bottles of beer on the wall, 86 bottles of beer.
Take one down and pass it around, 85 bottles of beer on the wall.

85 bottles of beer on the wall, 85 bottles of beer.
Take one down and pass it around, 84 bottles of beer on the wall.

84 bottles of beer on the wall, 84 bottles of beer.
Take one down and pass it around, 83 bottles of beer on the wall.

83 bottles of beer on the wall, 83 bottles of beer.
Take one down and pass it around, 82 bottles of beer on the wall.

82 bottles of beer on the wall, 82 bottles of beer.
Take one down and pass it around, 81 bottles of beer on the wall.

81 bottles of beer on the wall, 81 bottles of beer.
Take one down and pass it around, 80 bottles of beer on the wall.

80 bottles of beer on the wall, 80 bottles of beer.
Take one down and pass it around, 79 bottles of beer on the wall.

79 bottles of beer on the wall, 79 bottles of beer.
Take one down and pass it around, 78 bottles of beer on the wall.

78 bottles of beer on the wall, 78 bottles of beer.
Take one down and pass it around, 77 bottles of beer on the wall.

77 bottles of beer on the wall, 77 bottles of beer.
Take one down and pass it around, 76 bottles of beer on the wall.

76 bottles of beer on the wall, 76 bottles of beer.
Take one down and pass it around, 75 bottles of beer on the wall.

75 bottles of beer on the wall, 75 bottles of beer.
Take one down and pass it around, 74 bottles of beer on the wall.

74 bottles of beer on the wall, 74 bottles of beer.
Take one down and pass it around, 73 bottles of beer on the wall.

73 bottles of beer on the wall, 73 bottles of beer.
Take one down and pass it around, 72 bottles of beer on the wall.

72 bottles of beer on the wall, 72 bottles of beer.
Take one down and pass it around, 71 bottles of beer on the wall.

71 bottles of beer on the wall, 71 bottles of beer.
Take one down and pass it around, 70 bottles of beer on the wall.

70 bottles of beer on the wall, 70 bottles of beer.
Take one down and pass it around, 69 bottles of beer on the wall.

69 bottles of beer on the wall, 69 bottles of beer.
Take one down and pass it around, 68 bottles of beer on the wall.

68 bottles of beer on the wall, 68 bottles of beer.
Take one down and pass it around, 67 bottles of beer on the wall.

67 bottles of beer on the wall, 67 bottles of beer.
Take one down and pass it around, 66 bottles of beer on the wall.

66 bottles of beer on the wall, 66 bottles of beer.
Take one down and pass it around, 65 bottles of beer on the wall.

65 bottles of beer on the wall, 65 bottles of beer.
Take one down and pass it around, 64 bottles of beer on the wall.

64 bottles of beer on the wall, 64 bottles of beer.
Take one down and pass it around, 63 bottles of beer on the wall.

63 bottles of beer on the wall, 63 bottles of beer.
Take one down and pass it around, 62 bottles of beer on the wall.

62 bottles of beer on the wall, 62 bottles of beer.
Take one down and pass it around, 61 bottles of beer on the wall.

61 bottles of beer on the wall, 61 bottles of beer.
Take one down and pass it around, 60 bottles of beer on the wall.

60 bottles of beer on the wall, 60 bottles of beer.
Take one down and pass it around, 59 bottles of beer on the wall.

59 bottles of beer on the wall, 59 bottles of beer.
Take one down and pass it around, 58 bottles of beer on the wall.

58 bottles of beer on the wall, 58 bottles of beer.
Take one down and pass it around, 57 bottles of beer on the wall.

57 bottles of beer on the wall, 57 bottles of beer.
Take one down and pass it around, 56 bottles of beer on the wall.

56 bottles of beer on the wall, 56 bottles of beer.
Take one down and pass it around, 55 bottles of beer on the wall.

55 bottles of beer on the wall, 55 bottles of beer.
Take one down and pass it around, 54 bottles of beer on the wall.

54 bottles of beer on the wall, 54 bottles of beer.
Take one down and pass it around, 53 bottles of beer on the wall.

53 bottles of beer on the wall, 53 bottles of beer.
Take one down and pass it around, 52 bottles of beer on the wall.

52 bottles of beer on the wall, 52 bottles of beer.
Take one down and pass it around, 51 bottles of beer on the wall.

51 bottles of beer on the wall, 51 bottles of beer.
Take one down and pass it around, 50 bottles of beer on the wall.

50 bottles of beer on the wall, 50 bottles of beer.
Take one down and pass it around, 49 bottles of beer on the wall.

49 bottles of beer on the wall, 49 bottles of beer.
Take one down and pass it around, 48 bottles of beer on the wall.

48 bottles of beer on the wall, 48 bottles of beer.
Take one down and pass it around, 47 bottles of beer on the wall.

47 bottles of beer on the wall, 47 bottles of beer.
Take one down and pass it around, 46 bottles of beer on the wall.

46 bottles of beer on the wall, 46 bottles of beer.
Take one down and pass it around, 45 bottles of beer on the wall.

45 bottles of beer on the wall, 45 bottles of beer.
Take one down and pass it around, 44 bottles of beer on the wall.

44 bottles of beer on the wall, 44 bottles of beer.
Take one down and pass it around, 43 bottles of beer on the wall.

43 bottles of beer on the wall, 43 bottles of beer.
Take one down and pass it around, 42 bottles of beer on the wall.

42 bottles of beer on the wall, 42 bottles of beer.
Take one down and pass it around, 41 bottles of beer on the wall.

41 bottles of beer on the wall, 41 bottles of beer.
Take one down and pass it around, 40 bottles of beer on the wall.

40 bottles of beer on the wall, 40 bottles of beer.
Take one down and pass it around, 39 bottles of beer on the wall.

39 bottles of beer on the wall, 39 bottles of beer.
Take one down and pass it around, 38 bottles of beer on the wall.

38 bottles of beer on the wall, 38 bottles of beer.
Take one down and pass it around, 37 bottles of beer on the wall.

37 bottles of beer on the wall, 37 bottles of beer.
Take one down and pass it around, 36 bottles of beer on the wall.

36 bottles of beer on the wall, 36 bottles of beer.
Take one down and pass it around, 35 bottles of beer on the wall.

35 bottles of beer on the wall, 35 bottles of beer.
Take one down and pass it around, 34 bottles of beer on the wall.

34 bottles of beer on the wall, 34 bottles of beer.
Take one down and pass it around, 33 bottles of beer on the wall.

33 bottles of beer on the wall, 33 bottles of beer.
Take one down and pass it around, 32 bottles of beer on the wall.

32 bottles of beer on the wall, 32 bottles of beer.
Take one down and pass it around, 31 bottles of beer on the wall.

31 bottles of beer on the wall, 31 bottles of beer.
Take one down and pass it around, 30 bottles of beer on the wall.

30 bottles of beer on the wall, 30 bottles of beer.
Take one down and pass it around, 29 bottles of beer on the wall.

29 bottles of beer on the wall, 29 bottles of beer.
Take one down and pass it around, 28 bottles of beer on the wall.

28 bottles of beer on the wall, 28 bottles of beer.
Take one down and pass it around, 27 bottles of beer on the wall.

27 bottles of beer on the wall, 27 bottles of beer.
Take one down and pass it around, 26 bottles of beer on the wall.

26 bottles of beer on the wall, 26 bottles of beer.
Take one down and pass it around, 25 bottles of beer on the wall.

25 bottles of beer on the wall, 25 bottles of beer.
Take one down and pass it around, 24 bottles of beer on the wall.

24 bottles of beer on the wall, 24 bottles of beer.
Take one down and pass it around, 23 bottles of beer on the wall.

23 bottles of beer on the wall, 23 bottles of beer.
Take one down and pass it around, 22 bottles of beer on the wall.

22 bottles of beer on the wall, 22 bottles of beer.
Take one down and pass it around, 21 bottles of beer on the wall.

21 bottles of beer on the wall, 21 bottles of beer.
Take one down and pass it around, 20 bottles of beer on the wall.

20 bottles of beer on the wall, 20 bottles of beer.
Take one down and pass it around, 19 bottles of beer on the wall.

19 bottles of beer on the wall, 19 bottles of beer.
Take one down and pass it around, 18 bottles of beer on the wall.

18 bottles of beer on the wall, 18 bottles of beer.
Take one down and pass it around, 17 bottles of beer on the wall.

17 bottles of beer on the wall, 17 bottles of beer.
Take one down and pass it around, 16 bottles of beer on the wall.

16 bottles of beer on the wall, 16 bottles of beer.
Take one down and pass it around, 15 bottles of beer on the wall.

15 bottles of beer on the wall, 15 bottles of beer.
Take one down and pass it around, 14 bottles of beer on the wall.

14 bottles of beer on the wall, 14 bottles of beer.
Take one down and pass it around, 13 bottles of beer on the wall.

13 bottles of beer on the wall, 13 bottles of beer.
Take one down and pass it around, 12 bottles of beer on the wall.

12 bottles of beer on the wall, 12 bottles of beer.
Take one down and pass it around, 11 bottles of beer on the wall.

11 bottles of beer on the wall, 11 bottles of beer.
Take one down and pass it around, 10 bottles of beer on the wall.

10 bottles of beer on the wall, 10 bottles of beer.
Take one down and pass it around, 9 bottles of beer on the wall.

9 bottles of beer on the wall, 9 bottles of beer.
Take one down and pass it around, 8 bottles of beer on the wall.

8 bottles of beer on the wall, 8 bottles of beer.
Take one down and pass it around, 7 bottles of beer on the wall.

7 bottles of beer on the wall, 7 bottles of beer.
Take one down and pass it around, 6 bottles of beer on the wall.

6 bottles of beer on the wall, 6 bottles of beer.
Take one down and pass it around, 5 bottles of beer on the wall.

5 bottles of beer on the wall, 5 bottles of beer.
Take one down and pass it around, 4 bottles of beer on the wall.

4 bottles of beer on the wall, 4 bottles of beer.
Take one down and pass it around, 3 bottles of beer on the wall.

3 bottles of beer on the wall, 3 bottles of beer.
Take one down and pass it around, 2 bottles of beer on the wall.

2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take it down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
"""
        self.assertEqual(expected, BeerSong.lyrics())

if __name__ == "__main__":
    unittest.main()

# LS Solution ##
# class Verse:
#     def __init__(self, bottles):
#         self.bottles = bottles

#     def single_verse(self):
#         if self.bottles == 0:
#             return self._zero_bottle_verse()
#         elif self.bottles == 1:
#             return self._single_bottle_verse()
#         elif self.bottles == 2:
#             return self._two_bottle_verse()
#         else:
#             return self._default_verse()

#     def _default_verse(self):
#         return (
#             f"{self.bottles} bottles of beer on the wall, {self.bottles}"
#             f" bottles of beer.\nTake one down and pass it around, "
#             f"{self.bottles - 1} bottles of beer on the wall.\n"
#         )

#     def _two_bottle_verse(self):
#         return (
#             "2 bottles of beer on the wall, 2 bottles of beer.\n"
#             "Take one down and pass it around, 1 bottle of beer "
#             "on the wall.\n"
#         )

#     def _single_bottle_verse(self):
#         return (
#             "1 bottle of beer on the wall, 1 bottle of beer.\n"
#             "Take it down and pass it around, no more bottles of beer "
#             "on the wall.\n"
#         )

#     def _zero_bottle_verse(self):
#         return (
#             "No more bottles of beer on the wall, no more bottles "
#             "of beer.\nGo to the store and buy some more, 99 bottles "
#             "of beer on the wall.\n"
#         )

# class BeerSong:
#     @classmethod
#     def verse(cls, number):
#         return Verse(number).single_verse()

#     @classmethod
#     def verses(cls, start, stop):
#         result = []
#         current_verse = start
#         while current_verse >= stop:
#             result.append(cls.verse(current_verse))
#             current_verse -= 1
#         return "\n".join(result)

#     @classmethod
#     def lyrics(cls):
#         return cls.verses(99, 0)