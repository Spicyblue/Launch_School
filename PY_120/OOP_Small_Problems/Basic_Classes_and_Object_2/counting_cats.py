'''
Counting Cats.

Create a class named Cat that tracks the number of times a new Cat object is instantiated.
The total number of Cat instances should be printed when total is invoked.

Examples
Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3

'''

# Solution

class Cat:
    
    total_cat = 0

    def __init__(self):
        Cat.total_cat += 1

    @classmethod
    def total(cls):
        print(Cat.total_cat)

Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3

## LS Solution ##
# class Cat:
#     number_of_cats = 0

#     def __init__(self):
#         Cat.number_of_cats += 1

#     @classmethod
#     def total(cls):
#         print(cls.number_of_cats)

# Cat.total()         # 0

# kitty1 = Cat()
# Cat.total()         # 1

# kitty2 = Cat()
# Cat.total()         # 2

# print(Cat())        # <__main__.Cat object at 0x104ed7290>
# Cat.total()         # 3