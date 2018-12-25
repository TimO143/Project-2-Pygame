from Values import *
from MG4_Values import *

class Starschip(py.sprite.Sprite):
    # This class represents a starschip

    def __init__(self, arrow1, arrow2, arrow3, arrow4, img, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the picture and remove the black background
        self.image = img
        self.image = py.transform.rotate(self.image, 270)
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 552
        self.naarhanger = False

        # Standaard variablen bepalen.
        self.arrow1 = arrow1
        self.arrow2 = arrow2
        self.arrow3 = arrow3
        self.arrow4 = arrow4

        self.color = color
        self.gotohanger = False

        # Variablen voor deads
        self.dead = 0
        self.ep = 0

        # Variablen voor score
        self.score = 0
        self.sk = 0

    def update(self):
        #Standaard waarde bepaalen.

        self.dead = 0
        self.score = 0

        #Bepaal waar het vliegtuig heen beweegt.

        if(self.rect.x > 152 and self.rect.y == 552):
            #Landen op de landingsbaan.
            self.rect.x = self.rect.x - 8

        elif (self.rect.x <= 152 and self.rect.y == 552):
            #Draaien van landingsbaan naar de taxiebaan.
            self.image = py.transform.rotate(self.image, 270)
            self.rect.y = self.rect.y - 2
            self.rect.x = 152

        elif (self.rect.x == 152 and self.rect.y > 220):
            #Taxien op de taxiebaan.
            self.rect.y = self.rect.y - 2

        elif (self.rect.x == 152 and self.rect.y > 90 and self.arrow1 == True or
              self.rect.x == 152 and self.rect.y > 90 and self.gotohanger == True):
            #Naar de blauwe hanger taxien.
            self.rect.y = self.rect.y - 2
            self.gotohanger = True

        elif (self.rect.x == 152 and self.rect.y > 80 < 90 and self.arrow1 == True or
              self.rect.x == 152 and self.rect.y > 80 < 90 and self.gotohanger == True):
            #Naar de blauwe hanger taxien.
            self.remove(all_sprites_list)

            if self.color != "Blue":
                self.dead = self.dead + 1
            else:
                self.score = self.score + 10

        elif (self.rect.x == 152 and self.rect.y == 220):
            #Van het eerste kruispunt draaien.
            self.image = py.transform.rotate(self.image, 270)
            self.rect.x = self.rect.x + 2

        elif (self.rect.x == 410 and self.rect.y > 90 and self.arrow2 == True and self.naarhanger == False):
            #Naar de bruine hanger gaan.
            self.image = py.transform.rotate(self.image, 90)
            self.rect.y - self.rect.y - 2
            self.naarhanger = True
            self.gotohanger = True

        elif (self.rect.x == 410 and self.rect.y > 90 and self.arrow2 == True and self.naarhanger == True or
              self.rect.x == 410 and self.rect.y > 90 and self.gotohanger == True and self.naarhanger == True):
            #Naar de bruine hanger gaan.
            self.rect.y = self.rect.y - 2

        elif (self.rect.x == 410 and self.rect.y > 88 and self.arrow2 == True and self.naarhanger == True or
              self.rect.x == 410 and self.rect.y > 88 and self.gotohanger == True and self.naarhanger == True):
            #Verwijder het spaceschip als deze in bruine hanger is.
            self.remove(all_sprites_list)

            if self.color != "Brown":
                self.dead = self.dead + 1
            else:
                self.score = self.score + 10

        elif (self.rect.x >= 665 and self.rect.x < 667 and self.rect.y > 90 and self.arrow3 == True and self.naarhanger == False):
            #Naar de Groene hanger gaan.
            self.image = py.transform.rotate(self.image, 90)
            self.rect.y - self.rect.y - 2
            self.naarhanger = True
            self.gotohanger = True

        elif (self.rect.x >= 665 and self.rect.x < 667 and self.rect.y > 90 and self.arrow3 == True and self.naarhanger == True or
              self.rect.x >= 665 and self.rect.x < 667 and self.rect.y > 90 and self.gotohanger == True and self.naarhanger == True):
            #Naar de Groene hanger gaan.
            self.rect.y = self.rect.y - 2

        elif (self.rect.x >= 665 and self.rect.x < 667 and self.rect.y > 88 and self.arrow3 == True and self.naarhanger == True or
              self.rect.x >= 665 and self.rect.x < 667 and self.rect.y > 88 and self.gotohanger == True and self.naarhanger == True):
            #Verwijder de spaceschip als deze in groene hanger is.
            self.remove(all_sprites_list)

            if self.color != "Green":
                self.dead = self.dead + 1
            else:
                self.score = self.score + 10

        elif (self.rect.x >= 920 and self.rect.x < 922 and self.rect.y > 90 and self.arrow4 == True and self.naarhanger == False):
            #Naar de Paarse hanger gaan.
            self.image = py.transform.rotate(self.image, 90)
            self.rect.y - self.rect.y - 2
            self.naarhanger = True
            self.gotohanger = True

        elif (self.rect.x >= 920 and self.rect.x < 922 and self.rect.y > 90 and self.arrow4 == True and self.naarhanger == True or
              self.rect.x >= 920 and self.rect.x < 922 and self.rect.y > 90 and self.gotohanger == True and self.naarhanger == True):
            #Naar de Paarse hanger gaan.
            self.rect.y = self.rect.y - 2

        elif (self.rect.x >= 920 and self.rect.x < 922 and self.rect.y > 88 and self.arrow4 == True and self.naarhanger == True or
              self.rect.x >= 920 and self.rect.x < 922 and self.rect.y > 88 and self.gotohanger == True and self.naarhanger == True):
            #Verwijderen als het spaceschip in paarse hanger is..
            self.remove(all_sprites_list)

            if self.color != "Purple":
                self.dead = self.dead + 1
            else:
                self.score = self.score + 10

        elif (self.rect.x > 152 and self.rect.y == 220 and self.rect.x <= 1200):
            #De laatste taxiebaan af taxieén.
            self.rect.x = self.rect.x + 2

        elif (self.rect.x >= 1200 and self.rect.y == 220):
            #Als het spaceschip van de taxiebaan af rijd deze ook weer verwijderen.
            self.remove(all_sprites_list)
            self.dead = self.dead + 1


    def importarrow(self, arrow1, arrow2, arrow3, arrow4):
        #Importeer arrow positions.
        self.arrow1 = arrow1
        self.arrow2 = arrow2
        self.arrow3 = arrow3
        self.arrow4 = arrow4

    def exportdead(self):
        # Hier wordt de dead geexporteerd en de sprite gekilled als de dead gexporteerd is.
        if self.ep > 0:
            self.kill()

        self.ep = self.dead
        self.dead = 0
        return self.ep

    def exportscore(self):
        #Hier wordt de score gexporteert.
        self.sk = self.score
        self.score = 0
        return self.sk