import random

# Constants
NUM_ROUNDS = 5

def play_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers for the player and the computer
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {your_number}")
        
        # Get user input for their guess
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        # Validate user input
        while guess not in ['higher', 'lower']:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        # Determine if the guess is correct
        if (guess == 'higher' and your_number > computer_number) or (guess == 'lower' and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
        print()  # Blank line for visual separation of rounds

    # Conditional ending message based on performance
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game
play_game()
