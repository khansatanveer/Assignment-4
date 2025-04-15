def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")

    low = 1
    high = 100
    guesses = 0

    # Game loop
    while low <= high:
        guesses += 1
        guess = (low + high) // 2  # Guess the middle number
        
        # Ask the player if the guess is correct, too high, or too low
        print(f"Is your number {guess}?")
        feedback = input("Enter 'h' if it's higher, 'l' if it's lower, or 'c' if it's correct: ").lower()

        if feedback == 'h':
            low = guess + 1  # If the number is higher, adjust the low bound
        elif feedback == 'l':
            high = guess - 1  # If the number is lower, adjust the high bound
        elif feedback == 'c':
            print(f"Yay! I guessed your number {guess} in {guesses} tries!")
            break  # Game ends when the computer guesses the correct number
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    guess_the_number()