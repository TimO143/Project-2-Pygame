from Values import *
from MG4_Values import *

class UFO(py.sprite.Sprite):
    # This class represents a UFO

    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        if color == "Blue":
            self.image = ufo_img_blue
        elif color == "Green":
            self.image = ufo_img_green
        elif color == "Red":
            self.image = ufo_img_red
        elif color == "Yellow":
            self.image = ufo_img_yellow

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 350

    def update(self):
        self.rect.x = self.rect.x - 5

        if self.rect.x < -100:
            self.remove(all_sprites_list)