from unittest.mock import patch
from playgame import play_game

def main():
    while True:
        play_game()

        answer = input("\nWould you like to play again? (yes/no): ")

        if answer.lower() != "yes":
            print("\nThanks for playing Mystery Island!")
            break

if __name__ == "__main__":
    main()
                   
