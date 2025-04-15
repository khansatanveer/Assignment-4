def mad_libs():
    print("Welcome to Computer Mad Libs!")
    print("Please provide the following words:\n")

    adjective = input("Adjective: ")
    noun = input("Noun: ")
    verb = input("Verb (past tense): ")

    story = f"""
    The {adjective} {noun} tried to {verb} on the computer, but it crashed immediately.
    In a panic, the developer accidentally spilled coffee on the {noun}.
    Surprisingly, the computer started working better than before — it was a {adjective} miracle!
    """

    print("\nHere's your computer-themed 3-line Mad Libs story:")
    print(story)

    print("Thanks for playing!")
if __name__ == "__main__":
    mad_libs()
