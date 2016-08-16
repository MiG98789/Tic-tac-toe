import random

def drawboard(board): #Draw the board
    print(board[0],'|',board[1],'|',board[2])
    print('---------')
    print(board[3],'|',board[4],'|',board[5])
    print('---------')
    print(board[6],'|',board[7],'|',board[8])
    print("\n")

def reset(): #Reset the board
    drawboard([' ',' ',' ',' ',' ',' ',' ',' ',' '])

def botORplayer():
    flag = False
    selection = input("Do you want to play against a bot or another player? (bot or player) \n").lower()
    if selection.startswith('b') == True:
        flag = True
    elif selection.startswith('p') == True:
        flag = True
    else:
        flag = False
    while flag == False:
        selection = input("That was an invalid input. Please input again.\n").lower()
        if selection.startswith('b') == True:
            flag = True
        elif selection.startswith('p') == True:
            flag = True
        else:
            flag = False
    
    if selection.startswith('b'):
        difficulty()
    elif selection.startswith('p'):
        firstPlayerVSplayer()
    
def playAgain(): #After the game, ask if play again
    again = input("\nDo you want to play again? (yes or no)\n")
    again = again.lower().startswith('y')
    if again == True:
        print("\n")
        reset()
        botORplayer()

def difficulty():
    flag = False
    diff = input("What difficulty level do you want? (easy: level 1 or hard: level 2)\n")
    if(diff == '1' or diff == '2'):
        flag = True
    else:
        flag = False
    while flag == False:
        diff = input("That was an invalid input. Please input again.\n")
        if diff == '1':
            flag = True
        elif diff == '2':
            flag = True
        else:
            flag = False

    firstPlayerVSbot(diff)

def victoryCheck(VSbotORVSplayer, board, i, check, first, p1name, p2name):  
    if VSbotORVSplayer.startswith('b') == True: #If VS Bot
        if first == True:
            Owin = "\nYou win!"
            Xwin = "Bot wins!"
        else:
            Owin = "Bot wins!"
            Xwin = "\nYou win!"

    elif VSbotORVSplayer.startswith('p') == True: #If VS Player
        Owin = ''.join((p1name, ' wins!'))
        Xwin = ''.join((p2name, ' wins!'))
                
    if (board[0] == board[1] and board[1] == board[2]): #Top row
        if board[0] == 'O':
            print(Owin)
            return 1
        elif board[0] == 'X':
            print(Xwin)
            return 1
            
    elif (board[3] == board[4] and board[4] == board[5]): #Middle row
        if board[3] == 'O':
            print(Owin)
            return 1
        elif board[3] == 'X':
            print(Xwin)
            return 1

    elif (board[6] == board[7] and board[7] == board[8]): #Bottom row
        if board[6] == 'O':
            print(Owin)
            return 1
        elif board[6] == 'X':
            print(Xwin)
            return 1

    elif (board[0] == board[3] and board[3] == board[6]): #Right column
        if board[0] == 'O':
            print(Owin)
            return 1
        elif board[0] == 'X':
            print(Xwin)
            return 1

    elif (board[1] == board[4] and board[4] == board[7]): #Middle column
        if board[4] == 'O':
            print(Owin)
            return 1
        elif board[4] == 'X':
            print(Xwin)
            return 1

    elif (board[2] == board[5] and board[5] == board[8]): #Right column
        if board[2] == 'O':
            print(Owin)
            return 1
        elif board[2] == 'X':
            print(Xwin)
            return 1

    elif (board[6] == board[4] and board[4] == board[2]): #Positive-slope diagonal
        if board[6] == 'O':
            print(Owin)
            return 1
        elif board[6] == 'X':
            print(Xwin)
            return 1

    elif (board[0] == board[4] and board[4] == board[8]): #Negative-slope diagonal
        if board[0] == 'O':
            print(Owin)
            return 1
        elif board[0] == 'X':
            print(Xwin)
            return 1

    elif i == 5:
        print("Nobody wins.")
        return 1
        
    elif check == 5:
        print("Nobody wins.")
        return 1
    
#For VS Bot        
def firstPlayerVSbot(diff): #Determines who goes first
    first = str(random.randint(0,1))
    first = first.startswith('1')

    if diff == '1':
        gameVSeasybot(first)
    elif diff == '2':
        gameVShardbot()

