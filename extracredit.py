import numpy as np

from screen import Screen
from mesh import Mesh
from transform import Transform
from camera import OrthoCamera

import numpy as np

def render_triangle():
    width = 500
    height = 500

    # define 3D triangle in world space
    triangle = Mesh()
    triangle.verts = [np.array([-0.5, 0.25,-0.5]), np.array([-0.75, 0.65,-0.85],np.array([-1.0, 0.5,-0.65]))]
    triangle.faces = [[2, 1, 0]]
    triangle.normals = [np.array([0, 1, 0])]

    # define an ortho camera
    camera = OrthoCamera(-1.5, 1.5, -1.5, 1.5, -1, -50)
    camera.transform.set_position(-.5, 0, 0)

    # define a screen and background/foreground colors for silhouette
    bg_color  = (255, 255, 255)
    obj_color = (0, 0, 0)

    screen = Screen(width, height)
    image_buffer = np.full((height, width, 3), bg_color)

    verts_device_coords = [camera.project_point(triangle.transform.apply_to_point(p)) for p in triangle.verts]
    
    #TODO: transform verts_device_coords from device (normalized) to screen (pixel) coordinates 

    #TODO: determine which pixels to check for rendering triangle (bounding box in screen coordinates)

    #TODO: loop over pixels, check which are inside the triangle and set image_buffer at that pixel = obj_color.

    screen.draw(image_buffer)

    screen.show()

if __name__ == '__main__':
    render_triangle()
    