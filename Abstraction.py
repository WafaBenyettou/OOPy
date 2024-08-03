from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 78.5

circle = Circle()
print(circle.area())  # 78.5


"""
Usage:

Abstract Classes:

Used when you want to create a base class that other classes can inherit from.
Can include some method implementations.

Interfaces:

Used when you want to ensure that different classes adhere to the same set of methods without dictating how they should be implemented.
Cannot include any method implementations.

Methods:

Abstract Classes:

Can have both abstract methods (no implementation) and regular methods (with implementation).

Interfaces:

Can only have abstract methods (no implementation).

Inheritance:

Abstract Classes:

A class can only inherit from one abstract class.

Interfaces:

A class can implement multiple interfaces.
Example: A worker can sign multiple contracts, each listing different tasks to be done.
Example:
Imagine we have a blueprint and a contract for vehicles.

Abstract Class (Vehicle):

Says every vehicle must have a way to start (abstract method) and can provide a default way to check fuel (regular method).
Example: A blueprint that says "every vehicle must have an engine" (abstract method) and "every vehicle should have a fuel gauge" (regular method).
Interface (Drivable):

Says every drivable object must have methods to start and stop, but doesn’t specify how.
Example: A contract that says "every drivable object must be able to start and stop" without details on how to do these.
Car (Class):

Inherits from the abstract class Vehicle and implements the interface Drivable.
Defines how to start the car (following the blueprint) and how to start and stop (following the contract).
"""