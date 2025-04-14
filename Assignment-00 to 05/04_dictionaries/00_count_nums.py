def main():
    numbers = []
    while True:
        entry = input("Enter a number: ")
        if entry == "":
            break
        numbers.append(int(entry))

    # Count occurrences using a dictionary
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    # Print the results with colored output
    for number, count in counts.items():
        print(f"\033[1;34m{number} appears {count} times.\033[0m")  # Bold Blue

if __name__ == '__main__':
    main()
