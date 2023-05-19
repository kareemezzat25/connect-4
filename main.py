import random
import math
num_rows = 6
num_columns = 7
player_piece = 1
Ai_piece = 2
# check if top row is empty or not
def isValid_location(board, column):
    return board[num_rows-1][column] == 0
# get next empty row for this column
def getNext_emptyRow(board,column):
    for row in range(num_rows):
        if board[row][column] == 0:
            return row
# function who is win
def winning(board,piece):
    # check horizontal
    for column in range(num_columns-3):
        for row in range(num_rows):
            # - - - -
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True
    # check vertical
    for column in range(num_columns):
        for row in range(num_rows-3):
            # check if 4 row in same column have same piece or no
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece and board[row+3][column] == piece:
                return True
      # check diagonal
    for column in range(num_columns-3):
        for row in range(num_rows-3):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece and board[row+3][column+3] == piece:
                return True

    for column in range(num_columns-3):
        for row in range(3, num_rows):
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece and board[row-3][column+3] == piece:
                return True
def evaluate_window(window,piece):
    score = 0
    opp_piece = player_piece
    # if piece == 2 else 2
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score +=2
    # check in opposite piece
    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -=4
    return score

def position_ofScore(board, piece):
    score = 0
    centerArray = [int(i) for i in list(board[:, 3])]
    centerCount = centerArray.count(piece)
    score += centerCount*3
    for row in range (board.shape[0]):
        rowArray = [int(i) for i in list(board[row, :])]
        for column in range(num_columns-3):
            window = rowArray[column:column+4]
            score += evaluate_window(window,piece)
    # score of vertical
    for column in range (num_columns):
        columnArray = [int(i) for i in list(board[:,column])]
        for row in range(num_rows-3):
            window = columnArray[row:row+4]
            score += evaluate_window(window,piece)
    # score diagonal
    for row in range(num_rows-3):
        for column in range(num_columns-3):
            window = [board[row+i][column+i] for i in range(4)]
            score += evaluate_window(window, piece)

    for row in range(num_rows - 3):
        for column in range(num_columns - 3):
            window = [board[row +3- i][column + i] for i in range(4)]
            score += evaluate_window(window, piece)
    return score
# return list of columns that have valid locations
def getValidLocations(board):
    validLocations = []
    for column in range(num_columns):
        if isValid_location(board, column):
            validLocations.append(column)
    return validLocations
# check if this is terminalnode or not
def isTerminal(board):
    # one of player win or no place to add in it
    return winning(board, player_piece) or winning(board, Ai_piece) or len((getValidLocations(board))) == 0
# minimax
def minimax(board,depth,alpha,beta,maximizing_player):
    # get the columns that have valid locations
    validlocations = getValidLocations()
    isTerminal = isTerminal.node(board)
    if depth == 0 or isTerminal:
        if isTerminal:
            if winning(board,2):            # AI is the winner
                return(None,100000000000000)    
            elif winning(board,1):          # player is the winner
                return(None,-100000000000000)
            else:                           # no one winner
                return(None,0)
        else:                               # Depth = 0
            return(None,position_ofScore(board,2))
    if maximizing_player:
        value = -math.inf
        column = random.choice(validlocations)
        for col in validlocations:
            row = getNext_emptyRow(board,col)
            board_copy = board.copy()
            new_score = minimax(board_copy,depth-1,alpha,beta,False)[1]
            if new_score > value:
                value = new_score
                column = col
                alpha = max(alpha,value)
                if alpha >= beta:
                    break
                return column,value
    else:                                   # minimizing player
        value = math.inf
        column = random.choice(validlocations)
        for col in validlocations:
            row = getNext_emptyRow(board,col)
            board_copy = board.copy()
            new_score = minimax(board_copy,depth-1,alpha,beta,True)[1]
            if new_score < value:
                column = col
                beta = min(beta,value)
                if alpha >= beta:
                    break
                return column,value