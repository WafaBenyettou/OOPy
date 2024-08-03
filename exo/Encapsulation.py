"""
Exercise 3: Encapsulation
Objective: Practice encapsulation by making attributes private and providing getter and setter methods.

Make the battery_size attribute private in the ElectricCar class.
Provide get_battery_size and set_battery_size methods to access and modify the battery size.

"""



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
        # Make the battery_size attribute private
        self.__battery_size = battery_size

    # Define a getter method for battery_size
    def get_battery_size(self):
        return self.__battery_size

    # Define a setter method for battery_size
    def set_battery_size(self, battery_size):
        if battery_size > 0:
            self.__battery_size = battery_size

    # Override the display_info method to include battery size information
    def display_info(self):
        super().display_info()
        print(f"Battery size: {self.__battery_size} kWh")

# Create an instance of ElectricCar with specific attributes
electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
# Call the display_info method on the electric_car instance
electric_car.display_info()
# Set a new value for the battery_size attribute using the setter method
electric_car.set_battery_size(120)
# Get the updated value of the battery_size attribute using the getter method
print(f"Updated battery size: {electric_car.get_battery_size()} kWh")
