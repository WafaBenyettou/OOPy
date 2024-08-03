# Define the classes for different animals
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

# Function that uses duck typing
def make_animal_speak(animal):
    print(animal.speak())

# Create instances of different animals
dog = Dog()
cat = Cat()
duck = Duck()

# Call the function with different animals
make_animal_speak(dog)   # Output: Woof!
make_animal_speak(cat)   # Output: Meow!
make_animal_speak(duck)  # Output: Quack!


"""
If it acts like a duck, then I'll treat it like a duck
"""