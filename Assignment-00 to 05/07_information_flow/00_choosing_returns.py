ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False

def main():
    age : str = int(input("How old is this person?: "))
    print(f"\033[34m{is_adult(age)}\033[0m") 
    
if __name__ == "__main__":
    main()