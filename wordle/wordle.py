import random
from words import wordList

blue = "\033[94m"
red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"


def randomWord():
    randWord = random.choice(wordList)
    return randWord


def game(randWord):
    guessNumber = 0

    while guessNumber < 5:
        guess = input("Please enter your word: ")

        for x in guess:
            if x in randWord:
                indexGuessChar = [i for i, b in enumerate(guess) if b == x]
                indexWordChar = [i for i, a in enumerate(randWord) if a == x]
                for b in indexGuessChar:
                    for a in indexWordChar:
                        if b == a:
                            print(f"{green}", x)
                        else:
                            print(f"{blue}", x)
            else:
                print(f"{red}", x)

        guessNumber += 1

        print(randWord)
        print(guessNumber)


game(randomWord())
