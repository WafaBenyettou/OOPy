class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())  # Bark Meow


"""
polymorphism allows different types of objects to be controlled through a common interface or method.
So, you can use the same commands to operate different objects, even though each object may perform 
those commands in its own unique way.
"""

