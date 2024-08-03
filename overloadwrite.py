class Shape:
    def describe(self, color="unknown"):
        return f"This is a shape with color {color}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def describe(self, color="unknown"):
        return f"This is a {color} circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def describe(self, color="unknown"):
        return f"This is a {color} rectangle with width {self.width} and height {self.height}"

# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(10, 20)

# Call the overridden method
print(circle.describe("red"))          # Output: This is a red circle with radius 5
#print(rectangle.describe("blue"))      # Output: This is a blue rectangle with width 10 and height 20

# Call the method with default argument
#print(circle.describe())               # Output: This is a unknown circle with radius 5
#print(rectangle.describe())            # Output: This is a unknown rectangle with width 10 and height 20
