from Values import *

""" spritesheet voor player """
class Spritesheet:
    def __init__(self, filename):   # filename wordt wel gebruikt maar niet hier
        self.spritesheet = spritesheet1

    def get_image(self, x, y, width, height):
        image = py.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))         # pak uit spritesheet een klein deel
        image = py.transform.scale(image, (width-2, height -1))
        return image

""" laden van spritesheets """
class Spritesheet_enemy:
    def __init__(self, filename):   # filename wordt wel gebruikt maar niet hier
        self.spritesheet_enemy = spritesheet_enemy

    def get_image(self, x, y, width, height):
        image = py.Surface((width, height))
        image.blit(self.spritesheet_enemy, (0, 0), (x, y, width, height))         # pak uit spritesheet een klein deel
        image = py.transform.scale(image, (width // 2, height // 2-10))
        return image
