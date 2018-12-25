from Values import *


class Heart(py.sprite.Sprite):
    # This class represent the arrows for controlling the starschip.

    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # laad de afbeelding
        self.image = Full_heart

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def changeimage(self, image):
        self.image = image

