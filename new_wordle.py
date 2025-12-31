#start from scratch -- organize with functions and comments

import random #import random
from word_selection import ALL_WORDS #import word bank

#Set up used letter tracker
used_letters = []

#Set up max limit of tries and guess counter
MAX_TRIES = 6
guess_counter = 0

#Set up Game Board with 6 rows and 5 cols
GAME_BOARD_ROWS = 6
GAME_BOARD_COLS = 5
game_board = [["[   ]" for col in range(GAME_BOARD_COLS)] for row in range(GAME_BOARD_ROWS)]

#Function to display game board and used letters
def display(board):
    for row in board:
        print(*row)
    print("Used Letter: ", sorted(used_letters))

        
#Function to reset game board
def reset():
    global used_letters
    global game_board
    
    used_letters = []
    for row in range(GAME_BOARD_ROWS):
        for col in range(GAME_BOARD_COLS):
            game_board[row][col] = "[   ]" 
            
#Function to return solution word
def pick_solution(ALL_WORDS):
    random_index = random.randint(0, len(ALL_WORDS)-1) #randomize solution
    SOLUTION = ALL_WORDS[random_index]
    return SOLUTION

        
#Function to handle round
def play_round(MAX_TRIES, guess_counter):
    reset() #reset game board and used letter tracker 
    SOLUTION = pick_solution(ALL_WORDS) #pick a random solution word
    display(game_board) #display initial game board
    while guess_counter < 6:
        print(MAX_TRIES - guess_counter, " Tries Left")
        guess = input("Enter a 5 letter guess: ").lower() #turn guess lower-case
        for letter in guess:
            if letter.upper() not in used_letters:
                used_letters.append(letter.upper())
               
        if guess in ALL_WORDS:
            if guess == SOLUTION:
                print("You got it!")
                for i in range (5):
                    game_board[guess_counter][i] = ("["+guess[i].upper() + "🟩 ]")
                display(game_board)
                break
            
            for i in range (5):
                if guess[i] == SOLUTION[i]:
                    game_board[guess_counter][i] = ("["+guess[i].upper() + "🟩 ]")
                elif guess[i] in SOLUTION:
                    game_board[guess_counter][i] = ("["+guess[i].upper() + "🟨 ]")
                else:
                    game_board[guess_counter][i] = ("["+guess[i].upper() + "⬛ ]")
            display(game_board)
            guess_counter += 1
        else:
            print("Invalid Word. Try Again")
       
    if guess_counter == MAX_TRIES:
        print("Ran out of tries")
        print("Word was: "+SOLUTION)
        
if __name__ == "__main__":
    try_again = 1
    while try_again:
        play_round(MAX_TRIES, guess_counter)
        try_again_input = input("Try Again? Y/N: ")
        try_again = 1 if try_again_input.lower() == "y" else 0
    print("Thanks For Playing!")

    
