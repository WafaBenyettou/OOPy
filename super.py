class Parent:
    def show(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        super().show()  # Call the show method from the Parent class
        print("This is the Child class")

# Using the classes
child = Child()
child.show()

"""
The super() function is a way for a child class to call 
methods or access properties from its base class 
(also known as the parent class).
"""