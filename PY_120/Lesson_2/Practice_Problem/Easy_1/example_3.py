'''
Example 3.

If we have a Car class and a Truck class and we want to be able to go_fast,
how can we add the ability for them to go_fast using the mix-in SpeedMixin?
How can you check whether your Car or Truck can now go fast?

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car:
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck:
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

'''

# Solution
# Allow the class Car and class Truck to inherit the mixin SpeedMixin,
# create an new instance object of Car and Truck and call the `go_fast`
# instance method on the object

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck(SpeedMixin):
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

car = Car()
car.go_fast()           # outputs I am a super fast Car

truck = Truck()
truck.go_fast()         # outputs I am a super fast Truck


## LS Solution ##

# To give the go_fast method to the Truck and the Car
# we need to add the mix-in to the inheritance list for those classes:

# class SpeedMixin:
#     def go_fast(self):
#         print(f'I am a super fast {self.__class__.__name__}!')

# class Car(SpeedMixin):

#     def go_slow(self):
#         print('I am safe and driving slow.')

# class Truck(SpeedMixin):

#     def go_very_slow(self):
#         print('I am a heavy truck and like going very slow.')

# Now that everything looks right, we can confirm that our Truck and Car can go_fast:

# blue_truck = Truck()
# blue_truck.go_fast() # I am a super fast Truck!

# small_car = Car()
# small_car.go_fast()  # I am a super fast Car!

# As you can see we can now go fast in our Car and Truck.

