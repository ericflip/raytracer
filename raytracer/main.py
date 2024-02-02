from canvas import Canvas
from color import Color
import numpy as np
from PIL import Image

if __name__ == "__main__":
    canvas = Canvas(200, 200)

    color = Color(0, 1, 0)

    for i in range(50):
        for j in range(50):
            canvas.put_pixel(i, j, color)

    canvas.image.save("./test.png")
