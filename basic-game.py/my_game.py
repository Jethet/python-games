import pygame

pygame.init()

# set up drawing window
screen = pygame.display.set_mode((500, 500))

# run until user asks to quit
running = True

while running:
    # did user click quit button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
