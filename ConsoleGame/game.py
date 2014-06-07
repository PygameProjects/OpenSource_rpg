"""
This file will contain the Game class.
This class will be responsible for every action that our
main function was responsible for thus far.
"""

# Import the Player class from our player.py module
from player import *


class Game():
    def __init__(self, screen_width, screen_height, player_width, player_height, background):
        # Initialize pygame
        pygame.init()

        # Create screen and add title
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        pygame.display.set_caption("Game")

        # FPS clock. Will be used to set max fps
        self.clock = pygame.time.Clock()

        # Create a player object
        self.player = Player(player_width, player_height, player_width, player_height)

        self.background = background


    # Draw handler
    def draw(self, surface):
        surface.fill(self.background)

        # Update and draw player
        self.player.update()
        self.player.draw(surface)

        # Update the display
        pygame.display.flip()


    """
    Key down and key up handlers. Note:
    We are probably only going to need
    to move the player but just in case
    we'll have it like that
    """

    def keydown(self, key):
        self.player.keydown(key)

    def keyup(self, key):
        self.player.keyup(key)

    def run(self):
        """
        Method to run the game
        """

        # Main loop of the game
        running = True
        while running:
            # Event processing
            for event in pygame.event.get():
                # If user hits 'x' exit
                if event.type == pygame.QUIT:
                    running = False

                # Key down events
                elif event.type == pygame.KEYDOWN:
                    self.keydown(event.key)

                # Key up events
                elif event.type == pygame.KEYUP:
                    self.keyup(event.key)

            # Drawing
            self.draw(self.screen)

            # Set fps clock to 60 frames per second
            self.clock.tick(60)

        pygame.quit()
