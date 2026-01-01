#Set up Game Board with 6 rows and 5 cols
GAME_BOARD_ROWS = 6
GAME_BOARD_COLS = 5
game_board = [["[    ]" for col in range(GAME_BOARD_COLS)] for row in range(GAME_BOARD_ROWS)]

used_letters = {}


key = "steak"
guess_counter = 0


def display(board):
    for row in board:
        print(*row)
    print("Used Letters: ")
    for i in sorted(used_letters):
        print((i, used_letters[i]), end=" ")
    

def is_repeated_letters(guess):
    letter_count = False
    for letter in guess:
        if(guess.count(letter) > 1):
           letter_count = True 
    return(letter_count)

def handle_repeated_letters(guess):
    repeated_letters_in_guess = {}
    for letter in guess:
        if guess.count(letter) > 1:
            repeated_letters_in_guess[letter] = guess.count(letter)

    for i in range (5):
        if guess[i] in repeated_letters_in_guess:
            print("REPEAT LETTER")
        else:
            if guess[i] == key[i]:
                game_board[guess_counter][i] = ("["+guess[i] + "🟩 ]")
                used_letters[guess[i]]='🟩 ' #Override used letter tracker
            elif guess[i] in key:
                game_board[guess_counter][i] = ("["+guess[i] + "🟨 ]")
                
            else:
                game_board[guess_counter][i] = ("["+guess[i] + "⬛ ]")

while True:
    guess = input("Enter guess: ")
    #Update used letter tracker
    for letter in guess:
        if letter in key:
            used_letters[letter]='🟨 '
        else:
            used_letters[letter]='⬛ '
            
    if(is_repeated_letters(guess) == True):
        handle_repeated_letters(guess)
        
    else:
        for i in range (5):
            if guess[i] == key[i]:
                game_board[guess_counter][i] = ("["+guess[i] + "🟩 ]")
                used_letters[guess[i]]='🟩 ' #Override used letter tracker
            elif guess[i] in key:
                game_board[guess_counter][i] = ("["+guess[i] + "🟨 ]")
            else:
                game_board[guess_counter][i] = ("["+guess[i] + "⬛ ]")
    display(game_board)
    guess_counter += 1

    




