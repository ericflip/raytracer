from vec3 import Vec3
from dataclasses import dataclass
from color import Color


@dataclass
class Sphere:
    center: Vec3
    radius: float
    color: Color
