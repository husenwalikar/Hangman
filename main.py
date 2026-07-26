import argparse

from game import Hangman
from words import categories, select_word

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--category", help="Selecting a category")
parser.add_argument("-d", "--difficulty", choices=["easy", "medium", "hard"], help="Selecting the diificulty")
def select_category():
    while True:   
        category = input(f"Select category out of {", ".join(categories.keys())}: ")
        if category in categories:
            return category
        
        print("Invalid category")

def select_level():
    while True:
        level = input("Select the diificulty, type 'easy', 'medium' or 'hard': ")
        if level == 'easy':
            return 10
        elif level == 'medium':
            return 8
        elif level == 'hard':
            return 5
        print("Invalid difficulty")

    
wins, losses = 0, 0
while True:
    user_input = input('''Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ''')
    if user_input == "play":
        category = select_category()
        level = select_level()
        word_selected = select_word(category)
        hangman = Hangman(word_selected, level)
        while not(hangman.is_won() or hangman.is_lost()):
            rendered_gallow = hangman.render_gallows()
            rendered_word = hangman.render_word()
            print(rendered_gallow)
            print(rendered_word)

            entered_letter = input("Enter a letter to guess or '?' for a hint: ")
            if entered_letter == '?':
                hangman.use_hint()

            else:
                hangman.guess(entered_letter)

        rendered_gallow = hangman.render_gallows()
        print(rendered_gallow)
        print(word_selected)

        if hangman.is_won():
            print("You Won")
            wins += 1

        else:
            print("You Lost")
            losses += 1 

    elif user_input == "results":
        print(f"Wins: {wins} Losses: {losses}")
    elif user_input == "exit":
        break
    else:
        print("Invalid input!")
        continue
