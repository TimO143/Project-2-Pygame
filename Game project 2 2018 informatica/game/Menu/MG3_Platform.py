from Values import *

class Platform(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = grass
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Platform_ground(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = ground
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Platform_ice(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = ice
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Platform_ice_ground(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = ice_ground
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
