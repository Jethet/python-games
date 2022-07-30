import pygame
import itertools

pygame.init()

# set up drawing window
screen = pygame.display.set_mode((800, 600))
colors = itertools.cycle(["blue", "purple", "red", "orange",
                          "green", "yellow"])
clock = pygame.time.Clock()

base_color = next(colors)
next_color = next(colors)
current_color = base_color

FPS = 60
change_every_x_seconds = 3.0  # why the dot?
number_of_steps = change_every_x_seconds * FPS
step = 1

font1 = pygame.font.SysFont("Arial", 50)
font2 = pygame.font.SysFont("Arial", 40, italic=True)

# run until user asks to quit
running = True

while running:
    # did user click quit button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    text1 = font1.render(
        "fading {a} to {b}".format(a=base_color, b=next_color),
        True,
        pygame.color.Color("black"),
    )
    text2 = font2.render(
      "this was built with pygame",
      True,
      pygame.color.Color("black"))

    step += 1
    # formula to fade old color to new color
    if step < number_of_steps:
        current_color = [
            x + (((y - x) / number_of_steps) * step)
            for x, y in zip(
                pygame.color.Color(base_color), pygame.color.Color(next_color)
            )
        ]
    else:
        step = 1
        base_color = next_color
        next_color = next(colors)

    # fill the background with white
    screen.fill(pygame.color.Color("white"))
    """ add blue circle inside white background:
     first element is WHERE you draw
     second element is the COLOR (tuple with RGB values)
     third element is the CENTRE of the circle (here: centre of screen)
     fourth element is the RADIUS of the circle
    """
    pygame.draw.circle(screen, current_color,
                       screen.get_rect().center, 100)
    screen.blit(text1, (180, 100))
    screen.blit(text2, (180, 450))

    # to make this appear on your screen:
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