#For VS Easy Bot
def gameVSeasybot(first): #VS Easy Bot
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    usedMoves = ['F','F','F','F','F','F','F','F','F']
    check = 0
    
    if first == True: #If Player is first to move
        print("You go first.\n")
        for i in range(0,5):
            #Victory check
            if victoryCheck('b', board, i, check, first, '','') == 1:
                drawboard(board)
                break
            
            #Player's move
            playerPosition = int(input("Where do you want to put O?\n"))
            playerPosition -= 1

            #Verification of position for Player's move
            for j in range(0,8):
                if usedMoves[playerPosition] == 'T':
                    while usedMoves[playerPosition] == 'T':
                        playerPosition = int(input("That space has already been taken. Please input the position again.\n"))
                        playerPosition -= 1
                    usedMoves[playerPosition] = 'T'
                    break
                else:
                    usedMoves[playerPosition] = 'T'
                    break

            check += 1    
            board[playerPosition] = "O"

            #Victory check    
            if victoryCheck('b', board, i, check, first, '','') == 1:
                drawboard(board)
                break
                
            #Bot's move
            botPosition = playerPosition
            while botPosition == playerPosition:     
                botPosition = random.randint(0,8)

                #Verification of position for Bot's move
                for k in range(0,8):
                    if usedMoves[botPosition] == 'T':
                        while usedMoves[botPosition] == 'T':
                            botPosition = random.randint(0,8)
                        usedMoves[botPosition] = 'T'
                        break
                    else:
                        usedMoves[botPosition] = 'T'
                        break

                board[botPosition] = "X"
            
            drawboard(board)
            print("\n")            
            i+= 1
            

    else: #If Bot is first to move
        print("You go second.\n")
        check = 0
        #Bot goes first
        botPosition = random.randint(0,8)
        usedMoves[botPosition] = 'T'
        board[botPosition] = "O"
        
        for i in range(0,5):
            drawboard(board)
            
            #Victory check
            if victoryCheck('b', board, i, check, first, '','') == 1:
                break
            
            #Player's move
            playerPosition = int(input("Where do you want to put X?\n"))
            playerPosition -= 1

            #Verification of position for Player's move
            for j in range(0,8):
                if usedMoves[playerPosition] == 'T':
                    while usedMoves[playerPosition] == 'T':
                        playerPosition = int(input("That space has already been taken. Please input the position again.\n"))
                        playerPosition -= 1
                    usedMoves[playerPosition] = 'T'
                    break
                else:
                    usedMoves[playerPosition] = 'T'
                    break

            check += 1
            board[playerPosition] = "X"

            #Victory check
            if victoryCheck('b', board, i, check, first, '','') == 1:
                drawboard(board)
                break

            #Bot's move
            botPosition = playerPosition
            while botPosition == playerPosition:
                botPosition = random.randint(0,8)

                #Verification of position for Bot's move
                for k in range(0,8):
                    if usedMoves[botPosition] == 'T':
                        while usedMoves[botPosition] == 'T':
                            botPosition = random.randint(0,8)
                        usedMoves[botPosition] = 'T'
                        break
                    else:
                        usedMoves[botPosition] = 'T'
                        break

            
            board[botPosition] = "O"
                
            i+= 1

    #End of game
    playAgain()


