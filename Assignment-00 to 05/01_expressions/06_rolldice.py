import random 

NUM_SIDES = 6

def main():
    # Get the number of sides from the user
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    # Get their total
    total = die1 + die2

    # Print out the results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# Ensuring the script runs when executed directly
if __name__ == "__main__":
    main()





