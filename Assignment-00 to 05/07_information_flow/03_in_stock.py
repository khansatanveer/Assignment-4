def num_in_stock(fruit):
    # A sample inventory of fruits and their stock numbers
    inventory = {
        'apple': 50,
        'pear': 1000,
        'banana': 200,
        'grapes': 0,
        'orange': 150
    }
    
    # Return the stock number if the fruit is in the inventory, otherwise 0
    return inventory.get(fruit.lower(), 0)  

# Main function to interact with the user
def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ").strip()

    # Get the number of that fruit in stock
    stock = num_in_stock(fruit)

    # Print the result based on the stock quantity
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(f"\033[1m\033[3m{stock}\033[0m")
    else:
        print("This fruit is not in stock.")

# Run the program
if __name__ == '__main__':
    main()
