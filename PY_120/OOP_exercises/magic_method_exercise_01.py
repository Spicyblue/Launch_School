'''
Exercise 1
Create a Car class that makes the following code work as indicated:

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

'''

# Solution

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color


    def __str__(self):
        model = self._model
        year = self._year
        color = self._color
        return f'{color.title()} {year} {model}'
    
    def __repr__(self):
        model = repr(self._model)
        year = repr(self._year)
        color = repr(self._color)
        return f'Car({model}, {year}, {color})'

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

## LS Answer ##

# class Car:

#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color

#     def __str__(self):
#         return f'{self.color.title()} {self.year} {self.model}'

#     def __repr__(self):
#         color = repr(self.color)
#         year = repr(self.year)
#         model = repr(self.model)
#         return f'Car({model}, {year}, {color})'