'''
Created on 24-Nov-2017

@author: Premkumar Jayakumar
'''
player1 = 'X'
player2 = 'O'
MAX_X_SCORE = int(10)
MAX_O_SCORE = int(-10)
DRAW_SCORE = int(0)

def evaluate_board(board):
    if (board[0][0] == board[1][1] == board[2][2]):
        if board[0][0] == 'X':
            return MAX_X_SCORE
        elif board[0][0] == 'O':
            return MAX_O_SCORE
    
    if (board[2][0] == board[1][1] == board[0][2]):
        if board[2][0] == 'X':
            return MAX_X_SCORE
        elif board[2][0] == 'O':
            return MAX_O_SCORE
        
    #Check Row Matching
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return MAX_X_SCORE
            elif board[row][0] == 'O':
                return MAX_O_SCORE
    
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return MAX_X_SCORE
            elif board[0][col] == 'O':
                return MAX_O_SCORE
        
    return DRAW_SCORE


def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

def minimax(board, depth, isMax):
    score = evaluate_board(board)
    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    
    if is_moves_left(board) == False:
        return DRAW_SCORE
    
    if isMax == True:
        best_val = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    cur_best = minimax(board, depth+1, False)
                    best_val = max(cur_best, best_val)
                    board[i][j] = '_'
                    return best_val
    else:
        best_val = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    cur_best = minimax(board, depth+1, True)
                    best_val = min(cur_best, best_val)
                    board[i][j] = '_'
                    return best_val
    
    
def find_best_move(board, player):
    next_row = -1
    next_col = -1
    if player == player1: #'X'
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    this_best = minimax(board, 0, False)
#                     print("Player1: Best at ({},{}) is {}".format(i, j, this_best))
                    if best < this_best:
                        best = this_best
                        next_row = i
                        next_col = j
                    board[i][j] = '_'
    elif player == player2: #'O'
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    this_best = minimax(board, 0, True)
                    print("Player2: Best at ({},{}) is {}".format(i, j, this_best))
                    if best > this_best:
                        best = this_best
                        next_row = i
                        next_col = j
                    board[i][j] = '_'
    else:
        print("Invalid Player")
        return None
    
    return (next_row, next_col)

def print_board(board):
    print("$$$$$$$")
    row = ""
    for i in range(3):
        for j in range(3):
            row += board[i][j] + " "
        print(row)
        row = ""
    print("$$$$$$$")

if __name__ == '__main__':
    board = [['X','O','X'],
             ['_','O','_'],
             ['_','_','_']]
    
    print(find_best_move(board, player1))

#     move_count = 1
#     while evaluate_board(board) == 0 and is_moves_left(board) == True:
#         print_board(board)
#         if move_count % 2 == 1:
#             print("Player#1: Choose your Position. Enter row,col. Ex: 0,1")
#             row,col = input().split(",")
#             board[int(row)][int(col)] = player1
#             move_count += 1
#         else:
#             next_row, next_col = find_best_move(board, player2)
#             board[next_row][next_col] = player2
#             move_count += 1            
#     
#     final_board_score = evaluate_board(board) 
#     if final_board_score == MAX_X_SCORE:
#         print("Player1: You win!!")
#     elif final_board_score == MAX_O_SCORE:
#         print("Player2: Computer Wins!!") 
#     else:
#         print("Game Draw!!")
