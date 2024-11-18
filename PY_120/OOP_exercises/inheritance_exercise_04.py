'''
Exercise 4

Print the method resolution order for cars, trucks, boats, 
and vehicles as defined in the previous exercise.

'''

# solution

class Vehicles:

    vehicles_count = 0
    
    def __init__(self):
       Vehicles.vehicles_count += 1
    
    @classmethod
    def vehicles(cls):
        return Vehicles.vehicles_count

class CarSignalMixin:

    def signal_left(self):
        print('Signalling left')

    def signal_right(self):
        print('Signalling right')
    
    def signal_off(self):
        print('Signal is now off')

class Car(CarSignalMixin, Vehicles):
    
    def __init__(self):
        super().__init__()

class Truck(CarSignalMixin, Vehicles):

     def __init__(self):
        super().__init__()

class Boat(Vehicles):

     def __init__(self):
        super().__init__()


print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicles.mro())

## LS Answer ##
# class Vehicle:
#     number_of_vehicles = 0

#     def __init__(self):
#         Vehicle.number_of_vehicles += 1

#     @classmethod
#     def vehicles(cls):
#         return Vehicle.number_of_vehicles

# class SignalMixin:

#     def signal_left(self):
#         print('Signalling left')

#     def signal_right(self):
#         print('Signalling right')

#     def signal_off(self):
#         print('Signal is now off')

# class Car(SignalMixin, Vehicle):

#     def __init__(self):
#         super().__init__()

# class Truck(SignalMixin, Vehicle):

#     def __init__(self):
#         super().__init__()

# class Boat(Vehicle):

#     def __init__(self):
#         super().__init__()

# print(Car.mro())
# print(Truck.mro())
# print(Boat.mro())
# print(Vehicle.mro()) 