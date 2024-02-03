from dataclasses import dataclass
from vec3 import Vec3


@dataclass
class Light:
    intensity: float


class AmbientLight(Light):
    pass


@dataclass
class PointLight(Light):
    position: Vec3


@dataclass
class DirectionalLight(Light):
    direction: Vec3
