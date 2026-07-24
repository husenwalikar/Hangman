class Hangman:
    def __init__(self, target_word: str, max_attempt: int):
        self.target_word = target_word
        self.letter_guessed: set[str] = set()
        self.max_attempt = max_attempt
        self.attempt_remain = max_attempt

    def guess(self, letter: str):
        if not(len(letter) == 1):
            print("Length cannot be One")

        elif not(letter.islower()):
            print("Must be lower")

        elif letter in self.letter_guessed:
             print("Letter already guessed")

        elif letter not in self.letter_guessed and letter in self.target_word:
            self.letter_guessed.add(letter)
            self.is_lost()
            self.is_won()
            self.return_word(letter)

        else:
            self.attempt_remain -= 1
            self.letter_guessed.add(letter)
            self.is_lost()
            self.is_won()
            print("Wrong guess")

    def return_word(letter):
        pass

    def is_won(self):
        target_word_set= set(self.target_word)
        return target_word_set.issubset(self.letter_guessed)


    def is_lost(self) -> bool:
        return self.attempt_remain == 0