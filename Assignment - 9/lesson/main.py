from abc import ABC, abstractmethod
import math

class Shape(ABC):
   @abstractmethod
   def perimeter(self):
       pass

   @abstractmethod
   def area(self):
       pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Circle(Shape):
   def __init__(self, radius):
       self.radius = radius

   def perimeter(self):
       return 2 * math.pi * self.radius

   def area(self):
       return math.pi * self.radius ** 2

if __name__ == '__main__':
    rec = Rectangle(4, 5)
    print(rec.perimeter())
    print(rec.area())

    cir = Circle(5)
    print(cir.perimeter())
    print(cir.area())
