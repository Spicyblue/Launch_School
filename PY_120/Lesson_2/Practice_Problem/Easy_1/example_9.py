'''
Example 9.

There are several variables listed below.
What are the different variable types and how do you know which is which?

Copy Code
excited_dog = 'excited dog'
self.excited_dog = 'excited dog'
self.__class__.excited_dog = 'excited dog'
BigDog.excited_dog = 'excited dog'

'''

# Solution.

# The first variable `excited_dog` is a local variable that references the string object `excited_dog`.
# Hence, it is of the class `Str`
# The second is an instance variable `excited_dog` that belong to a self. instance.
# It also references an string object `excited_dog`. This is often done with a setter method.
# The third is also an class variable that belong to the class of the self. instance. 
# This variable hold the string object `excited_dog`.
# The fourth is a class variable named `excited_dog` of the class `BigDog`.
# This variable hold the string object `excited_dog`.

## LS Solution ##

# Here we have the following variables:

# Variable                      Variable Type
# excited_dog                   Local variable
# self.excited_dog              Instance variable
# self.__class__.excited_dog    Class variable
# BigDog.excited_dog            Class variable

# We can tell which is which by how the variables are prefixed.
# Local variables don't have a prefix, while instance variables are usually prefixed with self.

# Class variables are prefixed with self.__class__.
# when self is an instance of the appropriate class or one of its subclasses.
# You can also use the name of the class as a prefix, e.g., BigDog..

# Though not shown here, there are three other ways to access class variables:
# You can use a cls. prefix inside class methods.
# You can use a type(self.object). prefix when self is an instance of the class or one of its subclasses.
# You can sometimes use a self. prefix when self is an instance of the class or one of its subclasses.
# However, this is not good practice and should be shunned.