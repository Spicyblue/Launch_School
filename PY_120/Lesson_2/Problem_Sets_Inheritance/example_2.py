'''
Example 1.

Let's create a few more methods for our Dog class.

class Dog:

    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

    def fetch(self):
        return 'fetching!'

Create a new class called Cat, which can do everything a dog can, except fetch.
Assume the methods do the exact same thing. Hint:
don't copy and paste any methods from Dog into Cat; come up with a class hierarchy instead.

'''

# Solution

class Pets:

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pets):

    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Cat(Pets):

    def speak(self):
        return 'meow!'

    pass

bogi = Dog()

print(bogi.speak())         # Ouputs bark!
print(bogi.sleep())         # Ouputs sleeping!
print(bogi.run())           # Ouputs running!
print(bogi.jump())          # Outputs jumping!
print(bogi.fetch())         # Outputs fetching!

haki = Cat()

print(haki.speak())         # Ouputs meow!
print(haki.sleep())         # Ouputs sleeping!
print(haki.run())           # Ouputs running!
print(haki.jump())          # Outputs jumping!
# print(haki.fetch())         # Outputs AttributeError: 'Cat' object has no attribute 'fetch'

## LS Solution ##

# class Pet:

#     def speak():
#         pass

#     def run(self):
#         return 'running!'

#     def jump(self):
#         return 'jumping!'

#     def sleep(self):
#         return 'sleeping!'

# class Dog(Pet):
#     def speak(self):
#         return 'bark!'

#     def fetch(self):
#         return 'fetching!'

# class Bulldog(Dog):
#    def sleep(self):
#        return "snoring!"

# class Cat(Pet):
#     def speak(self):
#         return 'meow!'

# pet = Pet()
# dave = Dog()
# bud = Bulldog()
# kitty = Cat()

# print(pet.run())              # running!
# print(kitty.run())            # running!
# print(kitty.speak())          # meow!
# try:
#     kitty.fetch()
# except Exception as exception:
#     print(exception.__class__.__name__, exception, "\n")
#     # AttributeError: 'Cat' object has no attribute 'fetch'

# print(dave.speak())           # bark!

# print(bud.run())              # running!
# print(bud.sleep())             # "snoring!"