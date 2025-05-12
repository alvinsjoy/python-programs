# Method overriding
class Shape:
    def area(self):
        return "Area calculation not implemented"
    
    def description(self):
        return "This is a generic shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):  # Override the area method
        return self.width * self.height
    
    def description(self):
        return f"Rectangle with width {self.width} and height {self.height}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):  # Override the area method
        return 3.14159 * self.radius * self.radius
    
    def description(self):
        return f"Circle with radius {self.radius}"
class Square(Shape):
    def __init__(self, edge):
        self.edge = edge
    def description(self):
        return f"Square with edge {self.edge}"
    def area(self):
        return self.edge ** 2

# Demonstrate polymorphism through method overriding
print("\nShape demonstrations:")
shape1 = Rectangle(5, 10)
shape2 = Circle(7)
shape3 = Square(4)

print(shape1.description())
print(shape2.description())
print(shape3.description())

print(f"Area of rectangle: {shape1.area()}")
print(f"Area of circle: {shape2.area()}")
print(f"Area of square: {shape3.area()}")
