import pygame
import itertools

pygame.init()

# set up drawing window
screen = pygame.display.set_mode((500, 500))
colors = itertools.cycle([])

# run until user asks to quit
running = True

while running:
    # did user click quit button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the background with white
    screen.fill((255, 255, 255))

    ''' add blue circle inside white background:
     first element is WHERE you draw
     second element is the COLOR (tuple with RGB values)
     third element is the CENTRE of the circle (here: centre of screen)
     fourth element is the RADIUS of the circle
    '''
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # to make this appear on your screen:
    pygame.display.flip()

pygame.quit()
