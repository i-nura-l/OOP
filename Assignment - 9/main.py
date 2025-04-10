from abc import ABC, abstractmethod
import math
import random

class Shape3D(ABC):
   @abstractmethod
   def surface_area(self):
       pass

   @abstractmethod
   def volume(self):
       pass

class Sphere(Shape3D):

    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height


class Cube(Shape3D):
    def __init__(self, length):
        self.length = length

    def surface_area(self):
        return 6 * self.length ** 2

    def volume(self):
        return self.length ** 3

if __name__ == '__main__':

    print("Check")
    sp = Sphere(4)
    print(sp.surface_area())
    print(sp.volume())

    cy = Cylinder(4, 5)
    print(cy.surface_area())
    print(cy.volume())

    cube = Cube(5)
    print(cube.surface_area())
    print(cube.volume())

    print()


    shapes = []

    for _ in range(10):
        shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])

        if shape_type == 'Sphere':
            radius = random.randint(1, 10)
            shape = Sphere(radius)
        elif shape_type == 'Cylinder':
            radius = random.randint(1, 10)
            height = random.randint(5, 20)
            shape = Cylinder(radius, height)
        elif shape_type == 'Cube':
            length = random.randint(1, 10)
            shape = Cube(length)

        shapes.append((shape_type, shape))

    for name, shape in shapes:
        print(f"Shape: {name}")
        print(f"Surface Area: {shape.surface_area():.2f}")
        print(f"Volume: {shape.volume():.2f}")
        print("-" * 20)

