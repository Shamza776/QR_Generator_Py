import random
'''New file'''
'''example of a new concept learnt,, end paramenter, sep, newline
print("This is line one \n" " This is line two") #using the end line character \n
print("This is line one", end=" ,") #using the end  parameter to change how print behaves
print("this is a statement withing the first line! ")
print("This a a different line from the next one", end="\n") #using end parameter  and using the escape sequence for newline.
print("The different line")
print("Another line", sep="")
print("line not  included in the output of the above statement") '''

'''Now let's work on the TicTacToe project'''
'''The outlook'''

possibleNumbers = [1,2,3,4,5,6,7,8,9]
def outlookBoard ():
    print("welcome to the Tic Tac Toe game")
    print("--------------------------------\n")
    #possibleNumbers = [1,2,3,4,5,6,7,8,9]
    board = [[1,2,3], [4,5,6],  [7,8,9]]  ##2D list containg the values of the board
    row = 3
    col = 3
    y = 1
##let us loop through the 2D list
    for x in range(row):
       print("\n+---+---+---+")
       print("| ", end="")
           
       for y in range(col):          ##looping through columns
            print( board[x][y], end=" | ")

def modifyBoard(num, turn):   #num is the  number that has been chosen by the user and turn is X or O
    global board                      ##accessing the global variable instead of creating a local one
    global possibleNumbers
    num -= 1    #to  match our index system when comparing the number the user picked and the one on the board
    if (num == 0):
        board[0][0] = turn
    elif (num == 1):
        board[0][1] = turn
    elif (num == 2):
        board[0][2] = turn
    elif (num == 3):
        board[1][0] = turn
    elif (num == 4):
        board[1][1] = turn
    elif (num == 5):
        board[1][2] = turn
    elif (num == 6):
        board[2][0] = turn
    elif (num == 7):
        board[2][1] = turn
    elif (num == 8):
        board[2][2] = turn


'''def checkForWinner():
    global board
    ##X axis the several ways of winning in the x axis
    if ((board[0][0]==board[1][1]==board[2][2])or \
        (board[0][2]==board[1][1]==board[2]

    ##Y axis '''


leaveLoop = False               ##this will be used later on to break from loops or end the game
turnCounter = 0  ##keep track on whether its the cpu's turn or the user's turn

while(leaveLoop == False):     #while this statement is true we want to operate the case 
   ##it's the player's turn
    if(turnCounter % 2 == 1): ## if the turn counter divided by two and the remainder is 1, we know it's ur turn
        outlookBoard()
        numPicked = int(input('\nEnter your move: (no. between 1 and 9); '))
        ##validate the input from the user
        if(numPicked >=1 or numPicked <= 9):  #meaning it's a valid choice from the user
            modifyBoard(numPicked,  "X")           #add the mark to the board
            possibleNumbers.remove(numPicked)   ##to exclude the no. picked
        else:
            print("\nInvalid Move! Please enter a number between 1-9.")
        turnCounter +=1
    else:      ##it's the computer's turn
        while True:       ##a loop within a loop which keeps running until a valid move for the computer is found
            cpuChoice = random.choice(possibleNumbers)
            print("\nCpu choice: ", cpuChoice)
            if(cpuChoice in possibleNumbers): #if cpu choice is among the possible  numbers then modify the board
                modifyBoard(cpuChoice,"O")          #add the mark to the board
                possibleNumbers.remove(cpuChoice)   ##exclude the chosen number from possibilities
            turnCounter += 1

    
            
            
                








