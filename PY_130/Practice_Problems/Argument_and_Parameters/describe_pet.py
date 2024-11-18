'''
Describe Pet.
Create a function named describe_pet that takes one positional argument animal_type
and one keyword argument name with a default value of an empty string.
The function should print a description of the pet.
The function should not accept more than 1 positional argument.
'''

# Solution

def describe_pet(name,*, breed = ''):
    if breed:
        print(f'{name} is of a breed call {breed}')
    else:
        print(f'{name} is a special pet')

describe_pet('Max', breed = 'Puddle' )  #  Max is of a breed call Puddle
describe_pet('Bruno' )                  #  Bruno is a special pet
describe_pet('Chad', 'Puddle')          # raises an TypeError


## LS Solution ##
# def describe_pet(animal_type, *, name=""):
#     print(f"The animal is a {animal_type} and its name is {name}.")

# print(describe_pet("Hamster", name="Harry"))
# # The animal is a Hamster and its name is Harry.

# describe_pet("Cat", "Dog", name="Pepe")
# # TypeError: describe_pet() takes 1 positional argument but
# # 2 positional arguments (and 1 keyword-only argument) were
# # given