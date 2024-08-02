class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

dog = Dog()
print(dog.sound())  # Bark
