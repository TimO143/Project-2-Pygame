from Values import *


class Enemy(py.sprite.Sprite):
    def __init__(self, x, y, game):
        py.sprite.Sprite.__init__(self)
        self.game = game
        self.image = game.spritesheet_enemy.get_image(395, 620, 107, 148)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # speed vector in de x en y richting
        self.speed_x = 4
        self.speed_y = 0

    """ bewegingen van enemy """
    def update(self):

        # Move left/right
        self.rect.x += self.speed_x

        """ enemy collide rechterkant """
        block_hit_list = py.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:
            if self.speed_x > 0:
                self.rect.right = block.rect.left
                self.speed_x = -abs(self.speed_x)

        """ enemy collide van linkerkant """
        block_hit_list = py.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:
            if self.speed_x < 0:
                self.rect.left = block.rect.right
                self.speed_x = abs(self.speed_x)

class Enemy_up(py.sprite.Sprite):
    def __init__(self, x, y, game):
        py.sprite.Sprite.__init__(self)
        self.game = game
        self.image = game.spritesheet_enemy.get_image(395, 620, 107, 148)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # speed vector in de x en y richting
        self.speed_x = 0
        self.speed_y = 3

    """ bewegingen van enemy """
    def update(self):

        # Move up/down
        self.rect.y += self.speed_y

        """ enemy collide bovenkant """
        block_hit_list = py.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:
            if self.speed_y > 0:
                self.rect.bottom = block.rect.top
                self.speed_y = -abs(self.speed_y)

        """ enemy collide van onderkant """
        block_hit_list = py.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:
            if self.speed_y < 0:
                self.rect.top = block.rect.bottom
                self.speed_y = abs(self.speed_y)
