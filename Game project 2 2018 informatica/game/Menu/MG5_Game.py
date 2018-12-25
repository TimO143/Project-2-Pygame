from Values import *
from Functions import Functions
import sys
from MG5_Sprites import *
from MG5_Map import *

class Game:
    def __init__(self):
        self.screen = py.display.set_mode((display_width, display_height))
        self.func = Functions()
        self.load_highscore()
        self.bg_y = 0
        self.font_name = py.font.match_font(FONT_NAME)

        """ Hierdoor ben je voor 3s niet te raken door enemies (zodat je geen levens verliest) """
        self.invincible_timer = py.time.get_ticks()
        self.invincible_status = False
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
                #Moving Background
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

                text_surface, text_rect = self.func.text_objects("SCORE {}".format(str(int(self.score))), medium_text, WHITE)
                text_rect.center = (display_width / 2, 220)
                display_screen.blit(text_surface, text_rect)

                # Score Checker
                if self.score > self.highscore or self.score == self.highscore:
                    self.highscore = int(self.score)
                    text_surf, text_rect = self.func.text_objects("NEW HIGHSCORE",
                                                                  small_text, RED)
                    text_rect.center = (display_width / 2, 260)
                    display_screen.blit(text_surf, text_rect)
                    with open(path.join(high_dir, mg5_highscore), 'w') as f:
                        f.write(str(int(self.score)))

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

    def load_highscore(self):
        with open(path.join(high_dir, mg5_highscore), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def load_data(self):
        Youtube = path.dirname(__file__)
        #choose random map
        self.map_list = ['map2.txt', 'map3.txt', 'map4.txt']
        self.map = Map(path.join(Youtube, random.choice(self.map_list)))
        self.player_img = mg5_player_img
        self.finish_img = finish
        self.wall_img = wall_img
        self.mob_img = mob_img


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

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = py.sprite.Group()
        self.walls = py.sprite.Group()
        self.flags = py.sprite.Group()
        self.mobs = py.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'F':
                    Flag(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'M':
                     Mob(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        # game loop - set self.playing = False to end the game
        self.state = 'run'
        self.load_data()
        self.new()
        self.ret = ""
        self.playing = True
        self.score = 2200
        while self.playing:
            if self.state == 'run':
                self.dt = clock.tick(FPS) / 1000.0
                #EVENTS HIERHEEN VERPLAATS ANDERS DEED DIE HET NIET
                for event in py.event.get():
                    if event.type == py.QUIT:
                        self.quit()
                    if event.type == py.KEYDOWN:
                        if event.key == py.K_ESCAPE:
                            self.state = 'pause'
                        #if event.key == py.K_SPACE:
                        #    ret = self.game_over('game_over')
                        #    if ret == 'main':
                        #        self.ret = 'main'
                        #        self.playing = False
                        #    if ret == 'instr':
                        #        self.ret = 'instr'
                        #        self.playing = False

                self.update()
                self.draw()
            if self.state == 'pause':
                ret = self.game_over('pause')
                if ret == 'main':
                    self.ret = 'main'
                    self.playing = False
                if ret == 'instr':
                    self.ret = 'instr'
                    self.playing = False

        return self.ret

    def quit(self):
        py.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

            #DIT GAAT ELKE MILLISECONDE MAAR MOET ELKE SECONDE ZIJN
        if py.time.get_ticks():
           self.score -= 0.1


        """ collision check met flag """
        flags = py.sprite.spritecollide(self.player, self.flags, True)
        if flags:
            ret = self.game_over('game_over')
            if ret == 'main':
                self.ret = 'main'
                self.playing = False
            if ret == 'instr':
                self.ret = 'instr'
                self.playing = False

        """ collision check met enemy """
        enemy_hit_list = py.sprite.spritecollide(self.player, self.mobs, False)
        if enemy_hit_list:
            if not self.invincible_status:            # self.player.lives >= 0 and
                self.player.lives -= 1
                self.invincible_status = True
                self.invincible_timer = py.time.get_ticks()
                invincible_sound.play(3)  # speelt het geluid 3 keer af geeft aan hoe lang je invincible bent

            if self.player.lives < 1:
                ret = self.game_over('game_over')
                if ret == 'main':
                    self.ret = 'main'
                    self.playing = False
                if ret == 'instr':
                    self.ret = 'instr'
                    self.playing = False

        # player is voor 3 seconden invincible, dus kan 3 seconden lang geen leven verliezen.
        if py.time.get_ticks() - self.invincible_timer > 3000:
            self.invincible_status = False

    def draw_grid(self):
        for x in range(0, display_width, TILESIZE):
            py.draw.line(display_screen, LIGHTGREY, (x, 0), (x, display_height))
        for y in range(0, display_width, TILESIZE):
            py.draw.line(display_screen, LIGHTGREY, (0, y), (display_width, y))

    def draw(self):
        display_screen.blit(bg, (0, 0))
        #display_screen.fill(DARKGREY)
        #self.draw_grid()
        for sprite in self.all_sprites:
            display_screen.blit(sprite.image, self.camera.apply(sprite))
        self.draw_text(str(int(self.score)), 22, WHITE, display_width / 2, 15)
        # py.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        self.draw_lives(display_screen, 5, 5, self.player.lives, Full_heart)
        py.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = py.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

#
# # create the game object
#g = Game()
#while True:
#      g.new()
#      g.run()
