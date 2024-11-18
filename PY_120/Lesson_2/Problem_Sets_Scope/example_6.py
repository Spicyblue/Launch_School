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

student1 = Student('Ochulor')
student2 = Student('Dave')
print(student1.info())      # Outputs Ochulor , Oxford
print(student2.info())      # Outputs Dave , Oxford

## LS Solution ##   
# class Student:
#     school_name = 'Oxford'

#     def __init__(self, name):
#         self.name = name

# student1 = Student('Alice')
# student2 = Student('Bob')

# print(student1.name, student1.__class__.school_name)  # Alice Oxford
# print(student2.name, student2.__class__.school_name)  # Bob Oxford
