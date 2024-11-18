'''
Exercise 2
Using decorators, 
- Add getter and setter methods to your Car class so you can view and change the color of your car.
- You should also add getter methods that let you view but not modify the car's model and year. 
- Don't forget to write some tests.

'''

# Solution
class ModelCar:

    def __init__(self, model, year, color, speed = 0):

        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    @property
    def color(self):
        print('Getter Colour in process')
        return f"The current model color is {self._color}"

    @color.setter
    def color(self, color):
        print('Setter Colour in process')

        if not isinstance(color, str):
            return 'Colour must be alphabetic'

        self._color = color

    @property
    def get_model(self):
        print('Getter Model in process')
        return f"The current model is {self.model}"

    @property
    def get_year(self):
        print('Getter Year in process')
        return f"The current model year is {self.year}"

    def engine_on(self):
        print('Getter Engine_on in process')
        self.speed += 1
        return f"The {self.model} is Turning on"

    def engine_off(self):
        print('Getter Engine_off in process')
        self.speed = 0
    
    def accelerate(self):
        print('Getter Acceleration in process')
        self.speed += 5

    def brake(self):
        print('Getter Brake in process')
        self.speed -= 3
            
    def current_speed(self):
        print('Getter Current speed in process')
        return f'The current speed of your {self.color} {self.model} is {self.speed}'

my_car = ModelCar('Telsa', 2027, 'sky blue')

print(my_car.current_speed())
# outputs
# Getter Current speed in process
# The current speed of your sky blue Telsa is 0

my_car.engine_on()      # speed increase by 1
my_car.accelerate()     # speed increase by 5
my_car.accelerate()     # speed increase by 5

print(my_car.current_speed())
# outputs
# Getter Current speed in process
# The current speed of your sky blue Telsa is 11

my_car.brake()          # speed decreases by 3
my_car.brake()          # speed decreases by 3

print(my_car.current_speed())
# outputs
# Getter Current speed in process
# The current speed of your sky blue Telsa is 5

my_car.engine_off()     # speed set to 0

print(my_car.current_speed())
# outputs
# Getter Current speed in process
# The current speed of your sky blue Telsa is 0

print(my_car.get_model)
# outputs
# Getter Model in process
# The current model is Telsa

print(my_car.get_year)
# outputs
# Getter Model in process
# The current model year is 2027

print(my_car.color)
# outputs
# Getter Colour in process
# The current model color is sky blue

my_car.color = 'royal gold'
# Setter Colour in process

print(my_car.color)
# Getter Colour in process
# The current model color is royal gold

## LS Answer ##

# class Car:

#     def __init__(self, model, year, color):
#         self._model = model
#         self._year = year
#         self._color = color
#         self.speed = 0

#     @property
#     def color(self):
#         return self._color

#     @color.setter
#     def color(self, color):
#         self._color = color

#     @property
#     def model(self):
#         return self._model

#     @property
#     def year(self):
#         return self._year

#     def engine_start(self):
#         print('The engine is on!')

#     def engine_off(self):
#         self.speed = 0
#         print("Let's park this baby!")
#         print('The engine is off!')

#     def speed_up(self, number):
#         self.speed += number
#         print(f'You accelerated {number} mph.')

#     def brake(self, number):
#         self.speed -= number
#         print(f'You decelerated {number} mph.')

#     def get_speed(self):
#         print(f'Your speed is {self.speed} mph.')

# lumina = Car('chevy lumina', 1997, 'white')
# lumina.engine_start() # The engine is on!
# lumina.get_speed()    # Your speed is 0 mph.
# lumina.speed_up(20)   # You accelerated 20 mph.
# lumina.get_speed()    # Your speed is 20 mph.
# lumina.speed_up(30)   # You accelerated 30 mph.
# lumina.get_speed()    # Your speed is 50 mph.
# lumina.brake(15)      # You decelerated 15 mph.
# lumina.get_speed()    # Your speed is 35 mph.
# lumina.brake(30)      # You decelerated 30 mph.
# lumina.get_speed()    # Your speed is 5 mph.
# lumina.engine_off()   # Let's park this baby!
#                       # The engine is off
# lumina.get_speed()    # Your speed is 0 mph.

# print(f'My car is {lumina.color}.')
# My car is white.

# print(f"My car's model is a {lumina.model}.")
# My car's model is a chevy lumina.

# print(f"My car's year is {lumina.year}.")
# My car's year is 1997.

# lumina.color = 'brown'
# print(f'My car is now {lumina.color}.')
# My car is now brown.

# lumina.year = 2023
# AttributeError: property 'year' of 'Car' object
# has no setter