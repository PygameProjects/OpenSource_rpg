import os, sys, inspect, pygame
from pygame.locals import *
import pygame.font

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"kezmenu")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
from kezmenu import KezMenu

OPTION_SELECTED = None

pygame.font.init()
screen = pygame.display.set_mode((640,480), 0, 32)

def option1():
    global OPTION_SELECTED
    OPTION_SELECTED = 1

def option2():
    global OPTION_SELECTED
    OPTION_SELECTED = 1

def option3():
    global OPTION_SELECTED
    OPTION_SELECTED = 1
    
def optionX(p):
    global OPTION_SELECTED
    OPTION_SELECTED = p
    
menu = KezMenu(
            ["First option!", option1],
            ["sEcond", option2],
            ["Again!", option3],
            ["Lambda", lambda: optionX(71)],
            ["Quit", sys.exit],
    )
menu.mouse_enabled = False
    
def drawMenu():
    screen.fill( (150,150,150,255) )
    menu.draw(screen)
    pygame.display.flip()

pygame.display.set_caption("Example 1: Use the KezMenu freely")
while True:
    events = pygame.event.get()
    menu.update(events)
    screen.fill( (150,150,150,255) )
    menu.draw(screen)
    pygame.display.flip()    
    if OPTION_SELECTED:
        break
