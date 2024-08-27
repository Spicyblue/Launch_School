'''
Example 4

Consider the following code from the previous assignment:

class SmartLamp:
    def __init__(self, color):
        self.color = color

    def glow(self):
        return (f'The lamp glows {self.color}.')

    @property
    def color(self):                    # Getter for _color
        return self._color

    @color.setter
    def color(self, color):             # Setter for _color
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')

        self._color = color

Your task for this problem is add a brightness property to this class.
Your code should work as shown in the following test code:

lamp = SmartLamp('blue', 70)
print(lamp.color)      # blue
print(lamp.brightness) # 70
print(lamp.glow())     # The lamp glows blue with brightness 70%.

lamp.color = 'red'
lamp.brightness = 90
print(lamp.color)      # red
print(lamp.brightness) # 90
print(lamp.glow())     # The lamp glows red with brightness 90%.

lamp.brightness = 120
# ValueError: Brightness must be between 0 and 100.

'''

# Solution

class SmartLamp:
    def __init__(self, color, brightness):
        self.color = color
        self.brightness = brightness

    def glow(self):
        return (f'The lamp glows {self.color} with brightness {self.brightness}%.')

    @property
    def color(self):                    # Getter for _color
        return self._color

    @color.setter
    def color(self, color):             # Setter for _color
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')

        self._color = color
    
    @property
    def brightness(self):                    # Getter for _brightness
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):             # Setter for _brightness
        if not isinstance(brightness, int):
            raise TypeError('Brightness must be a above 0.')
        if 0 <= brightness <= 100:
            raise ValueError('Brightness must be between 0 and 100.')

        self._brightness = brightness

lamp = SmartLamp('blue', 70)
print(lamp.color)      # blue
print(lamp.brightness) # 70
print(lamp.glow())     # The lamp glows blue with brightness 70%.

lamp.color = 'red'
lamp.brightness = 90
print(lamp.color)      # red
print(lamp.brightness) # 90
print(lamp.glow())     # The lamp glows red with brightness 90%.

# lamp.brightness = 120
# ValueError: Brightness must be between 0 and 100.

## LS Solution ##
# class SmartLamp:
#     def __init__(self, color, brightness):
#         self.color = color
#         self.brightness = brightness

#     def glow(self):
#         return (f'The lamp glows {self.color} with '
#                 f'brightness {self.brightness}%.')

#     @property
#     def color(self):
#         return self._color

#     @color.setter
#     def color(self, color):
#         if not isinstance(color, str):
#             raise TypeError('Color must be a color name.')

#         self._color = color

#     @property
#     def brightness(self):
#         return self._brightness

#     @brightness.setter
#     def brightness(self, brightness):
#         if isinstance(brightness, int):
#             if 0 <= brightness <= 100:
#                 self._brightness = brightness
#                 return

#         raise ValueError('Brightness must be between 0 and 100.')