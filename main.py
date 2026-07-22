import random
print("H A N G M A N")
word_list = ['python', 'java', 'swift', 'javascript']
word_choosen = random.choice(word_list)
print(word_choosen)
for i in word_list:
    print(f"'{i}'", end=", ")
n = 8
letter_choosen = []
for i in range(n):
    letter = input(f"Input a letter: ")
    letter_choosen += letter
    if letter_choosen[i] in word_choosen:
        for i in range(len(word_choosen)):
            if letter_choosen[i] == word_choosen[i]:
                print(word_choosen[i], end="")
                continue
            else:
                print("-", end="")

    else:
        continue

else:
    print("Thanks for playing!")