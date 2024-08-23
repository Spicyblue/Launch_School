'''
Rectangles and Squares.

Given the class from the previous problem:

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

Write a class called Square that inherits from the Rectangle class.
The Square class is used like this:

square = Square(5)
print(square.area == 25)      # True

'''

# Solution

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

class Square(Rectangle):

    def __init__(self, square_side):
        super().__init__(square_side, square_side)


square = Square(5)
print(square.area == 25)      # True

# A rectangle's area is given by its width times its height.

## LS Solution ##

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def area(self):
#         return self._width * self._height

# class Square(Rectangle):
#     def __init__(self, side_length):
#         super().__init__(side_length, side_length)
