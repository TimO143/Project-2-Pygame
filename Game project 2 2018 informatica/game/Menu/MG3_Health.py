from Values import *

class Heart(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = Full_heart
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y