'''
Example 7.

What would happen if you ran the following code? Don't run it until you've checked your answer:

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())
print(tv.model())

print(Television.manufacturer())
print(Television.model())
'''

# Solution

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())            # outputs Amazon
print(tv.model())                   # outputs Omni Fire

print(Television.manufacturer())    # Outputs Amazon
#print(Television.model())          # raises an error

## LS Solution ##

# print(tv.manufacturer())          # Amazon
# print(tv.model())                 # Omni Fire

# print(Television.manufacturer())  # Amazon
# print(Television.model())
# # TypeError: Television.model() missing 1 required
# # positional argument: 'self'
#The situation changes again with Television.model. 
# We're trying to invoke an instance method as though it were a class method.
# That simply doesn't work, so we get a TypeError. The error message is a bit hard to understand,
# but it basically means that you're calling a class method as an instance method.
