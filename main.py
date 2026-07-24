from game import Hangman
from words import categories, select_word

wins, losses = 0, 0
while True:
    user_input = input('''Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ''')
    if user_input == "play":
        category = input(f"Select category out of {", ".join(categories.keys())}: ")
        word_selected = select_word(category)
        hangman = Hangman(word_selected, 6)
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

        if hangman.is_won():
            print("You Won")
            wins += 1

        else:
            print("You Lost")
            losses += 1 

        rendered_gallow = hangman.render_gallows()
        print(rendered_gallow)
        print(word_selected)


    elif user_input == "results":
        print(f"Wins: {wins} Losses: {losses}")
    elif user_input == "exit":
        break
