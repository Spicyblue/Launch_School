'''
Example 5.

How could you change the light_status method name below so that the
method name is clearer and less repetitive?

class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def light_status(self):
        return (f'I have a brightness level of {self.brightness} '
                f'and a color of {self.color}')

my_light = Light(50, 'Red')
print(my_light.light_status())

'''

# Solution

class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def info(self):
        return (f'I have a brightness level of {self.brightness} '
                f'and a color of {self.color}')

my_light = Light(50, 'Red')
print(my_light.info())

## LS Solution ##
# Currently, the method is defined as light_status, which seems reasonable.
# But when using it with the my_light object, you end up saying my_light.light_status().
# Having the word "light" appear twice is redundant.

# Alternatively, we can rename the method to just status, then invoke it as my_light.status().
# This is more concise and arguably more readable.
# Remember, you're writing code to be readable by others as well as your future self.