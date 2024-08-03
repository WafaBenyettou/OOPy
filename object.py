class Dog:
    def __init__(self, name, breed):  #the constructor method
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# Creating an instance of the Dog class
my_dog = Dog("Rex", "German Shepherd")

# Now, my_dog is an object (instance) of the Dog class
print(my_dog.name)  # Output: Rex
my_dog.bark()       # Output: Woof!

#an object (instance) is a specific thing made using a class (blueprint), with its own data and actions it can perform.

"""
A constructor:

Is a special method that initializes an object's attributes.
* Takes parameters to set the initial state of the object.
* Is called automatically when a new instance of the class is created.
* Ensures each instance has its unique attributes properly set up from the beginning.
"""