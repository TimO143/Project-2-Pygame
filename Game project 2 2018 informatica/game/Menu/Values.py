import pygame as py
import os
from os import path
import random

#INITIALIZE
py.init()
py.mixer.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
py.display.set_caption("Main")

# DISPLAY
display_width = 1100
display_height = 700
display_screen = py.display.set_mode((display_width,display_height))

# BUTTONS
main_menu_buttonx = 500
main_menu_buttony = 50
instr_buttonx = 200
instr_buttony = 50

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
IACOLOR = (52, 52, 79)
ACOLOR = (48, 48, 66)


# TEXT
large_text = py.font.Font("C:\Windows\Fonts\guardians.ttf", 30)
medium_text = py.font.Font("C:\Windows\Fonts\guardians.ttf", 22)
small_text = py.font.Font("C:\Windows\Fonts\HELR65W.ttf", 15)
small_text_highlight = py.font.Font("C:\Windows\Fonts\HELR65W.ttf", 20)
game_over_text = py.font.Font("C:\Windows\Fonts\guardians.ttf", 80)

# CLOCK
clock = py.time.Clock()
clock = py.time.Clock()
FPS = 60

#DIRS
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
high_dir = path.join(path.dirname(__file__), 'high')


#HIGHSCORE FILE
mg1_highscore = 'mg1_highscore.txt'
mg2_highscore = 'mg2_highscore.txt'
mg3_highscore = 'mg3_highscore.txt'
mg4_highscore = 'mg4_highscore.txt'
mg5_highscore = 'mg5_highscore.txt'


# GAME MUSIC

# SOUNDS MG1 - METEOR STRIKE - BERKAY
shoot_sound = py.mixer.Sound(path.join(snd_dir, "Pew.wav"))
shoot_sound.set_volume(0.4)
expl_sound = py.mixer.Sound(path.join(snd_dir, "Explosion1.wav"))
expl_sound.set_volume(0.4)



# BACKGROUND IMAGES
bg = py.image.load(path.join(img_dir, "background.jpg")).convert()
bg = py.transform.scale(bg, (display_width,display_height))

bg_about = py.image.load(path.join(img_dir, "bg_about.png")).convert()
bg_about = py.transform.scale(bg_about, (display_width, display_height))

#INSTRUCTIES MENU IMAGES
mg1_instructions = py.image.load(path.join(img_dir, "mg1_instructie_scherm.png")).convert()
mg1_instructions = py.transform.scale(mg1_instructions, (display_width, display_height))

mg1_instructions2 = py.image.load(path.join(img_dir, "mg1_instructie_scherm2.png")).convert()
mg1_instructions2 = py.transform.scale(mg1_instructions2, (display_width, display_height))

mg1_instructions3 = py.image.load(path.join(img_dir, "mg1_instructie_scherm3.png")).convert()
mg1_instructions3 = py.transform.scale(mg1_instructions3, (display_width, display_height))

mg2_instructions = py.image.load(path.join(img_dir, "mg2_instructie_scherm.png")).convert()
mg2_instructions = py.transform.scale(mg2_instructions, (display_width, display_height))

mg3_instructions = py.image.load(path.join(img_dir, "mg3_instructie_scherm.png")).convert()
mg3_instructions = py.transform.scale(mg3_instructions, (display_width, display_height))

mg4_instructions = py.image.load(path.join(img_dir, "mg4_instructie_scherm.png")).convert()
mg4_instructions = py.transform.scale(mg4_instructions, (display_width, display_height))

mg5_instructions = py.image.load(path.join(img_dir, "mg5_instructie_scherm.png")).convert()
mg5_instructions = py.transform.scale(mg5_instructions, (display_width, display_height))

mg6_instructions = py.image.load(path.join(img_dir, "mg6_instructie_scherm.png")).convert()
mg6_instructions = py.transform.scale(mg6_instructions, (display_width, display_height))



