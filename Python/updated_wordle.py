import random
from word_selection import ALL_WORDS

#Function to set up game
def setup():
    #Set up used letter tracker dictionary
    used_letters = {}

    #Set up max limit of tries and guess counter
    MAX_TRIES = 6
    guess_counter = 0

    #Set up Game Board with 6 rows and 5 cols
    GAME_BOARD_ROWS = 6
    GAME_BOARD_COLS = 5
    game_board = [["[   ]" for col in range(GAME_BOARD_COLS)] for row in range(GAME_BOARD_ROWS)]

    return used_letters, MAX_TRIES, guess_counter, game_board

#Function to display game board and used letters
def display(board, letters):
    for row in board:
        print(*row)
    print("Used Letters: ")
    for i in sorted(letters):
        print((i, letters[i]), end=" ")

#Function to return solution word
def pick_solution(ALL_WORDS):
    return random.choice(ALL_WORDS)   

def has_repeated_letters(guess):
    result = False
    for letter in guess:
        if(guess.count(letter) > 1):
           result = True 
    return(result)

def handle_guess(guess, key, game_board, guess_counter, used_letters):
    if(has_repeated_letters(guess) == True):
        solution_as_list = list (key)
        for i in range(5): #check for green and black first and remove the letter from the solution if green
            if guess[i] == solution_as_list[i]:
                game_board[guess_counter][i] = ("["+guess[i] + "🟩 ]")
                used_letters[guess[i]]='🟩 ' #Override used letter tracker
                solution_as_list[i]="" #remove letter from solution
            else:
                game_board[guess_counter][i] = ("["+guess[i] + "⬛ ]") #default is black
                used_letters[guess[i]]='⬛ ' 

        for i in range(5): #check for yellow from remaining letters
            if guess[i] in solution_as_list and not game_board[guess_counter][i].endswith( "🟩 ]"):
                game_board[guess_counter][i] = ("["+guess[i] + "🟨 ]")
                used_letters[guess[i]]='🟨 ' 
                idx = solution_as_list.index(guess[i])
                solution_as_list[idx] = ""   
    else:
        for i in range (5):
            if guess[i] == key[i]:
                game_board[guess_counter][i] = ("["+guess[i] + "🟩 ]")
                used_letters[guess[i]]='🟩 ' #Override used letter tracker
            elif guess[i] in key:
                game_board[guess_counter][i] = ("["+guess[i] + "🟨 ]")
                if guess[i] not in used_letters:
                    used_letters[guess[i]] = "🟨 "
            else:
                game_board[guess_counter][i] = ("["+guess[i] + "⬛ ]")
                if guess[i] not in used_letters:
                    used_letters[guess[i]] = "⬛ "
    return game_board, used_letters    

#Function to handle round
def play_round():
    used_letters, MAX_TRIES, guess_counter, game_board = setup()
    SOLUTION = pick_solution(ALL_WORDS).upper() #pick a random solution word
    display(game_board, used_letters) #display initial game board
    while guess_counter < MAX_TRIES:
        print("\n",MAX_TRIES - guess_counter, " Tries Left")
        guess = input("Enter a 5 letter guess: ").upper() #turn guess upper-case
        if guess.lower() in ALL_WORDS:
            if guess == SOLUTION:
                for i in range (5):
                    game_board[guess_counter][i] = ("["+guess[i] + "🟩 ]")
                    used_letters[guess[i]]='🟩 ' #Override used letter tracker
                print("Congrats!")
                display(game_board, used_letters)
                print("\nYou Got it!!")
                print("\n----------------------------")
                break
            handle_guess(guess, SOLUTION, game_board, guess_counter, used_letters)
            display(game_board, used_letters)
            guess_counter += 1
        else:
            print("Invalid Word. Try Again")
    
    if guess_counter == MAX_TRIES:
        print("Ran out of tries")
        print("Word was: "+SOLUTION)

if __name__ == "__main__":
    try_again = 1
    while try_again:
        play_round()
        try_again_input = input("\nTry Again? Y/N: ")
        try_again = 1 if "Y" in try_again_input.upper() else 0
    print("Thanks For Playing!")


def test():
    print("TEST IMPORT")