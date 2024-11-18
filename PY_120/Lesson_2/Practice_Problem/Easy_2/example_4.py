'''
Example 4.

Suppose we have this code:

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

Without running the above code, what would each snippet do were you to run it?

Snippet 1
hello = Hello()
hello.hi()

Snippet 2
hello = Hello()
hello.bye()

Snippet 3
hello = Hello()
hello.greet()

Snippet 4
hello = Hello()
hello.greet('Goodbye')

Snippet 5
Hello.hi()

'''

# Solution

# Snippet one will print 'Hello'
# Snippet two will print raise an attribute error
# Snippet three will raise an error
# Snipplet four will print out 'Goodbye'
# Snippet five will print raise an error

## LS Solution ##
# Snippet 1 prints Hello.

# Snippet 2 raises an AttributeError since neither Hello nor Greeting define a bye method.

# Snippet 3 raises a TypeError since hello.greet() is missing greet's argument.

# Snippet 4 prints Goodbye.

# Snippet 5 raises a TypeError since Hello doesn't define a class method named hi. 
# It has an instance method named hi, but we're not invoking hi with an instance of Hello, 
# so Python looks for a class method instead.