#IMAGES MG1 - METEOR STRIKE - BERKAY

mg1_background2 = py.image.load(path.join(img_dir, "mg1_background2.jpg")).convert()
mg1_background2 = py.transform.scale(mg1_background2, (display_width, display_height))

mg1_background3 = py.image.load(path.join(img_dir, "mg1_background3.jpg")).convert()
mg1_background3 = py.transform.scale(mg1_background3, (display_width, display_height))

player_img = py.image.load(path.join(img_dir, "mg1_player_img.png")).convert()
player_img = py.transform.scale(player_img, (50, 50))

mg1_lives = py.image.load(path.join(img_dir, "mg4_full_heart.png"))
mg1_lives = py.transform.scale(mg1_lives, (40,40))

laser_red = py.image.load(path.join(img_dir, "mg1_laser_red.png")).convert()
laser_red = py.transform.scale(laser_red, (20,20))

laser_blue = py.image.load(path.join(img_dir, 'mg1_laserBlue11.png'))
laser_blue = py.transform.scale(laser_blue, (20, 20))

laser_green = py.image.load(path.join(img_dir, 'mg1_laserGreen15.png'))
laser_green = py.transform.scale(laser_green, (20,20))

mg1_boss1_laser1 = py.image.load(path.join(img_dir, "mg1_boss1_laser1.png"))
mg1_boss1_laser1 = py.transform.scale(mg1_boss1_laser1, (15,30))

mg1_boss1_laser2 = py.image.load(path.join(img_dir, "mg1_boss1_laser2.png"))
mg1_boss1_laser2 = py.transform.scale(mg1_boss1_laser2, (25,25))

mg1_boss1_laser3 = py.image.load(path.join(img_dir, "mg1_boss1_laser3.png"))
mg1_boss1_laser3 = py.transform.scale(mg1_boss1_laser3, (25,25))

mg1_boss2_laser1 = py.image.load(path.join(img_dir, "mg1_boss2_laser1.png"))
mg1_boss2_laser1 = py.transform.scale(mg1_boss2_laser1, (15,30))

mg1_boss2_laser2 = py.image.load(path.join(img_dir, "mg1_boss2_laser2.png"))
mg1_boss2_laser2 = py.transform.scale(mg1_boss2_laser2, (25,25))

mg1_boss3_laser1 = py.image.load(path.join(img_dir, "mg1_boss3_laser1.png"))
mg1_boss3_laser1 = py.transform.scale(mg1_boss3_laser1, (20,20))

mg1_boss3_laser3 = py.image.load(path.join(img_dir, "mg1_boss3_laser3.png"))
mg1_boss3_laser3 = py.transform.scale(mg1_boss3_laser3, (25,25))

meteor_images = []
meteor_list = ['mg1_meteorBrown_big1.png', 'mg1_meteorBrown_big2.png', 'mg1_meteorBrown_med1.png',
               'mg1_meteorBrown_med1.png', 'mg1_meteorBrown_small1.png', 'mg1_meteorBrown_small1.png',
               'mg1_meteorBrown_tiny1.png']
for meteor in meteor_list:
    meteor_images.append(py.image.load(path.join(img_dir, meteor)).convert())

stone_meteor_images = []
stone_meteor_list = ['mg1_meteorGrey_big1.png', 'mg1_meteorGrey_big2.png', 'mg1_meteorGrey_med1.png',
                     'mg1_meteorGrey_med1.png', 'mg1_meteorGrey_small1.png', 'mg1_meteorGrey_small1.png',
                     'mg1_meteorGrey_tiny1.png']
for meteor in stone_meteor_list:
    stone_meteor_images.append(py.image.load(path.join(img_dir, meteor)).convert())

