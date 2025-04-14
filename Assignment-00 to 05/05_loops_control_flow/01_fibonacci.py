def print_fibonacci_up_to_max():
    MAX_VALUE = 10000  # The maximum value for the Fibonacci sequence

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Print the first two Fibonacci numbers
    print(a)
    print(b)

    # Generate the next Fibonacci numbers and print them
    while True:
        # Calculate the next Fibonacci number
        a, b = b, a + b
        
        # Break the loop if the next number exceeds MAX_VALUE
        if b >= MAX_VALUE:
            break
        
        # Print the Fibonacci number
        print(b)

# Call the function to print the Fibonacci sequence
print_fibonacci_up_to_max()
