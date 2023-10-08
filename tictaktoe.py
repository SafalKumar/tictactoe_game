import random
board=["-","-","-",
       "-","-","-",           
       "-","-","-"]
currentPlayer="X"
winner=None
gameRunning=True

#printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)


#Take player input
def playerInput(board):
    inp=int(input("Enter number between 1-9: "))
    if inp>=1 and inp<=9:
        if board[inp-1] == "-":
            board[inp-1]=currentPlayer
        else:
            print("Sorry place already taken")
    else:
        print("Please Enter valid input")

#check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] ==board[1] == board[2] and board[0]!="-":
        winner=board[2]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner=board[5]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner=board[6]
        return True
    
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] !="-":
        winner=board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] !="-":
        winner=board[1]
        return True
    elif board[2] == board[5] == board[8] and board[8]!="-":
        winner=board[2]
        return True
    
    
def checkDig(board):
    global winner
    if board[0] == board [4] == board [8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!="-":
        winner=board[2]
        return True 
    
    
#check for tie


def checktie(board):
    global gameRunning 
    if "-" not in board:
        printBoard(board)
        print("It's a draw")
        gameRunning=False
                
    
def checkwin():
    global gameRunning
    if checkHorizontle (board) or checkRow(board) or checkDig(board):
        printBoard(board)
        print(f"Winner is {winner}")
        gameRunning = False
        
# smart computer
def generateComputerMove(board):
    for i in range(9):
        if board[i]=="-":
            board[i]="0"
            if checkwinningmove(board,"0"):
                return i
            board[i]="-"
            
    valid_moves=[i for i in range(9) if board[i] == "-"]
    return random.choice(valid_moves)
                
                
def checkwinningmove(board,currentPlayer):
    for i in range(9):
        if board[i] == "-":
            board[i] = currentPlayer
            if checkwinningmove(board,currentPlayer):
                board[i]="-"
                return True
            board[i]="-"
    return False
            
            

#def checkwinningmove(board,currentPlayer):
    
            
# switch Player
def switchPlayer():
    global currentPlayer 
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"
        
        
def computer(board):
    while currentPlayer == "0" :
        position= random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()
     
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkwin()
    checktie(board)
    switchPlayer()
    if gameRunning:
        #computer(board)
        position=generateComputerMove(board)
        board[position]="0"
        checkwin()
        checktie(board)
        switchPlayer()