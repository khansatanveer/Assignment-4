def main():
    # Get the length in feet.
    feet: float = float(input("Enter the number of feet: "))

    #  Calculate the total inches.
    inches: float = feet * 12  # There are 12 inches in a foot 

    # Print the result
    print("That is", inches, "inches!")

# Ensuring the script runs when executed directly
if __name__ == "__main__":
    main()
