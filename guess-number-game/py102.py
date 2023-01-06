import random

# generate random number
randomNum = (random.randrange(0,10)) 

user_name = input("What is your name? ")

num = -1
guesses = 0

while num != randomNum:
  # input number
  user_number = input("Guess a number between 1 and 10! ")
  num = int(user_number)
  guesses += 1
  if num < randomNum:
    print("Sorry {}, your guess {} is too low! Your number of guesses is {}".format(user_name, num, guesses))
  elif num > randomNum:
    print("Sorry {}, your guess {} is too high! Your number of guesses is {}".format(user_name, num, guesses))
  elif num > 10 | num < 0:
    print("You must enter a number between 0 and 10!")
  else:
    print("You guessed it, {} with {} guesses!".format(user_name, guesses))
    print("Game over!")
  

# print outcome
print("This is the secret number: ", randomNum)