import random

word_list = ['grapes', 'bananas', 'tangerines', 'pineapples', 'mangoes']
word = random.choice(word_list)

# User Input
guess = input('Guess a single letter\n>>> ')
while True:
    if len(guess) == 1:
        if guess.isalpha() == True:
            if guess in list(word):
                print(f"Good guess! {guess} is in the word.")
                break
            else:
                print(f"Sorry, {guess} is not in the word. Try again."  )
                guess = input('Guess a single letter\n>>> ')

        else:
            print("Invalid letter. Please, enter a single alphabetical character."  )
            guess = input('Guess a single letter\n>>> ')

def check_guess(guess):
    guess.lower()
    if guess in list(word):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again."  )
    

def ask_for_input(guess):
    if len(guess) == 1:
        if guess.isalpha() == True:
            print('Good guess!')
        else:
            print('Inbalid input')

ask_for_input(guess)
