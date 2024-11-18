'''
Exercise 1
Create a Car class that meets these requirements:

- Each Car object should have a model, model year, and color provided at instantiation time.

- You should have an instance variable that keeps track of the current speed. 
    -Initialize it to 0 when you instantiate a new car.

- Create instance methods that let you turn the 
    - engine on, 
    - accelerate, 
    - brake, and
    - turn the engine off. 
    Each method should display an appropriate message.

Create a method that prints a message about the car's current speed.

Write some code to test the methods.
'''

# Solution

class ModelCar:

    def __init__(self, model, year, color, speed = 0):

        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def engine_on(self):
        print('Getter Engine_on in process')
        self.speed += 1
        return f"The {self.model} is Turning on"

    def accelerate(self):
        print('Getter Acceleration in process')
        self.speed += 5

    def brake(self):
        print('Getter Brake in process')
        self.speed -= 3
    
    def engine_off(self):
        print('Getter Engine_off in process')
        self.speed = 0
            
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

## LS Answer ##

# class Car:

#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.speed = 0

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
