import random
from words import wordList

blue = "\033[94m"
red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"


def randomWord():
    randWord = random.choice(wordList)
    return randWord


def game(word):
    guessNumber = 0

    while guessNumber < 5:
        guess = input("Please enter your word: ")

        if guess == word:
            guessNumber = 5
            print(f"{green}","Correct! The word is", word)

        if guess != word:
            for x in guess:
                if x in word:
                    indexGuessChar = [i for i, b in enumerate(guess) if b == x]
                    indexWordChar = [i for i, a in enumerate(word) if a == x]
                    for b in indexGuessChar:
                        for a in indexWordChar:
                            if b == a:
                                print(f"{green}", x)
                            elif b != a:
                                print(f"{blue}", x)
                else:
                    print(f"{red}", x)
            guessNumber += 1
        
        if guessNumber == 5:
            print("Game over! The word is", word)


game(randomWord())