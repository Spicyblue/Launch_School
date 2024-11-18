'''
Example 3.

Create a Rectangle class with attributes _width and _height.
Add properties to get the width and height but to
disallow modification after the object is created (i.e., no setters).

'''

# Solution

class Rectangle:
    
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f'The width is {self._width}'

    @property
    def height(self):
        return f'The width is {self._height}'

my_box = Rectangle(10, 17)
print(my_box.width)             # outputs The width is 10
print(my_box.height)            # outputs The width is 17

# my_box.height = 12            # outputs AttributeError: can't set attribute 'height'

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

# rectangle = Rectangle(3, 7)
# print(rectangle.width, rectangle.height)      # 3 7

# rectangle.width = 8
# AttributeError: property 'width' of 'Rectangle' object
# has no setter
