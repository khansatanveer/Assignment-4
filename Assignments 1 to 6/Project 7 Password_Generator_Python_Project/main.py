import random
import string

def generate_password(length):
    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("🔐 Welcome to the Password Generator!")
    
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("What should be the length of each password? "))
        
        print("\nHere are your passwords:\n")
        for i in range(num_passwords):
            print(f"{i+1}. {generate_password(length)}")
    
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Run the generator
main()
