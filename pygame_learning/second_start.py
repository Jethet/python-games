import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Second attempt at Pygame")
running = True

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'),
             pygame.image.load('R3.png'), pygame.image.load('R4.png'),
             pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'),
             pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),
            pygame.image.load('L3.png'), pygame.image.load('L4.png'),
            pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'),
            pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
speed = 5
isJump = False
jumpCount = 10
# character: moving y/n, what direction, how much moved already
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    # each sprite is used in 3 frames and framerate is 27 per second
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()


# MAIN LOOP
while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - speed:
        x += speed
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    # when the character jumps, it cannot move up and down
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0

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

    redrawGameWindow()

pygame.quit()
