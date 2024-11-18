'''
Example 5.

Modify the code from the previous question so that Hello.hi()
uses the Greeting.greet instance method to print Hi.

'''

# Solution

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet('Hi')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

## LS Solution ##
# class Hello:
#     def hi(self):
#         self.greet('Hello')

#     # Make sure you define the class method after
#     # the instance method. If you try it the other
#     # way, the question below will prove a bit
#     # challenging.
#     @classmethod
#     def hi(cls):
#         greeting = Greeting()
#         greeting.greet('Hi')

# The problem now is that you can have a class method and an instance method with the same name in a class.
# However, if you try to use an instance of the class to call the instance method,
# Python will call the class method instead.