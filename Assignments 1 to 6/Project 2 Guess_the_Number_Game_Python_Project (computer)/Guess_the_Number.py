import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 to 100. Can you guess what it is?")

    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of guesses taken
    guesses_taken = 0

    # Game loop
    while True:
        try:
            # Ask the player for their guess
            guess = int(input("Enter your guess: "))
            guesses_taken += 1

            # Check if the guess is correct
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {guesses_taken} guesses.")
                break  # End the game when the player guesses correctly

        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()

