import argparse

from game import Hangman
from stats import load_stats, save_stats
from words import categories, select_word

parser = argparse.ArgumentParser(description="Play Hangman")
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

    return bool(hangman.is_won())

stats = load_stats()
wins, losses = stats["wins"], stats["losses"]
def update_results(round_result):
    global wins, losses
    if round_result:
        wins += 1
        print("You Won")
    else:
        losses += 1
        print("You Lost")
    save_stats(wins, losses)

if args.category and args.difficulty:
    difficulty_dict = {"easy": 10, "medium": 8, "hard": 5}
    level = difficulty_dict[args.difficulty]
    category = args.category
    round_result = play_round(category, level)
    update_results(round_result)

else:
    stats = load_stats()
    wins, losses = stats["wins"], stats["losses"]
    try:
        while True:
            user_input = input('''Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ''')
            if user_input == "play":
                category = select_category()
                level = select_level()
                round_result = play_round(category, level)
                update_results(round_result)

            elif user_input == "results":
                print(f"Wins: {wins} Losses: {losses}")

            elif user_input == "exit":
                save_stats(wins, losses)
                break

            else:
                print("Invalid input!")
                continue
    except KeyboardInterrupt:
        save_stats(wins, losses)
        print("\nThanks for playing! Goodbye.")