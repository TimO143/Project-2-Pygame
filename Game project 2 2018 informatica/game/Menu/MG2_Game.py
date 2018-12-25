from Values import *
from Functions import Functions
from MG2_Player import Player
from MG2_AsteroidUp import AsteroidUp
from MG2_AsteroidLeft import AsteroidLeft
from MG2_AsteroidRight import AsteroidRight
from MG2_AsteroidDown import AsteroidDown

# initialize

class Game():
    def __init__(self):
        self.func = Functions()
        self.bg_y = 0
    def load_data(self):
        with open(path.join(high_dir, mg2_highscore), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
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
                    with open(path.join(high_dir, mg2_highscore), 'w') as f:
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


    def gameExec(self, x):
        for i in range(x):
            a = AsteroidLeft()
            b = AsteroidUp()
            c = AsteroidRight()
            d = AsteroidDown()
            self.all_sprites.add(a, b, c, d)
            self.astr.add(a, b, c, d)

    def setup(self):
        self.all_sprites = py.sprite.Group()
        self.astr = py.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.score = 0
        self.ret = ""

    def draw_lives(self, surf, x, y, lives, img):
        for i in range(3):
            img_rect = Empty_heart.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surf.blit(Empty_heart, img_rect)
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surf.blit(img, img_rect)


    def loop(self):
        py.display.set_caption("Space Dodger")
        self.load_data()
        self.setup()
        self.state = 'run'
                        # load graphics
        background_rect = bg.get_rect()
        gameExit = False


        # GameLoop

        while not gameExit:
            if self.state == 'run':
                if self.score == 0:
                    self.gameExec(4)
                if int(self.score * 60) == 1150:
                    self.gameExec(1)
                if int(self.score * 60) == 2275:
                    self.gameExec(1)
                if int(self.score * 60) == 3600:
                    self.gameExec(4)
                hits = py.sprite.spritecollide(self.player, self.astr, False, py.sprite.collide_circle)

                if hits and not self.player.hidden:
                    invincible_sound.play()
                    if self.player.lives == 0:
                        self.score = int(self.score * 20)
                        ret = self.game_over('game_over')
                        if ret == 'main':
                            self.ret = 'main'
                            gameExit = True
                        if ret == 'instr':
                            self.ret = 'instr'
                            gameExit = True
                    else:
                        self.player.hide()
                        self.player.lives -= 1



                clock.tick(FPS)

                # Input
                for event in py.event.get():
                    if event.type == py.QUIT:
                        py.quit()
                        quit()
                    if event.type == py.KEYDOWN:
                        if event.key == py.K_ESCAPE:
                            self.state = 'pause'

                    # Update
                self.all_sprites.update()

                    # Draw / Render
                display_screen.fill(BLACK)
                display_screen.blit(bg, background_rect)
                self.all_sprites.draw(display_screen)
                scoretext = small_text.render(str(int(self.score*20)), 1, (255,255,255))
                display_screen.blit(scoretext, (display_width//2, 0))
                self.draw_lives(display_screen, display_width - 100, 5, self.player.lives, Full_heart)
                self.score += (1/FPS)
                #print(py.time.get_ticks())
                    # flip after render
                py.display.flip()

            if self.state == 'pause':
                ret = self.game_over('pause')
                if ret == 'main':
                    self.ret = 'main'
                    gameExit = True
                if ret == 'instr':
                    self.ret = 'instr'
                    gameExit = True


        display_screen.blit(bg, (0,0))
        py.display.update()
        return self.ret