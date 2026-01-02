#start from scratch -- organize with functions and comments
#add steps for double letters in solution
#add color code for used letters

import random #import random
from word_selection import ALL_WORDS #import word bank

#Set up used letter tracker dictionary
used_letters = {}

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
    print("Used Letters: ")
    for i in sorted(used_letters):
        print((i, used_letters[i]), end=" ")

        
#Function to reset game board
def reset():
    global used_letters
    global game_board
    
    used_letters = {}
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
    SOLUTION = pick_solution(ALL_WORDS).upper() #pick a random solution word
   
    display(game_board) #display initial game board
    while guess_counter < 6:
        print("\n",MAX_TRIES - guess_counter, " Tries Left")
        guess = input("Enter a 5 letter guess: ").upper() #turn guess upper-case
        if guess.lower() in ALL_WORDS:
            if guess == SOLUTION:
                for i in range (5):
                    game_board[guess_counter][i] = ("["+guess[i] + "🟩 ]")
                    used_letters[guess[i]]='🟩 ' #Override used letter tracker
                print("Congrats! You got it!")
                display(game_board)
                print("\n----------------------------")
                break
            
            for i in range (5):
                if guess[i] == SOLUTION[i]:
                    game_board[guess_counter][i] = ("["+guess[i] + "🟩 ]")
                    used_letters[guess[i]]='🟩 ' #Override used letter tracker
                elif guess[i] in SOLUTION:
                    game_board[guess_counter][i] = ("["+guess[i] + "🟨 ]")
                    if guess[i] not in used_letters:
                        used_letters[guess[i]] = "🟨 "
                else:
                    game_board[guess_counter][i] = ("["+guess[i] + "⬛ ]")
                    if guess[i] not in used_letters:
                        used_letters[guess[i]] = "⬛ "
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
        try_again_input = input("\nTry Again? Y/N: ")
        try_again = 1 if "Y" in try_again_input.upper() else 0
    print("Thanks For Playing!")

    
