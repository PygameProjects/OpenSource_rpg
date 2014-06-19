"""
This file contains the main() function of the game.
The game will be run from here.
"""
from game import *

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

def main():
    # Initialize game object
    game = Game(S_WIDTH, S_HEIGHT, P_WIDTH, P_HEIGHT, TILESIZE, WHITE)

    # Start game
    game.run()

if __name__ == '__main__': main()
