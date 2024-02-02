from vec3 import Vec3
import numpy as np

MAX_VALUE = 255
EPS = 0.99999999


class Color(Vec3):
    def __init__(self, x: float, y: float, z: float):
        """
        Params:
            - x, y, z are floats between 0 and 1 and represent rgb respectively
        """

        x = np.clip(x, 0, 1)
        y = np.clip(y, 0, 1)
        z = np.clip(z, 0, 1)

        super().__init__(x, y, z)

    @property
    def r(self):
        return int(np.floor(self.x * (MAX_VALUE + EPS)))

    @property
    def g(self):
        return int(np.floor(self.y * (MAX_VALUE + EPS)))

    @property
    def b(self):
        return int(np.floor(self.z * (MAX_VALUE + EPS)))
