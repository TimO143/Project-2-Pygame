from Values import *
from MG2_Values import *
import random


class AsteroidUp(py.sprite.Sprite):
        def __init__(self):
            py.sprite.Sprite.__init__(self)
            self.image = py.transform.scale(astr_img, (astr_width, astr_height))
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.radius = int(sprite_width / 2)
            self.rect.x = random.randrange(0, display_width - astr_width)
            self.rect.y = random.randrange(-500, -100)
            self.speedy = random.randrange(astr_speed_min, astr_speed_max)
            self.speedx = random.randrange(-astr_speed_side, astr_speed_side)

        def update(self):
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.top > display_height + 10:
                self.rect.x = random.randrange(0, display_width - astr_width)
                self.rect.y = random.randrange(-150, -40)
                self.speedy = random.randrange(astr_speed_min, astr_speed_max)
                self.speedx = random.randrange(-astr_speed_side, astr_speed_side)
