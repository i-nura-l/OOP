# 3D Shape Modeling with Abstraction in Python

## Objective
This project demonstrates the use of abstraction and polymorphism in Python by modeling various 3D shapes. It uses an abstract base class to define a common interface for all shapes, and then implements concrete shape classes that follow this interface.

---

## Concepts Used
- **Abstraction**: Using Python's `abc` module to define abstract methods for surface area and volume.
- **Polymorphism**: Treating different shape objects (Sphere, Cylinder, Cube) through the same abstract interface.
- **Inheritance**: Shape classes inherit from a common abstract base class.
- **Randomization**: Randomly generate shape types and dimensions using the `random` module.

---

## Shape Classes

### Shape3D (Abstract Base Class)
- Defines the interface for all 3D shapes.
- Contains two abstract methods:
  - `surface_area()`
  - `volume()`

### Sphere
- Attributes: `radius`
- Surface Area: `4 * π * r²`
- Volume: `(4/3) * π * r³`

### Cylinder
- Attributes: `radius`, `height`
- Surface Area: `2 * π * r * (r + h)`
- Volume: `π * r² * h`

### Cube
- Attributes: `length`
- Surface Area: `6 * a²`
- Volume: `a³`

--- 

## Program Behavior
- Creates a list of 10 random 3D shape objects.
- Shape type is randomly chosen: Sphere, Cylinder, or Cube.
- Dimensions (radius, height, or side length) are randomly generated.
- For each shape, the program outputs:
  - Shape type
  - Surface area
  - Volume

---

## How to Run
1. Ensure you have Python installed.
2. Run the script:

```bash
python main.py
```
---

## Example Outputs

Shape: Sphere
Surface Area: 201.06
Volume: 268.08
------------------------------
Shape: Cylinder
Surface Area: 376.99
Volume: 502.65
------------------------------
...
