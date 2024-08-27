'''
Example 6.

Modify the Student class from your answer to the previous problem.
The modified class should have a class method that returns the school's name.
Without instantiating any Student objects, print the school's name in two different ways: 
once with the class method, and once by accessing the class variable directly.

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