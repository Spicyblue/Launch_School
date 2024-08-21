'''
Generic Greeting (Part 1).

Create a class named Cat for which calling Cat.generic_greeting prints Hello! I'm a cat!.

Expected output
Hello! I'm a cat!

'''

# Solution

class Cat:
        
    @classmethod
    def generic_greeting(cls):
        print(f"Hello! I'm a cat!")

Cat.generic_greeting()

## LS Solution ##
# class Cat:
#     @classmethod
#     def generic_greeting(cls):
#         print("Hello! I'm a cat!")

# Cat.generic_greeting()        # Hello! I'm a cat!