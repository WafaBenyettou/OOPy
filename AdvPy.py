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

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        return "Drawing a circle"

circle = Circle()
print(circle.draw())  # Drawing a circle
