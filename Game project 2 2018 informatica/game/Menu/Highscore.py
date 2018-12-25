from Values import *
from Functions import Functions

class Highscore:
    def __init__(self):
        self.func = Functions()

    def loop(self):
        bg_y = 0
        running = True
        py.display.set_caption("Highscores")
        while running:

            # DRAW HIGHSCORE TABLE

            rel_y = bg_y % bg.get_rect().height
            display_screen.blit(bg, (0, rel_y - bg.get_rect().height))
            if rel_y < display_height:
                display_screen.blit(bg, (0, rel_y))
            bg_y += 0.1

            self.background = self.func.button("", BLACK, 150,100, 800,500, IACOLOR, IACOLOR)

            self.back_button = self.func.button("Back", WHITE, 20, display_height - instr_buttony - 20, instr_buttonx,
                                                instr_buttony,
                                                IACOLOR, ACOLOR)
            self.total_button = self.func.button("Total", WHITE, 175,125, instr_buttonx, instr_buttony, ACOLOR,
                                               ACOLOR)
            self.mg1_button = self.func.button("Meteor Strike", WHITE, 175,205, instr_buttonx, instr_buttony, ACOLOR,
                                               ACOLOR)
            self.mg2_button = self.func.button("Space Dodger", WHITE, 175,285, instr_buttonx, instr_buttony, ACOLOR,
                                               ACOLOR)
            self.mg3_button = self.func.button("Strange Planet", WHITE, 175,365, instr_buttonx, instr_buttony, ACOLOR,
                                               ACOLOR)
            self.mg4_button = self.func.button("Spaceship Parking", WHITE, 175,445, instr_buttonx, instr_buttony, ACOLOR,
                                               ACOLOR)
            self.mg5_button = self.func.button("Space Maze", WHITE, 175,525, instr_buttonx, instr_buttony, ACOLOR,
                                               ACOLOR)
            #TITLE
            text_surf, text_rect = self.func.text_objects("HIGHSCORES", medium_text, WHITE)
            text_rect.center = (self.background.centerx, self.background.top - 25)
            display_screen.blit(text_surf, text_rect)

            #MG1
            mg1_background = py.draw.rect(display_screen, ACOLOR, (175 + instr_buttonx + 25, 205, 525, instr_buttony))
            with open(path.join(high_dir, mg1_highscore), 'r') as f:
                try:
                    self.mg1_highscore = int(f.read())
                except:
                    print("error")
                    self.mg1_highscore = 0

            text_surf, text_rect = self.func.text_objects("Highscore {}".format(str(self.mg1_highscore)), small_text,
                                                          WHITE)
            text_rect.center = ((175 + instr_buttonx + 25) + 525/2, 205 + instr_buttony/2)
            display_screen.blit(text_surf, text_rect)
            #MG2
            mg2_background = py.draw.rect(display_screen, ACOLOR, (175 + instr_buttonx + 25, 285, 525, instr_buttony))
            with open(path.join(high_dir, mg2_highscore), 'r') as f:
                try:
                    self.mg2_highscore = int(f.read())
                except:
                    self.mg2_highscore = 0

            text_surf, text_rect = self.func.text_objects("Highscore {}".format(str(self.mg2_highscore)), small_text,
                                                          WHITE)
            text_rect.center = ((175 + instr_buttonx + 25) + 525/2, 285 + instr_buttony/2)
            display_screen.blit(text_surf, text_rect)
            #MG3
            mg3_background = py.draw.rect(display_screen, ACOLOR, (175 + instr_buttonx + 25, 365, 525, instr_buttony))
            with open(path.join(high_dir, mg3_highscore), 'r') as f:
                try:
                    self.mg3_highscore = int(f.read())
                except:
                    self.mg3_highscore = 0

            text_surf, text_rect = self.func.text_objects("Highscore {}".format(str(self.mg3_highscore)), small_text,
                                                          WHITE)
            text_rect.center = ((175 + instr_buttonx + 25) + 525/2, 365 + instr_buttony/2)
            display_screen.blit(text_surf, text_rect)
            #MG4
            mg4_background = py.draw.rect(display_screen, ACOLOR, (175 + instr_buttonx + 25, 445, 525, instr_buttony))
            with open(path.join(high_dir, mg4_highscore), 'r') as f:
                try:
                    self.mg4_highscore = int(f.read())
                except:
                    self.mg4_highscore = 0

            text_surf, text_rect = self.func.text_objects("Highscore {}".format(str(self.mg4_highscore)), small_text,
                                                          WHITE)
            text_rect.center = ((175 + instr_buttonx + 25) + 525/2, 445 + instr_buttony/2)
            display_screen.blit(text_surf, text_rect)

            #MG5
            mg5_background = py.draw.rect(display_screen, ACOLOR, (175 + instr_buttonx + 25, 525, 525, instr_buttony))
            with open(path.join(high_dir, mg5_highscore), 'r') as f:
                try:
                    self.mg5_highscore = int(f.read())
                except:
                    self.mg5_highscore = 0

            text_surf, text_rect = self.func.text_objects("Highscore {}".format(str(self.mg5_highscore)), small_text,
                                                          WHITE)
            text_rect.center = ((175 + instr_buttonx + 25) + 525/2, 525 + instr_buttony/2)
            display_screen.blit(text_surf, text_rect)

            # Total
            total_background = py.draw.rect(display_screen, ACOLOR, (175 + instr_buttonx + 25, 125, 525, instr_buttony))
            self.total_score = self.mg1_highscore + self.mg2_highscore + self.mg3_highscore + self.mg4_highscore +\
                               self.mg5_highscore

            text_surf, text_rect = self.func.text_objects("Total score {}".format(str(self.total_score)), small_text,
                                                          WHITE)
            text_rect.center = ((175 + instr_buttonx + 25) + 525 / 2, 125 + instr_buttony / 2)
            display_screen.blit(text_surf, text_rect)

            #EVENT HANDLER
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    mouse_pos = py.mouse.get_pos()
                    if self.back_button.collidepoint(mouse_pos):
                        running = False


            py.display.update()

