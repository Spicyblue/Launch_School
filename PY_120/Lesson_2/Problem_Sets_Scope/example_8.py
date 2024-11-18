'''
Example 8.

Create a Car class that has a class variable named manufacturer and an instance variable named manufacturer.
Initialize these variables to different values.
Add a show_manufacturer method that prints both the class and instance variables.

'''

# Solution

class Car:

    manufacture = 'Telsa'

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def show_manufacturer(self):
        print(f'{self.manufacturer} {Car.manufacture}')

odessy = Car('Odessy')
odessy.show_manufacturer() # Outputs Odessy Telsa

## LS Solution ##   
# class Car:
#     manufacturer = 'Toyota'

#     def __init__(self, manufacturer):
#         self.manufacturer = manufacturer

#     def show_manufacturer(self):
#         print(f'{Car.manufacturer=}')
#         print(f'{self.manufacturer=}')

# car = Car('Honda')
# car.show_manufacturer()
# # Car.manufacturer=Toyota
# # self.manufacturer=Honda
