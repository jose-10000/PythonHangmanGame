# First try at a hangman game in python

import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

# Choose a random word from the list
secret_word = random.choice(word_list)

# Initialize variables to track the guesses and attempts

correct_guesses = set ()
incorrect_guesses = set ()
attempts_remaining = 6

# Function to display the current state of the game

def display_game_state():
  # Display the secret word with guessed letters filled in
    display_word = "".join([letter if letter in correct_guesses else "_" for letter in secret_word])
    print(f"Word: {display_word}")
    print(f"Attempts remaining: {attempts_remaining}")
    
# Main game loop
while True:
    display_game_state()
    guess = input("Enter a letter: ").lower()
    
    # Check if the gues is in the secret word
    if guess in secret_word:
        correct_guesses.add(guess)
        
      # Check if the player has won
        if set(secret_word).issubset(correct_guesses):
            print("You win!")
            break
    else:
        incorrect_guesses.add(guess)
        attempts_remaining -= 1
        
        # Check if the player has lost
        if attempts_remaining == 0:
            print("You lose!")
            print(f"The word was: {secret_word}")
            break
        