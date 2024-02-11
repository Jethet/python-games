import random
from words import wordList

blue = "\033[94m"
red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"


# def randomWord():
#     randWord = random.choice(wordList)
#     return randWord


# def game(randWord):

word = "peter"

def game(word):
    guessNumber = 0

    while guessNumber < 5:
        guess = input("Please enter your word: ")

        if guess == word:
            guessNumber = 5
            print(f"{green}",word, "Correct!")

        if guess != word:
            # go through each character in the guess
            for x in guess:
                # if the character is in the goal word
                if x in word:
                    # find all the positions in the guess at which this character appears
                    indexGuessChar = [i for i, b in enumerate(guess) if b == x]
                    # find all the positions in the goal word at which this character appears
                    indexWordChar = [i for i, a in enumerate(word) if a == x]
                                                        # baker
                    for guessIndex in indexGuessChar:   #    3
                                                        # peter
                        for wordIndex in indexWordChar: #  1 3
                            if guessIndex == wordIndex:
                                print(f"{green}", x)
                            
                            if guessIndex != wordIndex and guessIndex not in indexWordChar:
                                print(f"{blue}", x)
                else:
                    print(f"{red}", x)

            guessNumber += 1

            if guessNumber == 5:
                print("Sorry, you have no more guesses left.")
        # print(word)
        # print(guessNumber)

game(word)
