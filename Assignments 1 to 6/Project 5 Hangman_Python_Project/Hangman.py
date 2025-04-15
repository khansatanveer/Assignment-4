import random

def hangman():
    word_list = ['python', 'developer', 'hangman', 'function', 'variable', 'keyboard']
    chosen_word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    print("🎮 Welcome to Hangman!")
    print("_ " * len(chosen_word))

    while tries > 0:
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("✅ Correct guess!")
        else:
            tries -= 1
            print(f"❌ Wrong guess! Tries left: {tries}")

        # Display current word progress
        display_word = [letter if letter in guessed_letters else '_' for letter in chosen_word]
        print(' '.join(display_word))

        # Check win condition
        if '_' not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break
    else:
        print(f"\n💀 Game Over! The word was: {chosen_word}")

# Run the game
hangman()



