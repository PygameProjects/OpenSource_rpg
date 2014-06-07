"""
This file contains the Player class with any necessary methods
to control the player which is by the way a sprite object.
"""


import pygame


class Player(pygame.sprite.Sprite):

    # Think of this as the velocity of the player
    change_x = 0
    change_y = 0

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        # Create player image and set the coordinates
        # of image rectangle
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_speed(self, x, y):
        """
        Changes the speed of the player
        """

        self.change_x += x
        self.change_y += y

    def update(self):
        """
        Updates the position of the player
        """

        # Move left/right
        self.rect.x += self.change_x

        # Move up/down
        self.rect.y += self.change_y

    def draw(self, surface):
        """
        Draws the player on the screen and updates
        """
        surface.blit(self.image, self.rect)

    # Key down handler
    def keydown(self, key):
        if key == pygame.K_UP:
            self.change_speed(0, -5)
        elif key == pygame.K_DOWN:
            self.change_speed(0, 5)
        elif key == pygame.K_RIGHT:
            self.change_speed(5, 0)
        elif key == pygame.K_LEFT:
            self.change_speed(-5, 0)

    # Key up handler
    def keyup(self, key):
        if key == pygame.K_UP:
            self.change_speed(0, 5)
        elif key == pygame.K_DOWN:
            self.change_speed(0, -5)
        elif key == pygame.K_RIGHT:
            self.change_speed(-5, 0)
        elif key == pygame.K_LEFT:
            self.change_speed(5, 0)
            
