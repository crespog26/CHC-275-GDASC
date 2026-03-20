
"""
Name: Gabby Crespo
Section: 275-02
Description: Connect 4
"""


def drawBoard(board):
    
    print("\n 1 2 3 4 5 6 7")
    for row in range(6):
        print("|", end="")
        for col in range(7):
            cell = board[row][col]
            if cell == 0:
                print(" .", end="")
            else:
                print(f" {cell}", end="")
        print(" |")
    print("  ---------------\n")
 

def switchPlayer(player):
    
    if player =='X':
        return 'O'
    else:
        return 'X'

    
def dropPiece(board,player,column):
    
    col_idx = column - 1
    for row in range(5, -1, -1):
        if board[row][col_idx] == 0:
            board[row][col_idx] = player
            return True
    print(f"Column {column} is full. choose another column.")
    return False
    
    
def checkWinner(board,player):
   
    #Check Horizontal Win
    for row in range(6):
        for col in range(4):
            if (board[row][col] == player and
                board[row][col+1] == player and
                board[row][col+2] == player and
                board[row][col+3] == player ):
                return True
    
    #Check Vertical Win
    for col in range(7):
        for row in range(3):
            if (board[row][col] == player and
                board[row+1][col] == player and
                board[row+2][col] == player and
                board[row+3][col] == player ):
                return True

    #Check Right Diagonal Win
    for row in range(3):
            for col in range(4):
                if (board[row][col] == player and
                    board[row+1][col+1] == player and
                    board[row+2][col+2] == player and
                    board[row+3][col+3] == player ):
                    return True
                
    #Check Left Diagonal win
    for row in range(3):
        for col in range(3, 7):
            if (board[row][col] == player and
                board[row+1][col-1] == player and
                board[row+2][col-2] == player and
                board[row+3][col-3] == player ):
                return True
            
    return False 


def main():
    ROWS = 6
    COLUMNS = 7
    board = [ 
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],        
    ]

    current_player = "X"
    game_over = False
    
    print("Welcome to Connect 4 (o゜▽゜)o☆")
    drawBoard(board)
    
    while not game_over:
        print(f"Player {current_player}'s turn.")
        try:
            col = int(input("Choose a column (1-7): "))
            if col < 1 or col > 7:
                print("Please enter a number between 1 and 7.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if dropPiece(board, current_player, col):
            drawBoard(board)

            if checkWinner(board, current_player):
                print(f"Player {current_player} wins! 🎉")
                game_over = True
            else:
                current_player = switchPlayer(current_player)

        if all(cell != 0 for row in board for cell in row):
            print("The board is full. It's a tie!")
            game_over = True
    
if __name__ == "__main__":
    main()