import argparse

from game import Hangman
from stats import load_stats, save_stats
from ui import display_board
from words import categories, select_word

parser = argparse.ArgumentParser(description="Hangman Quick Round")
parser.add_argument("-c", "--category", help="Selecting a category")
parser.add_argument("-d", "--difficulty", choices=["easy", "medium", "hard"], help="Selecting the diificulty")
args = parser.parse_args()

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

def play_round(category: str, level: int):
    word_selected = select_word(category)
    hangman = Hangman(word_selected, level)
    while not(hangman.is_won() or hangman.is_lost()):
        display_board(  hangman.render_gallows(),
                        hangman.render_word(),
                        hangman.attempt_remain,
                        hangman.letter_guessed  )
        
        entered_letter = input("Enter a letter to guess or '?' for a hint: ")
        if entered_letter == '?':
            hint_check = hangman.use_hint()
            if hint_check == "hints_unavailable":
                print("Hints not avialable at this difficulty")

        else:
            status: str = hangman.guess(entered_letter)

            if status == "invalid_length":
                print("Please enter exactly one letter!")
            elif status == "invalid_letter":
                print("Must be a lowercase letter!")
            elif status == "already_guessed":
                print("You already guessed that letter!")
            elif status == "invalid_guess":
                pass

    display_board(  hangman.render_gallows(),
                    hangman.render_word(),
                    hangman.attempt_remain,
                    hangman.letter_guessed  )

    return bool(hangman.is_won())

stats = load_stats()
def update_results(round_result, stats: dict):
    if round_result:
        stats["wins"] += 1
        print("You Won")
    else:
        stats["losses"] += 1
        print("You Lost")
    save_stats(stats["wins"], stats["losses"])

if args.category and args.difficulty:
    difficulty_dict = {"easy": 10, "medium": 8, "hard": 5}
    level = difficulty_dict[args.difficulty]
    category = args.category
    round_result = play_round(category, level)
    update_results(round_result, stats)

else:
    try:
        while True:
            user_input = input('''Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ''')
            if user_input == "play":
                category = select_category()
                level = select_level()
                round_result = play_round(category, level)
                update_results(round_result,stats)

            elif user_input == "results":
                print(f"Wins: {stats["wins"]} Losses: {stats["losses"]}")

            elif user_input == "exit":
                save_stats(stats["wins"], stats["losses"])
                break

            else:
                print("Invalid input!")
                continue

    except KeyboardInterrupt:
        save_stats(stats["wins"], stats["losses"])
        print("\nThanks for playing! Goodbye.")