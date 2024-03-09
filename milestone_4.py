import random
word_list = ['florida', 'kansas', 'arizona', 'kentucky', 'colorado']
list_of_guesses = []
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letters in self.word]
        self.num_letters = len(self.word)
        self.word_list = word_list
        self.num_lives = 5
        self.list_of_guesses = list_of_guesses
    
    def check_guess(guess):
        guess.lower()
        if guess in list(self.word):
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while True:
            guess = input('Guess a single letter\n>>> ')
            if len(guess) == 1:
                if guess.isalpha() == True:
                    if guess in list_of_guesses:
                        print("You already tried that letter! - Try again")
                    else:
                        print(check_guess(guess))
                        list_of_guesses.append(guess)
                        break
                else:
                    print("Invalid letter. Please, enter a single alphabetical character."  )
                    guess = input('Guess a single letter\n>>> ')
                    
    ask = ask_for_input(guess)                 
                





        