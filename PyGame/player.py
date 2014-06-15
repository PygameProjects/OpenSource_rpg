"""
This file contains the Player class with any necessary methods
to control the player which is by the way a sprite object.
"""
import pygame
from main import *


class Player(pygame.sprite.Sprite):

    # Think of this as the velocity of the player
    change_x = 1
    change_y = 1

    def __init__(self, x, y, width, height, tile_size):
        pygame.sprite.Sprite.__init__(self)

        # Create player image and set the coordinates
        # of image rectangle
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.tile_size = tile_size

    def move(self, x, y):
        """
        Changes the location of the player
        """
        if x != 0:
            new_x = self.x + x
            self.x = new_x
        if y != 0:
            new_y = self.y + y
            self.y = new_y

    def draw(self, screen):
        """
        Draws the player on the screen and updates
        """
        pygame.draw.rect(screen, BLACK, [self.x * self.tile_size, self.y * self.tile_size, self.tile_size, self.tile_size], 0);

    # Key down handler
    def keydown(self, key):
        if key == pygame.K_UP:
            self.move(0, -1)
        elif key == pygame.K_DOWN:
            self.move(0, 1)
        elif key == pygame.K_RIGHT:
            self.move(1, 0)
        elif key == pygame.K_LEFT:
            self.move(-1, 0)

    # Key up handler
    def keyup(self, key):
        if key == pygame.K_UP:
            self.move(0, 5)
        elif key == pygame.K_DOWN:
            self.move(0, -5)
        elif key == pygame.K_RIGHT:
            self.move(-5, 0)
        elif key == pygame.K_LEFT:
            self.move(5, 0)
            
