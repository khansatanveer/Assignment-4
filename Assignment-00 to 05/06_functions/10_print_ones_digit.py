def print_ones_digit(num):
    # Use the modulo operator to get the ones digit
    ones_digit = num % 10
    print(f"\033[34mThe ones digit is {ones_digit}\033[0m")

def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    # Call the print_ones_digit function with the entered number
    print_ones_digit(num)

if __name__ == '__main__':
    main()
