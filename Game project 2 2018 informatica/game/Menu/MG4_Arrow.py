from Values import *


class Arrow(py.sprite.Sprite):
    # This class represent the arrows for controlling the starschip.

    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # laad de afbeelding
        self.image = Arrowright_img
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #Defineer alle overige Waardes.
        self.direction = False
        self.mousein = False

    def update(self):

        mouse = py.mouse.get_pos()
        click = py.mouse.get_pressed()

        if not self.mousein and click[0] == 1:
            self.mousein = True

            if self.rect.x + arrowupwidth > mouse[0] > self.rect.x and self.rect.y + arrowuphight > mouse[1] > self.rect.y or self.rect.x + arrowuphight > mouse[0] > self.rect.x and self.rect.y + arrowupwidth > mouse[1] > self.rect.y:
                if click[0] == 1 and self.direction == True:
                    self.image = Arrowright_img
                    self.direction = False

                elif click[0] == 1 and self.direction == False:
                    self.image = Arrowup_img
                    self.direction = True
        elif self.mousein and click[0] == 0:
            self.mousein = False

        else:
            self.mousin = False

    def exchange(self):
        return self.direction
