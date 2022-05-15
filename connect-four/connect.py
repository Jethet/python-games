import numpy as np

def create_board():
  board = np.zeros((6, 7))
  return board

board = create_board()

game_over = False
turn = 0

while not game_over:
  # ask player 1 input
  if turn == 0:
    selection = int(input("Player 1 make your selection (0-6): "))
    print(selection)
    print(type(selection))
  
  # ask player 2 input

print(board)