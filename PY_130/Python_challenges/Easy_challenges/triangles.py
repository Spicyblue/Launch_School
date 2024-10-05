import unittest
'''
Triangles.
Write a program to determine whether a triangle is equilateral, isosceles, or scalene.
An equilateral triangle has all three sides the same length.
An isosceles triangle has exactly two sides of the same length.
A scalene triangle has all sides of different lengths.

Note: For a shape to be a triangle at all, all sides must be of length > 0, 
and the sum of the lengths of any two sides must be greater than the length of the third side.
'''

# Solution
'''
PEDAC
Problem:
    Input: Integers
    output: Strings or Exceptions.

    Exp: 
    - To be a valid triangle, each side length must be greater than 0.
    - To be a valid triangle, the sum of the lengths of any two sides
      must be greater than the length of the remaining side.
    - An equilateral triangle has three sides of equal length.
    - An isosceles triangle has exactly two sides of the equal length.
    - A scalene triangle has three sides of unequal length (no two sides have equal length).

    imp:
    - unittest test cases show that our triangle object is an instance 
      of class Triange which accepts three arguments.
    - The triangle class should have a kind method.
    - Triangle raises a ValueError if the sum of the lengths of any two sides 
      is lesser than the lenght of the remaining side

Examples:
Using unittest TestCase


Data Structure:
Class 

Algorithm:
    Highend
    - Get all sides of the triangles.
    - Ensure they are valid.
    - Return the type of the angles based on the sides given.


    Lowend:
        - Define a class Triangles which accepts three argument using the Triangle constructor.
        - Creat a local variable triangle_sides that is a list with 
          its element as arguments(sides) of the Triangles class.
        - Check if the sum of any two sides is great the third:
            - if yes, raise ValueError
        - check if 0 is an element in the list.
            - if yes, raise ValueError.
        - check if any negative number is an element in the list.
            - if yes, raise ValueError
        - If not, assign the list to instance variables _sides.
        - Define a property kind:
            - Check is all instance variables of Triangle are same:
                - return equilateral
            - check if any two instance variable if Triangle are same:
                - return isosceles
            - check if none of the instance variables of Triangle are same:
                - return scalene
'''

class Triangle:

    def __init__(self, side1, side2, side3):
        triangle_sides = [side1, side2, side3]
        if 0 in triangle_sides:
            raise ValueError('A side cannot have zero lenght')
        elif sum([side1, side2]) <= side3 or sum([side1, side3]) <= side2 or sum([side2, side3]) <= side1:
            raise ValueError('Sum of two sides not greater than third side')

        self._sides = triangle_sides

    @property
    def kind(self):
        if len(set(self._sides)) == 1:
            return 'equilateral'
        elif len(set(self._sides)) ==2:
            return 'isosceles'
        else:
            return 'scalene'
        
class TestTriangle(unittest.TestCase):
    def test_equilateral_equal_sides(self):
        triangle = Triangle(2, 2, 2)
        self.assertEqual(triangle.kind, "equilateral")

    def test_larger_equilateral_equal_sides(self):
        triangle = Triangle(10, 10, 10)
        self.assertEqual(triangle.kind, "equilateral")

    def test_isosceles_last_two_sides_equal(self):
        triangle = Triangle(3, 4, 4)
        self.assertEqual(triangle.kind, "isosceles")

    def test_isosceles_first_last_sides_equal(self):
        triangle = Triangle(4, 3, 4)
        self.assertEqual(triangle.kind, "isosceles")

    def test_isosceles_first_two_sides_equal(self):
        triangle = Triangle(4, 4, 3)
        self.assertEqual(triangle.kind, "isosceles")

    def test_isosceles_exactly_two_sides_equal(self):
        triangle = Triangle(10, 10, 2)
        self.assertEqual(triangle.kind, "isosceles")

    def test_scalene_no_equal_sides(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.kind, "scalene")

    def test_scalene_larger_no_equal_sides(self):
        triangle = Triangle(10, 11, 12)
        self.assertEqual(triangle.kind, "scalene")

    def test_scalene_no_equal_sides_descending(self):
        triangle = Triangle(5, 4, 2)
        self.assertEqual(triangle.kind, "scalene")

    def test_small_triangles_are_legal(self):
        triangle = Triangle(0.4, 0.6, 0.3)
        self.assertEqual(triangle.kind, "scalene")

    def test_no_size_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)

    def test_negative_size_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(3, 4, -5)

    def test_size_inequality_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    def test_size_inequality_is_illegal_2(self):
        with self.assertRaises(ValueError):
            Triangle(7, 3, 2)

    def test_size_inequality_is_illegal_3(self):
        with self.assertRaises(ValueError):
            Triangle(10, 1, 3)

    def test_size_inequality_is_illegal_4(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 2)

if __name__ == "__main__":
    unittest.main()


## LS Solution ##

# class Triangle:
#     def __init__(self, side1, side2, side3):
#         self.sides = [side1, side2, side3]
#         if not self._is_valid():
#             raise ValueError("Invalid triangle lengths")

#     @property
#     def kind(self):
#         if len(set(self.sides)) == 1:
#             return "equilateral"
#         elif len(set(self.sides)) == 2:
#             return "isosceles"
#         else:
#             return "scalene"

#     def _is_valid(self):
#         return (
#             all(side > 0 for side in self.sides)
#             and self.sides[0] + self.sides[1] > self.sides[2]
#             and self.sides[1] + self.sides[2] > self.sides[0]
#             and self.sides[0] + self.sides[2] > self.sides[1]
#         )