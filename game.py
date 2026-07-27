import random

from ui import gallow_stages


class Hangman:
    def __init__(self, target_word: str, max_attempt: int):
        self.target_word = target_word
        self.target_letters = set(target_word)
        self.letter_guessed: set[str] = set()
        self.max_attempt = max_attempt
        self.attempt_remain = max_attempt

    def guess(self, letter: str):
        # Guard Clauses
        if len(letter) != 1:
            return "invalid_length"

        elif not(letter.isalpha()) or not(letter.islower()):
            return "invalid_letter"

        elif letter in self.letter_guessed:
             return "already_guessed"

        self.letter_guessed.add(letter)
        if letter not in self.target_word:
            self.attempt_remain -= 1
            return "invalid_guess"

    def render_word(self):
        rendered_word: str = ""
        for i in self.target_word:
            if i in self.letter_guessed:
                rendered_word += i
            else:
                rendered_word += "_"
        return rendered_word


    def is_won(self) -> bool:
        return self.target_letters.issubset(self.letter_guessed)


    def is_lost(self) -> bool:
        return self.attempt_remain == 0

    def use_hint(self):
        if self.max_attempt == 5:
            return "hints_unavailable"
        else:
            remaining: set[str] = self.target_letters.difference(self.letter_guessed)
            if not remaining:
                return "no_letters_left"
            self.attempt_remain -= 1
            hint_letter: str = random.choice(list(remaining))
            self.letter_guessed.add(hint_letter)

    def render_gallows(self):
        mistakes_made = self.max_attempt - self.attempt_remain
        index = int(mistakes_made / self.max_attempt * 10)
        return gallow_stages[index]
