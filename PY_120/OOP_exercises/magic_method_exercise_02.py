'''
Exercise 2
Don't let the mathiness of this problem scare you off. 
You don't have to know any math; you only need to know how to write code.

Earlier, we wrote the following class:

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        self.x += other.x
        self.y += other.y
        return self

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

Update this class so the following code works as indicated:

print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17
print(abs(v1)) # 13.0

In this code, the * operator should compute the dot product of the two vectors. 
For instance, if you have Vector(a, b) and Vector(c, d),
the dot product is a * c + b * d, where * and + are the usual arithmetic operators.

The abs function computes the magnitude of a vector.
If you have a vector Vector(a, b), the magnitude is given by sqrt(a**2 + b**2).
You will need the math module to access the sqrt function.
Note that abs is a built-in function, so you don't want to override it entirely;
you only want to change its behavior for Vector objects.
There's a magic method you can use.

Don't worry about augmented assignment in this exercise.
'''

# Solution

import math
class Vector:

    def __init__(self, x, y):
        print('Instantiation')
        self.x = x
        self.y = y

    def __add__(self, other):
        print('adding in proccess')
        if not isinstance(other, Vector):
            return NotImplemented

        add_x = self.x + other.x
        add_y = self.y + other.y
        print('adding finished ')
        return Vector(add_x, add_y)
    
    def __sub__(self, other):
        print('subtracting in process')
        if not isinstance(other, Vector):
            return NotImplemented

        sub_x = self.x - other.x
        sub_y = self.y - other.y
        
        print('substracting finished')
        return Vector(sub_x, sub_y)
    
    def __mul__(self, other):
        print('multiplication in process')
        if not isinstance(other, Vector):
            return NotImplemented

        mul_x = self.x * other.x
        mul_y = self.y * other.y
        prod = mul_x + mul_y
        
        print('multiplication is finished')
        return prod

    def __abs__(self):
        print('absolute value in process')

        abs_x = self.x**2
        abs_y = self.y**2
        main_abs = math.sqrt(abs_x + abs_y)

        print('absolute value is finished')
        return main_abs

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
# Output
# Instantiation

v2 = Vector(13, -4)
# Output
# Instantiation

print(v1 + v2)
# Output
# adding in proccess
# adding finished 
# Instantiation
# Vector(18, 8)

print(v1 - v2) # Vector(-8, 16)
# Output
# subtracting in process
# substracting finished
# Instantiation
# Vector(-8, 16)

print(v1 * v2) # 17
# Output
# multiplication in process
# multiplication is finished
# 17

print(abs(v1)) # 13.0
# Output
# absolute value in process
# absolute value is finished
# 13.0

## LS Answer ##

# import math

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)

#     def __sub__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x - other.x
#         new_y = self.y - other.y
#         return Vector(new_x, new_y)

#     def __mul__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         dot_product = ((self.x * other.x) +
#                         (self.y * other.y))
#         return dot_product

#     def __abs__(self):
#         sum_of_squares = ((self.x ** 2) +
#                           (self.y ** 2))
#         return math.sqrt(sum_of_squares)

#     def __repr__(self):
#         x = repr(self.x)
#         y = repr(self.y)
#         return f'Vector({x}, {y})'
