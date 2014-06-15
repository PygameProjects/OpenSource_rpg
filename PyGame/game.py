"""
This file will contain the Game class.
This class will be responsible for every action that our
main function was responsible for thus far.
"""
# Import the Player class from our player.py module
from player import *
from main import *


class Game():
    def __init__(self, screen_width, screen_height, player_width, player_height, tile_size, background):
        # Initialize pygame
        pygame.init()

        # Create screen and add title
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        pygame.display.set_caption("Game")

        # FPS clock. Will be used to set max fps
        self.clock = pygame.time.Clock()

        # Create a player object
        player_x, player_y = 1, 1
        self.player = Player(player_x, player_y, player_width, player_height, tile_size)

        self.background = background
        
        self.screen_width, self.screen_height = screen_width, screen_height
        
        self.tile_size = tile_size

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
        
    def draw_room(self, screen):
        for x in range(int(self.screen_width / self.tile_size)):
            pygame.draw.rect(screen, GRAY, [x * self.tile_size, 0, self.tile_size, self.tile_size], 0);
            pygame.draw.rect(screen, GRAY, [x * self.tile_size, self.screen_height - self.tile_size, self.tile_size, self.tile_size], 0);
        for y in range(int(self.screen_height / self.tile_size)):
            pygame.draw.rect(screen, GRAY, [0, y * self.tile_size, self.tile_size, self.tile_size], 0);
            pygame.draw.rect(screen, GRAY, [self.screen_width - self.tile_size, y * self.tile_size, self.tile_size, self.tile_size], 0);            

    def run(self):
        """
        Method to run the game
        """        
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

            # Drawing
            self.screen.fill(self.background)
            self.draw_room(self.screen)

            # Update and draw player
            self.player.draw(self.screen)

            # Update the display
            pygame.display.flip()

            # Set fps clock to 60 frames per second
            self.clock.tick(60)

        pygame.quit()
