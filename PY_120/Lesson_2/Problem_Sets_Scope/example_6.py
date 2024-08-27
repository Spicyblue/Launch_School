'''
Example 6.

Modify the Student class from your answer to the previous problem.
The modified class should have an instance variable called name that gets initialized during instantiation.
Create two Student objects with different names but the same school, then print the name and school for both students.

'''

# Solution

class Student:
    name = 'Ochulor'

    def __init__(self, school_name):
        self._school_name = school_name

    def info(self):
        return f'{self.name} , {self._school_name}'

oxford = Student('Oxford')
print(oxford.info())      # Outputs Ochulor , Oxford

oxford.name = 'Okechukwu'
print(oxford.info())      # Outputs Okechukwu , Oxford

## LS Solution ##   
# class Student:
#     school_name = 'Oxford'

#     def __init__(self, name):
#         self.name = name

# student1 = Student('Alice')
# student2 = Student('Bob')

# print(student1.name, student1.__class__.school_name)  # Alice Oxford
# print(student2.name, student2.__class__.school_name)  # Bob Oxford