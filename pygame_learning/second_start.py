from ast import literal_eval
import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Second attempt at Pygame")

walkRight = [
    pygame.image.load("R1.png"),
    pygame.image.load("R2.png"),
    pygame.image.load("R3.png"),
    pygame.image.load("R4.png"),
    pygame.image.load("R5.png"),
    pygame.image.load("R6.png"),
    pygame.image.load("R7.png"),
    pygame.image.load("R8.png"),
    pygame.image.load("R9.png"),
]
walkLeft = [
    pygame.image.load("L1.png"),
    pygame.image.load("L2.png"),
    pygame.image.load("L3.png"),
    pygame.image.load("L4.png"),
    pygame.image.load("L5.png"),
    pygame.image.load("L6.png"),
    pygame.image.load("L7.png"),
    pygame.image.load("L8.png"),
    pygame.image.load("L9.png"),
]
bg = pygame.image.load("bg.jpg")
char = pygame.image.load("standing.png")

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        # this determines what direction the character is facing when firing
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            # each sprite is used in 3 frames and framerate is 27 per second
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def redrawGameWindow():
    win.blit(bg, (0, 0))
    small_guy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# MAIN LOOP
small_guy = player(300, 410, 64, 64)
bullets = []
running = True

while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if small_guy.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            # the numbers are rounded to avoid decimals
            bullets.append(
                projectile(round(small_guy.x + small_guy.width // 2),
                round(small_guy.y + small_guy.height // 2),
                 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and small_guy.x > small_guy.speed:
        small_guy.x -= small_guy.speed
        small_guy.left = True
        small_guy.right = False
        small_guy.standing = False
    elif keys[pygame.K_RIGHT] and small_guy.x < 500 - small_guy.width - small_guy.speed:
        small_guy.x += small_guy.speed
        small_guy.right = True
        small_guy.left = False
        small_guy.standing = False
    else:
        small_guy.standing = True
        small_guy.walkCount = 0
    # when the character jumps, it cannot move up and down
    if not (small_guy.isJump):
        if keys[pygame.K_UP]:
            small_guy.isJump = True
            small_guy.right = False
            small_guy.left = False
            small_guy.walkCount = 0

    # what is a jump: move up, accelerate, hang still, move down, accelerate
    else:
        if small_guy.jumpCount >= -10:
            neg = 1
            if small_guy.jumpCount < 0:
                neg = -1
            small_guy.y -= (small_guy.jumpCount**2) * 1 * neg
            small_guy.jumpCount -= 1

        else:
            small_guy.isJump = False
            small_guy.jumpCount = 10

    redrawGameWindow()

pygame.quit()
