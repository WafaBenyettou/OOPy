class Animal:
    def make_sound(self,a , b):
        return a*b 

class Dog(Animal):
    def make_sound(self, a ,b ):
        return a+b

my_dog = Dog()
print(my_dog.make_sound())  # Output: Bark

"""
Same method name and parameters, but different implementations in subclasses. 
Customizes or extends the behavior inherited from a parent class.

"""