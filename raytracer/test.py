from canvas import Canvas
from color import Color
from viewport import Viewport
from camera import Camera
from vec3 import Vec3
from sphere import Sphere
from ray import Ray
import math
from tqdm import tqdm


def hit_sphere(ray: Ray, viewport: Viewport, sphere: Sphere):
    """
    Checks if a ray hits a sphere as seen from the viewport.

    Returns: True, [t_1, t_2] if a hit, else False
    """

    a = ray.direction @ ray.direction
    b = 2 * (ray.origin - sphere.center) @ ray.direction
    c = (ray.origin - sphere.center) @ (ray.origin - sphere.center) - sphere.radius**2

    determinant = b**2 - 4 * a * c

    # does not hit sphere (0 intersection points)
    if determinant < 0:
        return False, []

    # hits surface of sphere (1 intersection point)
    if determinant == 0:
        return True, [-b / 2 * a]

    t1 = (-b + determinant**0.5) / (2 * a)
    t2 = (-b - determinant**0.5) / (2 * a)

    return True, [t1, t2]


def trace(ray: Ray, viewport: Viewport, spheres: list[Sphere] = []):
    """
    Calculates the color of the ray
    """
    closest_sphere: Sphere = None
    closest_t = float("inf")

    for sphere in spheres:
        hit, ts = hit_sphere(ray, viewport, sphere)

        if hit:
            for t in ts:
                if viewport.d < t and t < closest_t:
                    closest_t = t
                    closest_sphere = sphere

    if closest_sphere:
        return closest_sphere.color

    return Color(1, 1, 1)  # background color


def convert_canvas_to_viewport(
    c_x: float, c_y: float, canvas: Canvas, viewport: Viewport
):
    """
    Convert canvas coordinates to viewport coordinates
    """
    v_x = viewport.width / canvas.width * c_x
    v_y = viewport.height / canvas.height * c_y

    return Vec3(v_x, v_y, viewport.d)


if __name__ == "__main__":
    viewport = Viewport(width=1, height=1, d=1)
    canvas = Canvas(100, 100)
    camera = Camera(position=Vec3(0, 0, 0))

    # vectors across horizontal and vertical direction of canvas
    canvas_u = Vec3(canvas.width, 0, 0)
    canvas_v = Vec3(0, -canvas.height, 0)

    delta_u = canvas_u / canvas.width
    delta_v = canvas_v / canvas.height

    # calculate top left pixels center
    canvas_upper_left = camera.position - canvas_u / 2 - canvas_v / 2
    pixel00 = canvas_upper_left + delta_u / 2 + delta_v / 2

    # objects in scene
    spheres = [
        Sphere(center=Vec3(0, -1, 3), radius=1, color=Color(1, 0, 0)),
        Sphere(center=Vec3(2, 0, 4), radius=1, color=Color(0, 1, 0)),
        Sphere(center=Vec3(-2, 0, 4), radius=1, color=Color(0, 0, 1)),
    ]

    # loop thr. pixels
    num_pixels = canvas.height * canvas.width
    pbar = tqdm(total=num_pixels)

    for j in range(canvas.height):
        for i in range(canvas.width):
            pixel_loc = pixel00 + i * delta_u + j * delta_v
            viewport_coords = convert_canvas_to_viewport(
                pixel_loc.x, pixel_loc.y, canvas, viewport
            )

            # create ray from camera to viewport
            direction = viewport_coords - camera.position
            ray = Ray(origin=camera.position, direction=direction)

            color = trace(ray, viewport, spheres)
            canvas.put_pixel(pixel_loc.x, pixel_loc.y, color)

            # update progress bar
            pbar.update(1)

    canvas.image.save("./test.png")
