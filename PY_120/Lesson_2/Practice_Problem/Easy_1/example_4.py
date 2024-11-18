'''
Example 4.

In the previous question, we had a mix-in called SpeedMixin that contained a go_fast method. 
We add this mix-in to the Car class as shown below:

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

small_car = Car()
print(small_car.go_fast())
# I am a super fast Car!

When we called small_car.go_fast, you may have noticed that the output includes the vehicle type.
How is this done?

'''

# Solution
# This is so because the inherited mixin method `go_fast`
# uses the magic variable __class__.__name__ on the instance self. 
# This magic variable returns a string of the class name of the calling object `small_car,
# which in this case is `Car``.


## LS Solution ##

# We use self.__class__.__name__ in the method. It works like so:
# self refers to the object referenced by small_car. In this case, that's a Car object.
# self.__class__ returns a reference to the Car class, which is an object of type class.
# Finally, self.__class__.__name__ returns the name of the Car class as a string: 'Car'.

