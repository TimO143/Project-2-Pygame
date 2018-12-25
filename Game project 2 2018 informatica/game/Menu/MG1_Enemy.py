from Values import *
from MG1_Bullet import Bullet

class Enemy(py.sprite.Sprite):
    def __init__(self, all_sprites, enemy_bullets, round):
        py.sprite.Sprite.__init__(self)
        self.round = round
        if self.round == 6:
            self.image = alien_round6
            self.shield = 4000
            self.speed_x = 6
            self.speed_y = 5
            self.shoot_delay = 400
        elif self.round == 4:
            self.image = alien_round4
            self.shield = 2500
            self.speed_x = 5
            self.speed_y = 4
            self.shoot_delay = 450
        else:
            self.image = alien_round2
            self.shield = 1000
            self.speed_x = 4
            self.speed_y = 3
            self.shoot_delay = 500

        self.shield_timer = py.time.get_ticks()
        self.shield_active = False
        self.first_shield = False
        self.second_shield = False
        self.third_shield = False
        self.shield_copy = self.shield
        self.image.set_colorkey(BLACK)
        self.all_sprites = all_sprites
        self.enemy_bullets = enemy_bullets
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.y = 100
        self.rect.centerx = display_width / 2
        self.start_moving = False
        self.power = 1
        self.last_shot = py.time.get_ticks()
        self.dirx = 0
        self.diry = 0
        self.hit = False

    def update(self):

        if self.delay and py.time.get_ticks() - self.delay_timer > 4000:
            if self.round == 6:
                self.image = alien_round6
            elif self.round == 4:
                self.image = alien_round4
            else:
                self.image = alien_round2
            self.delay = False
        if not self.delay:

            if self.shield_active and not self.hit:
                self.image = alien_round6_shield
                self.shoot_delay = 1000
            elif not self.shield_active and self.round == 6 and not self.hit:
                self.image = alien_round6
                self.shoot_delay = 400

            if self.power == 3 and self.round == 6:
                self.shoot_delay = 800

            # BEGIN MOVING
            if random.randrange(0,2) == 0 and not self.start_moving:
                self.dirx = 1
                self.diry = 1
                self.start_moving = True
            elif random.randrange(0,2) == 1 and not self.start_moving:
                self.dirx = 2
                self.diry = 2
                self.start_moving = True
            # CHECK IF HIT WALLS X
            if self.rect.left <= 10:
                self.dirx = 2
            if self.rect.right >= display_width - 10:
                self.dirx = 1

            if self.round == 6:
                if self.rect.top <= 5:
                    self.diry = 2
                if self.rect.bottom >= 180:
                    self.diry = 1
            elif self.round == 4:
                if self.rect.top <= 20:
                    self.diry = 2
                if self.rect.bottom >= 170:
                    self.diry = 1
            else:
                if self.rect.top <= 40:
                    self.diry = 2
                if self.rect.bottom >= 160:
                    self.diry = 1



            #MOVE
            if self.dirx == 1:  # Moving left
                self.rect.x -= self.speed_x

            if self.dirx == 2:  # Moving right
                self.rect.x += self.speed_x

            if self.diry == 1:  # Moving up
                self.rect.y -= self.speed_y

            if self.diry == 2:  # Moving down
                self.rect.y += self.speed_y

            # Shoot logic
            if self.shield < self.shield_copy/4:
                self.power = 3
            elif self.shield < self.shield_copy/2:
                self.power = 2

            #Hit timer
            if self.hit and py.time.get_ticks() - self.hit_timer > 800:
                self.hit = False
                if self.round == 6:
                    self.image = alien_round6
                elif self.round == 4:
                    self.image = alien_round4
                else:
                    self.image = alien_round2

            if self.round == 6:
                if self.shield  <= 3000 and not self.first_shield:
                    self.first_shield = True
                    self.spawn_shield()
                if self.shield  <= 2000 and not self.second_shield:
                    self.second_shield = True
                    self.spawn_shield()
                if self.shield  <= 1000 and not self.third_shield:
                    self.third_shield = True
                    self.spawn_shield()

            if self.shield_active == True and py.time.get_ticks() - self.shield_timer > 10000:
                self.shield_active = False
                self.image = alien_round6

            if self.alive():
                self.shoot()


    def draw_shield_bar(self, surf, x, y, pct):
        if pct < 0:
            pct = 0
        bar_width = 100
        bar_height = 10

        fill = (pct / self.shield_copy) * bar_width
        outline_rect = py.Rect(x, y, bar_width, bar_height)
        fill_rect = py.Rect(x, y, fill, bar_height)
        if pct <= self.shield_copy/4:
            py.draw.rect(surf, RED, fill_rect)
        elif pct <= self.shield_copy/2:
            py.draw.rect(surf, YELLOW, fill_rect)
        else:
            py.draw.rect(surf, GREEN, fill_rect)
        py.draw.rect(surf, WHITE, outline_rect, 2)

    def spawn_shield(self):
        self.shield_active = True
        self.image = alien_round6_shield
        self.shield_timer = py.time.get_ticks()

    def boss1_shoot(self):
        if self.power == 3:
            bullet1 = Bullet(self.rect.left, self.rect.centery, self.power, True, 'l', self.round)
            bullet2 = Bullet(self.rect.centerx, self.rect.centery, self.power, True, 'c', self.round)
            bullet3 = Bullet(self.rect.right, self.rect.centery, self.power, True, 'r', self.round)
            self.all_sprites.add(bullet1)
            self.all_sprites.add(bullet2)
            self.all_sprites.add(bullet3)
            self.enemy_bullets.add(bullet1)
            self.enemy_bullets.add(bullet2)
            self.enemy_bullets.add(bullet3)
            shoot_sound.play()
        elif self.power == 2:
            bullet1 = Bullet(self.rect.left, self.rect.centery, self.power, True, 'l', self.round)
            bullet2 = Bullet(self.rect.right, self.rect.centery, self.power, True, 'r', self.round)
            self.all_sprites.add(bullet1)
            self.all_sprites.add(bullet2)
            self.enemy_bullets.add(bullet1)
            self.enemy_bullets.add(bullet2)
            shoot_sound.play()
        else:
            bullet = Bullet(self.rect.centerx, self.rect.bottom, self.power, True, 'c', self.round)
            self.all_sprites.add(bullet)
            self.enemy_bullets.add(bullet)
            shoot_sound.play()

    def boss2_shoot(self):
        if self.power == 3:
            bullet1 = Bullet(self.rect.left, self.rect.centery, self.power, True, 'l', self.round)
            bullet2 = Bullet(self.rect.centerx - 15, self.rect.bottom, self.power, True, 'c', self.round)
            bullet3 = Bullet(self.rect.centerx + 15, self.rect.bottom, self.power, True, 'c', self.round)
            bullet4 = Bullet(self.rect.right, self.rect.centery, self.power, True, 'r', self.round)
            self.all_sprites.add(bullet1)
            self.all_sprites.add(bullet2)
            self.all_sprites.add(bullet3)
            self.all_sprites.add(bullet4)
            self.enemy_bullets.add(bullet1)
            self.enemy_bullets.add(bullet2)
            self.enemy_bullets.add(bullet3)
            self.enemy_bullets.add(bullet4)
            shoot_sound.play()
        elif self.power == 2:
            bullet1 = Bullet(self.rect.left - 35, self.rect.centery, self.power, True, 'll', self.round)
            bullet2 = Bullet(self.rect.left, self.rect.bottom, self.power, True, 'l', self.round)
            bullet3 = Bullet(self.rect.right, self.rect.bottom, self.power, True, 'r', self.round)
            bullet4 = Bullet(self.rect.right + 35, self.rect.centery, self.power, True, 'rr', self.round)
            self.all_sprites.add(bullet1)
            self.all_sprites.add(bullet2)
            self.all_sprites.add(bullet3)
            self.all_sprites.add(bullet4)
            self.enemy_bullets.add(bullet1)
            self.enemy_bullets.add(bullet2)
            self.enemy_bullets.add(bullet3)
            self.enemy_bullets.add(bullet4)
            shoot_sound.play()

        else:
            bullet1 = Bullet(self.rect.centerx - 15, self.rect.bottom, self.power, True, 'c', self.round)
            bullet2 = Bullet(self.rect.centerx + 15, self.rect.bottom, self.power, True, 'c', self.round)
            self.all_sprites.add(bullet1)
            self.all_sprites.add(bullet2)
            self.enemy_bullets.add(bullet1)
            self.enemy_bullets.add(bullet2)
            shoot_sound.play()

    def boss3_shoot(self):
        if self.shield_active:
            bullet1 = Bullet(self.rect.left - 15, self.rect.centery, self.power, True, 'll', self.round, True)
            bullet2 = Bullet(self.rect.left, self.rect.bottom, self.power, True, 'l', self.round, True)
            bullet3 = Bullet(self.rect.centerx, self.rect.bottom, self.power, True, 'c', self.round, True)
            bullet4 = Bullet(self.rect.right, self.rect.bottom, self.power, True, 'r', self.round, True)
            bullet5 = Bullet(self.rect.right + 15, self.rect.centery, self.power, True, 'rr', self.round, True)
            self.all_sprites.add(bullet1)
            self.all_sprites.add(bullet2)
            self.all_sprites.add(bullet3)
            self.all_sprites.add(bullet4)
            self.all_sprites.add(bullet5)
            self.enemy_bullets.add(bullet1)
            self.enemy_bullets.add(bullet2)
            self.enemy_bullets.add(bullet3)
            self.enemy_bullets.add(bullet4)
            self.enemy_bullets.add(bullet5)
            shoot_sound.play()
        elif self.power == 3:
            bullet1 = Bullet(self.rect.left, self.rect.centery, self.power, True, 'l', self.round)
            bullet2 = Bullet(self.rect.centerx, self.rect.centery, self.power, True, 'c', self.round)
            bullet3 = Bullet(self.rect.right, self.rect.centery, self.power, True, 'r', self.round)
            self.all_sprites.add(bullet1)
            self.all_sprites.add(bullet2)
            self.all_sprites.add(bullet3)
            self.enemy_bullets.add(bullet1)
            self.enemy_bullets.add(bullet2)
            self.enemy_bullets.add(bullet3)
            shoot_sound.play()
        else:
            bullet1 = Bullet(self.rect.centerx - 15, self.rect.bottom, self.power, True, 'c', self.round)
            bullet2 = Bullet(self.rect.centerx + 15, self.rect.bottom, self.power, True, 'c', self.round)
            self.all_sprites.add(bullet1)
            self.all_sprites.add(bullet2)
            self.enemy_bullets.add(bullet1)
            self.enemy_bullets.add(bullet2)
            shoot_sound.play()

    def shoot(self):
        now = py.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                if self.round == 6:
                    self.boss3_shoot()
                elif self.round == 4:
                    self.boss2_shoot()
                else:
                    self.boss1_shoot()
            if self.power == 2:
                if self.round == 6:
                    self.boss3_shoot()
                elif self.round == 4:
                    self.boss2_shoot()
                else:
                    self.boss1_shoot()
            if self.power == 3:
                if self.round == 6:
                    self.boss3_shoot()
                elif self.round == 4:
                    self.boss2_shoot()
                else:
                    self.boss1_shoot()

    def enemy_hit(self):
        self.hit = True
        if self.round == 6:
            self.image = alien_round6_hit
        elif self.round == 4:
            self.image = alien_round4_hit
        else:
            self.image = alien_round2_hit
        self.hit_timer = py.time.get_ticks()

    def delay(self):
        self.delay = True
        if self.round == 6:
            self.image = alien_round6_shield
        elif self.round == 4:
            self.image = alien_round4_shield
        else:
            self.image = alien_round2_shield
        self.delay_timer = py.time.get_ticks()

