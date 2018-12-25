from MG4_Hanger import Hanger
from MG4_Arrow import Arrow
from MG4_Starschip import Starschip
from MG4_Hearts import Heart
from MG4_UFO import UFO
from MG4_Values import *
from Functions import Functions



class Game():
    def __init__(self):
        self.bg_y = 0
        self.func = Functions()
        self.load_data()
    def uit(self):
        py.quit()
        quit()

    def spawnrandomspace(self, endran, endcount):
        # Genereer een random number van 0 tot 90.
        ran = int(random.randint(0, endran))

        # Als de self.counter hoger is dan 0 en ran 9 is dan spawnt die een spaceschip.
        if ran == 1 and self.counter <= int(endcount):
            # Maakt een random number aan van 0 - 3 om een random kleur van het schip te bepalen.
            ran = int(random.randint(0, 3))

            # Maakt het schip met bijbehorende kleuren.
            if ran == 0:
                self.playerstarschip2 = Starschip(self.arrow1, self.arrow2, self.arrow3, self.arrow4, starschip1_img, "Blue")
            elif ran == 1:
                self.playerstarschip2 = Starschip(self.arrow1, self.arrow2, self.arrow3, self.arrow4, starschip2_img, "Brown")
            elif ran == 2:
                self.playerstarschip2 = Starschip(self.arrow1, self.arrow2, self.arrow3, self.arrow4, starschip3_img, "Green")
            elif ran == 3:
                self.playerstarschip2 = Starschip(self.arrow1, self.arrow2, self.arrow3, self.arrow4, starschip4_img, "Purple")

            self.counter = self.time
            starchip.add(self.playerstarschip2)
            all_sprites_list.add(self.playerstarschip2)

    def difficulty(self, score, endran, endcount):

        if score <= 0:

            if endran <= 1:
                endran = 1

            if endcount >= 180:
                endcount = 180

            return endran, endcount

        else:
            pair = self.difficulty(score - 40, endran - 10, endcount + 4)

            endran = pair[0]
            endcount = pair[1]

            if endran <= 1:
                endran = 1

            if endcount >= 180:
                endcount = 180

            return endran, endcount

    def text_objects(self, text, font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = py.mouse.get_pos()
        click = py.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            py.draw.rect(display_screen, ac, (x, y, w, h))

            if click[0] == 1:
                action()
                return True

        else:
            py.draw.rect(display_screen, ic, (x, y, w, h))

        textSurf, textRect = self.text_objects(msg, small_text_highlight)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        display_screen.blit(textSurf, textRect)

    def load_data(self):

        with open(path.join(high_dir, mg4_highscore), 'r') as f:
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

                # buttons
                main_menu_button = self.func.button("Main Menu", WHITE, display_width / 2 - main_menu_buttonx / 2, 325,
                                                    main_menu_buttonx, main_menu_buttony, IACOLOR, ACOLOR)
                restart_button = self.func.button("Restart", WHITE, display_width / 2 - main_menu_buttonx / 2, 400,
                                                  main_menu_buttonx,
                                                  main_menu_buttony, IACOLOR, ACOLOR)

                # text

                text_surface, text_rect = self.func.text_objects("GAME OVER", game_over_text, WHITE)
                text_rect.center = (display_width / 2, 100)
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
                    with open(path.join(high_dir, mg4_highscore), 'w') as f:
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


    def reset(self):
        all_sprites_list.empty()
        arrow.empty()
        starchip.empty()
        hartgroup.empty()

    def loop(self):
        #Set title van het spel.
        py.display.set_caption("Spaceschip Parking the Game")
        self.reset()
        self.state = 'run'
        self.ret = ''

        #Maakt de vier hangers.
        hanger1 = Hanger(Hanger_Blue_img, 120, 5)
        hanger2 = Hanger(Hanger_Brown_img, 378, 5)
        hanger3 = Hanger(Hanger_Groen_img, 633, 5)
        hanger4 = Hanger(Hanger_Paarse_img, 890, 5)

        #Maakt de arrows.
        self.arrow1 = Arrow(180, 240)
        self.arrow2 = Arrow(430, 240)
        self.arrow3 = Arrow(690, 240)
        self.arrow4 = Arrow(950, 240)

        #Maakt het eerste ruimte schip.
        playerstarschip = Starschip(self.arrow1, self.arrow2, self.arrow3, self.arrow4, starschip1_img, "Blue")

        #Maak de drie hartjes.
        hart1 = Heart(5, 10)
        hart2 = Heart(40, 10)
        hart3 = Heart(75, 10)

        #Voeg de hartjes toe aan hartgroup.
        hartgroup.add(hart1)
        hartgroup.add(hart1)
        hartgroup.add(hart1)

        #Voeg de pijlen toe aan arrow group.
        arrow.add(self.arrow1)
        arrow.add(self.arrow2)
        arrow.add(self.arrow3)
        arrow.add(self.arrow4)
        starchip.add(playerstarschip)

        #Voeg alle standaard sprites toe aan de sprite groeps.
        all_sprites_list.add(self.arrow1)
        all_sprites_list.add(self.arrow2)
        all_sprites_list.add(self.arrow3)
        all_sprites_list.add(self.arrow4)
        all_sprites_list.add(playerstarschip)
        all_sprites_list.add(hanger1)
        all_sprites_list.add(hanger2)
        all_sprites_list.add(hanger3)
        all_sprites_list.add(hanger4)
        all_sprites_list.add(hart1)
        all_sprites_list.add(hart2)
        all_sprites_list.add(hart3)

        done = False

        #Set een paar standaard variablen.
        self.time = 250
        self.counter = self.time
        dead = 0
        score = 0


        #Set variablen voor voorbijvliegen UFO
        ufo_run_1 = False
        ufo_run_2 = False
        ufo_run_3 = False
        ufo_run_4 = False

        while not done:
            if self.state == 'run':
                for event in py.event.get():
                    if event.type == py.QUIT:
                        self.uit()
                    if event.type == py.KEYDOWN:
                        if event.key == py.K_ESCAPE:
                            self.state = 'pause'

                clock.tick(60)

                # Laat de self.counter af lopen als deze hoger is dan null zodat de schepen niet te snel achter elkaar spawnen.
                if self.counter > 0:
                    self.counter = self.counter - 1
                else:
                    self.counter = 0

                #Roept functie difficulty aan die de moeilijkheid bepaalt aan de hand van de score.
                vardiffic = self.difficulty(score, 100, 0)

                endran = vardiffic[0]
                endcount = vardiffic[1]

                #Roept de functie spawnrandomspace aan die misschien een schip spawnt.
                self.spawnrandomspace(endran, endcount)

                # Update
                # Verwijderd en voegt vervolgens de hangers weer toe.
                all_sprites_list.remove(hanger1)
                all_sprites_list.remove(hanger2)
                all_sprites_list.remove(hanger3)
                all_sprites_list.remove(hanger4)

                all_sprites_list.add(hanger1)
                all_sprites_list.add(hanger2)
                all_sprites_list.add(hanger3)
                all_sprites_list.add(hanger4)

                # Haalt de richtingen op van de pijlen op.
                direction1 = Arrow.exchange(self.arrow1)
                direction2 = Arrow.exchange(self.arrow2)
                direction3 = Arrow.exchange(self.arrow3)
                direction4 = Arrow.exchange(self.arrow4)

                # Exporteer de richting van alle pijlen naar de starschepen.
                for starschip in starchip.sprites():
                    starschip.importarrow( direction1, direction2, direction3, direction4)

                # Haalt de deads op uit de starschip.
                for starschip in starchip.sprites():
                    k = starschip.exportdead()
                    dead = dead + k

                # Haalt de score op uit de starschip.
                for starschip in starchip.sprites():
                    k = starschip.exportscore()
                    score = score + k

                # Geeft de score door aan de class score.
                #Score.importscore(scorec, score)

                label = small_text.render("Score: " + str(score), 1, WHITE)

                self.score = score

                # Zorgt er voor dat je de hoeveelheid levens kan zien.
                if dead >= 1:
                    Heart.changeimage(hart3, Empty_heart)
                if dead >= 2:
                    Heart.changeimage(hart2, Empty_heart)
                if dead >= 3:
                    Heart.changeimage(hart1, Empty_heart)
                if dead >= 4:
                    ret = self.game_over('game_over')
                    if ret == 'main':
                        self.ret = 'main'
                        done = True
                    if ret == 'instr':
                        self.ret = 'instr'
                        done = True

                # Laat UFO voorbij vliegen op een score van 100, 500, 1000, 10000

                if score >= 100 and not ufo_run_1:
                    ufo_run_1 = True
                    ufo = UFO("Blue")
                    all_sprites_list.add(ufo)
                elif score >= 500 and not ufo_run_2:
                    ufo_run_2 = True
                    ufo = UFO("Green")
                    all_sprites_list.add(ufo)
                elif score >= 1000 and not ufo_run_3:
                    ufo_run_3 = True
                    ufo = UFO("Red")
                    all_sprites_list.add(ufo)
                elif score >= 10000 and not ufo_run_4:
                    ufo_run_4 = True
                    ufo = UFO("Yellow")
                    all_sprites_list.add(ufo)

                all_sprites_list.update()

                # Draw / render
                display_screen.blit(bg_airport, (0, 0))

                all_sprites_list.draw(display_screen)

                display_screen.blit(label, (550, 5))

                # Flip the screen
                py.display.flip()

            if self.state == 'pause':
                ret = self.game_over('pause')
                if ret == 'main':
                    self.ret = 'main'
                    done = True
                if ret == 'instr':
                    self.ret = 'instr'
                    done = True

        display_screen.blit(bg, (0, 0))
        py.display.update()
        return self.ret


