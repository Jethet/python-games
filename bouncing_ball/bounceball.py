import pygame, sys

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame:
        if event.type == pygame.QUIT:
            sys.exit