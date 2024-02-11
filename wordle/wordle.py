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
            # go through each character in the guess
            for guessChar in guess:
                # if the character guessed is in the word
                if guessChar in word:
                    # find all the positions in the guess at which this character appears
                    guessCharIndices = [
                        index for index, char in enumerate(guess)
                        if char == guessChar
                    ]
                    # find all the positions in the goal word at which this character appears
                    wordCharIndices = [
                        index for index, char in enumerate(word)
                        if char == guessChar
                    ]
                    for guessCharIndex in guessCharIndices:
                        for wordCharIndex in wordCharIndices:
                            if guessCharIndex == wordCharIndex:
                                print(f"{green}", guessChar)
                            elif guessCharIndex != wordCharIndex:
                                print(f"{blue}", guessChar)
                else:
                    print(f"{red}", guessChar)
            guessNumber += 1
        
        if guessNumber == 5:
            print("Game over! The word is", word)


from os import getenv
cheat_word = getenv("WORD")
if cheat_word:
    game(cheat_word)
else:
    game(randomWord())
    
