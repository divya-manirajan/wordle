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
    

    

key = "steak"

while True:
    guess = input("Enter a word: ")

    # print(is_repeated_letters(guess))
    # print(handle_repeated_letters(guess))

    if is_repeated_letters(guess) == True:
        handle_repeated_letters(guess)


