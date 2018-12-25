from Values import *
import random

class Mob(py.sprite.Sprite):
    def __init__(self, round=0):
        py.sprite.Sprite.__init__(self)
        self.round = round
        if round == 5:
            self.image_orig = random.choice(stone_meteor_images)
            self.total_health= 100
        elif round == 3:
            self.image_orig = random.choice(stone_meteor_images)
            self.total_health = 100
        else:
            self.image_orig = random.choice(meteor_images)
            self.total_health = 50
        self.health = self.total_health
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.reset_image = self.image
        self.rect = self.image_orig.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.y = random.randrange(-500, -450 )
        self.rect.x = random.randrange(0, display_width - self.rect.width - 100)
        self.speed_y = random.randrange(1, 8)
        self.speed_x = random.randrange(-3,3)
        self.rot =  0
        self.rot_speed = random.randint(-8, 8)
        self.last_update = py.time.get_ticks()
        self.delay_time = False
        self.hit = False

    def rotate(self):
        now = py.time.get_ticks()
        if now - self.last_update > 200:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = py.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):

        if self.delay and py.time.get_ticks() - self.delay_time > 2000:
            self.delay = False
        if not self.delay:
            self.rotate()
            self.rect.y += self.speed_y
            self.rect.x += self.speed_x
            if self.rect.top > display_height + 20 or self.rect.right < -20 or self.rect.left > display_width + 20:
                self.rect.x = random.randrange(0, display_width - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speed_y = random.randrange(1, 8)
                self.speed_x = random.randrange(-3, 3)
                self.health = self.total_health
                self.image_orig = self.reset_image
        if self.health < self.total_health:
            self.mob_hit()

    def mob_hit(self):
        if self.round == 3 or self.round == 5:
            if self.radius == 51:
                self.image_orig = stone_meteor_big2_hit
            if self.radius == 42:
                self.image_orig = stone_meteor_big1_hit
            if self.radius == 18:
                self.image_orig = stone_meteor_med1_hit
            if self.radius == 11:
                self.image_orig = stone_meteor_small1_hit
            if self.radius == 7:
                self.image_orig = stone_meteor_tiny1_hit
    def delay(self):
        self.delay = True
        self.delay_time = py.time.get_ticks()