stone_meteor_big1_hit = py.image.load(path.join(img_dir, 'mg1_meteorGrey_big1_hit.png'))
stone_meteor_big2_hit = py.image.load(path.join(img_dir, 'mg1_meteorGrey_big2_hit.png'))
stone_meteor_med1_hit = py.image.load(path.join(img_dir, 'mg1_meteorGrey_med1_hit.png'))
stone_meteor_small1_hit = py.image.load(path.join(img_dir, 'mg1_meteorGrey_small1_hit.png'))
stone_meteor_tiny1_hit = py.image.load(path.join(img_dir, 'mg1_meteorGrey_tiny1_hit.png'))


explosion_anim = {}
explosion_anim['large'] = []
explosion_anim['small'] = []
explosion_anim['mega'] = []
for i  in range(9):
    filename = 'mg1_explosion{}.png'.format(i)
    img = py.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_large = py.transform.scale(img, (75,75))
    explosion_anim['large'].append(img_large)
    img_small = py.transform.scale(img, (32,32))
    explosion_anim['small'].append(img_small)
    img_mega = py.transform.scale(img, (120, 120))
    explosion_anim['mega'].append(img_mega)

powerup_images = {}
powerup_images['shield']  = py.image.load(path.join(img_dir, "mg1_shield_gold.png"))
powerup_images['gunx2'] = py.image.load(path.join(img_dir, "mg1_bolt_gold.png"))
powerup_images['gunx3'] = py.image.load(path.join(img_dir, "mg1_powerup3.png"))

powerup_images['heart'] = mg1_lives

spawn_shield = py.image.load(path.join(img_dir, "mg1_shield.png"))
spawn_shield = py.transform.scale(spawn_shield, (90, 80))
spawn_shield.set_colorkey(BLACK)

alien_round2 = py.image.load(path.join(img_dir, "mg1_alien_round2.png"))
alien_round2 = py.transform.scale(alien_round2, (80, 80))

alien_round2_hit = py.image.load(path.join(img_dir, "mg1_alien_round2_hit.png"))
alien_round2_hit = py.transform.scale(alien_round2_hit, (80,80))

alien_round2_shield = py.image.load(path.join(img_dir, "mg1_alien_round2_shield.png"))
alien_round2_shield = py.transform.scale(alien_round2_shield, (80,80))

alien_round4 = py.image.load(path.join(img_dir, "mg1_alien_round4.png"))
alien_round4 = py.transform.scale(alien_round4, (100,100))

alien_round4_hit = py.image.load(path.join(img_dir, "mg1_alien_round4_hit.png"))
alien_round4_hit = py.transform.scale(alien_round4_hit, (100,100))

alien_round4_shield = py.image.load(path.join(img_dir, "mg1_alien_round4_shield.png"))
alien_round4_shield = py.transform.scale(alien_round4_shield, (100,100))

alien_round6 = py.image.load(path.join(img_dir, "mg1_alien_round6.png"))
alien_round6 = py.transform.scale(alien_round6, (120,120))

alien_round6_hit = py.image.load(path.join(img_dir, "mg1_alien_round6_hit.png"))
alien_round6_hit = py.transform.scale(alien_round6_hit, (120,120))

alien_round6_shield = py.image.load(path.join(img_dir, "mg1_alien_round6_shield.png"))
alien_round6_shield = py.transform.scale(alien_round6_shield, (120,120))

# IMAGES MG2 - SPACE DODGER - PERRY
pleft_img = py.image.load(path.join(img_dir, 'mg2_astroLeft.png')).convert()
pright_img = py.image.load(path.join(img_dir, 'mg2_astroRight.png')).convert()
astr_img = py.image.load(path.join(img_dir, 'mg2_astroidMob.png')).convert()
astr_img2 = py.image.load(path.join(img_dir, 'mg2_astroidMob2.png')).convert()
hit_img = py.image.load(path.join(img_dir, 'mg2_dmg_sprite.png')).convert()



# IMAGES MG3 - STRANGE PLANET - TIM
grass = py.image.load(path.join(img_dir,"mg3_grass.png")).convert()
grass = py.transform.scale(grass, (64, 64))         #grootte die wordt getoond op scherm

