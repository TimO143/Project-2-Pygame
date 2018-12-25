from MG1_Bullet import Bullet
from Values import *

class Player(py.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
        py.sprite.Sprite.__init__(self)
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 23
        self.rect.centerx = display_width / 2
        self.rect.bottom = display_height - 10
        self.speed_x = 0
        self.speed_y = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = py.time.get_ticks()
        self.hidden = False
        self.lives = 3
        self.power = 1
        self.shield_active = False
        self.shield_timer = py.time.get_ticks()
        self.damage = 50
        self.powerup_time = 5000

    def update(self):
        #timeout for powerups
        if self.power >= 2 and py.time.get_ticks() - self.power_time > self.powerup_time:
            self.power = 1
            self.power_time = py.time.get_ticks()
        #unhide if hidden
        if self.hidden and py.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center =(display_width/2, display_height - 10)
        # Activate shield
        if py.time.get_ticks() - self.shield_timer > 3000:
            self.shield_active = False

        self.speed_x = 0
        self.speed_y = 0

        if self.power == 1:
            self.damage = 50

        if not self.hidden:
            keystate = py.key.get_pressed()
            if keystate[py.K_LEFT]:
                self.speed_x = -5
            if keystate[py.K_RIGHT]:
                self.speed_x = 5
            if keystate[py.K_UP]:
                self.speed_y -= 5
            if keystate[py.K_DOWN]:
                self.speed_y +=5
            if keystate[py.K_SPACE]:
                self.shoot()
            self.rect.y += self.speed_y
            self.rect.x += self.speed_x

            if self.rect.right > display_width:
                self.rect.right = display_width
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 150:
                self.rect.top = 150
            if self.rect.bottom > display_height:
                self.rect.bottom = display_height

    def powerup(self, type):
        if type == 'gunx2':
            self.power = 2
            self.damage = 75
            self.power_time = py.time.get_ticks()
        if type == 'gunx3':
            self.power = 3
            self.damage = 100
            self.power_time = py.time.get_ticks()

    def shoot(self):
        now = py.time.get_ticks()
        if now - self.last_shot > self.shoot_delay and not self.hidden:
                self.last_shot = now
                if self.power == 1:
                    bullet = Bullet(self.rect.centerx, self.rect.top, self.power, False)
                    self.all_sprites.add(bullet)
                    self.bullets.add(bullet)
                    shoot_sound.play()
                if self.power == 2:
                    bullet1 = Bullet(self.rect.left, self.rect.centery, self.power, False)
                    bullet2 = Bullet(self.rect.right, self.rect.centery, self.power, False)
                    self.all_sprites.add(bullet1)
                    self.all_sprites.add(bullet2)
                    self.bullets.add(bullet1)
                    self.bullets.add(bullet2)
                    shoot_sound.play()
                if self.power == 3:
                    bullet1 = Bullet(self.rect.left, self.rect.centery, self.power, False)
                    bullet2 = Bullet(self.rect.centerx, self.rect.centery, self.power, False)
                    bullet3 = Bullet(self.rect.right, self.rect.centery, self.power, False)
                    self.all_sprites.add(bullet1)
                    self.all_sprites.add(bullet2)
                    self.all_sprites.add(bullet3)
                    self.bullets.add(bullet1)
                    self.bullets.add(bullet2)
                    self.bullets.add(bullet3)
                    shoot_sound.play()
    def hide(self):
        self.hidden =True
        self.hide_timer = py.time.get_ticks()
        self.rect.center = (display_width/2, display_height + 200)

    def spawn_shield(self):
        self.shield_timer = py.time.get_ticks()
        self.shield_active = True