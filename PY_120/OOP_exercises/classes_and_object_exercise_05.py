'''
Exercise 5
Create a Person class with two instance variables to hold a person's first and last names. 
- The names should be passed to the constructor as arguments and stored separately. 
- The first and last names are required and must consist entirely of alphabetic characters.
- The class should also have a getter method that returns the person's name as a full name
- The first and last names are separated by spaces, with both first and last names capitalized correctly.

- The class should also have a setter method that takes the name from a two-element tuple. 
- These names must meet the requirements given for the constructor.

Yes, this class is somewhat contrived.

You can use the following code snippets to test your class.
Since some tests cause exceptions, we've broken them into
separate snippets.

'''

# Solution

class Person:

    def __init__(self, first, last):
        print('Instantiation in Process')
        for char in first, last:
            if not char.isalpha():
                raise ValueError('Name must be alphabetic')

        self._full_name = (first, last)

    @property
    def name(self):
        print('Getter Name in process')
        first, last = self._full_name
        first = first.capitalize()
        last = last.capitalize()
        return f'{first} {last}'

    @name.setter
    def name(self, full_name):
        print('Setter Name in process')
        first, last =  full_name
        for char in first, last:
            if not char.isalpha():
                raise ValueError('Name must be alphabetic')

        self._full_name = (first, last)

actor = Person('Mark', 'Sinclair')
# output
# Instantiation in Process

print(actor.name)              # Mark Sinclair
# output
# Getter Name in process
# Mark Sinclair

actor.name = ('Vin', 'Diesel')
# output
# Instantiation in Process

print(actor.name)
# Setter Name in process
# Getter Name in process
# Vin Diesel

# actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
# output
# Instantiation in Process

print(character.name)
# Getter Name in process
# Annie Hall

# character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
# output
# Instantiation in Process

print(friend.name)
# Getter Name in process
# Lynn Blake

friend.name = ('Lynn', 'Blake-John')
# Setter Name in process
# ValueError: Name must be alphabetic.

# ## LS Answer ##
# class Person:

#     def __init__(self, first_name, last_name):
#         self._set_name(first_name, last_name)

#     @property
#     def name(self):
#         first_name = self._first_name.title()
#         last_name = self._last_name.title()
#         return f'{first_name} {last_name}'

#     @name.setter
#     def name(self, name):
#         first_name, last_name = name
#         self._set_name(first_name, last_name)

#     @classmethod
#     def _validate(cls, name):
#         if not name.isalpha():
#             raise ValueError('Name must be alphabetic.')

#     def _set_name(self, first_name, last_name):
#         Person._validate(first_name)
#         Person._validate(last_name)
#         self._first_name = first_name
#         self._last_name = last_name