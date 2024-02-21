print(
'''
These are the positions:
[1][2][3]     
[4][5][6]    
[7][8][9]    

"x" always moves first

Player 1 moves first and marks the x's
Player 2 moves second and marks the o's
''')

dictionary = {"1": ' ', "2": ' ', "3": ' ', "4": ' ', "5": ' ', "6": ' ', "7": ' ', "8": ' ', "9": ' '}
# defines initial, empty board

def printboard():
    board = f'''
This is current board:
{dictionary.get('1')}|{dictionary.get('2')}|{dictionary.get('3')}
-+-+-
{dictionary.get('4')}|{dictionary.get('5')}|{dictionary.get('6')}
-+-+-
{dictionary.get('7')}|{dictionary.get('8')}|{dictionary.get('9')}
'''
    print(board)
printboard()
# retrieves values of dictionary then prints board

non_numerals = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '\\', '|', '~', '`']
# List of invalid inputs

alive = True
used_non_numeral = False
victory = False

def checkwin():
    '''
    Defines all the sequences of 3 consecutive blocks on tic-tac-toe board
    If it is found that all the elements in one of these sequences are equal
    then the game is won
    '''
    combos = [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'),('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),('1', '5', '9'), ('3', '5', '7')]
    for combo in combos:
        if dictionary.get(combo[0]) == dictionary.get(combo[1]) == dictionary.get(combo[2]) != ' ':
            return True
    return False


def playagain():
    response = input("Would you like to play again (yes/no): ")
    if response.lower() == 'yes':
        return True
    else:
        print("Game over")
        return False
# Allows users to play another game

def clearboard():
    global dictionary
    dictionary = {"1": ' ', "2": ' ', "3": ' ', "4": ' ', "5": ' ', "6": ' ', "7": ' ', "8": ' ', "9": ' '}
    board = f'''
This is current board:
{dictionary.get('1')}|{dictionary.get('2')}|{dictionary.get('3')}
-+-+-
{dictionary.get('4')}|{dictionary.get('5')}|{dictionary.get('6')}
-+-+-
{dictionary.get('7')}|{dictionary.get('8')}|{dictionary.get('9')}
'''
    print(board)
# Resets the board if the user chooses to play another game

def gameloop(used_non_numeral, alive):
    '''
    main game loop
    '''
    turns = 0
    while alive:
        choice = (input('Player 1 turn. For "X" please input a position from 1-9: '))
        for non_numeral in non_numerals:
            if non_numeral in choice:
                print("Invalid input: No letters, spaces, or special characters")
                used_non_numeral = True
                break
        if used_non_numeral is True:
            used_non_numeral = False
            continue
        if int(choice) not in range(1,10):
            print("Invalid input: Choose a value 1-9")
            continue
        if int(choice) in range (1, 10):
            if dictionary.get(choice) != " ":
                print("Invalid input: Choose a empty square")
                continue
            else: 
                dictionary[choice] = 'X'
                turns += 1
                printboard()
                #checkwin() <---- this is not necessary
                if checkwin():
                    print("Player 1 is the winner")
                    if playagain():
                        clearboard()
                        continue
                    else: 
                        break
                elif turns == 9 and checkwin() is False:
                    print('It is a draw, no winner.')
                    if playagain():
                        clearboard()
                        continue
                    else: 
                        break
        player2 = True
        while player2:
            choice2 = (input('Player 2 turn. For "O" please input a position from 1-9: ')) # Loop works good up until here
            for non_numeral in non_numerals:
                if non_numeral in choice2:
                    print("Invalid input: No letters, spaces, or special characters")
                    used_non_numeral = True
                    break
            if used_non_numeral is True:
                used_non_numeral = False
                continue
            if int(choice2) not in range(1,10):
                print("Invalid input: Choose a value 1-9")
                continue
            if int(choice2) in range (1, 10):
                if dictionary.get(choice2) != " ":
                    print("Invalid input: Choose a empty square")
                    continue
                else: 
                    dictionary[choice2] = 'O'
                    turns += 1
                    printboard()
                if checkwin():
                    print("Player 2 is the winner")
                    if playagain():
                        clearboard()
                        return
                else: 
                    player2 = False

gameloop(used_non_numeral, alive)
# starts the game for the first time
