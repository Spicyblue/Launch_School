import unittest
'''
Diamond.
The diamond exercise takes as its input a letter, and outputs it in a diamond shape.
Given a letter, it prints a diamond starting with 'A', with the supplied letter at the widest point.

The first row contains one 'A'.
The last row contains one 'A'.
All rows, except the first and last, have exactly two identical letters.
The diamond is horizontally symmetric.
The diamond is vertically symmetric.
The diamond has a square shape (width equals height).
The letters form a diamond shape.
The top half has the letters in ascending order.
The bottom half has the letters in descending order.
The four corners (containing the spaces) are triangles.

'''

# Solution
'''
PEDAC
Problem:
    Input: string
    output: string

    Exp: 
    - The first row contains one 'A'.
    - All rows, except the first and last, have exactly two identical letters.
    - The diamond has a square shape (width equals height)
    - The diamond is horizontally and vertically symmetric.
    - The letters form a diamond shape.
    - The top half has the letters in ascending order.
    - The bottom half has the letters in descending order.
    - The four corners (containing the spaces) are triangles.

    imp:
    - unittest test cases show that our we need a Diamond class thats doesnt accept any arguments passed to its constructor.
    - The class should have a make_diamond classmethod which takes a letter and makes a diamond out of it.

Examples:
Using unittest TestCase

Data Structure:
Class with class variables and methods.

Algorithm:
    Highend
    - Get the Letter with A being the first 1 and Z being the last 26.
    - Build the top half with letters in ascending order.
    - Build the second half with letters in descending order.
    - Return the diamond.

    Lowend:
    - Bit hard to explain.. Hope the code helps.
'''

class Diamond:
    @classmethod
    def make_diamond(cls, char):
        start_char = ord(char)
        end_char = ord('A')
        steps = start_char - end_char
        if steps == 0:
            return "A\n"

        main_diamond = cls.get_upper_diamond(steps, end_char)
        main_diamond += cls.get_lower_diamond(steps, end_char)

        return '\n'.join(main_diamond) + '\n'

    @staticmethod
    def get_upper_diamond(steps, end_char):
        upper_diamond = []

        for idx in range(steps + 1):
            if idx == 0:
                line = ' ' * (steps) + 'A' + ' ' * (steps)
            else:
                outer_spaces = ' ' * (steps - idx)
                inner_spaces = ' ' * (2*idx - 1)
                line = outer_spaces + chr(end_char + idx) + inner_spaces + chr(end_char + idx) + outer_spaces
            upper_diamond.append(line)
        return upper_diamond

    @staticmethod
    def get_lower_diamond(steps, end_char):
        lower_diamond = []

        for idxx in range(steps - 1, -1, -1):
            if idxx == 0:
                line = ' ' * (steps) + 'A' + ' ' * (steps)
            else:
                outer_spaces = ' ' * (steps - idxx)
                inner_spaces = ' ' * (2*idxx - 1)
                line = outer_spaces + chr(end_char + idxx) + inner_spaces + chr(end_char + idxx) + outer_spaces
            lower_diamond.append(line)
        
        return lower_diamond


# Test the class
print(Diamond.make_diamond('E'))

class DiamondTest(unittest.TestCase):

    def test_letter_a(self):
        answer = Diamond.make_diamond('A')
        self.assertEqual("A\n", answer)

    def test_letter_b(self):
        answer = Diamond.make_diamond('B')
        expected = " A \nB B\n A \n"
        self.assertEqual(expected, answer)

    def test_letter_c(self):
        answer = Diamond.make_diamond('C')
        expected = "  A  \n" \
                   " B B \n" \
                   "C   C\n" \
                   " B B \n" \
                   "  A  \n"
        self.assertEqual(expected, answer)

    def test_letter_e(self):
        answer = Diamond.make_diamond('E')
        expected = "    A    \n" \
                   "   B B   \n" \
                   "  C   C  \n" \
                   " D     D \n" \
                   "E       E\n" \
                   " D     D \n" \
                   "  C   C  \n" \
                   "   B B   \n" \
                   "    A    \n"
        self.assertEqual(expected, answer)

if __name__ == '__main__':
    unittest.main()

# LS Solution ##
# class Diamond:
#     @classmethod
#     def make_diamond(cls, letter):
#         upper_range = list(chr(i) for i in range(65, ord(letter) + 1))
#         lower_range = list(chr(i) for i in range(65, ord(letter)))[::-1]
#         full_range = upper_range + lower_range

#         diamond_width = cls._max_width(letter)

#         return '\n'.join([cls._make_row(let).center(diamond_width) for let in full_range]) + '\n'

#     @classmethod
#     def _make_row(cls, letter):
#         if letter == 'A':
#             return "A"
#         return letter + cls._determine_spaces(letter) + letter

#     @classmethod
#     def _determine_spaces(cls, letter):
#         return ' ' * (2 * (ord(letter) - ord('A')) - 1)

#     @classmethod
#     def _max_width(cls, letter):
#         if letter == 'A':
#             return 1
#         return 2 * (ord(letter) - ord('A')) + 1

