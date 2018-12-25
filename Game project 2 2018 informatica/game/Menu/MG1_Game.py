from MG1_Mob import Mob
from MG1_Player import Player
from MG1_Explosion import Explosion
from MG1_Powerup import Powerup
from Functions import Functions
from MG1_Enemy import  Enemy
from Values import  *


class Game:

    def __init__(self):
        self.bg_y = 0
        self.func = Functions()
        self.load_data()
        self.text_time = 2000
        self.round1_text = False
        self.round2_text = False
        self.round2_text_timer = py.time.get_ticks()
        self.round3_text_timer = py.time.get_ticks()
        self.round4_text_timer = py.time.get_ticks()
        self.round5_text_timer = py.time.get_ticks()
        self.round6_text_timer = py.time.get_ticks()

    def load_data(self):

        with open(path.join(high_dir, mg1_highscore), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def draw_lives(self, surf, x, y, lives, img):
        for i in range (3):
            img_rect = Empty_heart.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surf.blit(Empty_heart, img_rect)
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surf.blit(img, img_rect)

    def draw_shield_bar(self, surf, x, y, pct):
        if pct < 0:
            pct = 0
        bar_width = 100
        bar_height = 10
        fill = (pct / 100) * bar_width
        outline_rect = py.Rect(x, y, bar_width, bar_height)
        fill_rect = py.Rect(x, y, fill, bar_height)
        if pct <= 20:
            py.draw.rect(surf, RED, fill_rect)
        elif pct <= 50:
            py.draw.rect(surf, YELLOW, fill_rect)
        else:
            py.draw.rect(surf, GREEN, fill_rect)
        py.draw.rect(surf, WHITE, outline_rect, 2)

    def game_over(self, val):
        running = True

        while running:

            if val == 'pause':
                    # DRAW
                    text_obj, text_surf = self.func.text_objects("Paused", large_text, WHITE)
                    text_surf.center = (display_width / 2, display_height / 2 - 150)
                    display_screen.blit(text_obj, text_surf)

                    # DRAW BUTTONS
                    resume_button = self.func.button("Resume", WHITE, display_width / 2 - main_menu_buttonx / 2,
                                                     display_height / 2 - 75,
                                                     main_menu_buttonx, main_menu_buttony, IACOLOR, ACOLOR)
                    main_menu_button = self.func.button("Main Menu", WHITE, display_width / 2 - main_menu_buttonx / 2,
                                                        display_height / 2,
                                                        main_menu_buttonx, main_menu_buttony, IACOLOR, ACOLOR)
                    for event in py.event.get():
                        if event.type == py.QUIT:
                            py.quit()
                            quit()
                        if event.type == py.KEYDOWN:
                            if event.key == py.K_ESCAPE:
                                self.state = 'run'
                                running = False
                        if event.type == py.MOUSEBUTTONDOWN:
                            mouse_pos = py.mouse.get_pos()
                            if resume_button.collidepoint(mouse_pos):
                                self.state = 'run'
                                running = False
                            if main_menu_button.collidepoint(mouse_pos):
                                return 'main'

                    py.display.update()
            if val == 'game_over':

                rel_y = self.bg_y % bg.get_rect().height
                display_screen.blit(bg, (0, rel_y - bg.get_rect().height))
                if rel_y < display_height:
                    display_screen.blit(bg, (0, rel_y))
                self.bg_y += 0.1

                #buttons
                main_menu_button = self.func.button("Main Menu", WHITE, display_width/2 - main_menu_buttonx/2, 325,
                                                    main_menu_buttonx, main_menu_buttony, IACOLOR, ACOLOR)
                restart_button = self.func.button("Restart", WHITE, display_width/2 - main_menu_buttonx/2, 400, main_menu_buttonx,
                                 main_menu_buttony, IACOLOR, ACOLOR)

                #text

                text_surface, text_rect = self.func.text_objects("GAME OVER", game_over_text, WHITE)
                text_rect.center = (display_width/2, 100)
                display_screen.blit(text_surface, text_rect)

                text_surface, text_rect = self.func.text_objects("SCORE {}".format(str(self.score)), medium_text, WHITE)
                text_rect.center = (display_width / 2, 220)
                display_screen.blit(text_surface, text_rect)

                if self.score > self.highscore or self.score == self.highscore:
                    self.highscore = self.score
                    text_surf, text_rect = self.func.text_objects("NEW HIGHSCORE",
                                                                  small_text, RED)
                    text_rect.center = (display_width / 2, 260)
                    display_screen.blit(text_surf, text_rect)
                    with open(path.join(high_dir, mg1_highscore), 'w') as f:
                        f.write(str(self.score))

                else:
                    text_surf, text_rect = self.func.text_objects("HIGHSCORE {}".format(str(self.highscore)),
                                                                   small_text, WHITE)
                    text_rect.center = (display_width / 2, 260)
                    display_screen.blit(text_surf, text_rect)


                for event in py.event.get():
                    if event.type == py.QUIT:
                        py.quit()
                        quit()
                    if event.type == py.MOUSEBUTTONDOWN:
                        mouse_pos = py.mouse.get_pos()
                        if main_menu_button.collidepoint(mouse_pos):
                            return 'main'
                        if restart_button.collidepoint(mouse_pos):
                            return 'instr'


            py.display.update()

    def setup(self):
        self.all_sprites = py.sprite.Group()
        self.bullets = py.sprite.Group()
        self.enemy_bullets = py.sprite.Group()
        self.powerups = py.sprite.Group()
        self.player = Player(self.all_sprites, self.bullets)
        self.all_sprites.add(self.player)
        self.mobs = py.sprite.Group()
        self.round1_active = False
        self.round2_active = False
        self.round3_active = False
        self.round4_active = False
        self.round5_active = False
        self.round6_active = False
        self.boss1_killed = False
        self.boss2_killed = False
        self.boss3_killed = False
        self.round2_finished = False
        self.round4_finished = False
        self.score = 0
        self.ret = ""

    def spawner(self, round):
        print(round)
        if round == 1:
            for i in range(15):
                mob = Mob(round)
                mob.delay()
                self.all_sprites.add(mob)
                self.mobs.add(mob)
        elif round == 3:
            for i in range(20):
                mob = Mob(round)
                mob.delay()
                self.all_sprites.add(mob)
                self.mobs.add(mob)
        elif round == 5:
            for i in range(25):
                mob = Mob(round)
                mob.delay()
                self.all_sprites.add(mob)
                self.mobs.add(mob)

        return round

    def loop(self):
        py.display.set_caption("Meteor Strike")
        self.setup()
        self.state = 'run'
        # Game loop
        running = True
        self.round_timer = py.time.get_ticks()
        while running:
            # keep loop running at the right speed

            if self.state == 'run':
                # Process input (events)
                for event in py.event.get():
                    # check for closing window
                    if event.type == py.QUIT:
                        py.quit()
                        quit()
                    elif event.type == py.KEYDOWN:
                        if event.key == py.K_SPACE:
                            self.player.shoot()
                        if event.key == py.K_ESCAPE:
                            self.state = 'pause'
                # Update
                self.all_sprites.update()

                # Score checker

                #ROUND 1
                if self.round1_active == False and self.score == 0:
                    self.round1_text = True
                    if py.time.get_ticks() - self.round_timer > 2000:
                        self.current_round = self.spawner(1)
                        self.round1_active = True
                        self.round1_text = False

                # ROUND 2 BOSS FIGHT
                if self.round2_active == False and self.score >= 750:
                    self.round2_active = True
                    self.round2_text_timer = py.time.get_ticks()
                    # Kill all mobs
                    for mob in self.mobs:
                        expl_sound.play()
                        expl = Explosion(mob.rect.center, 'large')
                        self.all_sprites.add(expl)
                        mob.kill()
                    #Spawn Enemy
                    self.ufo = Enemy(self.all_sprites, self.enemy_bullets, 2)
                    self.ufo.delay()
                    self.all_sprites.add(self.ufo)

                # ROUND 3
                if self.boss1_killed and self.round3_active == False:
                    self.round2_finished = True
                    self.round3_text_timer = py.time.get_ticks()
                    self.round3_active = True
                    self.current_round = self.spawner(3)

                # ROUND 4 BOSS FIGHT
                if self.round4_active == False and self.score >= 1500:
                    self.round4_active = True
                    self.round4_text_timer = py.time.get_ticks()
                    # Kill all mobs
                    for mob in self.mobs:
                        expl_sound.play()
                        expl = Explosion(mob.rect.center, 'large')
                        self.all_sprites.add(expl)
                        mob.kill()
                    # Spawn Enemy
                    self.ufo = Enemy(self.all_sprites, self.enemy_bullets, 4)
                    self.ufo.delay()
                    self.all_sprites.add(self.ufo)

                # ROUND 5
                if self.boss2_killed and self.round5_active == False:
                    self.round4_finished = True
                    self.round5_text_timer = py.time.get_ticks()
                    self.round5_active = True
                    self.current_round = self.spawner(5)

                # FINAL BOSS
                if self.round6_active == False and self.score >= 2250:
                    self.round6_active = True
                    self.round6_text_timer = py.time.get_ticks()
                    # Kill all mobs
                    for mob in self.mobs:
                        expl_sound.play()
                        expl = Explosion(mob.rect.center, 'large')
                        self.all_sprites.add(expl)
                        mob.kill()
                    # Spawn Enemy
                    self.ufo = Enemy(self.all_sprites, self.enemy_bullets, 6)
                    self.ufo.delay()
                    self.all_sprites.add(self.ufo)

                # Check if player gets hit by the enemy boss bullets
                hits = py.sprite.spritecollide(self.player, self.enemy_bullets, True, py.sprite.collide_circle)
                for hit in hits:
                    if not self.player.shield_active:
                        self.player.shield -= 40
                    expl = Explosion(hit.rect.center, 'small')
                    expl_sound.play()
                    self.all_sprites.add(expl)

                    if self.player.shield <= 0:
                        expl = Explosion(self.player.rect.center, 'mega')
                        expl_sound.play()
                        self.all_sprites.add(expl)
                        self.player.hide()
                        self.player.spawn_shield()
                        self.player.power = 1
                        self.player.lives -= 1
                        if self.player.lives<= 0:
                            self.player.shield = 0
                        else:
                            self.player.shield = 100


                # Check if enemy ufo gets hit by player bullets

                try:
                    if self.ufo.alive():
                        hits = py.sprite.spritecollide(self.ufo, self.bullets, True, py.sprite.collide_circle)

                        for hit in hits:
                            if not self.ufo.delay:

                                if not self.ufo.shield_active:
                                    if self.player.power == 1:
                                        self.ufo.shield -= 20
                                    elif self.player.power == 2:
                                        self.ufo.shield -= 20
                                    elif self.player.power == 3:
                                        self.ufo.shield -= 20

                                    self.ufo.enemy_hit()

                                if self.ufo.shield <= 0:
                                    if self.ufo.round == 6:
                                        self.boss3_killed = True
                                    elif self.ufo.round == 4:
                                        self.boss2_killed = True
                                    else:
                                        self.boss1_killed = True

                                    expl = Explosion(self.ufo.rect.center, 'mega')
                                    expl_sound.play()
                                    self.all_sprites.add(expl)
                                    self.ufo.kill()

                                if random.random() > 0.9:
                                    pow = Powerup(hit.rect.center, self.score, self.player.lives)
                                    self.all_sprites.add(pow)
                                    self.powerups.add(pow)
                except:
                    pass
                # check if bullet hits a mob
                hits = py.sprite.groupcollide(self.mobs, self.bullets, False, True)
                for hit in hits:
                    # Add score
                    if hit.radius == 51 or hit.radius == 42:
                        self.score += 5
                    if hit.radius == 18:
                        self.score += 7
                    if hit.radius == 11:
                        self.score += 10
                    if hit.radius == 7:
                        self.score += 15


                    # Drop Powerups
                    if random.random() > 0.9:
                        pow = Powerup(hit.rect.center, self.score, self.player.lives)
                        self.all_sprites.add(pow)
                        self.powerups.add(pow)

                    # Reduce mob life
                    hit.health-= self.player.damage

                    if hit.health <= 0:
                        expl_sound.play()
                        expl = Explosion(hit.rect.center, 'large')
                        self.all_sprites.add(expl)
                        hit.kill()
                        # Draw mob to screen
                        mob = Mob(self.current_round)
                        mob.hit = False
                        self.all_sprites.add(mob)
                        self.mobs.add(mob)

                # Check if mob hit player
                hits = py.sprite.spritecollide(self.player, self.mobs, True, py.sprite.collide_circle)
                for hit in hits:
                    if not self.player.shield_active:
                        self.player.shield -= hit.radius * 2
                    expl = Explosion(hit.rect.center, 'small')
                    expl_sound.play()
                    self.all_sprites.add(expl)
                    #Spawn mobs
                    mob = Mob(self.current_round)
                    self.all_sprites.add(mob)
                    self.mobs.add(mob)

                    if self.player.shield <= 0:
                        expl = Explosion(self.player.rect.center, 'mega')
                        expl_sound.play()
                        self.all_sprites.add(expl)
                        self.player.hide()
                        self.player.spawn_shield()
                        self.player.power = 1
                        self.player.lives -= 1
                        if self.player.lives<= 0:
                            self.player.shield = 0
                        else:
                            self.player.shield = 100


                # Check if powerups are collected
                hits = py.sprite.spritecollide(self.player, self.powerups, True)
                for hit in hits:
                    if hit.type == 'shield':
                        self.player.shield += random.randrange(10, 30)
                        if self.player.shield >= 100:
                            self.player.shield = 100
                    if hit.type == 'gunx2':
                        self.player.powerup('gunx2')
                    if hit.type == 'gunx3':
                        self.player.powerup('gunx3')
                    if hit.type == 'heart':
                        if self.player.lives <= 2:
                            self.player.lives += 1

                # Dead
                if self.player.lives <= 0 and not expl.alive():
                    ret = self.game_over('game_over')
                    if ret == 'main':
                        self.ret = 'main'
                        running = False
                    if ret == 'instr':
                        self.ret = 'instr'
                        running = False
                #If game completed
                if self.boss3_killed and not expl.alive():
                    ret = self.game_over('game_over')
                    if ret == 'main':
                        self.ret = 'main'
                        running = False
                    if ret == 'instr':
                        self.ret = 'instr'
                        running = False

                # Draw / render

                if self.round4_finished:
                    display_screen.blit(mg1_background3, (0, 0))
                    rel_y = self.bg_y % mg1_background3.get_rect().height
                    display_screen.blit(mg1_background3, (0, rel_y - mg1_background3.get_rect().height))
                    if rel_y < display_height:
                        display_screen.blit(mg1_background3, (0, rel_y))
                    self.bg_y += 1
                elif self.round2_finished:
                    display_screen.blit(mg1_background2, (0, 0))
                    rel_y = self.bg_y % mg1_background2.get_rect().height
                    display_screen.blit(mg1_background2, (0, rel_y - mg1_background2.get_rect().height))
                    if rel_y < display_height:
                        display_screen.blit(mg1_background2, (0, rel_y))
                    self.bg_y += 1
                else:
                    display_screen.blit(bg, (0, 0))
                    rel_y = self.bg_y % bg.get_rect().height
                    display_screen.blit(bg, (0, rel_y - bg.get_rect().height))
                    if rel_y < display_height:
                        display_screen.blit(bg,(0, rel_y))
                    self.bg_y += 1


                self.all_sprites.draw(display_screen)
                if self.player.shield_active == True:
                    display_screen.blit(spawn_shield, (self.player.rect.centerx - 45, self.player.rect.top - 25))
                text_surface, text_rect = self.func.text_objects(str(self.score), small_text, WHITE)
                text_rect.center = (display_width/2, 10)
                display_screen.blit(text_surface, text_rect)
                self.draw_shield_bar(display_screen, display_width - 110,5, self.player.shield)
                self.draw_lives(display_screen, 5, 5, self.player.lives, Full_heart)

                try:
                    if self.ufo.shield > 0 and self.round2_active:
                        self.ufo.draw_shield_bar(display_screen, self.ufo.rect.centerx - 50, self.ufo.rect.bottom + 15,
                                                 self.ufo.shield)
                        if self.ufo.shield_active:
                            text_object, text_rect = self.func.text_objects("SHIELD ACTIVATED", small_text, WHITE)
                            text_rect.center = (self.ufo.rect.centerx, self.ufo.rect.bottom + 35)
                            display_screen.blit(text_object, text_rect)
                except:
                    pass

                # TEXT BLITTER (ROUNDS)
                if self.round1_text:
                    text_object, text_rect = self.func.text_objects("ROUND 1", large_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2)
                    display_screen.blit(text_object, text_rect)

                    text_object, text_rect = self.func.text_objects("Meteor Rain", medium_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2 + 50)
                    display_screen.blit(text_object, text_rect)

                if self.round2_active == True and py.time.get_ticks() - self.round2_text_timer > 100 \
                    and py.time.get_ticks() - self.round2_text_timer < 3000:

                    text_object, text_rect = self.func.text_objects("BOSS INCOMING", large_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2)
                    display_screen.blit(text_object, text_rect)

                    text_object, text_rect = self.func.text_objects("Sepiroth The Great", medium_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2 + 50)
                    display_screen.blit(text_object, text_rect)

                if self.round3_active == True and py.time.get_ticks() - self.round3_text_timer > 100 \
                    and py.time.get_ticks() - self.round3_text_timer < 3000:

                    text_object, text_rect = self.func.text_objects("ROUND 3", large_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2)
                    display_screen.blit(text_object, text_rect)

                    text_object, text_rect = self.func.text_objects("Grey Asteroids", medium_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2 + 50)
                    display_screen.blit(text_object, text_rect)

                if self.round4_active == True and py.time.get_ticks() - self.round4_text_timer > 100 \
                    and py.time.get_ticks() - self.round4_text_timer < 3000:

                    text_object, text_rect = self.func.text_objects("BOSS INCOMING", large_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2)
                    display_screen.blit(text_object, text_rect)

                    text_object, text_rect = self.func.text_objects("Aether The Destroyer", medium_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2 + 50)
                    display_screen.blit(text_object, text_rect)

                if self.round5_active == True and py.time.get_ticks() - self.round5_text_timer > 100 \
                    and py.time.get_ticks() - self.round5_text_timer < 3000:

                    text_object, text_rect = self.func.text_objects("ROUND 5", large_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2)
                    display_screen.blit(text_object, text_rect)

                    text_object, text_rect = self.func.text_objects("AVOID THE LASERS !", medium_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2 + 50)
                    display_screen.blit(text_object, text_rect)

                if self.round6_active == True and py.time.get_ticks() - self.round6_text_timer > 100 \
                    and py.time.get_ticks() - self.round6_text_timer < 3000:
                    text_object, text_rect = self.func.text_objects("BOSS INCOMING", large_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2)
                    display_screen.blit(text_object, text_rect)

                    text_object, text_rect = self.func.text_objects("BERAVDB", medium_text, WHITE)
                    text_rect.center = (display_width / 2, display_height / 2 + 50)
                    display_screen.blit(text_object, text_rect)
                # *after* drawing everything, flip the display
                clock.tick(FPS)
                py.display.flip()

                # Check if paused
            if self.state == 'pause':
                ret = self.game_over('pause')
                if ret == 'main':
                    self.ret = 'main'
                    running = False
                if ret == 'instr':
                    self.ret = 'instr'
                    running = False

        display_screen.blit(bg, (0,0))
        py.display.update()
        return self.ret