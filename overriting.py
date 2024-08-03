class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

my_dog = Dog()
print(my_dog.make_sound())  # Output: Bark

"""
Same method name and parameters, but different implementations in subclasses. 
Customizes or extends the behavior inherited from a parent class.

"""