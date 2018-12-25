import About
import Functions
from Highscore import Highscore
from Values import *
from Settings import Settings

#STARTSCREEN


class Main():
    def __init__(self, selected_vol, selected_music):
        self.selected_vol = selected_vol
        self.selected_music = selected_music

    def game_intro(self):

        self.about = About.About()
        self.func = Functions.Functions()
        self.high = Highscore()
        self.intro = True
        self.sett = Settings(self.selected_vol, self.selected_music)

        bg_y = 0
        while(self.intro):
            py.display.set_caption("Main")


            rel_y = bg_y % bg.get_rect().height
            display_screen.blit(bg, (0, rel_y - bg.get_rect().height))
            if rel_y < display_height:
                display_screen.blit(bg, (0, rel_y))
            bg_y += 0.1


            # BUTTONS
            mg_menu_button = self.func.button("Mini Games", WHITE, display_width / 2 - main_menu_buttonx / 2, 225,
                                              main_menu_buttonx, main_menu_buttony, IACOLOR, ACOLOR)

            highscores_button = self.func.button("Highscores", WHITE, display_width / 2 - main_menu_buttonx / 2, 300,
                                                 main_menu_buttonx, main_menu_buttony, IACOLOR, ACOLOR)


            settings_button = self.func.button("Settings", WHITE, display_width / 2 - main_menu_buttonx / 2, 375,
                main_menu_buttonx, main_menu_buttony, IACOLOR, ACOLOR)

            instr_menu_button = self.func.button("About", WHITE, display_width / 2 - main_menu_buttonx / 2, 450,
                                                 main_menu_buttonx, main_menu_buttony, IACOLOR, ACOLOR)

            exit_button = self.func.button("Exit", WHITE, 20, display_height - instr_buttony - 20, instr_buttonx, instr_buttony,
                                           IACOLOR, ACOLOR)



            # TEXT
            text_surface, text_rect = self.func.text_objects("MAIN MENU", large_text, WHITE)
            text_rect.center = (display_width/2, 150)
            display_screen.blit(text_surface, text_rect)

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    mouse_pos = py.mouse.get_pos()
                    if mg_menu_button.collidepoint(mouse_pos):
                        self.value = 'mini'
                        self.intro = False
                    if highscores_button.collidepoint(mouse_pos):
                        self.high.loop()
                    if instr_menu_button.collidepoint(mouse_pos):
                        self.about.loop()
                    if settings_button.collidepoint(mouse_pos):
                        self.selected_vol, self.selected_music = self.sett.loop()
                    if exit_button.collidepoint(mouse_pos):
                        py.quit()
                        quit()

            py.display.update()

        return self.selected_vol, self.selected_music,  self.value

