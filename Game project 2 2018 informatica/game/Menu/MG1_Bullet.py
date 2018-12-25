from Values import *

class Bullet(py.sprite.Sprite):
    def __init__(self, x, y, power, enemy, dir='c', round=0, shield=False):
        py.sprite.Sprite.__init__(self)
        self.shield = shield
        self.round = round
        self.power = power
        self.enemy = enemy
        self.dir = dir
        # Bullet selection Boss 1
        if not self.enemy:
            if self.power == 1:
                self.image = laser_red
            if self.power == 2:
                self.image = laser_blue
            if self.power == 3:
                self.image = laser_green
        else:
            if self.round == 6:
                # Bullet selection Boss 3
                if self.power == 1:
                    self.image = mg1_boss3_laser1
                if self.power == 2:
                    self.image = mg1_boss3_laser1
                if self.power == 3:
                    if self.dir == "r" or self.dir == 'l':
                        self.image = mg1_boss3_laser3
                    else:
                        self.image = mg1_boss3_laser1
            elif self.round == 4:
                # Bullet selection Boss 2
                if self.power == 1:
                    self.image = mg1_boss2_laser1
                if self.power == 2:
                    if self.dir == "rr" or self.dir == "ll":
                        self.image = mg1_boss2_laser2
                    else:
                        self.image = mg1_boss2_laser1
                if self.power == 3:
                    self.image = mg1_boss2_laser1
            else:
                # Bullet selection Boss 1
                if self.power == 1:
                    self.image = mg1_boss1_laser1
                if self.power == 2:
                    self.image = mg1_boss1_laser2
                if self.power == 3:
                    self.image = mg1_boss1_laser3
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = 10
        self.speed_x = 3

    def boss1_handler(self):
        self.rect.y += self.speed_y
        if self.power == 2:
            if self.dir == 'l':
                self.rect.x -= self.speed_x
            if self.dir == 'r':
                self.rect.x += self.speed_x
        if self.power == 3:
            if self.dir == 'l':
                self.rect.x -= self.speed_x
            if self.dir == 'r':
                self.rect.x += self.speed_x
    def boss2_handler(self):
        self.rect.y += self.speed_y
        if self.power == 3:
            if self.dir == 'l':
                self.rect.x -= self.speed_x
            if self.dir == 'r':
                self.rect.x += self.speed_x
    def boss3_handler(self):

        if self.shield == True:
            self.rect.y += self.speed_y - 2
            if self.dir == 'll' or self.dir == 'l':
                self.rect.x += self.speed_x * 3
            if self.dir == 'rr' or self.dir == 'r':
                self.rect.x -= self.speed_x * 3
            if self.dir == 'c':
                if random.randrange(0, 2) == 0:
                    self.rect.x += self.speed_x
                else:
                    self.rect.x -= self.speed_x
        elif self.power == 3:
            self.rect.y += self.speed_y
            if self.dir == 'l':
                self.rect.x -= self.speed_x
            if self.dir == 'r':
                self.rect.x += self.speed_x
            else:
                if random.randrange(0,2) == 1:
                    self.rect.x += self.speed_x * 3
                else:
                    self.rect.x -= self.speed_x * 3
        elif self.power == 1 or self.power == 2:
            self.rect.y += self.speed_y
            if self.dir == 'c':
                if random.randrange(0,2) == 0:
                    self.rect.x += self.speed_x
                else:
                    self.rect.x -= self.speed_x

    def update(self):
        # player shoot
        if not self.enemy:
            self.rect.y -= self.speed_y
        else:
            if self.round == 6:
                self.boss3_handler()
            elif self.round == 4:
                self.boss2_handler()
            else:
                self.boss1_handler()
        # kill if it moves off screen
        if self.rect.bottom < 0 or self.rect.top > display_height:
            self.kill()
