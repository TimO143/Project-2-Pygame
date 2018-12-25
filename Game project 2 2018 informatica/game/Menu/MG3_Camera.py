from Values import *

""" camera op player """
class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = py.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

""" oude camera houd geen rekening met level lengte """
def simple_camera(camera, target_rect):
    z, t, _, _ = target_rect
    _, _, w, h = camera
    return py.Rect(-z + HALF_WIDTH, -t + HALF_HEIGHT, w, h)

""" nieuwe camera houd rekening met level lengte """
def complex_camera(camera, target_rect):
    z, t, _, _ = target_rect                                         # x en y van player
    _, _, w, h = camera                                              # width en height van scherm
    z, t, _, _ = -z + HALF_WIDTH, -t + HALF_HEIGHT-80, w, h          # beweging van camera op de helft van scherm

    z = min(0, z)                                   # stop scrolling at the left edge
    z = max(-(camera.width - display_width), z)     # stop scrolling at the right edge
    t = max(-(camera.height - display_height), t)   # stop scrolling at the bottom
    t = min(0, t)                                   # stop scrolling at the top
    return py.Rect(z, t, w, h)
