'''
Triangle Sides. 

A triangle is classified as follows:
Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side,
and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments
and returns one of the following four strings representing the triangle's classification:
'equilateral', 'isosceles', 'scalene', or 'invalid'.

# Problem
- Input: 
Integer
- Output:
String

- Rules
    Explicit:
    To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side and every side must have a length greater than 0.
    If either of these conditions is not satisfied, the triangle is invalid.
    Equilateral: All three sides have the same length.
    Isosceles: Two sides have the same length, while the third is different.
    Scalene: All three sides have different lengths.

    Implicit:

# Examples
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

# Data structure
List

# Algorithm
    - High End:
        1. Get input.
        2. Create a list to hold all input.
        3. Sort the list in ascending order
        4. Check if any of the input is zero, return invalid.
        5. Check if the sum of the first two is greater the the third:
            - If not, result invalid.
        6. Check the criteria for each triangle, 
            - If they match, return the traingle name.

# Code
'''

# Solution
def triangle(side1, side2, side3):

    all_sides = [side1, side2, side3]
    all_sides.sort()

    if 0 in all_sides:
        return 'invalid'

    if sum(all_sides[:2]) <= all_sides[-1]:
        return 'invalid'

    elif all_sides[ : ] == all_sides[ : : -1]:
        return 'equilateral'
    
    elif all_sides[0] == all_sides[1] or all_sides[1] == all_sides[2]:
        return 'isosceles'

    else:
        return 'scalene'
    
# code check
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(5, 3, 4) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

# Note!
# Time take to write PEDAC and test/debug code is 17 mins, 30 seconds.

## LS Answer ##
# def get_triangle_type(side1, side2, side3):
#     if side1 == side2 == side3:
#         return "equilateral"
#     elif side1 == side2 or side1 == side3 or side2 == side3:
#         return "isosceles"
#     else:
#         return "scalene"

# def is_valid(shortest, middle, longest):
#     return shortest > 0 and shortest + middle > longest

# def triangle(side1, side2, side3):
#     perimeter = side1 + side2 + side3
#     longest = max(side1, side2, side3)
#     shortest = min(side1, side2, side3)
#     middle = perimeter - longest - shortest

#     if is_valid(shortest, middle, longest):
#         return get_triangle_type(side1, side2, side3)
#     else:
#         return "invalid"
