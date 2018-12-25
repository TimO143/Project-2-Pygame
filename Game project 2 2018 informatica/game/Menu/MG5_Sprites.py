from Values import *
from MG5_Map import collide_hit_rect
vec = py.math.Vector2

class Player(py.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0
        self.lives = 3

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = py.key.get_pressed()


        if keys[py.K_LEFT] or keys[py.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[py.K_RIGHT] or keys[py.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[py.K_UP] or keys[py.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[py.K_DOWN] or keys[py.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = py.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2.0
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2.0
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = py.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2.0
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2.0
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = py.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center

class Wall(py.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Flag(py.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.flags
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.finish_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Mob(py.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.rect.center = self.pos

        # speed vector in de x en y richting
        self.speed_x = 3
        self.speed_y = 0

    """ bewegingen van enemy """
    def update(self):

        # Move left/right
        self.rect.x += self.speed_x

        """ enemy collide rechterkant """
        block_hit_list = py.sprite.spritecollide(self, self.game.walls, False)
        for block in block_hit_list:
            if self.speed_x > 0:
                self.rect.right = block.rect.left
                self.speed_x = -abs(self.speed_x)

        """ enemy collide van linkerkant """
        block_hit_list = py.sprite.spritecollide(self, self.game.walls, False)
        for block in block_hit_list:
            if self.speed_x < 0:
                self.rect.left = block.rect.right
                self.speed_x = abs(self.speed_x)


