class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, b):
        return Vector(self.x + b.x, self.y + b.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)
