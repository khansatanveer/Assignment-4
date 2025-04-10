def main():
    # Get the numbers we want to divide
    dividend: float = float(input("\033[1;3m Please enter an integer to be divided:\033[0m "))
    divisor: float = float(input("\033[1;3m Please enter an integer to divide by:\033[0m "))
    
    # Divide with no remainder/decimals (integer division)
    quotient: float = dividend // divisor

    # Get the remainder of the division
    remainder: float = dividend % divisor

    # Print the result
    print(f"The quotient is {quotient} and the remainder is {remainder}")
    
# Ensuring the script runs when executed directly
if __name__ == "__main__":
    main()