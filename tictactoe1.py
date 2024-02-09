possibleNum = [1,2,3,4,5,6,7,8,9] #list of the numbers the player will choose
board = [[1,2,3],[4,5,6],[7,8,9]] ##2d list of the values to be present on the board

def outLook():
    global possibleNum
    global board
    y = 0
    print("Welcome to our Tic Tac Toe game")
    print("--------------------------------")
    for x in range(3):
        print("\n+---+---+---+")  ##foundation look of the tic tac toe game
        print("|", end="")

        for y in range(3):
            print(board[x][y], end=" | ") 
            
        #y+=1
outLook()

def modyfication():
    pass

def checkWinner():
    pass