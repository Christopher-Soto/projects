import time

# /Users/csoto/Documents/projects/test.py


def print_slow(text, delay=0.05):
    """Print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    print_slow("Welcome to the Adventure Game!")
    print_slow("You find yourself in a dark forest. There are two paths ahead.")
    print_slow("Do you go left or right?")

    choice = input("Type 'left' or 'right': ").strip().lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print_slow("Invalid choice. The forest swallows you whole.")
        game_over()

def left_path():
    print_slow("You walk down the left path and encounter a wild wolf!")
    print_slow("Do you fight or run?")
    
    choice = input("Type 'fight' or 'run': ").strip().lower()

    if choice == "fight":
        print_slow("You bravely fight the wolf and emerge victorious!")
        print_slow("Congratulations, you win!")
    elif choice == "run":
        print_slow("You run away safely, but the adventure ends here.")
        print_slow("Game over.")
    else:
        print_slow("Invalid choice. The wolf attacks you.")
        game_over()

def right_path():
    print_slow("You walk down the right path and find a treasure chest!")
    print_slow("Do you open it or leave it?")
    
    choice = input("Type 'open' or 'leave': ").strip().lower()

    if choice == "open":
        print_slow("You open the chest and find a pile of gold!")
        print_slow("Congratulations, you're rich!")
    elif choice == "leave":
        print_slow("You leave the chest and walk away, missing out on the treasure.")
        print_slow("Game over.")
    else:
        print_slow("Invalid choice. The chest vanishes into thin air.")
        game_over()

def game_over():
    print_slow("Thank you for playing. Better luck next time!")
    exit()

if __name__ == "__main__":
    start_game()