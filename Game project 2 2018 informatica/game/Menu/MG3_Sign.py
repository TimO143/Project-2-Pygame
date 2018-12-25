from Values import *

class Sign_hard(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = board_hard
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Sign_easy(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = board_easy
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Egg(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = easter_egg
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Uitleg(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = uitleg
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Springveer(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = spring
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Springveer_left(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = spring_left
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Springveer_right(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = spring_right
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Springveer_down(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = spring_down
        self.image.set_colorkey(BLACK)              # maakt transparant.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
