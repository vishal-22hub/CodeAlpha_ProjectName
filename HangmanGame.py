import random

def play_hangman():
    # 1. Setup predefined words and game variables
    words = ['python', 'coding', 'logic', 'system', 'mobile']
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6
    
    print("--- Welcome to Hangman! ---")
    
    # 2. Main Game Loop
    while attempts_left > 0:
        # Display the current status (e.g., p _ t h _ n)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Check if the player has won
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word!")
            break
            
        # 3. Get user input
        guess = input("Guess a letter: ").lower()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different one.")
            continue
            
        guessed_letters.append(guess)
        
        # 4. Check guess
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not there.")
            
    else:
        # This runs if the while loop finishes because attempts reached 0
        print("\nGame Over!")
        print(f"The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    play_hangman()