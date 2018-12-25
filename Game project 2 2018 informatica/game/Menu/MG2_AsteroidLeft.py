from Values import *
from MG2_Values import *
import random

class AsteroidLeft(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(astr_img, (astr_width, astr_height))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = int(sprite_width / 2)
        self.rect.x = random.randrange(-500, -100)
        self.rect.y = random.randrange(0, display_height - astr_height)
        self.speedx = random.randrange(astr_speed_min, astr_speed_max)
        self.speedy = random.randrange(-astr_speed_side, astr_speed_side)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left > display_width + 10:
            self.rect.x = random.randrange(-150, -40)
            self.rect.y = random.randrange(0, display_width - astr_height)
            self.speedx = random.randrange(astr_speed_min, astr_speed_max)
            self.speedy = random.randrange(-astr_speed_side, astr_speed_side)
