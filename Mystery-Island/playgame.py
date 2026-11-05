from createplayer import create_player
from enterjungle import enter_jungle
from entercave import enter_cave
from crossbridge import cross_bridge
from lighthouse import enter_lighthouse
from showstatus import show_status
from showlocation import show_location


def show_menu():
    print("\n========== MYSTERY ISLAND ==========")
    print("1. Explore the beach")
    print("2. Enter the jungle")
    print("3. Enter the cave")
    print("4. Cross the old Bridge")
    print("5. Enter the Lighthouse")
    print("6. Check your status")
    print("7. Quit game")
    print("8. Take a dangerous shortcut in the cave")


def play_game():
    player = create_player()

    print("\nWelcome to Mystery Island!")

    show_status(player)
    show_location(player)

    while not player["game_over"]:

        show_menu()

        try:
            choice = int(input("\nEnter your choice: "))

        except ValueError:
            print("\nInvalid choice! Please enter a number.")
            continue

        if choice == 1:
            print("\nYou are exploring the beach!")

        elif choice == 2:
            enter_jungle(player)

        elif choice == 3:
            enter_cave(player)

        elif choice == 4:
            cross_bridge(player)

        elif choice == 5:
            enter_lighthouse(player)

        elif choice == 6:
            show_status(player)

        elif choice == 7:
            print("\nThanks for playing!")
            player["game_over"] = True

        elif choice == 8:
            if player["location"] == "Cave":
                print("\nYou took a dangerous shortcut!")
                print("You fell into a deep hole!")

                player["energy"] -= 3

                if player["energy"] <= 0:
                    player["energy"] = 0
                    player["game_over"] = True
                    print("\nGAME OVER! You ran out of energy.")

        else:
            print("\nInvalid choice. Please try again.")

        if player["energy"] <= 0:
            player["energy"] = 0
            player["game_over"] = True

    if not player["won"] and player["energy"] <= 0:
        print("\nGAME OVER!")

    print("\nThank you for playing Mystery Island!")