def main():
    name: str = input("What's your name? ")
    print(greet(name))  

def greet(name):
    return "\033[1m\033[3mGreetings " + name + "!\033[0m"   

if __name__ == '__main__':
    main() 

