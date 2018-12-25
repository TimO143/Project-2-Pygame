from Values import *
from Functions import Functions

class Settings():
    def __init__(self, selected_vol, selected_music):
        self.func = Functions()
        self.selected_music = selected_music
        self.selected_vol = selected_vol


    def loop(self):
        bg_y = 0
        running = True
        py.display.set_caption("Settings")
        while running:
            #DRAWING

            rel_y = bg_y % bg.get_rect().height
            display_screen.blit(bg, (0, rel_y - bg.get_rect().height))
            if rel_y < display_height:
                display_screen.blit(bg, (0, rel_y))
            bg_y += 0.1

            self.background = self.func.button("", BLACK, 150, 100, 800, 500, IACOLOR, IACOLOR)
            self.back_button = self.func.button("Back", WHITE, 20, display_height - instr_buttony - 20, instr_buttonx,
                                                instr_buttony,
                                                IACOLOR, ACOLOR)
            # DRAW HIGHLIGHT SELECTION
            if self.selected_vol == 1:
                vol1_select_button = self.func.button("", WHITE, 258, self.background.top + 108, 79,
                                                    79, WHITE, WHITE)
            if self.selected_vol == 2:
                vol2_select_button = self.func.button("", WHITE, 383, self.background.top + 108, 79,
                                                    79, WHITE, WHITE)
            if self.selected_vol == 3:
                vol3_select_button = self.func.button("", WHITE, 508, self.background.top + 108, 79,
                                                    79, WHITE, WHITE)
            if self.selected_vol == 4:
                vol4_select_button = self.func.button("", WHITE, 633, self.background.top + 108, 79,
                                                    79, WHITE, WHITE)
            if self.selected_vol == 5:
                vol5_select_button = self.func.button("", WHITE, 758, self.background.top + 108, 79,
                                                    79, WHITE, WHITE)

            if self.selected_music == "":
                music_off_select_button = self.func.button("", WHITE, 284, self.background.bottom - 202, 129,
                                                    129, WHITE, WHITE)
            if self.selected_music == "StarTrip.mp3":
                music_1_select_button = self.func.button("", WHITE, 484, self.background.bottom - 202, 129,
                                                129, WHITE, WHITE)
            if self.selected_music == "DarkOrbit.ogg":self.func.button("Dark Orbit", WHITE, 684, self.background.bottom - 202,
                                                                  129, 129, WHITE, WHITE)


            #DRAW BUTTONS

            vol1_button = self.func.button("1", WHITE, 260, self.background.top + 110, 75,
                                                75, ACOLOR, ACOLOR)
            vol2_button = self.func.button("2", WHITE, 385, self.background.top + 110, 75,
                                                75, ACOLOR, ACOLOR)
            vol3_button = self.func.button("3", WHITE, 510, self.background.top + 110, 75,
                                                75, ACOLOR, ACOLOR)
            vol4_button = self.func.button("4", WHITE, 635, self.background.top + 110, 75,
                                                75, ACOLOR, ACOLOR)
            vol5_button = self.func.button("5", WHITE, 760, self.background.top + 110, 75,
                                                75, ACOLOR, ACOLOR)

            #DRAW MUSIC BUTTONS
            music_off_button = self.func.button("Music OFF", WHITE, 286, self.background.bottom - 200, 125,
                                              125, ACOLOR, ACOLOR)
            music_1_button = self.func.button("Star Trip", WHITE, 486, self.background.bottom - 200, 125,
                                                125, ACOLOR, ACOLOR)
            music_2_button = self.func.button("Dark Orbit", WHITE, 686, self.background.bottom - 200, 125,
                                              125, ACOLOR, ACOLOR)

            #DRAW TEXT
            text_surf, text_rect = self.func.text_objects("SETTINGS", medium_text, WHITE)
            text_rect.center = (self.background.centerx, self.background.top - 25)
            display_screen.blit(text_surf, text_rect)

            text_surf, text_rect = self.func.text_objects("VOLUME", small_text, WHITE)
            text_rect.center = (self.background.centerx - 5, self.background.top + 75)
            display_screen.blit(text_surf, text_rect)

            text_surf, text_rect = self.func.text_objects("MUSIC", small_text, WHITE)
            text_rect.center = (self.background.centerx - 5, self.background.top + 250)
            display_screen.blit(text_surf, text_rect)

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    self.mouse_pos  = py.mouse.get_pos()
                    #SELECT VOLUME
                    if self.back_button.collidepoint(self.mouse_pos):
                        running = False

                    if vol1_button.collidepoint(self.mouse_pos):
                        self.selected_vol = 1
                        if self.selected_music != "":
                            py.mixer.music.stop()
                            py.mixer.music.load(path.join(snd_dir, self.selected_music))
                            py.mixer.music.set_volume(0.2)
                            py.mixer.music.play(loops=-1)

                    if vol2_button.collidepoint(self.mouse_pos):
                        self.selected_vol = 2
                        if self.selected_music != "":
                            py.mixer.music.stop()
                            py.mixer.music.load(path.join(snd_dir, self.selected_music))
                            py.mixer.music.set_volume(0.4)
                            py.mixer.music.play(loops=-1)

                    if vol3_button.collidepoint(self.mouse_pos):
                        self.selected_vol = 3
                        if self.selected_music != "":
                            py.mixer.music.stop()
                            py.mixer.music.load(path.join(snd_dir, self.selected_music))
                            py.mixer.music.set_volume(0.6)
                            py.mixer.music.play(loops=-1)

                    if vol4_button.collidepoint(self.mouse_pos):
                        self.selected_vol = 4
                        if self.selected_music != "":
                            py.mixer.music.stop()
                            py.mixer.music.load(path.join(snd_dir, self.selected_music))
                            py.mixer.music.set_volume(0.8)
                            py.mixer.music.play(loops=1)

                    if vol5_button.collidepoint(self.mouse_pos):
                        self.selected_vol = 5
                        if self.selected_music != "":
                            py.mixer.music.stop()
                            py.mixer.music.load(path.join(snd_dir, self.selected_music))
                            py.mixer.music.set_volume(1)
                            py.mixer.music.play(loops=-1)

                    #MUSIC
                    if music_off_button.collidepoint(self.mouse_pos):
                        self.selected_music = ""
                        self.selected_vol = 0
                        py.mixer.music.stop()
                    if music_1_button.collidepoint(self.mouse_pos):
                        self.selected_vol = 1
                        self.selected_music = "StarTrip.mp3"
                        py.mixer.music.load(path.join(snd_dir, self.selected_music))
                        py.mixer.music.set_volume(0.1)
                        py.mixer.music.play(loops=-1)
                    if music_2_button.collidepoint(self.mouse_pos):
                        self.selected_vol = 1
                        self.selected_music = "DarkOrbit.ogg"
                        py.mixer.music.load(path.join(snd_dir, self.selected_music))
                        py.mixer.music.set_volume(0.1)
                        py.mixer.music.play(loops=-1)
            py.display.update()
        return (self.selected_vol, self.selected_music)