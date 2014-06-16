"""
This file will contain the Game class.
This class will be responsible for every action that our
main function was responsible for thus far.
"""
# Import the Player class from our player.py module
from player import *
from main import *
from pprint import pprint as pp


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
        
        self.tiles = self.generate_tiles()

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
        
    def generate_tiles(self):
        tiles = []
        for y in range(int(self.screen_height / self.tile_size)):
            tiles.append([])
            for x in range(int(self.screen_width / self.tile_size)):
                if x in (0, int(self.screen_width / self.tile_size) - 1) or y in (0, int(self.screen_height / self.tile_size) - 1):
                    tiles[y].append(True)
                else:
                    tiles[y].append(False)
        return tiles
        
    def draw_room(self, tiles, screen):
        for y in range(len(tiles)):
            for x in range(len(tiles[y])):
                if tiles[y][x]:
                    pygame.draw.rect(screen, GRAY, [x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size], 0);

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
                    if event.key == pygame.K_UP:
                        self.player.move(0, -1, self.tiles)
                    elif event.key == pygame.K_DOWN:
                        self.player.move(0, 1, self.tiles)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(1, 0, self.tiles)
                    elif event.key == pygame.K_LEFT:
                        self.player.move(-1, 0, self.tiles)

            # Drawing
            self.screen.fill(self.background)
            self.draw_room(self.tiles, self.screen)

            # Update and draw player
            self.player.draw(self.screen)

            # Update the display
            pygame.display.flip()

            # Set fps clock to 60 frames per second
            self.clock.tick(60)

        pygame.quit()
