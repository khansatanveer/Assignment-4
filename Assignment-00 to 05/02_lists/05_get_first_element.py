def get_first_element(lst):
    print(lst[0])  # Prints the first element of the list

########## No need to edit code past this point

def main():
    n = int(input("How many elements do you want to enter? "))
    lst = []
    for _ in range(n):
        element = input("Enter an element: ")
        lst.append(element)

    get_first_element(lst)  # Call the function to print the first element

if __name__ == "__main__":
    main()
