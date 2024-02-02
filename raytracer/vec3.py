class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Vec3"):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vec3"):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float):
        return self * scalar

    def __truediv__(self, scalar: float):
        return self * (1 / scalar)

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def __matmul__(self, other: "Vec3"):
        return self.x * other.x + self.y * other.y + self.z * other.z
