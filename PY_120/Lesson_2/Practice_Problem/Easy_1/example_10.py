'''
Example 10.

Suppose you have the following class:

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

Explain what the _cats_count variable is,
what it does in this class, and how it works.
Write some code to test your theory.

'''

# Solution.
# The `_cats_count` is a class variable that is scoped within the class `cats`.
# It keeps count of how many `Cat` instances are created.
# When ever a new car instance is created, an augumented addition operation
# increments the value of the `_cats_count` variable by 1. 
# The classmethod then returns the current value referenced by the class variable `_cats_count `

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

cat1 = Cat('male')

print(cat1.cats_count())        # 1
print(Cat.cats_count())         # 1

cat2 = Cat('female')

print(cat1.cats_count())        # 2
print(cat2.cats_count())        # 2
print(Cat.cats_count())         # 2

## LS Solution ##

# The _cats_count variable is here to keep track of how many cat instances have been created.
# We know this since _cats_count gets incremented every time a new Cat object is created.
# Every time we create a Cat object, Python will call Cat.__init__.
# After saving the cat type in an instance variable, __init__ increments _cats_count.
# Note that we need to reference self.__class__._cats_count to access the class variable.
# Finally, the class method named cats_count returns the current value of the _cats_count class variable.
# To test your theory, you can call the cats_count class method each time you create a Cat object, then print it:

# Cat('tabby')
# print(Cat.cats_count())                 # 1

# Cat('russian blue')
# print(Cat.cats_count())                 # 2

# Cat('shorthair')
# print(Cat.cats_count())                 # 3
