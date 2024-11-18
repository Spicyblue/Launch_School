'''
Example 5

Continuing with our Person class definition, what do you think the following code prints?

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")

'''

# Solution

class Person:
    
    def __init__(self, name, last_name = ""):
        self._first_name = name
        self._last_name = last_name

    @property
    def name(self):
        return self._first_name + ' ' + self._last_name
    
    @name.setter
    def name(self, name):
        self._name = name.split()
        if len(self._name) == 1:
            self._first_name = self._name[0]
            self._last_name = ''

        elif len(self._name) > 1:
            self._first_name = self._name[0]
            self._last_name = " ".join([names for names in self._name[1:]])

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")
print("The person's name is: " + bob.name)
# The person's name is: Robert Smith
print(f"The person's name is: {bob.name}")

## LS Solution ##

# Notes

# We're using string interpolation in this code, as opposed to string concatenation.
# Python automatically calls the str function on the expression between the {}. 
# Every object in Python responds to the str function which, by default, is inherited from the object class. 
# By default, it prints out some gibberish, which represents the object's place in memory.
# Until we learn how to override str's behavior, we must construct the output string in some other way.
