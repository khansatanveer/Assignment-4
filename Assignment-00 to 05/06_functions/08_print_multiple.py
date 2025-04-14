def print_multiple(message: str, repeats: int):
    message = f"\033[1;34m{message}\033[0m"
    
    for i in range(repeats):
        print(message)


def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
