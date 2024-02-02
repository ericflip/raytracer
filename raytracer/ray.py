from dataclasses import dataclass
from vec3 import Vec3


@dataclass
class Ray:
    origin: Vec3
    direction: Vec3

    def at(self, t: float):
        return self.origin + t * self.direction
