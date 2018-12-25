from Values import *
from Functions import Functions
from MG3_Player import Player
from MG3_Platform import *
from MG3_Coin import Coin
from MG3_Enemy import *
from MG3_Flag import *
from MG3_Camera import *
from MG3_Spritesheet import *
from MG3_Health import *
from MG3_Sign import *


class Game:
    def __init__(self):
        # initialize game window
        self.screen = py.display.set_mode((display_width, display_height))
        self.clock = py.time.Clock()
        self.running = True
        self.font_name = py.font.match_font(FONT_NAME)
        self.func = Functions()
        self.bg_y = 0
        self.load_data()

        """ Hierdoor ben je voor 3s niet te raken door enemies (zodat je geen levens verliest) """
        self.invincible_timer = py.time.get_ticks()
        self.invincible_status = False

    def load_data(self):

        with open(path.join(high_dir, mg3_highscore), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                print("error")
                self.highscore = 0

        """ laden van spritesheets """
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        self.spritesheet_enemy = Spritesheet_enemy(path.join(img_dir, SPRITESHEET_ENEMY))

    """ Tekenen van levens """
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

    """ niet aanzitten """
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
                    with open(path.join(high_dir, mg3_highscore), 'w') as f:
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

    """ Wat er geladen wordt bij begin van een nieuwe game """
    def new(self):
        # start a new game
        py.display.set_caption(TITLE)
        self.ret = ""
        self.score = 0
        self.all_sprites = py.sprite.Group()        # voeg een all_sprites groep toe die alle sprites vasthoud
        self.platforms = py.sprite.Group()          # maak groep voor platforms   Hiermee collide je!
        self.coins = py.sprite.Group()              # maak groep voor coins
        self.enemies = py.sprite.Group()            # maak groep voor enemy
        self.flag = py.sprite.Group()               # maak groep voor vlag
        self.hearts = py.sprite.Group()             # maak groep voor hart
        self.sign = py.sprite.Group()               # maak groep voor borden
        self.flag_end = py.sprite.Group()           # maak groep voor eindvlag

        self.spring_up = py.sprite.Group()              # maak groep voor springveer up
        self.spring_down = py.sprite.Group()            # maak groep voor springveer down
        self.spring_right = py.sprite.Group()           # maak groep voor springveer right
        self.spring_left = py.sprite.Group()            # maak groep voor springveer left

        """ Maken van het level """
        """ kleine c = coin, grote P = platform , grote E = enemy_rechts, G = grond , M = player spawn , e = enemy_up
            H = hart, o = easy-sign , h = hard-sign, q = easteregg-sign , u = uitleg"""
        x = y = 0
        level = [
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "G         HH HH       ccccccc cccc   cccc   cccc   c c c                         G",
            "G        H  H  H   cc    c    c  c   c   c  c   c  c c c                         G",
            "G         H   H   ccP    c    c  c   c   c  c   c  c c c           q           c G",
            "GF         H H   cccG    c    cccc   cccc   c   c  c c c                         G",
            "GPPPPPPPP   H   PPPPG    c    c      c   c  c   c  c c c                         G",
            "GcccccccG           G    c    c      cccc   cccc   ccccc            c e c        G",
            "G   c   GPP         GPPPPPPPPPPPPP  PPPPPP  PPPPPPP PPP   PPPPPP  c PPPPPP       G",
            "G   c   GGGPP  e           G                                        G     c      G",
            "G   c       GPP            G                      ccc             c G       PP   G",
            "G             GPP          G                      ccc          P    G    c       G",
            "G                PP        G                      PPP          G  c G      c   c G",
            "Gc                 PP      G      c c  c c c c                 G    G   PPPPPPPPPG",
            "Gcc                        G      c c  c c c c            c    G  c G           HG",
            "Gccc                  e  ccG      P   e   E  P           c c   G    G        c   G",
            "Gccccc      E   PPPPPPPPPPcG      GPPPPPPPPPPG          c   c  G  c GP     c     G",
            "Gccccccc          c  c     c                         e c            G            G",
            "GPPPPPPPPPPPPP                  c    e          c     c           c GH cE  P     G",
            "G          c          c  E                   c     c c      PPPPPPPPGPPPPPPG     G",
            "G     c                           c    c  c      PPPPP              G        P   G",
            "G              PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  c  cHcG   c          G            G",
            "G              G               e            GP    cccG              G           PG",
            "G      e P  PPP c            c     c     c   GPP  cccG   c          G   c        G",
            "G    PPE             c                            cccG E            G   P   E  cHG",
            "G                         c    c            c    cccHG   c          G   GPPPPPPPPG",
            "GPP             H   e                            PPPPG              G            G",
            "GGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  e    c      G              GP  c        G",
            "G                  c            e      PP        c   G       Hu     G    c    c  G",
            "G       c               c                 PP         G       P      GPPPPPP    cPG",
            "G          c     e   E   c                      c    G       G                PPGG",
            "G            c                 cc      c      PP    cG                      cPGGGG",
            "G                                          c        PG                   c cPGGGGG",
            "G      E    e      c     e              c       Ec cGG     h        o   cPPPGGGGGG",
            "GH    PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGG       PPP    PPPPPGGGGGGGGG",
            "G                        e                     c             GGGPc    e       E  G",
            "G                            c                   c  c       UGGGGP               G",
            "GPP       c             c     e         c   e               PGGGGG    c    c   c G",
            "GGGP   c           c               c             c  c        GGGGGP              G",
            "GGGGP         e                     e         c     c     HH GGGGGGP   c      M  G",
            "GGGGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGGGGGGPPPPPPPPPPPPPG", ]

        for row in level:
            for col in row:                         # zet hier in de dingen die je wilt spawnen
                if col == "P":
                    p = Platform(x, y)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                if col == "G":
                    h = Platform_ground(x, y)
                    self.all_sprites.add(h)
                    self.platforms.add(h)
                if col == "c":
                    c = Coin(x, y)
                    self.all_sprites.add(c)
                    self.coins.add(c)
                if col == "E":
                    E = Enemy(x, y, self)
                    self.all_sprites.add(E)
                    self.enemies.add(E)
                if col == "e":
                    E = Enemy_up(x, y, self)
                    self.all_sprites.add(E)
                    self.enemies.add(E)
                if col == "F":
                    F = Flag(x, y)
                    self.all_sprites.add(F)
                    self.flag.add(F)
                if col == "H":
                    h = Heart(x, y)
                    self.all_sprites.add(h)
                    self.hearts.add(h)
                if col == "h":
                    a = Sign_hard(x, y)
                    self.all_sprites.add(a)
                    self.sign.add(a)
                if col == "o":
                    h = Sign_easy(x, y)
                    self.all_sprites.add(h)
                    self.sign.add(h)
                if col == "q":
                    h = Egg(x, y)
                    self.all_sprites.add(h)
                    self.sign.add(h)
                if col == "u":
                    h = Uitleg(x, y)
                    self.all_sprites.add(h)
                    self.sign.add(h)
                if col == "U":
                    h = Springveer(x, y)
                    self.all_sprites.add(h)
                    self.spring_up.add(h)
                if col == "M":
                    self.player = Player(x, y ,self)
                    self.all_sprites.add(self.player)
                x += 64                 # maakt de grids uitelkaar (horizontaal)
            y += 64                     # maakt de grids uitelkaar (verticaal)
            x = 0

        total_level_width = len(level[0]) * 64      # houd dit even groot als de x hierboven
        total_level_height = len(level) * 64        # houd dit even groot als de y hierboven
        self.camera = Camera(complex_camera,total_level_width,total_level_height)       # dit regelt de camera

    def level2(self):
        # start a new game
        py.display.set_caption(TITLE)
        self.score = self.score                     # Score wordt onthouden van lvl 1
        self.all_sprites = py.sprite.Group()        # voeg een all_sprites groep toe die alle sprites vasthoud
        self.platforms = py.sprite.Group()          # maak groep voor platforms   Hiermee collide je!
        self.coins = py.sprite.Group()              # maak groep voor coins
        self.enemies = py.sprite.Group()            # maak groep voor enemy
        self.flag = py.sprite.Group()               # maak groep voor vlag
        self.hearts = py.sprite.Group()             # maak groep voor hart
        self.sign = py.sprite.Group()               # maak groep voor borden
        self.flag_end = py.sprite.Group()           # maak groep voor eindvlag

        self.spring_up = py.sprite.Group()              # maak groep voor springveer up
        self.spring_down = py.sprite.Group()            # maak groep voor springveer down
        self.spring_right = py.sprite.Group()           # maak groep voor springveer right
        self.spring_left = py.sprite.Group()            # maak groep voor springveer left


        """ Maken van het level """
        """ kleine c = coin, grote P = platform , grote E = enemy_rechts, G = grond , M = player spawn , e = enemy_up
            H = hart, o = easy-sign , h = hard-sign, q = easteregg-sign, V = springveer"""
        x = y = 0
        level2 = [
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "G  ccccc  cc  ccc c  cc  c  c       ccc c c c c ccc          c c  c ccc  c     c G",
            "G  c c c c  c c c   c  c cc c       c c c c c c c  c    q      cc c c    c     c G",
            "G  c c c cccc cc  c cccc c cc       cc  c c c c c  c         c c cc ccc  c  c  c G",
            "G  c c c c  c c c c c  c c  c       c c ccc ccc ccc          c c  c c    c  cccc G",
            "G                                                                                G",
            "G         P                  LP      P                     LPPPP                 G",
            "GPPPPPP   GPPPPPPPPPPPPPPPPPPPGP    PGPPPPPPPPPPPPPPPPPPPPPP        PP       PP  G",
            "GGGGGGG DPGGGGGGGGGGGGGGGGGGGGGGPDDDGG M Gc c             D       PP          G  G",
            "GRRR RR c  R R R R R Rc c D G        G   G c                    PP            G  G",
            "G  R RR c  R R R R R Rc c D G    DDDDG   Gc c                 PP              GUUG",
            "GUUPPPP cPPPPPPPPPPPPPPPP c GP       G   GPPP               PP                G  G",
            "G  Gc   D          GRRR D   R        G   GR               PP                  G  G",
            "GUUGc   c          G    L c R    DDD G   G              PP          c  U      G  G",
            "G  Gc   c          G    L    P    c  G   G            PP          c   PPPPP   GUUG",
            "G  GU ccccccc  D   G   P  c  G    c  G   GU        PPP          c   P         G  G",
            "GUUGPPPPPPPPPP     GD  G     GDDDDDDDG   GPP                  c   P           G  G",
            "G   ccccccccccc        G  P  G  c c  G   GGGPU              c   P             G  G",
            "G   ccccccccccc        G     G  c c  G   GGGGPP           c                 U G  G",
            "G   ccc     ccc        G     G  c c  G   GGGGGGP        c   P    ccccccccPccP G  G",
            "GU   c       c        UGU F UG  c c  G   GR  DDGP         P           cPPG  G G  G",
            "GPPPPPPPPUUUUPPPP  PPPPGPPPPPGPPc c  G   G     GG       P            PP       G  G",
            "G  RRRRRRc   R R    R R  D  c c c cLLG   G      GP                 PP c       GUUG",
            "G  c     c   R R   RR R  D  c c c cLLG   G      GG     U              c       G  G",
            "G UUU   Pc R R R R RR R  D PPPPPPPPPPG   G   PPPGGP                   c       G  G",
            "G  c  PPGc PPPPPPPPPPPPP   G  c c c  G   G c c c c P          PP      c       G  G",
            "G  c  G  U             G c G c      cG   G c H H c  P       PP    U        U  G  G",
            "G UUU G  c             G   G c   H  cG   GUc H H c         P cc   PP      PP  GUUG",
            "G  c  G  c             G c G c      cG   G c c c c       PP ccc         PP    G  G",
            "G  c  G  U  c c c c c  G D G c c c c G   G cPPPP       UP   ccc               G  G",
            "G  c  GPPPPPPPPPPP  c  G   G   PPPPPPG   G cG         PP    PPPP              G  G",
            "G UUU GD            c  G c GU        G   GU G        P                U       G  G",
            "G  c  Gc            c  G   G         G   G         PP                 PP  PP  G UG",
            "G  c  G  c c c  c c U  G c G        LG   G        P                 PP      PPG  G",
            "G  c  G  c PPPPPPPPPPPPG D GPPPP     G   G       P                PP ccccccc  G  G",
            "G  c  G  c      c  c LG  c           G   GU P                        c        G  G",
            "G UUU G  c            G             UG   G   PU               PP     c  U     G  G",
            "G  c  G  U           cG  c           G   G    P             PPR      c        G  G",
            "G  c  GPPPPPPPPPPPPP  G              G   G     P           PG     PP c        G  G",
            "G  c                 cG  c          UG   G      P         PG        PPcccccc DG UG",
            "G  c                  G              G   GU      P       PG           PPU     G  G",
            "G  U c c c  c c c c  UG  c           G   G        P     PG              PP    G  G",
            "GPPPPPPPPPP c PPPPPPPPG             UG   G             P             ccccc    G  G",
            "GR      D   c Gc c c c   c           G   G            P              c        G  G",
            "G           c Gc c c c               G   G          UP    PP  U      ccccc   PG  G",
            "Gc  c c c c U Gc c c c   L           G   G          P       PPP      c     UP G  G",
            "G  PPPPPPPPPPPGPPPPPPPPPPPP          G   G         P           PP    ccccPPP  G UG",
            "Gc G                                UG   G  cccc  Pccc    ccccc    c   PP     G  G",
            "G  G                             PPPPG   GU c  c Pc  c  PPc   c    c          G  G",
            "Gc G                                     GP ccccP ccc PP  c PPc    c          G  G",
            "G                          PPP              c     c c     c   c c  c             G",
            "GU         LP    UUUUUUUUUUGGGP             c     c  Uc   ccccc cccU            UG",
            "GPPPPPPPPPPPGPPPPPPPPPPPPPPGGGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG", ]

        for row in level2:
            for col in row:                         # zet hier in de dingen die je wilt spawnen
                if col == "P":
                    p = Platform_ice(x, y)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                if col == "G":
                    h = Platform_ice_ground(x, y)
                    self.all_sprites.add(h)
                    self.platforms.add(h)
                if col == "c":
                    c = Coin(x, y)
                    self.all_sprites.add(c)
                    self.coins.add(c)
                if col == "E":
                    E = Enemy(x, y, self)
                    self.all_sprites.add(E)
                    self.enemies.add(E)
                if col == "e":
                    E = Enemy_up(x, y, self)
                    self.all_sprites.add(E)
                    self.enemies.add(E)
                if col == "F":
                    F = Flag_ice(x, y)
                    self.all_sprites.add(F)
                    self.flag_end.add(F)
                if col == "H":
                    h = Heart(x, y)
                    self.all_sprites.add(h)
                    self.hearts.add(h)
                if col == "q":
                    h = Egg(x, y)
                    self.all_sprites.add(h)
                    self.sign.add(h)
                if col == "U":
                    h = Springveer(x, y)
                    self.all_sprites.add(h)
                    self.spring_up.add(h)
                if col == "D":
                    h = Springveer_down(x, y)
                    self.all_sprites.add(h)
                    self.spring_down.add(h)
                if col == "R":
                    h = Springveer_right(x, y)
                    self.all_sprites.add(h)
                    self.spring_right.add(h)
                if col == "L":
                    h = Springveer_left(x, y)
                    self.all_sprites.add(h)
                    self.spring_left.add(h)
                if col == "M":
                    self.player = Player(x, y ,self)
                    self.all_sprites.add(self.player)
                x += 64                 # maakt de grids uitelkaar (horizontaal)    pixels
            y += 64                     # maakt de grids uitelkaar (verticaal)      pixels
            x = 0

        total_level_width = len(level2[0]) * 64      # houd dit even groot als de x hierboven
        total_level_height = len(level2) * 64        # houd dit even groot als de y hierboven
        self.camera = Camera(complex_camera,total_level_width,total_level_height)

    """ niet aanzitten """
    def run(self):
        # Game Loop
        self.new()
        self.playing = True
        #py.mixer.music.play(loops=-1)
        self.state = 'run'
        while self.playing:
            if self.state == 'run':
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()
            if self.state == 'pause':
                ret = self.game_over('pause')
                if ret == 'main':
                    self.ret = 'main'
                    self.playing= False
                if ret == 'instr':
                    self.ret = 'instr'
                    self.playing = False

        # RETURNS TO MINIGAMES
        display_screen.blit(bg, (0,0))
        py.display.update()
        return self.ret

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        self.camera.update(self.player)

        """ collision check met coin """
        coin_hit_list = py.sprite.spritecollide(self.player, self.coins,True)  # True zorg ervoor dat coin in de list wordt weggehaald
        if coin_hit_list:
            self.score += 4
            coin_sound.play()

        """ collision check met springveer up """
        springup_hit_list = py.sprite.spritecollide(self.player, self.spring_up,False)  # True zorg ervoor dat coin in de list wordt weggehaald
        if springup_hit_list:
            self.player.speed_y = -30
            springveer_sound.play()

        """ collision check met springveer down """
        springdown_hit_list = py.sprite.spritecollide(self.player, self.spring_down,False)  # True zorg ervoor dat coin in de list wordt weggehaald
        if springdown_hit_list:
                self.player.speed_y  = 30
                self.player.stop()
                springveer_sound.play()

        """ collision check met springveer rechts """
        springright_hit_list = py.sprite.spritecollide(self.player, self.spring_right,False)  # True zorg ervoor dat coin in de list wordt weggehaald
        if springright_hit_list:
            self.player.speed_x  =  80
            springveer_sound.play()

        """ collision check met springveer links """
        springleft_hit_list = py.sprite.spritecollide(self.player, self.spring_left,False)  # True zorg ervoor dat coin in de list wordt weggehaald
        if springleft_hit_list:
            self.player.speed_x  = -40
            springveer_sound.play()

        """ collision check met heart """
        heart_hit_list = py.sprite.spritecollide(self.player, self.hearts,True)  # True zorg ervoor dat coin in de list wordt weggehaald
        if heart_hit_list:
            self.player.lives += 1
            hp_up_sound.play()

        """ collision check met enemy """
        enemy_hit_list = py.sprite.spritecollide(self.player, self.enemies, False)
        if enemy_hit_list:
            if not self.invincible_status:            # self.player.lives >= 0 and
                self.player.lives -= 1
                self.invincible_status = True
                self.invincible_timer = py.time.get_ticks()
                invincible_sound.play(3)  # speelt het geluid 3 keer af geeft aan hoe lang je invincible bent

            if self.player.lives < 1:
                #py.mixer.music.stop()
                #py.mixer.stop()
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

        """ collision check met flag """
        flag_level2 = py.sprite.spritecollide(self.player, self.flag, True)
        if flag_level2:
            self.level2()

        flag_end = py.sprite.spritecollide(self.player, self.flag_end, True)
        if flag_end:
            #py.mixer.music.stop()
            #py.mixer.stop()
            ret = self.game_over('game_over')
            if ret == 'main':
                self.ret = 'main'
                self.playing = False
            if ret == 'instr':
                self.ret = 'instr'
                self.playing = False

    """ niet aanzitten """
    def events(self):
        # Game Loop - events
        for event in py.event.get():
            # check for closing window
            if event.type == py.QUIT:
                py.quit()
                quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    self.player.go_left()
                if event.key == py.K_RIGHT:
                    self.player.go_right()
                if event.key == py.K_UP:
                    self.player.jump()
                if event.key == py.K_ESCAPE:
                    self.state = 'pause'
                    self.player.stop()

            if event.type == py.KEYUP:
                if event.key == py.K_LEFT and self.player.speed_x < 0:
                    self.player.stop()
                if event.key == py.K_RIGHT and self.player.speed_x > 0:
                    self.player.stop()

    """ Tekenen van alles op het scherm """
    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.screen.blit(bg, (0, 0))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.draw_text(str(self.score), 22, WHITE, display_width / 2, 15)

        self.draw_lives(display_screen, 5, 5, self.player.lives, Full_heart)

        # *after* drawing everything , flip the display
        py.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = py.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
