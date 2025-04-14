def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"\033[34mI am excited to add this {word} to my vast collection of them!\033[0m")  # Blue
    elif part_of_speech == 1:
        print(f"\033[34mIt's so nice outside today it makes me want to {word}!\033[0m")  # Blue
    elif part_of_speech == 2:
        print(f"\033[34mLooking out my window, the sky is big and {word}!\033[0m")  # Blue
    else:
        print("\033[34mPart of speech must be 0, 1, or 2! Can't make a sentence.\033[0m")  # Blue

def main():
    word: str = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
