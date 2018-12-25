from Values import *
from MG2_Values import *


class Player(py.sprite.Sprite):
        def __init__(self):
            py.sprite.Sprite.__init__(self)
            self.image = py.transform.scale(pleft_img, (sprite_width, sprite_height))
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.radius = int(sprite_width/3.5)
            self.rect.centerx = display_width / 2
            self.rect.bottom = display_height / 2
            self.speedx = 0
            self.speedy = 0
            self.lives = 3
            self.hidden = False
            self.hide_timer = py.time.get_ticks()

        def update(self):
         #   self.rect.x += self.speedx
         #   self.rect.y += self.speedy
            self.org_image = self.image
            if self.hidden and py.time.get_ticks() - self.hide_timer > 2000:
                self.hidden = False
            elif self.hidden and py.time.get_ticks() - self.hide_timer < 1000:
                self.image = hit_img
                self.image.set_colorkey(WHITE)
            elif self.hidden and 1000 <= py.time.get_ticks() - self.hide_timer <= 1020:
                self.rect.center = (display_width / 2 - sprite_width / 2, display_height / 2 - sprite_height / 2)
                self.image = py.transform.scale(pleft_img, (sprite_width, sprite_height))
                self.image.set_colorkey(WHITE)
            keypress = py.key.get_pressed()
            if keypress[py.K_LEFT]:
                self.rect.x += -sprite_speed
                if not self.hidden:
                    self.image = py.transform.scale(pleft_img, (sprite_width, sprite_height))
                    self.image.set_colorkey(WHITE)
            if keypress[py.K_RIGHT]:
                self.rect.x += sprite_speed
                if not self.hidden:
                    self.image = py.transform.scale(pright_img, (sprite_width, sprite_height))
                    self.image.set_colorkey(WHITE)
            if keypress[py.K_DOWN]:
                self.rect.y += sprite_speed
            if keypress [py.K_UP]:
                self.rect.y += -sprite_speed

        # boundaries
            if self.rect.x <= 0:
                self.rect.x = 0
            elif self.rect.x >= display_width - 93:
                self.rect.x = display_width - 93
            if self.rect.y <= 0:
                self.rect.y = 0
            elif self.rect.y >= display_height - 82:
                self.rect.y = display_height - 82

        def hide(self):
            self.hidden = True
            self.hide_timer = py.time.get_ticks()



