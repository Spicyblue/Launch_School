'''
Find Person.
Create a function named find_person that accepts any number of keyword arguments
in which each key is someone's name and the value is their associated profession.
The function should check whether any of the key/value pairs has a key of "Antonina" and then,
if the key is found, print a message that shows Antonina's profession.
Otherwise, it should say "Antonina not found". The function should not accept any positional arguments.

'''

# Solution

def find_person(**kwargs):
    person_name = 'Antonina'

    if person_name in kwargs.keys():
        print(kwargs[person_name])
    else:
        print(f"{person_name} not found!")

find_person(Carolina =  'Solution Architect',
            Antonina =  'Backend Engineer',
            Emeka    =  'Solution Architect',
            Gozie    =  'Senior Devs Ops',
            Harry    =  'Front End Engineer',
            Mary     =  'Product Manager',
            Larry    =  'Backend Engineer' ) # Backend Engineer

find_person(Carolina =  'Solution Architect',
            Ontonina =  'Backend Engineer',
            Emeka    =  'Solution Architect',
            Gozie    =  'Senior Devs Ops',
            Harry    =  'Front End Engineer',
            Mary     =  'Product Manager',
            Larry    =  'Backend Engineer' ) # Antonina not found!

## LS Solution ##
# def find_person(**kwargs):
#     if "Antonina" in kwargs:
#         print(f"Antonina's profession is {kwargs['Antonina']}")
#     else:
#         print("Antonina not found")

# find_person(John="Engineer", Antonina="Software Engineer")
# # Antonina's profession is Software Engineer

# find_person(John="Engineer", Ginni="Software Engineer")
# # Antonina not found