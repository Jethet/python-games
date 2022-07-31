# TO DO: REPLACE BULLETS BY APPLES OR HEARTS OR FLOWERS
#        ADD TIME BAR THAT CHANGES FROM GREEN TO RED WHEN SECONDS PASS

from ast import literal_eval
import pygame
import time

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Second Pygame")

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
# heart = pygame.image.load("heart.png")
bulletSound = pygame.mixer.Sound("bulletSound.mp3")
hitSound = pygame.mixer.Sound("hitSound.mp3")

music = pygame.mixer.music.load("music.mp3")
# to play the music continuously, never stopping:
pygame.mixer.music.play(-1)

hitNumber = 0
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
        # hit boxes around characters make it possible to create collisions
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # code line 72 draws red rect around char to show hitbox
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        #  this is resetting the char after a hit and shows it as standing
        self.x = 60
        self.y = 410
        self.walkCount = 0
        textCollide = pygame.font.SysFont("comicsans", 40)
        text = textCollide.render("You collided! -5 hits", 1, (255, 0, 0))
        # text has to be in center: calculate center of screen minus half of textwidth
        # the 200 for the height is a bit random (screenheight is 480 here)
        win.blit(text, ((500/2) - (text.get_width()/2), 200))
        pygame.display.update()
        # to see the text we need to pause the game for a bit BUT it has to still be
        # possible to quit the game:
        i = 0
        while i < 200:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()

class projectile(object):
    def __init__(self, x, y, color, radius, facing):
        self.x = x
        self.y = y
        # self.heart = heart
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        # win.blit(heart, (self.x, self.y))

# the enemy char moves across the x axis between two coordinates
class enemy(object):
    walkRight = [
        pygame.image.load("R1E.png"),
        pygame.image.load("R2E.png"),
        pygame.image.load("R3E.png"),
        pygame.image.load("R4E.png"),
        pygame.image.load("R5E.png"),
        pygame.image.load("R6E.png"),
        pygame.image.load("R7E.png"),
        pygame.image.load("R8E.png"),
        pygame.image.load("R9E.png"),
        pygame.image.load("R10E.png"),
        pygame.image.load("R11E.png"),
    ]
    walkLeft = [
        pygame.image.load("L1E.png"),
        pygame.image.load("L2E.png"),
        pygame.image.load("L3E.png"),
        pygame.image.load("L4E.png"),
        pygame.image.load("L5E.png"),
        pygame.image.load("L6E.png"),
        pygame.image.load("L7E.png"),
        pygame.image.load("L8E.png"),
        pygame.image.load("L9E.png"),
        pygame.image.load("L10E.png"),
        pygame.image.load("L11E.png"),
    ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.speed = 3
        self.hitbox =(self.x + 17, self.y + 2, 31, 57)
        self.health = 9
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.speed > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 45, 10))
            # the calculation below calculates how much of the green healthbar has to become red: 50 width divided by 10 health
            #   and then multiplied by the remaining health number that is descending, so the green becomes less and red increases
            #   every time the goblin is hit until the total health number is used (with the 11th hit all 10 health are used) 
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/11) * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # code line 142 draws red rect around char to show hitbox
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.speed > 0:
            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkCount = 0
        else:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("Hit")

def redrawGameWindow():
    win.blit(bg, (0, 0))
    textHits = font.render(f"Small guy hit goblin {hitNumber} times", 1, (0,0,0))
    win.blit(textHits, (40, 40))
    textTime = font.render(f"You have {playSeconds} seconds left", 1, (0,0,0))
    win.blit(textTime, (40, 10))
    small_guy.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# MAIN LOOP
font = pygame.font.SysFont("comicsans", 30, True)
pygame.time.set_timer(pygame.USEREVENT, 1000)
small_guy = player(300, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
bullets = []
shootLoop = 0
running = True
playSeconds = 20

while running:

    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT: 
                playSeconds -= 1
        if playSeconds == 0:
            print("Time's up!")
            running = False
    # the char collides with the goblin, calculated via the hitboxes, 5 hitnumber is deducted for every collision
    if small_guy.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and small_guy.hitbox[1] + small_guy.hitbox[3] > goblin.hitbox[1]:
        if small_guy.hitbox[0] + small_guy.hitbox[2] > goblin.hitbox[0] and small_guy.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            small_guy.hit()
            hitNumber -= 5

    for bullet in bullets:
        # check if bullet is in hitbox: check top and bottom of hitbox rectangle
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                hitNumber +=1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if small_guy.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            # the numbers are rounded to avoid decimals
            bullets.append(projectile(round(small_guy.x + small_guy.width // 2), round(small_guy.y + small_guy.height // 2), (0, 0, 0), 6, facing))
        shootLoop = 1

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
