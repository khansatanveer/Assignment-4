def main():
    # Get the number from the user
    number = float (input("\033[1;3m Type a number to see its square: \033[0m "))

    # Calculate the square of the number
    square = number * number
    # Print the result
    print(f"The square of {number} is {square}")

# Ensuring the script runs when executed directly
if __name__ == "__main__":
    main()
