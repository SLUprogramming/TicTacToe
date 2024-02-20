Tic Tac Toe Game
This program allows two players to play a game of Tic Tac Toe in the console.

Instructions
Run the program.
Player 1, marked as "X", will be prompted to enter a position from 1 to 9 to place their mark on the board.
Player 2, marked as "O", will then input their position in the same manner.
The game continues until either one player wins by placing their mark in a row, column, or diagonal, or all positions on the board are filled (a draw).
After each game, the players are given the option to play again.
How to Use
Upon running the program, follow the prompts to input positions for Player 1 and Player 2.
Ensure that only numeric values from 1 to 9 are entered for position selection.
Players cannot select positions that are already marked.
The game will notify you of invalid inputs and guide you through the gameplay.
Enjoy playing Tic Tac Toe with a friend!
Code Overview
The code consists of several functions:

printboard(): Prints the current state of the board.
checkwin(): Checks if any player has won the game.
playagain(): Asks the players if they want to play another game.
clearboard(): Resets the game board for a new game.
gameloop(): Manages the game loop, where players take turns and the game state is updated accordingly.
Additional Information
The game starts with Player 1 always marking "X".
Players are prevented from entering non-numeric or out-of-range positions.
Special characters, spaces, and letters are not allowed as inputs.
Each game ends with a victory message, a draw message, or an option to play again.
Feel free to customize and enhance the game as needed!
