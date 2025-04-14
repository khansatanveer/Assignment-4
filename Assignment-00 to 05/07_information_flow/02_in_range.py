def in_range(n, low, high):
    # Returns True if n is between low and high, inclusive
    return low <= n <= high

def main():
    # Get user input
    n = int(input("Enter the number: "))
    low = int(input("Enter the low value: "))
    high = int(input("Enter the high value: "))

    # Check if the number is in range
    result = in_range(n, low, high)
    print(result)

if __name__ == '__main__':
    main()

