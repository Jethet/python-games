import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
  board = np.zeros((ROW_COUNT, COLUMN_COUNT))
  return board

def drop_piece(board, row, col, piece):
  board[row][col] = piece

def is_valid_location(board, col):
  # board has six rows, 0 to 6, bottom is 0 and top row is 5
  return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
  for r in range(ROW_COUNT):
    if board[r][col] == 0:
      return r

def print_board(board):
  print (np.flip(board, 0))   # numpy command to flip top and bottom

def winning_move(board, piece):
  # check horizontal locations for winning combination
  for c in range(COLUMN_COUNT - 3):    # you cannot have 4 starting from the last 3
    for r in range(ROW_COUNT):
      # check every place from 0 to 4 to see if 4 are connected
      if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
        return True
  
  # check vertical locations for winning combination, based on ROW_COUNT <= 0, 1 or 2
  for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT - 3):
      if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
        return True

  # check positively sloped diagonals: determine last possible row for 4 connect
  for c in range(COLUMN_COUNT - 3):
    for r in range(ROW_COUNT - 3):
      if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
        return True
  
  # check negatively sloped diagonals
  for c in range(COLUMN_COUNT - 3):
    for r in range(3, ROW_COUNT):
      if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
        return True
    

board = create_board()
print_board(board)

game_over = False
turn = 0

while not game_over:
  # ask player 1 input
  if turn == 0:
    col = int(input("Player 1 make your selection (0-6): "))
    
    if is_valid_location(board, col):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col, 1)
      
      if winning_move(board, 1):
        print("Player 1 wins!")
        game_over = True
    # print(selection)
    # print(type(selection))
  
  # ask player 2 input
  else:
    col = int(input("Player 2 make your selection (0-6): "))
    
    if is_valid_location(board, col):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col, 2)
      
      if winning_move(board, 2):
        print("Player 2 wins!")
        game_over = True
  
  print_board(board)
  
  # to alternate between 0 and 1: increase turn and use modular to get 0 or 1
  turn += 1
  turn = turn % 2

