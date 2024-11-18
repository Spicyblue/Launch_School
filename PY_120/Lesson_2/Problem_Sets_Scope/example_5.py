'''
Example 5.

Define a Student class that has a class variable named school_name. 
You should initialize the school name to 'Oxford'. 
After defining the class, instantiate an instance of the Student class and 
print the school name using that instance.

'''

# Solution

class Student:
    school_name= 'Oxford'

    def __init__(self, name):
        self.name = name

    def info(self):
        return f'{self.name} , {self.school_name}'

oxford = Student('Oxford')
print(oxford.info())      # Outputs Ochulor , Oxford

oxford.name = 'Okechukwu'
print(oxford.info())      # Outputs Okechukwu , Oxford

## LS Solution ##   
# class Student:
#     school_name = 'Oxford'

# student = Student()
# print(student.__class__.school_name)     # Oxford
# print(student.school_name)               # Oxford