def gameVShardbot():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    usedMoves = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    check = 0
    corner = [0,2,6,8]
    edge = [1,3,5,7]
    flag = 0
    i = 0
    win = 0
    
    first = True
    
    if first == True: #If Player is first to move
        print("You go first.\n")

        #Player's move
        playerPosition = int(input("Where do you want to put O?\n"))
        playerPosition -= 1

        check += 1    
        board[playerPosition] = "O"
        usedMoves[playerPosition] = 'O'

        #Bot's move
        while flag == 0:    
            if playerPosition != 4:
                botPosition = 4
                flag = 1
            else:
                botPosition = random.randint(0,3)
                botPosition = corner[botPosition]
                flag = 1

        usedMoves[botPosition] = 'X'
        board[botPosition] = "X"
        flag = 0
        drawboard(board)
        print("\n")
        i+=1

        #Player's move
        playerPosition = int(input("Where do you want to put O?\n"))
        playerPosition -= 1

        #Verification of position for Player's move
        for j in range(0,8):
            if(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                while(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                    playerPosition = int(input("That space has already been taken. Please input the position again.\n"))
                    playerPosition -= 1
                usedMoves[playerPosition] = 'O'
                break
            else:
                usedMoves[playerPosition] = 'O'
                break

        check += 1    
        board[playerPosition] = "O"

        #Bot's move
        if(((board[8]=='O' and board[4]=='O')or(board[1]=='O' and board[2]=='O')or(board[3]=='O' and board[6]=='O')) and board[0] == ' '): #Put X in cell 1
            botPosition = 0
        elif(((board[7]=='O' and board[4]=='O')or(board[0]=='O' and board[2]=='O')) and board[1] == ' '): #Put X in cell 2
            botPosition = 1
        elif(((board[6]=='O' and board[4]=='O')or(board[1]=='O' and board[0]=='O')or(board[5]=='O' and board[8]=='O')) and board[2] == ' '): #Put X in cell 3
            botPosition = 2
        elif(((board[0]=='O' and board[6]=='O')or(board[4]=='O' and board[5]=='O')) and board[3] == ' '): #Put X in cell 4
            botPosition = 3
        elif(((board[2]=='O' and board[8]=='O')or(board[4]=='O' and board[3]=='O')) and board[5] == ' '): #Put X in cell 6
            botPosition = 5
        elif(((board[2]=='O' and board[4]=='O')or(board[7]=='O' and board[8]=='O')or(board[0]=='O' and board[3]=='O')) and board[6] == ' '): #Put X in cell 7
            botPosition = 6
        elif(((board[6]=='O' and board[8]=='O')or(board[4]=='O' and board[1]=='O')) and board[7] == ' '): #Put X in cell 8
            botPosition = 7
        elif(((board[6]=='O' and board[7]=='O')or(board[4]=='O' and board[0]=='O')or(board[2]=='O' and board[5]=='O')) and board[8] == ' '): #Put X in cell 9
            botPosition = 8
        else:
            botPosition = random.randint(0,3)
            botPosition = corner[botPosition]
            while flag == 0:
                for j in range(0,8):
                    if(usedMoves[botPosition]=='O' or usedMoves[botPosition]=='X'):
                        while(usedMoves[botPosition]=='O' or usedMoves[botPosition]=='X'):
                            botPosition = random.randint(0,3)
                            botPosition = corner[botPosition]
                        break
                    flag = 1
       
        usedMoves[botPosition] = 'X'
        board[botPosition] = "X"
        flag = 0
        drawboard(board)
        print("\n")
        i+=1

       #Player's move
        playerPosition = int(input("Where do you want to put O?\n"))
        playerPosition -= 1

        #Verification of position for Player's move
        for j in range(0,8):
            if(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                while(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                    playerPosition = int(input("That space has already been taken. Please input the position again.\n"))
                    playerPosition -= 1
                usedMoves[playerPosition] = 'O'
                break
            else:
                usedMoves[playerPosition] = 'O'
                break

        check += 1    
        board[playerPosition] = "O"

        #Bot's move
        if(((board[8]=='X' and board[4]=='X')or(board[1]=='X' and board[2]=='X')or(board[3]=='X' and board[6]=='X')) and board[0]==' '): #Put X in cell 1
            botPosition = 0
        elif(((board[7]=='X' and board[4]=='X')or(board[0]=='X' and board[2]=='X'))and board[1]==' '): #Put X in cell 2
            botPosition = 1
        elif(((board[6]=='X' and board[4]=='X')or(board[1]=='X' and board[0]=='X')or(board[5]=='X' and board[8]=='X')) and board[2]==' '): #Put X in cell 3
            botPosition = 2
        elif(((board[0]=='X' and board[6]=='X')or(board[4]=='X' and board[5]=='X'))and board[3]==' '): #Put X in cell 4
            botPosition = 3
        elif(((board[2]=='X' and board[8]=='X')or(board[4]=='X' and board[3]=='X'))and board[5]==' '): #Put X in cell 6
            botPosition = 5
        elif(((board[2]=='X' and board[4]=='X')or(board[7]=='X' and board[8]=='X')or(board[0]=='X' and board[3]=='X'))and board[6]==' '): #Put X in cell 7
            botPosition = 6
        elif(((board[6]=='X' and board[8]=='X')or(board[4]=='X' and board[1]=='X'))and board[7]==' '): #Put X in cell 8
            botPosition = 7
        elif(((board[6]=='X' and board[7]=='X')or(board[4]=='X' and board[0]=='X')or(board[2]=='X' and board[5]=='X'))and board[8]==' '): #Put X in cell 9
            botPosition = 8
        elif(((board[8]=='O' and board[4]=='O')or(board[1]=='O' and board[2]=='O')or(board[3]=='O' and board[6]=='O')) and board[0] == ' '): #Put X in cell 1
            botPosition = 0
        elif(((board[7]=='O' and board[4]=='O')or(board[0]=='O' and board[2]=='O')) and board[1] == ' '): #Put X in cell 2
            botPosition = 1
        elif(((board[6]=='O' and board[4]=='O')or(board[1]=='O' and board[0]=='O')or(board[5]=='O' and board[8]=='O')) and board[2] == ' '): #Put X in cell 3
            botPosition = 2
        elif(((board[0]=='O' and board[6]=='O')or(board[4]=='O' and board[5]=='O')) and board[3] == ' '): #Put X in cell 4
            botPosition = 3
        elif(((board[2]=='O' and board[8]=='O')or(board[4]=='O' and board[3]=='O')) and board[5] == ' '): #Put X in cell 6
            botPosition = 5
        elif(((board[2]=='O' and board[4]=='O')or(board[7]=='O' and board[8]=='O')or(board[0]=='O' and board[3]=='O')) and board[6] == ' '): #Put X in cell 7
            botPosition = 6
        elif(((board[6]=='O' and board[8]=='O')or(board[4]=='O' and board[1]=='O')) and board[7] == ' '): #Put X in cell 8
            botPosition = 7
        elif(((board[6]=='O' and board[7]=='O')or(board[4]=='O' and board[0]=='O')or(board[2]=='O' and board[5]=='O')) and board[8] == ' '): #Put X in cell 9
            botPosition = 8
        else:
            botPosition = random.randint(0,8)
            while flag == 0:
                for j in range(0,8):
                    if(usedMoves[botPosition]=='O' or usedMoves[botPosition]=='X'):
                        while(usedMoves[botPosition]=='O' or usedMoves[botPosition]=='X'):
                            botPosition = random.randint(0,8)
                        break
                    flag = 1
       
        usedMoves[botPosition] = 'X'
        board[botPosition] = "X"
        flag = 0
        drawboard(board)
        print("\n")
        i+=1

        #Victory check    
        if victoryCheck('b', board, i, check, first, '', '') == 1:
            drawboard(board)
            win = 1
            
        if win == 0:
            for k in range(2):
                #Player's move
                playerPosition = int(input("Where do you want to put O?\n"))
                playerPosition -= 1

                #Verification of position for Player's move
                for j in range(0,8):
                    if(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                        while(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                            playerPosition = int(input("That space has already been taken. Please input the position again.\n"))
                            playerPosition -= 1
                        usedMoves[playerPosition] = 'O'
                        break
                    else:
                        usedMoves[playerPosition] = 'O'
                        break

                check += 1    
                board[playerPosition] = "O"

                #Victory check    
                if victoryCheck('b', board, i, check, first, '', '') == 1:
                    drawboard(board)
                    win = 1
                    break
                
                #Bot's move
                if(((board[8]=='X' and board[4]=='X')or(board[1]=='X' and board[2]=='X')or(board[3]=='X' and board[6]=='X')) and board[0]==' '): #Put X in cell 1
                    botPosition = 0
                elif(((board[7]=='X' and board[4]=='X')or(board[0]=='X' and board[2]=='X'))and board[1]==' '): #Put X in cell 2
                    botPosition = 1
                elif(((board[6]=='X' and board[4]=='X')or(board[1]=='X' and board[0]=='X')or(board[5]=='X' and board[8]=='X')) and board[2]==' '): #Put X in cell 3
                    botPosition = 2
                elif(((board[0]=='X' and board[6]=='X')or(board[4]=='X' and board[5]=='X'))and board[3]==' '): #Put X in cell 4
                    botPosition = 3
                elif(((board[2]=='X' and board[8]=='X')or(board[4]=='X' and board[3]=='X'))and board[5]==' '): #Put X in cell 6
                    botPosition = 5
                elif(((board[2]=='X' and board[4]=='X')or(board[7]=='X' and board[8]=='X')or(board[0]=='X' and board[3]=='X'))and board[6]==' '): #Put X in cell 7
                    botPosition = 6
                elif(((board[6]=='X' and board[8]=='X')or(board[4]=='X' and board[2]=='X'))and board[7]==' '): #Put X in cell 8
                    botPosition = 7
                elif(((board[6]=='X' and board[7]=='X')or(board[4]=='X' and board[0]=='X')or(board[2]=='X' and board[5]=='X'))and board[8]==' '): #Put X in cell 9
                    botPosition = 8
                elif(((board[8]=='O' and board[4]=='O')or(board[1]=='O' and board[2]=='O')or(board[3]=='O' and board[6]=='O')) and board[0] == ' '): #Put X in cell 1
                    botPosition = 0
                elif(((board[7]=='O' and board[4]=='O')or(board[0]=='O' and board[2]=='O')) and board[1] == ' '): #Put X in cell 2
                    botPosition = 1
                elif(((board[6]=='O' and board[4]=='O')or(board[1]=='O' and board[0]=='O')or(board[5]=='O' and board[8]=='O')) and board[2] == ' '): #Put X in cell 3
                    botPosition = 2
                elif(((board[0]=='O' and board[6]=='O')or(board[4]=='O' and board[5]=='O')) and board[3] == ' '): #Put X in cell 4
                    botPosition = 3
                elif(((board[2]=='O' and board[8]=='O')or(board[4]=='O' and board[3]=='O')) and board[5] == ' '): #Put X in cell 6
                    botPosition = 5
                elif(((board[2]=='O' and board[4]=='O')or(board[7]=='O' and board[8]=='O')or(board[0]=='O' and board[3]=='O')) and board[6] == ' '): #Put X in cell 7
                    botPosition = 6
                elif(((board[6]=='O' and board[8]=='O')or(board[4]=='O' and board[1]=='O')) and board[7] == ' '): #Put X in cell 8
                    botPosition = 7
                elif(((board[6]=='O' and board[7]=='O')or(board[4]=='O' and board[0]=='O')or(board[2]=='O' and board[5]=='O')) and board[8] == ' '): #Put X in cell 9
                    botPosition = 8
                else:
                    botPosition = random.randint(0,8)
                    while flag == 0:
                        for j in range(0,8):
                            if(usedMoves[botPosition]=='O' or usedMoves[botPosition]=='X'):
                                while(usedMoves[botPosition]=='O' or usedMoves[botPosition]=='X'):
                                    botPosition = random.randint(0,8)
                                break
                            flag = 1
               
                usedMoves[botPosition] = 'X'
                board[botPosition] = "X"
                flag = 0
                drawboard(board)
                print("\n")
                i+=1
                    
                #Victory check    
                if victoryCheck('b', board, i, check, first, '', '') == 1:
                    drawboard(board)
                    win = 1
                    break
###########################################################
    else:
        print("Bot goes first.\n")
        check = 0

        #Bot's move                             #WIP
        botPosition = 5
        usedMoves[botPosition] = 'O'
        board[botPosition] = 'O'
        drawboard(board)
        print("\n")
        check+=1

        #Player's move
        playerPosition = int(input("Where do you want to put X?\n"))
        playerPosition -= 1

        #Verification of position for Player's move
        for j in range(0,8):
            if(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                while(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                    playerPosition = int(input("That space has already been taken. Please input the position again.\n"))
                    playerPosition -= 1
                usedMoves[playerPosition] = 'X'
                break
            else:
                usedMoves[playerPosition] = 'X'
                break

        i += 1    
        board[playerPosition] = "X"

        #Bot's move
        if(((board[8]=='X' and board[4]=='X')or(board[1]=='X' and board[2]=='X')or(board[3]=='X' and board[6]=='X')) and board[0] == ' '): #Put O in cell 1
            botPosition = 0
        elif(((board[7]=='X' and board[4]=='X')or(board[0]=='X' and board[2]=='X')) and board[1] == ' '): #Put O in cell 2
            botPosition = 1
        elif(((board[6]=='X' and board[4]=='X')or(board[1]=='X' and board[0]=='X')or(board[5]=='X' and board[8]=='X')) and board[2] == ' '): #Put O in cell 3
            botPosition = 2
        elif(((board[0]=='X' and board[6]=='X')or(board[4]=='X' and board[5]=='X')) and board[3] == ' '): #Put O in cell 4
            botPosition = 3
        elif(((board[2]=='X' and board[8]=='X')or(board[4]=='X' and board[3]=='X')) and board[5] == ' '): #Put O in cell 6
            botPosition = 5
        elif(((board[2]=='X' and board[4]=='X')or(board[7]=='X' and board[8]=='X')or(board[0]=='X' and board[3]=='X')) and board[6] == ' '): #Put O in cell 7
            botPosition = 6
        elif(((board[6]=='X' and board[8]=='X')or(board[4]=='X' and board[1]=='X')) and board[7] == ' '): #Put O in cell 8
            botPosition = 7
        elif(((board[6]=='X' and board[7]=='X')or(board[4]=='X' and board[0]=='X')or(board[2]=='X' and board[5]=='X')) and board[8] == ' '): #Put O in cell 9
            botPosition = 8
        else:
            botPosition = random.randint(0,3)
            botPosition = corner[botPosition]
            while flag == 0:
                for j in range(0,8):
                    if(usedMoves[botPosition]=='O' or usedMoves[botPosition]=='X'):
                        while(usedMoves[botPosition]=='O' or usedMoves[botPosition]=='X'):
                            botPosition = random.randint(0,3)
                            botPosition = corner[botPosition]
                        break
                    flag = 1
       
        usedMoves[botPosition] = 'O'
        board[botPosition] = "O"
        flag = 0
        drawboard(board)
        print("\n")
        i+=1

        #Player's move
        playerPosition = int(input("Where do you want to put X?\n"))
        playerPosition -= 1

        #Verification of position for Player's move
        for j in range(0,8):
            if(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                while(usedMoves[playerPosition]=='O' or usedMoves[playerPosition]=='X'):
                    playerPosition = int(input("That space has already been taken. Please input the position again.\n"))
                    playerPosition -= 1
                usedMoves[playerPosition] = 'X'
                break
            else:
                usedMoves[playerPosition] = 'X'
                break

        i += 1    
        board[playerPosition] = "X"
###########################################################    
    playAgain()
            
#For VS Player    
def firstPlayerVSplayer(): #Determines who goes first
    player1 = input("\nWho is player 1?\n")
    player2 = input("\nWho is player 2?\n")
    first = str(random.randint(1,2))
    first = first.startswith('1')
    if first == "1":
        print(player1, "goes first.\n")
        gameVSplayer(player1,player2)
    else:
        print(player2, "goes first.\n")
        gameVSplayer(player2,player1)
    
#For VS Player    
def gameVSplayer(first, second):
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    usedMoves = ['F','F','F','F','F','F','F','F','F']
    check = 0

    for i in range(0,5):
        #Victory check    
        if victoryCheck('p', board, i, check, True, first, second):
            drawboard(board)
            break

        #Player 1's move
        print(first + "'s turn\n")
        p1Position = int(input("Where do you want to put O?\n"))
        p1Position -= 1

        #Verification of position for Player 1's move
        for j in range(0,8):
            if usedMoves[p1Position] == 'T':
                while usedMoves[p1Position] == 'T':
                    p1Position = int(input("That space has already been taken. Please input the position again.\n"))
                    p1Position -= 1
                usedMoves[p1Position] = 'T'
                break
            else:
                usedMoves[p1Position] = 'T'
                break

        check += 1    
        board[p1Position] = "O"
        drawboard(board)

        #Victory check    
        if victoryCheck('p', board, i, check, True, first, second):
            drawboard(board)
            break

        #Player 2's move
        print(second + "'s turn\n")
        p2Position = int(input("Where do you want to put X?\n"))
        p2Position -= 1

        #Verification of position for Player 2's move
        for j in range(0,8):
            if usedMoves[p2Position] == 'T':
                while usedMoves[p2Position] == 'T':
                    p2Position = int(input("That space has already been taken. Please input the position again.\n"))
                    p2Position -= 1
                usedMoves[p2Position] = 'T'
                break
            else:
                usedMoves[p2Position] = 'T'
                break
        
        board[p2Position] = "X"
        drawboard(board)

    playAgain()

#Initialisation
def main():
    reset()
    botORplayer()

main()
