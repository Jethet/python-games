from tkinter.tix import COLUMN
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
  board = np.zeros((6, 7))
  return board

def drop_piece(board, row, col, piece):
  board[row][col] == piece

def is_valid_location(board, col):
  # board has six rows, 0 to 6, so top row is 5
  return board[5][col]

def get_next_open_row(board, col):
  for r in range(ROW_COUNT):
    if board[r][col] == 0:
      return r
  
board = create_board()
print(board)

game_over = False
turn = 0

while not game_over:
  # ask player 1 input
  if turn == 0:
    col = int(input("Player 1 make your selection (0-6): "))
    
    if is_valid_location(board, col):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col, 1)
    # print(selection)
    # print(type(selection))
  
  # ask player 2 input
  else:
    col = int(input("Player 2 make your selection (0-6): "))
    
    if is_valid_location(board, col):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col, 2)

  # to alternate between 0 and 1: increase turn and use modular to get 0 or 1
  turn += 1
  turn = turn % 2

print(board)