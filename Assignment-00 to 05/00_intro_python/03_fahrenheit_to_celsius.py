def main():
    # Get the temperature in Fahrenheit from the user
    fahrenheit = float(input("\033[1;3m Enter the temperature in Fahrenheit\033[0m "))

    # Convert the input to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Print the result
    print(f"The temperature in Celsius is {celsius:.2f}°C")

# Ensuring the script runs when executed directly
if __name__ == "__main__":
    main()