ground = py.image.load(path.join(img_dir,"mg3_grassCenter.png")).convert()
ground = py.transform.scale(ground, (64, 64))         #grootte die wordt getoond op scherm

ice = py.image.load(path.join(img_dir,"mg3_snow.png")).convert()
ice = py.transform.scale(ice, (64, 64))         #grootte die wordt getoond op scherm

ice_ground = py.image.load(path.join(img_dir,"mg3_snow_ground.png")).convert()
ice_ground = py.transform.scale(ice_ground, (64, 64))         #grootte die wordt getoond op scherm

coin = py.image.load(path.join(img_dir,"mg3_coinGold.png")).convert()
coin = py.transform.scale(coin, (64, 64))

spring = py.image.load(path.join(img_dir,"mg3_springveer.png")).convert()
spring = py.transform.scale(spring, (64, 64))
spring_left = py.transform.rotate(spring,90)
spring_right = py.transform.rotate(spring,-90)
spring_down = py.transform.rotate(spring,180)

flag = py.image.load(path.join(img_dir,"mg3_flagBlue1.png")).convert()
flag = py.transform.scale(flag, (64, 64))

flag_ice = py.image.load(path.join(img_dir,"mg3_flag_ice.png")).convert()
flag_ice = py.transform.scale(flag_ice, (64, 64))

board_hard = py.image.load(path.join(img_dir,'mg3_hard.png')).convert()
board_easy = py.image.load(path.join(img_dir,'mg3_easy.png')).convert()
easter_egg = py.image.load(path.join(img_dir,'mg3_easter_egg.png')).convert()
uitleg = py.image.load(path.join(img_dir,'mg3_uitleg.png')).convert()

SPRITESHEET = 'mg3_AstroSpritesheet.png'
spritesheet1 = py.image.load(path.join(img_dir,'mg3_AstroSpritesheet.png')).convert()

SPRITESHEET_ENEMY = 'mg3_enemy_sheet.png'
spritesheet_enemy = py.image.load(path.join(img_dir,'mg3_enemy_sheet.png')).convert()

# SOUND MG3- STRANGE PLANET - TIM
invincible_sound = py.mixer.Sound(path.join(snd_dir,'snd3_invincible.wav'))
invincible_sound.set_volume(0.7)
coin_sound = py.mixer.Sound(path.join(snd_dir,'snd3_coin.wav'))
coin_sound.set_volume(0.5)
hp_up_sound = py.mixer.Sound(path.join(snd_dir,'snd3_hp_up.wav'))
hp_up_sound.set_volume(1)
springveer_sound = py.mixer.Sound(path.join(snd_dir,'snd3_springveer.wav'))
springveer_sound.set_volume(0.5)


# IMAGES MG4 - SPACESHIP PARKING - DION
bg_airport = py.image.load(path.join(img_dir, "mg4_airport_img.png")).convert()
bg_airport = py.transform.scale(bg_airport, (display_width,display_height))

Full_heart = py.image.load(path.join(img_dir, "mg4_full_heart.png"))
Full_heart = py.transform.scale(Full_heart, (40,40))

Empty_heart = py.image.load(path.join(img_dir, "mg4_empty_heart.png"))
Empty_heart = py.transform.scale(Empty_heart, (40,40))

ufo_img_blue = py.image.load(path.join(img_dir, "mg4_ufo_Blue.png")).convert()
ufo_img_blue = py.transform.scale(ufo_img_blue, (80, 80))

ufo_img_green = py.image.load(path.join(img_dir, "mg4_ufo_Green.png")).convert()
ufo_img_green = py.transform.scale(ufo_img_green, (80, 80))

ufo_img_red = py.image.load(path.join(img_dir, "mg4_ufo_Red.png")).convert()
ufo_img_red = py.transform.scale(ufo_img_red, (80, 80))

