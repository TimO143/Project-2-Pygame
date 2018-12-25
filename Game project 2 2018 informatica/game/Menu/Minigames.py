import Instructies
import Functions
from Values import *

class MiniGames():
    def __init__(self):
        self.func = Functions.Functions()
        self.instr = Instructies.Instructies()

    def loop(self):

        self.intro = True
        bg_y = 0
        while (self.intro):
            py.display.set_caption("Mini Games")
            rel_y = bg_y % bg.get_rect().height
            display_screen.blit(bg, (0, rel_y - bg.get_rect().height))
            if rel_y < display_height:
                display_screen.blit(bg, (0, rel_y))
            bg_y += 0.1



            self.mg1_button =self.func.button("Meteor Strike", WHITE, display_width / 2 - main_menu_buttonx / 2, 175,
                                              main_menu_buttonx, main_menu_buttony, IACOLOR, ACOLOR)

            self.mg2_button = self.func.button("Space Dodger", WHITE, display_width / 2 - main_menu_buttonx / 2, 250,
                                               main_menu_buttonx,
                                               main_menu_buttony, IACOLOR, ACOLOR)
            self.mg3_button = self.func.button("Strange Planet", WHITE, display_width / 2 - main_menu_buttonx / 2, 325,
                                               main_menu_buttonx,
                                               main_menu_buttony, IACOLOR, ACOLOR)
            self.mg4_button = self.func.button("Spaceship Parking", WHITE, display_width / 2 - main_menu_buttonx / 2, 400,
                                               main_menu_buttonx,
                                               main_menu_buttony, IACOLOR, ACOLOR)
            self.mg5_button = self.func.button("Space Maze", WHITE, display_width / 2 - main_menu_buttonx / 2, 475,
                                               main_menu_buttonx,
                                               main_menu_buttony, IACOLOR, ACOLOR)
            self.back_button = self.func.button("Back", WHITE, 20, display_height - instr_buttony - 20, instr_buttonx,
                                           instr_buttony,
                                           IACOLOR, ACOLOR)

            self.text_surface, self.text_rect = self.func.text_objects("MINIGAMES", large_text, WHITE)
            self.text_rect.center =  (display_width/2, 100)
            display_screen.blit(self.text_surface, self.text_rect)
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    self.mouse_pos = py.mouse.get_pos()
                    if self.back_button.collidepoint(self.mouse_pos):
                        self.intro = False
                    if self.mg1_button.collidepoint(self.mouse_pos):
                        ret = self.instr.loop("mg1")
                        if ret == 'main':
                            return 'main'
                    if self.mg2_button.collidepoint(self.mouse_pos):
                        ret = self.instr.loop("mg2")
                        if ret == 'main':
                            return 'main'
                    if self.mg3_button.collidepoint(self.mouse_pos):
                        ret = self.instr.loop("mg3")
                        if ret == 'main':
                            return 'main'
                    if self.mg4_button.collidepoint(self.mouse_pos):
                        ret = self.instr.loop("mg4")
                        if ret == 'main':
                            return 'main'
                    if self.mg5_button.collidepoint(self.mouse_pos):
                        ret = self.instr.loop("mg5")
                        if ret == 'main':
                            return 'main'


            py.display.update()
