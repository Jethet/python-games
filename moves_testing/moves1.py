# Move a string from right to left in an array

playerpos = 6
screen = [1, 2, 3, 4, 5, 6]

while playerpos > 0:
    playerpos = playerpos - 1
    screen[playerpos] = "player"
    print(screen)