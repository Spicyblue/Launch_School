'''
Example 4.

You are given the following code:

class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing

Write additional code for KrispyKreme such that the print invocations will work as shown above.

'''

# Solution

class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

    def __str__(self):
        if self.filling == None and self.glazing == None:
            return 'Plain'
        elif self.glazing == None and self.filling:
            return self.filling
        elif self.filling == None and self.glazing:
            return f"Plain with {self.glazing}"
        else:
            return f"{self.filling} with {self.glazing}" 

donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing

## LS Solution ##
# class KrispyKreme:
#     def __init__(self, filling, glazing):
#         self.filling = filling
#         self.glazing = glazing

# def __str__(self):
#     if (self.filling is None) and (self.glazing is None):
#         return 'Plain'
#     elif self.filling is None:
#         return f'Plain with {self.glazing}'
#     elif self.glazing is None:
#         return self.filling
#     else:
#         return f'{self.filling} with {self.glazing}'
