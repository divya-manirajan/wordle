
TRIES = 6
COUNT = 0

from word_selection import random_word
from word_selection import words

key = random_word #random 5 letter word lower-case
result = []

while COUNT < TRIES:
    print(TRIES-COUNT, " Tries Left")
    guess = input("Enter a 5 letter guess: ").lower() #turn guess lower-case
    if (guess in words):
        if guess == key:
            print("You got it!")
            for i in range (5):
                result.append(guess[i].upper() + " 🟩 ")
            print(*result)
            break
        
        for i in range (5):
            if guess[i] == key[i]:
                result.append(guess[i].upper() + " 🟩 ")
            elif guess[i] in key:
                result.append(guess[i].upper() + " 🟨 ")
            else:
                
                result.append(guess[i].upper() + " ⬜ ")
        print(*result)
        COUNT += 1
    else:
       print("Invalid Word. Try Again")
    
if COUNT == TRIES:
    print("Ran out of tries")
    print("Word was: "+key)
