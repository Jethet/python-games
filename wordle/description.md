WORDLE

- user gets random 5-letter word
-> create a list of words that have only 5 letters
-> create random function to select one word and return it

- user can guess six times
-> user is asked for input: input("Enter a word: ")
-> each input is counted: word_input += 1
-> after 6 times, message appears: "You have tried six times, it's over!"

- user inputs word, gets back:
    - green letter if letter is correct and in correct place
    - blue letter if letter is correct but in wrong place
    - red letter for letters that are not correct
-> if/else loop to compare letters and their indexes
-> change colour letter if correct || correct & right place || incorrect