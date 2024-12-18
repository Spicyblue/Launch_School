'''
Nobility.

Now that we have a WalkMixin mix-in, we are given a new challenge. 
Apparently some of our users are nobility, 
and the regular way of walking simply isn't good enough. 
Nobility struts.

We need a new class Noble that shows the title and name when walk is called.
We also require access to name and title; 
they are needed for other purposes that we aren't showing here.

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

'''

# Solution
class WalkMixin:

    def walk(self):
        return f"{self.feature()} {self.gait()} forward"

class Noble(WalkMixin):

    def __init__(self, name, title):
        self.name = name
        self.title = title

    def feature(self):
        return f"{self.title} {self.name}"

    def gait(self):
        return 'struts'

class Person(WalkMixin):

    def __init__(self, name):
        self.name = name

    def feature(self):
        return self.name

    def gait(self):
        return "strolls"

class Cat(WalkMixin):

    def __init__(self, name):
        self.name = name

    def feature(self):
        return self.name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin):

    def __init__(self, name):
        self.name = name
    
    def feature(self):
        return self.name

    def gait(self):
        return "runs"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

mike = Person("Mike")
print(mike.walk())      # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())     # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())     # Expected: "Flash runs forward"

## LS Solution ##

# class WalkMixin:
#     def walk(self):
#         return f"{self} {self.gait()} forward"

# class Person(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"

#     def __str__(self):
#         return self.name

# class Cat(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"

#     def __str__(self):
#         return self.name

# class Cheetah(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "runs"

#     def __str__(self):
#         return self.name

# class Noble(WalkMixin):
#     def __init__(self, name, title):
#         self.name = name
#         self.title = title

#     def __str__(self):
#         return f"{self.title} {self.name}"

#     def gait(self):
#         return "struts"
