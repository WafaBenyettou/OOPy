"""

Exercise 5: Combining Concepts
Objective: Apply multiple OOP concepts in a more complex scenario.

Define a Person class with attributes name and age.
Create a Driver class that inherits from Person and adds a vehicle attribute.
Implement a method in Driver to display driver and vehicle information.

"""




#solution:
# Define a base class named Person with an initializer (__init__) method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Define a method to display person information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Define a subclass named Driver that inherits from Person
class Driver(Person):
    def __init__(self, name, age, vehicle):
        # Call the initializer of the parent class (Person)
        super().__init__(name, age)
        # Add a new attribute for the driver's vehicle
        self.vehicle = vehicle

    # Override the display_info method to include vehicle information
    def display_info(self):
        super().display_info()
        print("Vehicle Info:")
        self.vehicle.display_info()

# Define a base class named Vehicle with an initializer (__init__) method
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Define a method to display vehicle information
    # This method should be overridden by subclasses
    def display_info(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Define a subclass named Car that inherits from Vehicle
class Car(Vehicle):
    # Override the display_info method
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Create an instance of Car with specific attributes
car = Car("Honda", "Accord", 2018)
# Create an instance of Driver with specific attributes
driver = Driver("Alice", 30, car)
# Call the display_info method on the driver instance
driver.display_info()
