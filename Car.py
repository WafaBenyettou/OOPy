class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0  # Initial speed is 0

    def start(self):
        print(f"The {self.make} {self.model} is now running.")

    def accelerate(self, increment):
        self.speed += increment
        print(f"The {self.make} {self.model} is now going at {self.speed} mph.")

    def brake(self, decrement):
        if self.speed - decrement < 0:
            self.speed = 0
        else:
            self.speed -= decrement
        print(f"The {self.make} {self.model} is now going at {self.speed} mph.")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Call methods on the car object
my_car.start()
my_car.accelerate(30)
my_car.brake(10)