ufo_img_yellow = py.image.load(path.join(img_dir, "mg4_ufo_Yellow.png")).convert()
ufo_img_yellow = py.transform.scale(ufo_img_yellow, (80, 80))

starschip1_img = py.image.load(path.join(img_dir, "mg4_starschip1.png")).convert()
starschip1_img = py.transform.scale(starschip1_img, (80, 80))

starschip2_img = py.image.load(path.join(img_dir, "mg4_starschip2.png")).convert()
starschip2_img = py.transform.scale(starschip2_img, (80, 80))

starschip3_img = py.image.load(path.join(img_dir, "mg4_starschip3.png")).convert()
starschip3_img = py.transform.scale(starschip3_img, (80, 80))

starschip4_img = py.image.load(path.join(img_dir, "mg4_starschip4.png")).convert()
starschip4_img = py.transform.scale(starschip4_img, (80, 80))

arrowupwidth = 28
arrowuphight = 34

Arrowright_img = py.image.load(path.join(img_dir, "mg4_Arrow right.png"))
Arrowright_img = py.transform.scale(Arrowright_img, (arrowuphight, arrowupwidth))

Arrowup_img = py.image.load(path.join(img_dir, "mg4_Arrow up.png"))
Arrowup_img = py.transform.scale(Arrowup_img, (arrowupwidth, arrowuphight))

Hanger_Blue_img = py.image.load(path.join(img_dir, "mg4_Hanger_blue.png"))
Hanger_Blue_img = py.transform.scale(Hanger_Blue_img, (145, 186))

Hanger_Brown_img = py.image.load(path.join(img_dir, "mg4_Hanger_Brown.png"))
Hanger_Brown_img = py.transform.scale(Hanger_Brown_img, (145, 186))

Hanger_Groen_img = py.image.load(path.join(img_dir, "mg4_Hanger_Groen.png"))
Hanger_Groen_img = py.transform.scale(Hanger_Groen_img, (145, 186))

Hanger_Paarse_img = py.image.load(path.join(img_dir, "mg4_Hanger_Paarse.png"))
Hanger_Paarse_img = py.transform.scale(Hanger_Paarse_img, (145, 186))


#IMAGES MG5 - SPACEWAY RACER - WOUTER
mg5_player_img = py.image.load(path.join(img_dir, "mg5_player_img.png")).convert()
mg5_player_img = py.transform.scale(mg5_player_img, (100, 100))
mg5_player_img.set_colorkey(BLACK)
finish = py.image.load(path.join(img_dir, "Finish.png")).convert_alpha()
finish = py.transform.scale(finish, (100, 100))
finish.set_colorkey(BLACK)
wall_img = py.image.load(path.join(img_dir, "Wall_img.png")).convert()
wall_img = py.transform.scale(wall_img, (128, 128))
mob_img = py.image.load(path.join(img_dir, "transparent_enemy.png")).convert_alpha()
mob_img = py.transform.scale(mob_img, (100, 100))
#mob_img.set_colorkey(BLACK)

TILESIZE = 128
GRIDWIDTH = display_width / TILESIZE
GRIDHEIGHT = display_height / TILESIZE

# Player settings
PLAYER_SPEED = 300.0
PLAYER_ROT_SPEED = 150.0
PLAYER_IMG = 'mg5_player_img.png'
PLAYER_HIT_RECT = py.Rect(0, 0, 35, 35)

# Finish settings
FINISH_IMG = 'Finish.png'
WALL_IMG = 'Wall_img.png'

#Mob settings
MOB_IMG = 'transparent_enemy.png'




#TIM
# Tim
HALF_WIDTH = int(display_width / 2)
HALF_HEIGHT = int(display_height / 2)
FONT_NAME = 'arial'

# Game settings Tim
TITLE = "Strange Planet"
GRAV = 0.91
JUMP_HOOGTE = -25
MOVE_LEFT = -6
MOVE_RIGHT = 6







