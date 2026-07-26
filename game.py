import random

from ui import gallows


class Hangman:
    def __init__(self, target_word: str, max_attempt: int):
        self.target_word = target_word
        self.letter_guessed: set[str] = set()
        self.max_attempt = max_attempt
        self.attempt_remain = max_attempt

    def guess(self, letter: str):
        # Graud Clauses
        if len(letter) != 1:
            print("Length cannot be more then One")
            return

        elif not(letter.isalpha()) or not(letter.islower()):
            print("Must be lower")
            return

        elif letter in self.letter_guessed:
             print("Letter already guessed")
             return

        self.letter_guessed.add(letter)
        if letter not in self.target_word:
            self.attempt_remain -= 1
            print("Wrong guess")

    def render_word(self):
        # rendered_word: str = "".join([i if i in self.letter_guessed else "_" for i in self.target_word])
        rendered_word: str = ""
        for i in self.target_word:
            if i in self.letter_guessed:
                rendered_word += i
            else:
                rendered_word += "_"
        return rendered_word


    def is_won(self) -> bool:
        target_word_set = set(self.target_word)
        return target_word_set.issubset(self.letter_guessed)


    def is_lost(self) -> bool:
        return self.attempt_remain == 0

    def use_hint(self):
        if self.max_attempt == 5:
            print("hints are unavailable at this difficulty.")
        else:
            self.attempt_remain -= 1
            target_word_set = set(self.target_word)
            hint_letter: str = random.choice(list(target_word_set.difference(self.letter_guessed)))
            self.letter_guessed.add(hint_letter)

    def render_gallows(self):
        mistakes_made = self.max_attempt - self.attempt_remain
        index = int(mistakes_made / self.max_attempt * 10)
        return gallows[index]
