def get_user_data():
    # Ask for user input
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")

    # Return the values as a tuple
    return first_name, last_name, email


def main():
    # Get the user data
    user_data = get_user_data()

    # Print the result
    print("Received the following user data:", user_data)


if __name__ == '__main__':
    main()
