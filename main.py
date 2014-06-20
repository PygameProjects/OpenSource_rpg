"""
This file contains the main() function of the game.
The game will be run from here.
"""
import os, sys, inspect, pygame
from pygame.locals import *
import pygame.font
from game import *

# Import KezMenu for the menu system
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"kezmenu")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
from kezmenu import KezMenu

# Global constants
S_WIDTH = 800
S_HEIGHT = 500

P_WIDTH = 20
P_HEIGHT = 40

TILESIZE = 20

WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
GREEN   = (  0, 204,   0)
GRAY    = ( 60,  60,  60)
BLUE    = (  0,  50, 255)

WALL    = '#'
KEY     = '@'
GOLD    = '$'
DOOR    = '-'

OPTION_SELECTED = None  # Global for the menu system
MAPFILE = 'map.txt'     # Map text file

def optionX(option):
    global OPTION_SELECTED
    OPTION_SELECTED = option
    
def draw_menu(menu, screen):
    screen.fill( (150,150,150,255) )
    menu.draw(screen)
    pygame.display.flip()

def main():
    # Display menu for player
    pygame.font.init()
    screen = pygame.display.set_mode( (640,480), 0, 32 )
    menu = KezMenu(
                ["New Game", lambda: optionX("new_game")],
                ["Load Game", lambda: optionX("load_game")],
                ["Quit!", lambda: optionX("quit")],
        )
    menu.mouse_enabled = False
    while True:
        events = pygame.event.get()
        menu.update(events)
        screen.fill( (150,150,150,255) )
        menu.draw(screen)
        pygame.display.flip()
        if OPTION_SELECTED:
            break
    
    if OPTION_SELECTED == "quit":
        print("Aww, that's too bad! See you next time!")
        pygame.quit()
        sys.exit()
    else:
        # Initialize game object
        game = Game(S_WIDTH, S_HEIGHT, P_WIDTH, P_HEIGHT, TILESIZE, WHITE)        
        # Load last saved game if it exists
        if OPTION_SELECTED == "load_game":
            if(game.save_exists()):
                game.load()

    # Start game
    game.run()
    
    # When exiting save game
    game.save(game.get_tiles())
    
    # Close game
    pygame.quit()
    sys.exit()

if __name__ == '__main__': main()
