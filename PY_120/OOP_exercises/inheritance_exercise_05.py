'''
Exercise 5

We've provided new Car and Truck classes and some tests below. 
Refactor them to use inheritance for as much behavior as possible. 
The tests shown in the code should still work as shown:

class Car:

    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

    def family_drive(self):
        print('Taking the family for a drive')

class Truck:

    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car

'''

# solution
class Vehicle:
    
    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

class Car(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car

'''
Exercise 5

We've provided new Car and Truck classes and some tests below. 
Refactor them to use inheritance for as much behavior as possible. 
The tests shown in the code should still work as shown:


class Car:

    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

    def family_drive(self):
        print('Taking the family for a drive')

class Truck:

    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car
'''

# solution
class Vehicle:
    
    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

class Car(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car


## LS Answer ##
# class Vehicle:

#     def __init__(self, fuel_capacity, mpg):
#         self.capacity = fuel_capacity
#         self.mpg = mpg

#     def max_range_in_miles(self):
#         return self.capacity * self.mpg

# class Car(Vehicle):

#     def __init__(self, fuel_capacity, mpg):
#         super().__init__(fuel_capacity, mpg)

#     def family_drive(self):
#         print('Taking the family for a drive')

# class Truck(Vehicle):

#     def __init__(self, fuel_capacity, mpg):
#         super().__init__(fuel_capacity, mpg)

#     def hookup_trailer(self):
#         print('Hooking up trailer')

# car = Car(12.5, 25.4)
# truck = Truck(150.0, 6.25)

# print(car.max_range_in_miles())         # 317.5
# print(truck.max_range_in_miles())       # 937.5

# car.family_drive()     # Taking the family for a drive
# truck.hookup_trailer() # Hooking up trailer

# try:
#     truck.family_drive()
# except AttributeError:
#     print('No family_drive method for Truck')
# # No family_drive method for Truck

# try:
#     car.hookup_trailer()
# except AttributeError:
#     print('No hookup_trailer method for Car')
# # No hookup_trailer method for Car