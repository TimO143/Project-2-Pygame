from Values import *


class Powerup(py.sprite.Sprite):
    def __init__(self, center, score, lives):
        py.sprite.Sprite.__init__(self)
        if score > 500:
            self.type = random.choice(['shield', 'gunx2', 'gunx3', 'heart'])
        else:
            self.type = random.choice(['shield', 'gunx2'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed_y = 4

    def update(self):
        self.rect.y += self.speed_y
        # kill if it moves off screen
        if self.rect.top > display_height:
            self.kill()
