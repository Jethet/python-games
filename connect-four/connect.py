import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
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

def draw_board(board):
  for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT):
      # draw a blue rectangle, with black row on top (= extra squaresize in r*squaresize+squaresize)
      pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
      pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
     
  for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT): 
      if board[r][c] == 1:
        pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
      elif board[r][c] == 2:
        pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
  pygame.display.update()
           

board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE    # extra row at the top to show ball
size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)  #circles slightly smaller than black square so they are not touching

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:  # create proper ending option for game
      sys.exit()
      
    if event.type == pygame.MOUSEBUTTONDOWN:
      # print(event.pos)
      # ask player 1 input
      if turn == 0:
        posx = event.pos[0]
        col = int(math.floor(posx/SQUARESIZE))
        
        if is_valid_location(board, col):
          row = get_next_open_row(board, col)
          drop_piece(board, row, col, 1)
          
          if winning_move(board, 1):
            print("Player 1 wins!")
            game_over = True
       
      else:
        if turn == 0:
          posx = event.pos[0]
          col = int(math.floor(posx/SQUARESIZE))
              
        if is_valid_location(board, col):
          row = get_next_open_row(board, col)
          drop_piece(board, row, col, 2)
          
          if winning_move(board, 2):
            print("Player 2 wins!")
            game_over = True
          
      print_board(board)
      draw_board(board)
  
      # to alternate between 0 and 1: increase turn and use modular to get 0 or 1
      turn += 1
      turn = turn % 2


  
  