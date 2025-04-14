def access_element(lst, index):
    # Check if the index is valid
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range"

def modify_element(lst, index, new_value):
    # Check if the index is valid
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range"

def slice_list(lst, start_index, end_index):
    # Handle out of range indices
    if start_index < 0 or end_index > len(lst) or start_index > end_index:
        return "Invalid indices"
    return lst[start_index:end_index]

def game():
    # Sample list for the game
    game_list = [10, 'apple', 3.14, 'banana', True]
    
    print("Welcome to the Index Game!")
    print("Current List:", game_list)
    
    # Game loop
    while True:
        print("\nChoose an operation:")
        print("1. Access Element")
        print("2. Modify Element")
        print("3. Slice List")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = access_element(game_list, index)
            print(f"Element at index {index}: {result}")
        
        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(game_list, index, new_value)
            print(f"Updated List: {result}")
        
        elif choice == '3':
            start_index = int(input("Enter the start index for slicing: "))
            end_index = int(input("Enter the end index for slicing: "))
            result = slice_list(game_list, start_index, end_index)
            print(f"Sliced List: {result}")
        
        elif choice == '4':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    game()
