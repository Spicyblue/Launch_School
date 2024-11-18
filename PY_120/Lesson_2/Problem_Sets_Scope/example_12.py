'''
Example 12.

Consider the following code:

class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())

Answer the following question without running the code.

What will this code output, and why?

'''

# Solution

class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())   

# this code will output `roar` because when we call the make_sound method from the class Cat,
# this returns the cls.sound instance variable of the calling class, which is Lion and this prints `roar``

## LS Solution ##   
# roar
# Since we called make_sound with Lion as the caller, 
# cls must be the Lion class. 
# Therefore, the return value is the value of Lion.sound.