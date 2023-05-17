import sys
import numpy as np
import pygame
# board rows=6 columns=7
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
num_rows = 6
num_columns = 7
def create_board():
    board = np.zeros((num_rows,num_columns))
    return  board
def drop_piece(board,row,column,piece):
    board[row][column] = piece
# top row in column not full
def isvalid_location(board,column):
    # 5
    return board[5][column] == 0

def next_emptyrow(board, column):
    for row in range(6):
        if board[row][column] == 0:
            return row
def wining_move(board,piece):
    # check horizotal
    for col in range (num_columns-3):
        for row in range(num_rows):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece :
                return True
    # check vertical
    for col in range(num_columns):
        for row in range(num_rows-3):
            if board[row][col] == piece and board[row+1][col]== piece and board[row+2][col] == piece and board [row+3][col] == piece:
                return True
        # diagonal
    for col in range(num_columns-3):
        for row in range(num_rows-3):
            if board[row][col] == piece and board[row + 1][col+1] == piece and board[row + 2][col+2] == piece and board[row + 3][col+3] == piece:
                return True
        # negative diagonal
    for col in range(num_columns - 3):
        for row in range(3, num_rows):
            if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
                return True

def print_flipboard( board ):
    print(np.flip(board, 0))
def print_boardGraphics(board):
    for c in range(num_columns):
        for r in range(num_rows):
            # rectangle column, row height width
            # shift with row
            pygame.draw.rect(screen, yellow, (c*squareSize, r*squareSize+squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, black, (int(c*squareSize+squareSize/2), int(r*squareSize+squareSize+squareSize/2)), radius)
board = create_board()
game_over = False
pygame.init()
# width and height of this game
squareSize = 100
width = num_columns*squareSize
height = (num_rows+1)*squareSize
size = (width, height)
# radius of circle
radius = int(squareSize/2 - 5)
screen = pygame.display.set_mode(size)
print_boardGraphics(board)
pygame.display.update()
# game not over
Flag = 0
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            sys.exit()
        # drop piece
        if event.type == pygame.MOUSEBUTTONDOWN:
           continue
            # input_of_player1
            #if Flag == 0:
             #   columnPlayer1 = int(input(" Player 1 Enter your selection (0-6) : "))
              #  if isvalid_location(board, columnPlayer1):
               #     row = next_emptyrow(board, columnPlayer1)
                #    drop_piece(board, row, columnPlayer1, 1)
                 #   if wining_move(board, 1) == True:
                  #      print("Player 1 is Win!!!!! ")
                   #     game_over = True
                    #Flag = 1
           # else:
            #    columnPlayer2 = int(input(" Player 2 Enter your selection (0-6) : "))
             #   if isvalid_location(board, columnPlayer2):
              #      row = next_emptyrow(board, columnPlayer2)
               #     drop_piece(board, row, columnPlayer2, 2)
                #    if wining_move(board, 2) == True:
                       # print_flipboard(board)
                 #       print("Player 2 is Win!!!!! ")
                  #      game_over = True
                   # Flag = 0
           # print_flipboard(board)