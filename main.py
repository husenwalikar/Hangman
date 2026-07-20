import random
print("H A N G M A N")
word_list = ['python', 'java', 'swift', 'javascript']
word_choosen = random.choice(word_list)
print(word_choosen)
for i in word_list:
    print(f"'{i}'", end=", ")
n = 2
for i in range(n):
    word = input(f"Guess the word!: ")

    if word == word_choosen:
        print("You survived!")
        break
    else:
        print("Try Again!")
        print(f"->{word_choosen[0:3]}{"_"*(len(word_choosen)-3)}")
else:
    print("You Lost!")