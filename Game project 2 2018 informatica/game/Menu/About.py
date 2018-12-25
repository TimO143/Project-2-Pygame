import Functions
from Values import *


class About():
    def __init__(self):
        self.func = Functions.Functions()
    def loop(self):
        self.intro = True
        py.display.set_caption("About")
        while (self.intro):
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    mouse_pos = py.mouse.get_pos()
                    if back_button.collidepoint(mouse_pos):
                        self.intro = False
            display_screen.blit(bg_about, (0,0))
            back_button = self.func.button("Back", WHITE, 20, display_height - instr_buttony - 20, instr_buttonx,
                                           instr_buttony,
                                           IACOLOR, ACOLOR)
            py.display.update()
