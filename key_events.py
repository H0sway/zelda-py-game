# Import dependencies
import pygame
import sys

"""
Library for all key events
"""

# Images for animating Link walking
img_path = './sprites/link/link_'
f_path = img_path + 'f'
b_path = img_path + 'b'
r_path = img_path + 'r'
l_path = img_path + 'l'

f_images = [f_path+str(f)+'.png' for f in range(7)]
b_images = [b_path+str(b)+'.png' for b in range(7)]
r_images = [r_path+str(r)+'.png' for r in range(7)]
l_images = [l_path+str(l)+'.png' for l in range(7)]

# Images for animating Wolf-Link walking
img_path = './sprites/wolf/wolf_'
wolf_f_path = img_path + 'f'
wolf_b_path = img_path + 'b'
wolf_r_path = img_path + 'r'
wolf_l_path = img_path + 'l'

wolf_f_images = [wolf_f_path+str(f)+'.png' for f in range(7)]
wolf_b_images = [wolf_b_path+str(b)+'.png' for b in range(7)]
wolf_r_images = [wolf_r_path+str(r)+'.png' for r in range(7)]
wolf_l_images = [wolf_l_path+str(l)+'.png' for l in range(7)]

class KeyEvents:
    def __init__(self, PLAYER):
        self.PLAYER = PLAYER
        self.counter = 0
        self.wolf_counter = 0
        self.wolf_counter_lr = 0
        self.movement = .25
        self.orbs = []

    def global_events(self):
        if self.PLAYER_TRANSFORM:
            self.movement = .5
        else:
            self.movement = .25

    def quit(self):
        pygame.quit()
        sys.exit()

    def key_down(self):
        self.PLAYER.PLAYER_POS[1] += self.movement
        self.PLAYER_DIRECTION = 'd'

        self.PLAYER.SPRITE_POS = pygame.image.load(f_images[self.counter])
        self.counter = (self.counter + 1) % len(f_images)

        if self.PLAYER_TRANSFORM:
            self.PLAYER.WOLF = pygame.image.load(wolf_f_images[self.wolf_counter])
            self.wolf_counter = (self.wolf_counter + 1) % len(wolf_f_images)

    def key_up(self):
        self.PLAYER.PLAYER_POS[1] -= self.movement
        self.PLAYER_DIRECTION = 'u'

        self.PLAYER.SPRITE_POS = pygame.image.load(b_images[self.counter])
        self.counter = (self.counter + 1) % len(b_images)

        if self.PLAYER_TRANSFORM:
            self.PLAYER.WOLF = pygame.image.load(wolf_b_images[self.wolf_counter])
            self.wolf_counter = (self.wolf_counter + 1) % len(wolf_b_images)

    def key_left(self):
        self.PLAYER.PLAYER_POS[1] -= self.movement
        self.PLAYER_DIRECTION = 'l'

        self.PLAYER.SPRITE_POS = pygame.image.load(l_images[self.counter])
        self.counter = (self.counter + 1) % len(l_images)

        if self.PLAYER_TRANSFORM:
            self.PLAYER.WOLF = pygame.image.load(wolf_l_images[self.wolf_counter])
            self.wolf_counter_lr = (self.wolf_counter_lr + 1) % len(wolf_l_images)

    def key_right(self):
        self.PLAYER.PLAYER_POS[1] += self.movement
        self.PLAYER_DIRECTION = 'r'

        self.PLAYER.SPRITE_POS = pygame.image.load(r_images[self.counter])
        self.counter = (self.counter + 1) % len(r_images)

        if self.PLAYER_TRANSFORM:
            self.PLAYER.WOLF = pygame.image.load(wolf_r_images[self.wolf_counter])
            self.wolf_counter_lr = (self.wolf_counter_lr + 1) % len(wolf_r_images)

    def key_space(self):
        if self.PLAYER.WEAPON:
            self.PLAYER.PLAYER_INV.remove(PLAYER.WEAPON)
            self.PLAYER.WEAPON.PLACED = True

        # Drop weapon location
            if self.PLAYER_DIRECTION == 'd':
                self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0]
                self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1] - 1
            elif self.PLAYER.DIRECTION == 'u':
                self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0]
                self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1] + 1
            elif self.PLAYER.DIRECTION == 'r':
                self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0] - 1
                self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1]
            elif self.PLAYER.DIRECTION == 'l':
                self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0] + 1
                self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1]

        self.PLAYER.WEAPON = False

    def key_w(self):
        self.PLAYER.TRANSFORMING()













































