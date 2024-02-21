from random import choice
# choice functions pseudo-randomly selects an element from a sequence
# if the player elects to play against the computer, the choice function
# will be the primary means through which the computer plays its moves.

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
# defines initial empty board

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
# retrives values of dictionary then prints board

non_numerals = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '\\', '|', '~', '`']
# list of invalid inputs

alive = True
used_non_numeral = False

def check_win():
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

def play_again():
    response = input("Would you like to play again (yes/no): ")
    if response.lower() in ['yes', 'ye', 'y']:
        return True
    else:
        print("Game over")
        return False
# Allows users to play another game
    
def generate_valid_inputs():
    '''
    Returns the list of valid inputs for the computer to choose one from the list
    '''
    global dictionary
    valid_inputs = []
    for object, value in dictionary.items():
        if value == ' ':
            valid_inputs.append(object)
    return valid_inputs

def clear_board():
    global dictionary
    dictionary = {"1": ' ', "2": ' ', "3": ' ', "4": ' ', "5": ' ', "6": ' ', "7": ' ', "8": ' ', "9": ' '}
    board = f'''
This is the current board:
{dictionary.get('1')}|{dictionary.get('2')}|{dictionary.get('3')}
-+-+-
{dictionary.get('4')}|{dictionary.get('5')}|{dictionary.get('6')}
-+-+-
{dictionary.get('7')}|{dictionary.get('8')}|{dictionary.get('9')}
'''
    print(board)
    game_loop(used_non_numeral, alive)
# If the user chooses to play another game, this function will clear the board then initiate the next game loop

def game_loop(used_non_numeral, alive):
    '''
    main game loop
    '''
    turns = 0
    player2_is_human = human_or_com()
    while alive:
        choice1 = (input('Player 1 turn. For "X" please input a position from 1-9: '))
        for non_numeral in non_numerals:
            if non_numeral in choice1:
                print("Invalid input: No letters, spaces, or special characters")
                used_non_numeral = True
                break
        if used_non_numeral:
            used_non_numeral = False
            continue
        if int(choice1) not in range(1,10):
            print("Invalid input: Choose a value 1-9")
            continue
        if int(choice1) in range (1, 10):
            if dictionary.get(choice1) != " ":
                print("Invalid input: Choose a empty square")
                continue
            else: 
                dictionary[choice1] = 'X'
                turns += 1
                printboard()
                if check_win():
                    print("Player 1 is the winner")
                    if play_again():
                        clear_board()
                    else: 
                        exit()
                elif turns == 9 and check_win() is False:
                    print('It is a draw, no winner.')
                    if play_again():
                        clear_board()
                        continue
                    else: 
                        break
        player2 = True
        while player2:
            if player2_is_human:
                choice2 = (input('Player 2 turn. For "O" please input a position from 1-9: ')) 
            elif not player2_is_human:
                valid_inputs = generate_valid_inputs()
                choice2 = choice(valid_inputs)
                print('The computer has made its move.')
            for non_numeral in non_numerals:
                if non_numeral in choice2:
                    print("Invalid input: No letters, spaces, or special characters")
                    used_non_numeral = True
                    break
            if used_non_numeral:
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
                if check_win():
                    print("Player 2 is the winner")
                    if play_again():
                        clear_board()
                    else:
                        exit()     
                else: 
                    player2 = False

def human_or_com():
    '''
    This function allows player1 to choose if player2 will be another human or the computer who makes random moves
    '''
    if input('Would you like to play against human or computer: ').lower() == 'human':
        return True
    return False
    # else statement not required. If true is returned then the function stops running.

game_loop(used_non_numeral, alive)
# starts the game for the first time
