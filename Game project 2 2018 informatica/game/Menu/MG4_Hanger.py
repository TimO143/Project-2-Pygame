from Values import *


class Hanger(py.sprite.Sprite):
    # This class represent the hangers for parking the starschip.

    def __init__(self, img, x, y):
        super().__init__()

        # Load the picture and remove the black background
        self.image = img

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
