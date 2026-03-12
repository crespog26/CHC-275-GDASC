

"""
tictactoe
"""
def main():
    curr = "x" 


    
print("Starting TicTacToe")

current_player = "O" #in this version of tic tac toe O is the starting player
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#our board is a 3x3 grid where the empty space is 0
#we need a printboard function that doesn't look terrible

def printBoard(board):
    #we want each row printed on its own line
    #we need a nested for-each loop
    for row in board: 
        #pull out every row
        for space in row: 
        #pulls out space in every row
            print(space, end="") #replace end with an empty string so all of the spaces in a row print on the same line
        print() #empty print function just prints \n to the terminal

def placePiece(row,col,board,current_player):
    #remember that when we pass control to a function we leave the global scope and enter local scope so 
    #we can't access variables declared in global scope 
    if board[row][col] == 0:
        board[row][col]=current_player #is this sufficient in the logic of tictactoe?
        return True #returning true so the program knows that the piece was actually placed
    else: 
        return False 
    
    """ 
    if we add a true and false return statement at the end, then our program knows whether or not placePiece executed
    successfully 
    """
    
print()
printBoard(board)
placePiece(1,1,board,"O")
print()
printBoard(board)
placePiece(1,1,board,"X")
print()
printBoard(board)

def switchPlayer(current_player):
    #are strings pass by value?
    if current_player == "O":
         return "X"
    elif current_player == "X":
         return "O"
        

"""print(current_player) #currently O
current_player = switchPlayer(current_player)
print(current_player) #Should be X"""

def checkWinner(board,current_player):
    #Row Victories 
    #I think a for loop might be useful here, but I need direct access to the memory
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == current_player:
           print(f"{current_player} wins")
           return True
    
    #Column Victories
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] == board[2][i] == current_player:
            print(f"{current_player} wins")
            return True
    #Diagonal Victories
    #left diagonal 
    
    """
    [0][0] [1][1] [2][2] 
    000
    000
    000
    """
    if board[0][0] == board[1][1] == board[2][2] == current_player:
            print(f"{current_player} wins")
            return True
        
    #right diagonal victories
    """ 
    000 [0][2] [1][1] [2][0]
    000
    000
    000
    """
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        print(f"{current_player} wins")
        return True
    
board1 = [
    ["O","O","O"],
    [0,0,0],
    [0,0,0]
]

board2 = [
    ["O",0,0],
    ["O",0,0],
    ["O",0,0]
]

board3 = [
    ["O",0,0],
    [0,"O",0],
    [0,0,"O"]
]

checkWinner(board1,"O")
checkWinner(board2,"O")
checkWinner(board3,"O")

#tie
#no empty spaces left
#the only reason why we return a value is to signal the game that we have finished playing
#if there's a tie, return true. if all else fails, return false, game continues
def placePiece(row,col,board,current_player):
    check = False
    for row in board:
        for space in row:
            if space == 0:
                return check
            
    return True

if __name__ == main():
    main()













