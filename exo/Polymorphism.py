"""
Polymorphism
Objective: Understand polymorphism by creating different subclasses that override a common method.

Create a Motorcycle class that inherits from Vehicle.
Override the display_info method in both Car and Motorcycle classes.
Create a function show_vehicle_info that takes a Vehicle object and calls its display_info method.

"""


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

# Define a subclass named Motorcycle that inherits from Vehicle
class Motorcycle(Vehicle):
    # Override the display_info method
    def display_info(self):
        print(f"Motorcycle: {self.year} {self.make} {self.model}")

# Define a function that takes a Vehicle object and calls its display_info method
def show_vehicle_info(vehicle):
    vehicle.display_info()

# Create an instance of Car with specific attributes
car = Car("Toyota", "Corolla", 2020)
# Create an instance of Motorcycle with specific attributes
motorcycle = Motorcycle("Yamaha", "MT-09", 2021)

# Call the show_vehicle_info function with the car instance
show_vehicle_info(car)
# Call the show_vehicle_info function with the motorcycle instance
show_vehicle_info(motorcycle)
