"""
This file will contain the Game class.
This class will be responsible for every action that our
main function was responsible for thus far.
"""
import os
from player import *
from main import *
from pprint import pprint as pp
import shelve


class Game():
    def __init__(self, screen_width, screen_height, player_width, player_height, tile_size, background):
        # Initialize pygame
        pygame.init()

        # Create screen and add title
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Game")

        # FPS clock. Will be used to set max fps
        self.clock = pygame.time.Clock()

        # Create a player object
        player_x, player_y = 1, 1
        self.player = Player(player_x, player_y, player_width, player_height, tile_size)

        # Set the game environment
        self.background = background        
        self.screen_width, self.screen_height = screen_width, screen_height        
        self.tile_size = tile_size
        self.tiles = self.read_mapfile('map.txt')
        self.camerax, self.cameray = 200, -300
        
    def read_mapfile(self, filename):
        """
        Reads a text file called filename and generates the map
        
        Input: Text file with spaces and #'s
        Output: 2 dimensional array of booleans
        """
        assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)
        
        # read file and store in a list
        mapfile_read = open(filename, 'r')
        content = mapfile_read.readlines() + ['\r\n']
        mapfile_read.close()

        levelmap = []    
        for linenum in range(len(content)):
           # process each line that was in the level file
            line = content[linenum].rstrip('\r\n')
            if line != '':
                levelmap.append([])
                for i in line:
                    if i == ' ':
                        levelmap[linenum].append(False)
                    elif i == '#':
                        levelmap[linenum].append(True)
                    else:
                        print("UNKONWN CHARACTER IN MAP FILE")
                
        return levelmap

    def save(self):
        """
        Write every variable value to a file using the shelve module.
        (a.k.a save the game state)
        """
        save_game_file = shelve.open('save_game')
        
        x, y = self.player.get_pos()
        save_game_file['player_posx'] = x
        save_game_file['player_posy'] = y
        
        save_game_file.close()

    def load(self):
        """
        Load all the variable values from a file created with save().
        (a.k.a load the game state)
        """
        save_game_file = shelve.open('save_game')
        
        self.player.x = save_game_file['player_posx']
        self.player.y = save_game_file['player_posy']
        
        save_game_file.close()
        
    def draw_room(self, tiles, mapsurf):
        """
        Notes: Draws the room
        Input:
            tiles - 2 dimensional array of booleans, True is a wall block
            mapsurf - Pygame map object
        """
        for y in range(len(tiles)):
            for x in range(len(tiles[y])):
                if tiles[y][x]:
                    pygame.draw.rect(mapsurf, GRAY, [x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size], 0);

    def run(self):
        running = True
        while running:
            # Event processing
            for event in pygame.event.get():
                # If user hits 'x' exit
                if event.type == pygame.QUIT:
                    self.save()
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
                        
                    # Load the game with the "L" key
                    elif event.key == pygame.K_l:
                        self.load()

            # Drawing
            self.screen.fill(self.background)            
            mapsurf = pygame.Surface((2000, 1000))
            mapsurf.fill(WHITE)
            
            # Update and draw room
            self.draw_room(self.tiles, mapsurf)

            # Update and draw player
            self.player.draw(mapsurf)
            
            # Update the display
            mapsurf_rect = mapsurf.get_rect()
            mapsurf_rect.center = (int(self.screen_width / 2) + self.camerax, int(self.screen_height / 2) - self.cameray)
            self.screen.blit(mapsurf, mapsurf_rect)
            pygame.display.flip()

            # Update the camera
            playerx, playery = self.player.get_pos()
            # Player x coordinate in relation to mapsurf
            playerx *= self.tile_size
            playerx += mapsurf_rect.left
            # Player y coordinate in relation to mapsurf
            playery *= self.tile_size
            playery += mapsurf_rect.top
            
            screen_rect = self.screen.get_rect()
            if screen_rect.bottom - playery < 100:
                self.cameray += self.tile_size
            elif playery - screen_rect.top < 100:
                self.cameray -= self.tile_size
            if screen_rect.right - playerx < 100:
                self.camerax -= self.tile_size
            elif playerx - screen_rect.left < 100:
                self.camerax += self.tile_size
            
            # Set fps clock to 60 frames per second
            self.clock.tick(60)

        pygame.quit()
