import sys
import numpy as np
import pygame
import math
# board rows=6 columns=7
red = (255, 0, 0)
blue = (0, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
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
            pygame.draw.circle(screen, white, (int(c*squareSize+squareSize/2), int(r*squareSize+squareSize+squareSize/2)), radius)
    for c in range(num_columns):
        for r in range(num_rows):
            # player number 1 ------>1 (red)
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c * squareSize + squareSize / 2), height-int(r * squareSize + squareSize / 2)), radius)
            # player number 2 ------->2 (blue)
            elif board[r][c] == 2 :
                pygame.draw.circle(screen, blue, (int(c * squareSize + squareSize / 2), height-int(r * squareSize + squareSize / 2)), radius)
    pygame.display.update()
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
# to write who is win
text = pygame.font.SysFont("monospace", 65)
# game not over
Flag = 0
while not game_over:
    for event in pygame.event.get():
       # if event.type == pygame.quit():
         #   sys.exit()
       if event.type == pygame.MOUSEMOTION:
           position=event.pos[0]
           pygame.draw.rect(screen, white, (0,0, width, squareSize))
           if Flag == 0:
               # player 1
               pygame.draw.circle(screen, red, (position, int(squareSize/2)), radius)
           else:
               pygame.draw.circle(screen, blue, (position, int(squareSize / 2)), radius)

       pygame.display.update()
        # drop piece
       if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, white, (0, 0, width, squareSize))
            # input_of_player1
            if Flag == 0:
                # pos
                posplayer1 = event.pos[0]
                columnPlayer1 = int(math.floor(posplayer1/squareSize))
                if isvalid_location(board, columnPlayer1):
                    row = next_emptyrow(board, columnPlayer1)
                    drop_piece(board, row, columnPlayer1, 1)
                    if wining_move(board, 1) == True:
                        label = text.render("Player 1 win !!!!", 1, red)
                        screen.blit(label, (10, 10))
                        game_over = True
                    Flag = 1
            else:
                posplayer2 = event.pos[0]
                columnPlayer2 = int(math.floor(posplayer2 / squareSize))
                if isvalid_location(board, columnPlayer2):
                    row = next_emptyrow(board, columnPlayer2)
                    drop_piece(board, row, columnPlayer2, 2)
                    if wining_move(board, 2) == True:
                       # print_flipboard(board)
                       label = text.render("Player 2 win !!!!", 1,blue)
                       screen.blit(label, (10, 10))
                       game_over = True
                    Flag = 0
            print_flipboard(board)
            print_boardGraphics(board)
            if game_over:
                pygame.time.wait(4000)