def humanMove(board):
    valid = None
    while valid != "success":
        move = int(input("where do you want to place your move? "))
        valid = checkMove(board, move)
        print(valid)
    return move

def cpuMove(board, posWins):
    x = checkHumanMoves(board,posWins)
    y = checkHumanMoves(board,posWins, "O")
    
    if checkHumanMoves(board,posWins) != False:
        valid = checkMove(board, x[2])
        if valid == "success":
            return x[2]
        
    elif y != False:
        valid = checkMove(board, i)
        if valid == "success":
            return x[2]
    
    bestPlaces = (4,0,2,6,8,1,3,5,7)
    for i in bestPlaces:
        valid = checkMove(board, i)
        if valid == "success":
            return i       
        

def checkHumanMoves(board, posWins, player = "X"):
    x = None
    for moveSet in posWins:
        count = 0
        if board[moveSet[0]] == player:
            count += 1
        if board[moveSet[1]] == player:
            count += 1
        if board[moveSet[2]] == player:
            count += 1
            return moveSet
    return False
    

def checkWin(board, posWins, player):
    count = 0
    for moveSet in posWins:
        count = 0
        if board[moveSet[0]] == player:
            count += 1
        if board[moveSet[1]] == player:
            count += 1
        if board[moveSet[2]] == player:
            count += 1
        
        if count == 3:
            return True
    
    for i in board:
        if i == 1:
            count += 1
    if count == 0:
        return "TIE"
    return False

    

def checkMove(board, move, maxMoves = 8):
    if move > maxMoves:
        return "this square does not exist"
    if board[move] != 1:
        return "this sqaure has already been used"
    return "success"

def printBoard(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8], "\n")

possibleWins =((0,1,2),
               (3,4,5),
               (6,7,8),
               (0,3,6),
               (1,4,7),
               (2,5,8),
               (0,4,8),
               (2,4,6))

game = "ongoing"
board = [x**0 for x in range(9)]

while game == "ongoing":
    
    board[humanMove(board)] = "X"
    printBoard(board)
    if checkWin(board, possibleWins, "X") == True:
        print("YOU WON")
        break
    
    if checkWin(board, possibleWins, "X") == "TIE":
        print("ITS A DRAW")
        break
                
    board[cpuMove(board, possibleWins)] = "O"
    printBoard(board)
    if checkWin(board, possibleWins, "O") == True:
        print("COMPUTER WINS")
        break
    
    if checkWin(board, possibleWins, "X") == "TIE":
        print("ITS A DRAW")
        break
print("game over")
    
    