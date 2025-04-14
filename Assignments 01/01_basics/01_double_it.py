def main():
    curr_value = int(input("Enter a number: "))
    
    # Repeat the process until the value is 100 or greater
    while curr_value < 100:
        # Double the current value and print it
        curr_value = curr_value * 2
        print(curr_value, end=" ")

if __name__ == '__main__':
    main()
