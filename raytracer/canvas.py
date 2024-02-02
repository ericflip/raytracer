import numpy as np
from PIL import Image
from color import Color

EPS = 0.00000001


class Canvas:
    """
    Canvas representing a 2d array of pixels
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.canvas = np.zeros((width, height, 3), dtype=np.int8)

    def put_pixel(self, c_x: int, c_y: int, color: Color):
        """
        Set the pixel at (c_x, c_y) to a color
        """
        s_x = self.width / 2 + c_x
        s_y = self.height / 2 - c_y

        # clamp i between [0, C_h) and j between [0, C_w)
        i = int(np.clip(s_y, 0, self.height - EPS))
        j = int(np.clip(s_x, 0, self.width - EPS))

        # set pixel color
        self.canvas[i, j] = [color.r, color.g, color.b]

    @property
    def image(self):
        return Image.fromarray(self.canvas, "RGB")
