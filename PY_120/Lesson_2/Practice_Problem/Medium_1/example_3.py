'''
Example 3.

Let's practice creating an object hierarchy.

Create a class called Animal with a single instance method called speak
that takes a string argument and prints that argument to the terminal.

Now create two other classes that inherit from Animal, one called Cat and one called Dog.
The Cat class should have a meow method that takes no arguments and prints Meow!.
The Dog class should have a bark method that says Woof! Woof! Woof! (dogs never bark just once).
Make use of the Animal class's speak method when implementing the Cat and Dog classes.
Don't invoke the print function in either of the subclasses.

'''

# Solution

class Animal:

    def speak(self, message):
        print(message)

class Cat(Animal):
    
    def meow(self):
        self.speak('Meow')

class Dog(Animal):

    def bark(self):
        self.speak('Woof! Woof! Woof!')

cat_a = Cat()
cat_a.meow()            # Outputs Hello

dog_a = Dog()
dog_a.bark()            # Outputs All good

## LS Solution ##
# class Animal:
#     def speak(self, message):
#         print(message)

# class Cat(Animal):
#     def meow(self):
#         self.speak('Meow!')

# class Dog(Animal):
#     def bark(self):
#         self.speak(('Woof! ' * 3).strip())

# cat = Cat()
# dog = Dog()

# cat.meow()
# dog.bark()