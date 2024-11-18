'''
Tri-Angles
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.

To be a valid triangle, the sum of the angles must be exactly 180 degrees,
and every angle must be greater than 0.
If either of these conditions is not satisfied,
the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments
and returns one of the following four strings representing the
triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values,
so you do not have to worry about floating point errors.
You may also assume that the arguments are in degrees.

# Problem
- Input: 
Integer
- Output:
String

- Rules
    Explicit:
    To be a valid triangle, the sum of the angles must be exactly 180 degrees, and every angle must be greater than 0.
    If either of these conditions is not satisfied, the triangle is invalid.
    All angles have integer values.
    ALL argumetns are in degrees.
    Right: One angle is a right angle (exactly 90 degrees).
    Acute: All three angles are less than 90 degrees.
    Obtuse: One angle is greater than 90 degrees.

    Implicit:

# Examples
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

# Data structure
List

# Algorithm
    - High End:
        1. Get input.
        2. Create a list to hold all input.
        3. Check if any of the input is zero, return invalid.
        4. Check if sum of the input is 180, return invalid.
        5. Check the criteria for each triangle.
            - If they match, return the triangle name.

# Code
'''

# Solution
def triangle(side1, side2, side3):

    all_sides = [side1, side2, side3]

    if 0 in all_sides or sum(all_sides) != 180:
        return 'invalid'

    if any(angle == 90 for angle in all_sides):
        return 'right'
    elif all(angle < 90 for angle in all_sides):
        return 'acute'
    else:
        return 'obtuse'

# code check
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

# Note!
# Time take to write PEDAC and test/debug code is 12 mins, 8 seconds.

## LS Answer ##
# def is_right_triangle(angle):
#     return angle == 90

# def is_acute_triangle(angle):
#     return angle < 90

# def get_triangle_type(angles):
#     if any([is_right_triangle(angle) for angle in angles]):
#         return "right"
#     elif all([is_acute_triangle(angle) for angle in angles]):
#         return "acute"
#     else:
#         return "obtuse"

# def is_valid(angles):
#     total_angle = sum(angles)
#     all_non_zero = all([angle > 0 for angle in angles])
#     return total_angle == 180 and all_non_zero

# def triangle(angle1, angle2, angle3):
#     angles = [angle1, angle2, angle3]
#     if is_valid(angles):
#         return get_triangle_type(angles)
#     else:
#         return "invalid"

