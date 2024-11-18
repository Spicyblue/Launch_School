'''
Generic Greeting (Part 1).

Create a class named Cat for which calling Cat.generic_greeting prints Hello! I'm a cat!.

Expected output
Hello! I'm a cat!

Further Exploration
Create an instance of the class named kitty and use the ibject to call the call method.
What happens if you run type(kitty).generic_greeting()? Can you explain this result?

'''

# Solution

class Cat:
        
    @classmethod
    def generic_greeting(cls):
        print(f"Hello! I'm a cat!")

Cat.generic_greeting()      # Ouputs Hello! I'm a cat!

kitty = Cat()       
kitty.generic_greeting()    # Ouputs Hello! I'm a cat!

print(type(kitty).generic_greeting())

#Can you explain this result

# Looking at the print(type(kitty).generic_greeting() statement, type(kitty) 
# returns the class of the kitty instance, which is Cat.
# So type(kitty).generic_greeting() is effectively the same as Cat.generic_greeting(). 
# This calls the generic_greeting method, which outputs "Hello! I'm a cat!".
# However, the generic_greeting() method does not return any value; 
# it only prints to the console. 
# Since the print function is used, it tries to print the return value of calling the generic_greeting method,
# which is None because the class method doesn't explicitly return anything.

## LS Solution ##
# class Cat:
#     @classmethod
#     def generic_greeting(cls):
#         print("Hello! I'm a cat!")

# Cat.generic_greeting()        # Hello! I'm a cat!
