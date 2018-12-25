from Main import Main
from Minigames import MiniGames


class Game():
    def __init__(self):
        self.selected_music = ""
        self.selected_vol = 0
    def loop(self):
        running = True
        self.main = Main(self.selected_vol, self.selected_music)
        self.mini = MiniGames()
        while running:
            self.selected_vol, self.selected_music, value = self.main.game_intro()
            if value == "mini":
                value = self.mini.loop()


if __name__ == "__main__":
    g = Game()
    g.loop()

