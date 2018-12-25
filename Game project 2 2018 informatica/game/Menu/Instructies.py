import MG1_Game
import MG2_Game
import MG3_Game
import MG4_Game
import MG5_Game
import Functions
from Values import *


class Instructies:
    def __init__(self):
        self.func = Functions.Functions()
        self.mg1 = MG1_Game.Game()
        self.mg2 = MG2_Game.Game()
        self.mg3 = MG3_Game.Game()
        self.mg4 = MG4_Game.Game()
        self.mg5 = MG5_Game.Game()


    def loop(self, mg):
        py.display.set_caption("Instruction Menu")
        self.running = True
        self.mg = mg
        self.mg1_screen = mg1_instructions
        self.mg1_screen_selected = 1
        while self.running:

            if mg == "mg1":
                display_screen.blit(self.mg1_screen, (0,0))
                mg1_start_button = self.func.button("Start", WHITE, display_width - instr_buttonx - 20,
                                                    display_height - instr_buttony - 20,
                                                    instr_buttonx, instr_buttony, IACOLOR, ACOLOR)
                if self.mg1_screen_selected == 1:
                    mg1_screen1_selected_button = self.func.button("", WHITE, display_width - 96, 179,
                                                          52, 52, WHITE, WHITE)
                if self.mg1_screen_selected == 2:
                    mg1_screen2_selected_button = self.func.button("", WHITE, display_width - 96, 244,
                                                          52, 52, WHITE, WHITE)
                if self.mg1_screen_selected == 3:
                    mg1_screen3_selected_button = self.func.button("", WHITE, display_width - 96, 309,
                                                      52, 52, WHITE, WHITE)

                mg1_screen1_button = self.func.button("1", WHITE, display_width - 95, 180,
                                                      50, 50, IACOLOR, ACOLOR)
                mg1_screen2_button = self.func.button("2", WHITE, display_width - 95, 245,
                                                      50, 50, IACOLOR, ACOLOR)
                mg1_screen3_button = self.func.button("3", WHITE, display_width - 95, 310,
                                                      50, 50, IACOLOR, ACOLOR)



            if mg == "mg2":
                display_screen.blit(mg2_instructions, (0, 0))
                mg2_start_button = self.func.button("Start", WHITE, display_width - instr_buttonx - 20, display_height - instr_buttony - 20,
                                           instr_buttonx, instr_buttony, IACOLOR, ACOLOR)

            if mg == "mg3":
                display_screen.blit(mg3_instructions, (0, 0))
                mg3_start_button = self.func.button("Start", WHITE, display_width - instr_buttonx - 20, display_height - instr_buttony - 20,
                                           instr_buttonx, instr_buttony, IACOLOR, ACOLOR)
            if mg == "mg4":
                display_screen.blit(mg4_instructions, (0, 0))
                mg4_start_button = self.func.button("Start", WHITE, display_width - instr_buttonx - 20, display_height - instr_buttony- 20,
                                           instr_buttonx, instr_buttony, IACOLOR, ACOLOR)

            if mg == "mg5":
                display_screen.blit(mg5_instructions, (0, 0))
                mg5_start_button = self.func.button("Start", WHITE, display_width - instr_buttonx - 20, display_height - instr_buttony  - 20,
                                           instr_buttonx, instr_buttony, IACOLOR, ACOLOR)



            back_button = self.func.button("Back", WHITE, 20, display_height - instr_buttony - 20, instr_buttonx, instr_buttony,
                                           IACOLOR, ACOLOR)

            py.draw.rect(display_screen, ACOLOR, (display_width/2 - 400/2,
                                            display_height - instr_buttony - 20, 400, main_menu_buttony))
            text_surf, text_rect = self.func.text_objects("Druk op ESC om het spel te pauzeren !", small_text, WHITE)
            text_rect.centerx = display_width/2
            text_rect.centery = display_height - 45
            display_screen.blit(text_surf, text_rect)
            py.display.update()

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    mouse_pos = py.mouse.get_pos()
                    if mg == "mg1":
                        if  mg1_start_button.collidepoint(mouse_pos):
                            ret = self.mg1.loop()
                            if ret == 'main':
                                return 'main'
                        if mg1_screen1_button.collidepoint(mouse_pos):
                            self.mg1_screen_selected = 1
                            self.mg1_screen = mg1_instructions
                        if mg1_screen2_button.collidepoint(mouse_pos):
                            self.mg1_screen_selected = 2
                            self.mg1_screen = mg1_instructions2
                        if mg1_screen3_button.collidepoint(mouse_pos):
                            self.mg1_screen_selected = 3
                            self.mg1_screen = mg1_instructions3


                    if mg == "mg2":
                        if  mg2_start_button.collidepoint(mouse_pos):
                            ret = self.mg2.loop()
                            if ret == 'main':
                                return 'main'
                    if mg == "mg3":
                        if  mg3_start_button.collidepoint(mouse_pos):
                            ret = self.mg3.run()
                            if ret == 'main':
                                return 'main'

                    if mg == "mg4":
                        if  mg4_start_button.collidepoint(mouse_pos):
                            ret = self.mg4.loop()
                            if ret == 'main':
                                return 'main'
                    if mg == "mg5":
                        if  mg5_start_button.collidepoint(mouse_pos):
                            ret = self.mg5.run()
                            if ret == 'main':
                                return 'main'

                    if back_button.collidepoint(mouse_pos):
                        self.running = False

