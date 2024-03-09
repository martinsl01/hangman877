import random

word_list = ['grapes', 'bananas', 'tangerines', 'pineapples', 'mangoes']
word = random.choice(word_list)

# User Input
guess = input('Guess a single letter\n>>> ')

if len(guess) == 1:
    if guess.isalpha() == True:
        print('Good guess!')

    else:
        print("Oops! That is not a valid input.")
        