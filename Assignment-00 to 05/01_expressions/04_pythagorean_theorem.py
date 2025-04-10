import math

def main():
    # Get the lengths of the two sides
    ab = float(input("Enter the length of side AB: "))
    ac = float(input("Enter the length of side AC: "))

    # Calculate the length of side AC using the Pythagorean theorem
    bc = math.sqrt(ab ** 2 + ac ** 2)

    # Display the result
    print(f"The length of BC the hypotenuse is {bc}")
    
# Ensuring the script runs when executed directly
if __name__ == "__main__":
    main()