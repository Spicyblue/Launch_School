'''
Example 5.

Consider the following class that represents a value that can be either a string or an integer:

class Silly:

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)

Assuming we have an expression like Silly(x) + y, the evaluation rules are as follows:

If either x or y is a non-numeric string, concatenate the string values of x and y.
Otherwise, compute the sum of the integer values of x and y. Another way to word that is:

If both x and y can be expressed as integers, compute the sum of the integer values of x and y.
Otherwise, concatenate the string values of x and y.
We'll use the latter description in our code: it'll be easier to write and understand.

A numeric string_ is a string that consists entirely of numeric digits.
You can use str.isdigit to determine whether a string is numeric.
A non-numeric string is a string that contains at least one character that is not a numeric digit.


'''

# Solution

class Silly:

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __add__(self, other):

        if (isinstance(other, str) and isinstance(self.value, str) 
            and other.isnumeric() and self.value.isnumeric()):
            other = int(other)
            self.value = int(self.value)
            result = self.value + other
            return Silly(result)

        elif (isinstance(other, int) and isinstance(self.value, str) 
              and self.value.isnumeric()):
            self.value = int(self.value)
            result = self.value + other
            return Silly(result)
        
        elif (isinstance(other, str) and isinstance(self.value, int)
              and other.isnumeric()):
            other = int(other)
            result = self.value + other
            return Silly(result)
        
        elif isinstance(other, int) and isinstance(self.value, int):
            result = self.value + other
            return Silly(result)
        
        elif isinstance(other, str) and isinstance(self.value, str):
            new_value = self.value + other
            return Silly(new_value)
        
        elif isinstance(other, int) and isinstance(self.value, str):
            other = str(other)
            new_value = self.value + other
            return Silly(new_value)
        
        elif isinstance(other, str) and isinstance(self.value, int):
            self.value = str(self.value)
            new_value = self.value + other
            return Silly(new_value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)

# ## LS Solution ##

# class Silly:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return f'Silly({repr(self.value)})'

#     def _is_numeric(self, value):
#         if isinstance(value, int):
#             return True

#         return value.isdigit()

#     def __add__(self, other):
#         if not isinstance(other, int):
#             if not isinstance(other, str):
#                 return NotImplemented

#         both_numeric = (self._is_numeric(self.value) and
#                         self._is_numeric(other))
#         if both_numeric:
#             return Silly(int(self.value) + int(other))
#         else:
#             return Silly(str(self.value) + str(other))