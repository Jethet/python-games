import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Second attempt at Pygame")
running = True

x = 5
y = 425
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10

while running:
    pygame.time.delay(100)  # = milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - speed:
        x += speed
    # when the character jumps, it cannot move up and down
    if not (isJump):
        if keys[pygame.K_UP] and y > speed:
            y -= speed
        if keys[pygame.K_DOWN] and y < 500 - height - speed:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    # what is a jump: move up, accelerate, hang still, move down, accelerate
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 1 * neg
            jumpCount -= 1
        
        else:
            isJump = False
            jumpCount = 10
        
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()