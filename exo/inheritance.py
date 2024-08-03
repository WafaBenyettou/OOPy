"""

Exercise 2: Inheritance
Objective: Learn how inheritance allows new classes to be based on existing ones.

Create a ElectricCar class that inherits from Car.
Add an attribute battery_size to ElectricCar.
Override the display_info method to include battery size information.

"""













#Solution

# Define a base class named Car with an initializer (__init__) method
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Define a method to display car information
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Define a subclass named ElectricCar that inherits from Car
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        # Call the initializer of the parent class (Car)
        super().__init__(make, model, year)
        # Add a new attribute specific to ElectricCar
        self.battery_size = battery_size

    # Override the display_info method to include battery size information
    def display_info(self):
        # Call the display_info method of the parent class (Car)
        super().display_info()
        print(f"Battery size: {self.battery_size} kWh")

# Create an instance of ElectricCar with specific attributes
electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
# Call the display_info method on the electric_car instance
electric_car.display_info()
