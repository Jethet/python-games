""" Goals of game:
- avoid incoming obstacles
  => player starts on left side of the screen
  => obstacles enter on the right and move left in straight line
- player can move right, left, up and down to avoid obstacles
- player cannot move off the screen
- game ends when player is hit by obstacle or when user quits
"""
import pygame
import sys
# import pygame.locals for access to keyboard coordinates
# from pygame.locals import (
#   K_UP,
#   KEY_DOWN,
#   K_LEFT,
#   K_RIGHT,
#   K_ESCAPE,
#   KEYDOWN,
#   QUIT,
# )

pygame.init()

# setting up display
size = width, height = 800, 800
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

logo = pygame.image.load("codewoman")
logorect = logo.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    logorect = logorect.move(speed)
    if logorect.left < 0 or logorect.right > width:
        speed[0] = -speed[0]
    if logorect.top < 0 or logorect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(logo, logorect)
    pygame.display.flip()
