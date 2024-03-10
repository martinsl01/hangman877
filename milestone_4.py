import random
word_list = ['florida', 'kansas', 'arizona', 'kentucky', 'colorado']
list_of_guesses = []
class Hangman:
    def __init__(self, word_list, num_lives=5): 
        '''Initializing the class and parsing a couple of parameters and adding multiple attributes.'''
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        '''This is to check whether the guess is in the word and to replace '_' with guessed letter.
        Also have lives reduced for every incorrect guesses.'''
        guess.lower()
        if guess in list(self.word):
            print(f"Good guess! {guess} is in the word.")
        else:
            self.num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.") 
            print(f"You have {self.num_lives} lives left.")

        for index, char in enumerate(list(self.words)):
            if char == guess:
                self.word_guessed[index] = char
        self.num_letters - 1

    def ask_for_input(self):
        '''This function helps to ask the player for a guess and it then directs the check
        of the guess to the 'check_guess' function.'''
        while True:
            guess = input('Guess a single letter\n>>> ')
            if len(guess) == 1:
                if guess.isalpha() == True:
                    if guess in list_of_guesses:
                        print("You already tried that letter! - Try again")
                    else:
                        print(self.check_guess(guess))
                        list_of_guesses.append(guess)
                        break
                else:
                    print("Invalid letter. Please, enter a single alphabetical character."  )
                    guess = input('Guess a single letter\n>>> ')
                    
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()                
                





        