# Import modules
import pygame, sys
from pygame.locals import *
from lib import enemies, heroes, items
from grid import *
import random
from key_events import KeyEvents
import math

# Instances of Game Objects
PLAYER = heroes.LINK()
key_events = KeyEvents(PLAYER)
WAND = items.WAND()
GOLD = items.GOLD()
SWORD = items.SWORD()
SHIELD = items.SHIELD()
BOW = items.BOW()
GANON = enemies.GANNON()
PORTAL = enemies.PORTAL()
TEMPLE = TEMPLE()
MIDNA = heroes.MIDNA()

# Goup related game objects together
GAME_ITEMS = [WAND, SWORD, SHIELD]
GAME_WEAPONS = [WAND, BOW]
BEAST_LIST = []
orbs_list = []

# Other config
INVFONT = pygame.font.SysFont('FreeSansBold.ttf', 20)
HEALTHFONT = pygame.font.SysFont('FreeSansBold.ttf', 40)
portal_path = './textures/portal/portal_'
portal_images = [portal_path +str(p) + '.png' for p in range(1, 7)]

"""
Timed Events
"""

# Ganon Movement
pygame.time.set_timer(USEREVENT, 400)
# Spawn Beasts
pygame.time.set_timer(USEREVENT + 1, 7500)
# Increment Beast Portal Frames
pygame.time.set_timer(USEREVENT + 2, 400)
# Move Beasts
pygame.time.set_timer(USEREVENT + 3, 1000)
# Orb Travel on Path
pygame.time.set_timer(USEREVENT + 4, 100)

GAME_OVER = False

# Game Loop
while not GAME_OVER:

    GANON_VULNERABLE_IF = [beast for beast in BEAST_LIST if beast.APPEAR == True]

    if len(GANON_VULNERABLE_IF) < 1:
        GANON_VULNERABLE = True
    else:
        GANON_VULNERABLE = False

    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        key_events.global_events()

        if event.type == QUIT:
            key_events.quit()

        if keys[K_w] and keys[K_t]:
            key_events.key_w()

        # Movement Commands
        if (keys[K_RIGHT]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
            key_events.key_right()

        if (keys[K_LEFT]) and PLAYER.PLAYER_POS[0] > 0:
            key_events.key_left()

        if (keys[K_UP]) and PLAYER.PLAYER_POS[1] > 0:
            key_events.key_up()

        if (keys[K_DOWN]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
            key_events.key_down()

        # Item Commands
        if (keys[K_SPACE]):
            key_events.key_space()

        if (keys[K_f]):
            if PLAYER.WEAPON == WAND:
                orbs_list.append(heroes.ORB(math.ceil(PLAYER.PLAYER_POS[0]), math.ceil(PLAYER.PLAYER_POS[1]), PLAYER.DIRECTIOIN))

        """
        Timed Events
        """








































