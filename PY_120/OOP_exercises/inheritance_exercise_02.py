'''
Exercise 2

Write the code needed to make the following code work as shown:

print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8
'''

# solution

class Vehicles:

    vehicles_count = 0
    
    def __init__(self):
       Vehicles.vehicles_count += 1
    
    @classmethod
    def vehicles(cls):
        return Vehicles.vehicles_count

class Car(Vehicles):
    
    def __init__(self):
        super().__init__()

class Truck(Vehicles):

     def __init__(self):
        super().__init__()

class Boat(Vehicles):

     def __init__(self):
        super().__init__()

print(Car.vehicles())     # 0

car1 = Car()

print(Car.vehicles())     # 1

car2 = Car()
car3 = Car()
car4 = Car()

print(Car.vehicles())     # 4

truck1 = Truck()
truck2 = Truck()

print(Truck.vehicles())   # 6

boat1 = Boat()
boat2 = Boat()

print(Boat.vehicles())    # 8



## LS Answer ##
# class Vehicle:
#     number_of_vehicles = 0

#     def __init__(self):
#         Vehicle.number_of_vehicles += 1

#     @classmethod
#     def vehicles(cls):
#         return Vehicle.number_of_vehicles

# class Car(Vehicle):

#     def __init__(self):
#         super().__init__()

# class Truck(Vehicle):

#     def __init__(self):
#         super().__init__()

# class Boat(Vehicle):

#     def __init__(self):
#         super().__init__()