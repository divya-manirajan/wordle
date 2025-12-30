#start from scratch -- organize with functions and comments

from word_selection import words #import word list
from word_selection import random_word #import key word

#Set up max limit of tries and guess counter
MAX_TRIES = 6
guess_counter = 0

#Set up Game Board with 6 rows and 5 cols
GAME_BOARD_ROWS = 6
GAME_BOARD_COLS = 5
game_board = [["[   ]" for col in range(GAME_BOARD_COLS)] for row in range(GAME_BOARD_ROWS)]


