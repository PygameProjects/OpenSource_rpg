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

WHITE = (255, 255, 255)


def main():
    # Initialize game object
    game = Game(S_WIDTH, S_HEIGHT, P_WIDTH, P_HEIGHT, WHITE)

    # Start game
    game.run()

if __name__ == '__main__': main()
