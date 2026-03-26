class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r}, {self.z!r})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __len__(self):
        return 3  # always 3 components

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range for Vector")
        
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index out of range for Vector")
        
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __contains__(self, item):
        return item in (self.x, self.y, self.z)
    
    def __bool__(self):
        return self.magnitude() > 0
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    
class Vector(Vector):
    pass
        
class scalar:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Scalar({self.value})"

    def __repr__(self):
        return f"Scalar({self.value!r})"

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.value * other.x, self.value * other.y, self.value * other.z)
        elif isinstance(other, scalar):
            return scalar(self.value * other.value)
        else:
            raise TypeError("Unsupported type for multiplication with Scalar")
        
class scalar(scalar):
    pass

# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
s1 = scalar(2)
print(v1)  # Vector(1, 2, 3)
print(v1 + v2)  # Vector(5, 7, 9)
print(v1.dot(v2))  # 32
print(v1.cross(v2))  # Vector(-3, 6, -3)
print(v1[0])  # 1
v1[0] = 10
print(v1)  # Vector(10, 2, 3)
print(len(v1))  # 3
print(v1 < v2)  # False
print(sorted ([v1, v2], key=lambda v: v.magnitude()))  # [Vector(10, 2, 3), Vector(4, 5, 6)]
print(10 in v1)  # True
print(7 in v1)  # False