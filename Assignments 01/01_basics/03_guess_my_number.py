import random

def main():
    # Random number between 0 and 99
    number_to_guess = random.randint(0, 99)
    
    # Initialize the guess
    guess = -1
    
    # Keep asking for guesses until the correct one is entered
    while guess != number_to_guess:
        # Ask the user for a guess
        guess = int(input("Enter a guess: "))
        
        # Check if the guess is too high or too low
        if guess > number_to_guess:
            print("Your guess is too high")
        elif guess < number_to_guess:
            print("Your guess is too low")
        guess: int = int(input("Enter a new guess: "))
    # If the guess is correct, congratulate the user
    print(f"Congrats! The number was: {number_to_guess}")

if __name__ == "__main__":
    main()
