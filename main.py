import argparse

from rich.align import Align
from rich.panel import Panel

from game import Hangman
from stats import load_stats, save_stats
from ui import console, display_board, display_welcome
from words import categories, select_word

DIFFICULTY_LEVELS = {"easy": 10, "medium": 8, "hard": 5}

parser = argparse.ArgumentParser(description="Hangman Quick Round")
parser.add_argument("-c", "--category", help="Selecting a category")
parser.add_argument("-d", "--difficulty", choices=["easy", "medium", "hard"], help="Selecting the difficulty")
args = parser.parse_args()
if args.category:
    args.category = args.category.lower()
if args.difficulty:
    args.difficulty = args.difficulty.lower()

def select_category():
    while True:   
        category = console.input(f"\n[prompt]❯[/] [label]Select category[/] [muted](<{', '.join(categories.keys())}>)[/]: ").strip().lower()
        if category in categories:
            return category
        
        console.print("\n⚠  Unknown category! Stick to the given options.", style="warning")

def select_level():
    while True:
        level = console.input("\n[prompt]❯[/] [label]Select difficulty[/] [muted](<easy / medium / hard>)[/]: ").strip().lower()
        if level in DIFFICULTY_LEVELS:
            return DIFFICULTY_LEVELS[level]
        console.print("\n⚠  Invalid difficulty! Choose your fate carefully.", style="warning")

def play_round(category: str, level: int):
    word_selected = select_word(category)
    hangman = Hangman(word_selected, level)
    message = ""
    while not(hangman.is_won() or hangman.is_lost()):
        console.clear()
        display_board(  hangman.render_gallows(),
                        hangman.render_word(),
                        hangman.attempt_remain,
                        hangman.letter_guessed,
                        hangman.max_attempt,
                        category,
                        level,
                        message
                    )
        message = ""
        entered_letter = console.input("\n[prompt]❯[/] [label]Enter a letter[/] [muted](<or '?' for a hint>)[/]: ").strip().lower()
        if entered_letter == '?':
            hint_check = hangman.use_hint()
            if hint_check == "hints_unavailable":
                message = "Hints disabled on HARD mode!"
            elif hint_check == "no_letters_left":
                message = "No unrevealed letters left!"

        else:
            status: str = hangman.guess(entered_letter)

            if status == "invalid_length":
                message = "Must enter a single character!"
            elif status == "invalid_letter":
                message = "Letters only (a-z)!"
            elif status == "already_guessed":
                message = "You already tried that letter!"
            elif status == "invalid_guess":
                message = "Incorrect guess!"
 
    console.clear()
    message = ""

    if hangman.is_won():
        revealed_word = hangman.render_word()
        message = "[success]You cheated death... this time.[/]"

    else:
        revealed_word = hangman.target_word
        message = "[danger]Your time has run out. [danger]You hang ☠[/]"

    display_board(  hangman.render_gallows(),
                    revealed_word,
                    hangman.attempt_remain,
                    hangman.letter_guessed,
                    hangman.max_attempt,
                    category,
                    level,
                    message                    
                )

    return hangman.is_won()

def update_results(round_result, stats: dict):
    if round_result:
        stats["wins"] += 1
    else:
        stats["losses"] += 1
    save_stats(stats["wins"], stats["losses"])

stats = load_stats()
try:
    if args.category or args.difficulty:
        if not args.category or not args.difficulty:
            console.print("\n⚠  You must provide BOTH --category and --difficulty for CLI mode.", style="warning")
        elif args.category not in categories:
            console.print(f"\n⚠  Unknown category: '{args.category}'", style="warning")
            console.print(f"[muted]Available: {', '.join(categories.keys())}[/]")
        else:
            level = DIFFICULTY_LEVELS[args.difficulty]
            category = args.category
            round_result = play_round(category, level)
            update_results(round_result, stats)

    else:
        display_welcome()
        while True:
            user_input = console.input("\n[prompt]❯[/] [label]MAIN MENU[/] [muted](<play / results / exit>)[/]: ").strip().lower()
            if user_input == "play":
                category = select_category()
                level = select_level()
                round_result = play_round(category, level)
                update_results(round_result,stats)

            elif user_input == "results":
                stats_info = f"[success]Wins: {stats['wins']}[/]  |  [danger]Losses: {stats['losses']}[/]"
                stats_panel = Panel(stats_info, title="[label]Scoreboard[/]", style="on #15131B", border_style="secondary", expand=False)
                console.print(Align.center(stats_panel))

            elif user_input == "exit":
                save_stats(stats["wins"], stats["losses"])
                break

            else:
                console.print("\n⚠  Command not recognized.", style="warning")
                continue

except KeyboardInterrupt:
    save_stats(stats["wins"], stats["losses"])
    console.print("[warning]\nThanks for playing! Goodbye.[/]")