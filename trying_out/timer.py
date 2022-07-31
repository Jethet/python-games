import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# counter, text = 10, '10'
counter = 10
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
            
        if event.type == pygame.USEREVENT: 
            counter -= 1
        if counter == 0:
            print("Time's up!")
            run = False
        
    screen.fill((255, 255, 255))
    text = f"You have {counter} left"
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)
