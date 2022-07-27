from re import T
import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Second attempt at Pygame")
running = True

x = 50
y = 50
width = 40
height = 60
speed = 5

while running:
    pygame.time.delay(100)  # = milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
        if x == 0:
            speed = 0

    if keys[pygame.K_RIGHT]:
        x += speed
        if x == 460:
            speed = 0

    if keys[pygame.K_UP]:
        y -= speed
        if y == 0:
            speed = 0

    if keys[pygame.K_DOWN]:
        y += speed
        if y == 440:
            speed = 0

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()