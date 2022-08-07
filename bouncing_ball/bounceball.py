import pygame, sys

pygame.init()

size = width, height = 620, 540
speed1 = [1.5, 1.5]
speed2 = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

img1 = pygame.image.load("ball.png")
img2 = pygame.image.load("ball2.png")
ball1 = pygame.transform.scale(img1, (65, 65))
ball2 = pygame.transform.scale(img2, (65, 65))
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect1 = ballrect1.move(speed1)
    ballrect2 = ballrect2.move(speed2)

    if ballrect1.left < 0 or ballrect1.right > width:
        speed1[0] = -speed1[0]
    if ballrect1.top < 0 or ballrect1.bottom > height:
        speed1[1] = -speed1[1]
    if ballrect2.left < 0 or ballrect2.right > width:
        speed2[0] = -speed2[0]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed2[1] = -speed2[1]

    screen.fill(black)
    screen.blit(ball1, ballrect1)
    screen.blit(ball2, ballrect2)

    pygame.display.flip()