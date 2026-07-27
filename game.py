import random

from ui import gallow_stages


class Hangman:
    def __init__(self, target_word: str, max_attempt: int):
        """
        Initializes a new Hangman game session.

        Args:
            target_word: The hidden word the player must guess.
            max_attempt: The total number of incorrect guesses allowed.
        """
        self.target_word = target_word
        self.target_letters = set(target_word)
        self.letter_guessed: set[str] = set()
        self.max_attempt = max_attempt
        self.attempt_remain = max_attempt

    def guess(self, letter: str):
        """
        Processes a single letter guess and updates the game state.

        Args:
            letter: The character inputted by the player.

        Returns:
            A status code if the guess is invalid ("invalid_length",
            "invalid_letter", "already_guessed", "invalid_guess").
            Returns None if the guess is valid and correct.
        """
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
        """
        Generates the current visual state of the hidden word.

        Returns:
            The word with unguessed characters masked as underscores (e.g. "h_ll_").
        """
        rendered_word: str = ""
        for i in self.target_word:
            if i in self.letter_guessed:
                rendered_word += i
            else:
                rendered_word += "_"
        return rendered_word


    def is_won(self) -> bool:
        """Checks if all letters in the target word have been guessed."""
        return self.target_letters.issubset(self.letter_guessed)


    def is_lost(self) -> bool:
        """Checks if the player has exhausted all attempts."""
        return self.attempt_remain == 0

    def use_hint(self):
        """
        Reveals one random unguessed letter at the cost of one life.
        Hints are disabled on hard mode (max_attempt == 5).

        Returns:
            A status code ("hints_unavailable" or "no_letters_left")
            if the hint cannot be used. Returns None on success.
        """
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
        """
        Selects the appropriate ASCII gallows art frame based on mistakes made.

        Returns:
            The ASCII art string for the current gallows state.
        """
        mistakes_made = self.max_attempt - self.attempt_remain
        index = int(mistakes_made / self.max_attempt * 10)
        return gallow_stages[index]
