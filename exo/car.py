"""
Exercise 1: Basic Class and Object
Objective: Understand the basics of defining a class and creating objects.

Define a Car class with attributes make, model, and year.
Create a method display_info that prints the car's details.
Instantiate two Car objects and call their display_info method.

"""










# Solution :

# Define a class named Car with an initializer (__init__) method
class Car:
    def __init__(self, make, model, year):
        # Assign the arguments to instance variables
        self.make = make
        self.model = model
        self.year = year

    # Define a method to display car information
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Create an instance of Car with specific attributes
car1 = Car("Toyota", "Corolla", 2020)
# Create another instance of Car with different attributes
car2 = Car("Honda", "Civic", 2019)

# Call the display_info method on car1
car1.display_info()
# Call the display_info method on car2
car2.display_info()

