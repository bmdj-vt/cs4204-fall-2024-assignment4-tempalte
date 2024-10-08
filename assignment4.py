import numpy as np

from mesh import Mesh
from transform import Transform
from camera import OrthoCamera

def ortho_camera():
    mesh = Mesh.from_stl("unit_cube.stl")
    mesh.transform.set_rotation(-45, -45, 45)
   
    camera = OrthoCamera(-1.5, 1.5, -1.5, 1.5, -1, -50)
    camera.transform.set_position(0, 0, 5)

    verts = [camera.project_point(p) for p in mesh.verts]

    #test unit cube in model space 
    for vert in verts:
        print(vert)

    #test camera coordinate system transform
    verts = [camera.transform.apply_inverse_to_point(p) for p in mesh.verts]

    for vert in verts:
        print(vert)

    #test unit cube in world space
    verts = [camera.project_point(mesh.transform.apply_to_point(p)) for p in mesh.verts]

    for vert in verts:
        print(vert)


def test_point():
    camera = OrthoCamera(-1.5, 1.5, -1.5, 1.5, -1, -50)
    camera.transform.set_position(0,0,3)

    #Test just camera translation
    assert np.allclose(camera.project_point(np.array([0,-2,1])),np.array([0.0, -1.3333333333333333, 0.9591836734693878]))

    camera = OrthoCamera(-2.5, 2.5, -1.5, 1.5, -1, -50)
    camera.transform.set_rotation(0.0,30.0,0.0)

    #Test just camera rotation
    assert np.allclose(camera.project_point(np.array([0,-2,1])),np.array([(-0.19999999999999998, -1.3333333333333333, 1.0761643021952834)]))

    camera = OrthoCamera(-3.5, 3.5, -2.5, 2.5, -1, -50)
    camera.transform.set_position(0,0,3)
    camera.transform.set_rotation(0.0,30.0,0.0)

    #Test camera translation and rotation
    assert np.allclose(camera.project_point(np.array([0,-2,1])),np.array([(0.28571428571428564, -0.8, 0.9701203752012704)]))

def test_inverse_point():
    camera = OrthoCamera(-1.5, 1.5, -1.5, 1.5, -1, -50)
    camera.transform.set_position(0,0,3)

    #Test just camera translation
    assert np.allclose(camera.inverse_project_point(np.array([0.5,0.5,-1.0])),np.array([0.75, 0.75, -47.00000000000001]))

    camera = OrthoCamera(-2.5, 2.5, -1.5, 1.5, -1, -50)
    camera.transform.set_rotation(0.0,30.0,0.0)

    #Test just camera rotation
    assert np.allclose(camera.inverse_project_point(np.array([0.5,0.5,-1.0])),np.array([-23.91746824526945, 0.75, -43.92627018922194]))

    camera = OrthoCamera(-3.5, 3.5, -2.5, 2.5, -1, -50)
    camera.transform.set_position(0,0,3)
    camera.transform.set_rotation(0.0,30.0,0.0)

    #Test camera translation and rotation
    assert np.allclose(camera.inverse_project_point(np.array([0.5,0.5,-1.0])),np.array([-23.484455543377234, 1.25, -41.17627018922194]))
    
def test_ratio():
    from math import isclose

    camera = OrthoCamera(-1.5, 1.5, -1.5, 1.5, -1, -50)
    assert isclose(camera.ratio(), 1.0)

    camera = OrthoCamera(-3.5, 3.5, -2.5, 2.5, -1, -50)
    assert isclose(camera.ratio(), 1.4)

if __name__ == '__main__':
    ortho_camera()





