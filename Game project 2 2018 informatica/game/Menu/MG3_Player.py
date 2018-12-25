from Values import *


class Player(py.sprite.Sprite):
    def __init__(self,x , y ,game):
        py.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames_r[0]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lives = 3

        """ houd bij welke kant de player voor het laatst naar is gericht """
        self.faceright = True

        """ snelheid in de x en y richting """
        self.speed_x = 0
        self.speed_y = 0

    """ laden van images uit spritesheets """
    def load_images(self):
        self.standing_frames_r = [self.game.spritesheet.get_image(32, 18, 64, 129),
                                self.game.spritesheet.get_image(144, 18, 64, 129),]
        for frame in self.standing_frames_r:
            frame.set_colorkey(GREEN)

        self.standing_frames_l = []
        for frame in self.standing_frames_l:
            frame.set_colorkey(GREEN)
        for frame in self.standing_frames_r:
            self.standing_frames_l.append(py.transform.flip(frame, True, False))

        self.walk_frames_r = [ self.game.spritesheet.get_image(22, 161, 80, 126),
                             self.game.spritesheet.get_image(129, 161, 76, 125),
                             self.game.spritesheet.get_image(242, 163, 73, 124),
                             self.game.spritesheet.get_image(349, 162, 82, 125),
                             self.game.spritesheet.get_image(457, 162, 85, 125),
                             self.game.spritesheet.get_image(565, 161, 83, 126),
                             self.game.spritesheet.get_image(675, 162, 81, 125),
                             self.game.spritesheet.get_image(773, 163, 71, 125),
                             self.game.spritesheet.get_image(864, 163, 81, 125),]
        for frame in self.walk_frames_r:
            frame.set_colorkey(GREEN)

        self.walk_frames_l = []
        for frame in self.walk_frames_l:
            frame.set_colorkey(GREEN)
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(py.transform.flip(frame, True, False))        # horizontal True, Vertical False

            """ dit wordt op het moment niet gebruikt """
        self.jump_frame_r = [self.game.spritesheet.get_image(22, 295, 76, 131),
                             self.game.spritesheet.get_image(130, 295, 76, 131),
                             self.game.spritesheet.get_image(241, 294, 76, 131),
                             self.game.spritesheet.get_image(351, 297, 76, 131),]
        for frame in self.jump_frame_r:
            frame.set_colorkey(GREEN)

        self.jump_frame_l = []
        for frame in self.jump_frame_l:
            frame.set_colorkey(GREEN)
        for frame in self.jump_frame_l:
            self.jump_frame_l.append(py.transform.flip(frame, True, False))        # horizontal True, Vertical False

    """ animatie toevoegen voor player"""
    def animate(self):
        now = py.time.get_ticks()
        if self.speed_x !=0:
            self.walking = True
        else:
            self.walking = False

        """ Loop animatie """
        if self.walking:
            if now - self.last_update > 100:                #lager dan beweegt player animatie sneller
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_r)
            if self.speed_x > 0:
                self.image = self.walk_frames_r[self.current_frame]
            else:
                self.image = self.walk_frames_l[self.current_frame]

        """ stilstaan animatie """
        if not self.jumping and not self.walking:
            if now - self.last_update > 400:            #mili seconden die voorbij zijn gegaan  hoe hoger , hoe slomer
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames_r)
                if self.faceright:
                    self.image = self.standing_frames_r[self.current_frame]
                else:
                    self.image = self.standing_frames_l[self.current_frame]

    """ Zwaartekracht voor player """
    def calc_grav(self):
        if self.speed_y == 0:
            self.speed_y = 1
        else:
            self.speed_y += 0.91  # verander gravity

    """ Jump alleen als player op platform staat """
    def jump(self):
        self.rect.y += 2    #2 pixel lager dan player
        hits = py.sprite.spritecollide(self, self.game.platforms, False)  #collide zelf met platform
        self.rect.y -= 2    #move rect weer omhoog
        # If it is ok to jump, set our speed upwards
        if len(hits) > 0:
            self.speed_y = -21             #spring hoogte in values

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.speed_x = -6                   #snelheid links
        self.faceright = False              #hierdoor worden alle sprites van stand naar links gezet

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.speed_x = 6                    #snelheid rechts in values
        self.faceright = True               #hierdoor worden alle sprites van stand naar rechts gezet

    """ als er geen keypress is dan beweegt player niet """
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.speed_x = 0               #stoppen van player

    def update(self):
        self.animate()
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.speed_x

        """ collision check met platform list x richting """
        block_hit_list = py.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.speed_x > 0:
                self.rect.right = block.rect.left
            elif self.speed_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.speed_y

        """ collision check met platform list y richting """
        block_hit_list = py.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.speed_y > 0:
                self.rect.bottom = block.rect.top
            elif self.speed_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.speed_y = 0