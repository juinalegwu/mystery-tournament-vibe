from unittest.mock import patch

def create_player():
    name = input("Enter your name: ")

    player = {
        "name": name,
        "energy": 5,
        "location": "Beach",
        "inventory": [],
        "game_over": False,
        "won": False
    }

    return player


def show_status(player):
    print("\n--- PLAYER STATUS ---")
    print(f"Name: {player['name']}")
    print(f"Energy: {player['energy']}")
    print(f"Location: {player['location']}")
    print(f"Inventory: {player['inventory']}")


def show_location(player):
    location = player["location"]

    if location == "Beach":
        print("\nYou are standing on a beautiful beach.")
        print("You can see a dark jungle ahead.")

    elif location == "Jungle":
        print("\nYou are inside a dark jungle.")
        print("You hear strange sounds around you.")

    elif location == "Cave":
        print("\nYou have entered a mysterious cave.")
        print("It is very dark inside.")

    elif location == "Old Bridge":
        print("\nYou are standing before an old wooden bridge.")
        print("The bridge looks dangerous.")

    elif location == "Lighthouse":
        print("\nYou have reached the old lighthouse.")
        print("You used your lantern to light it!")


def enter_jungle(player):
    if player["location"] == "Beach":
        player["energy"] -= 1
        player["location"] = "Jungle"

        if "rope" not in player["inventory"]:
            player["inventory"].append("rope")
            print("You found a rope!")

        show_location(player)
        print(f"Energy remaining: {player['energy']}")

    else:
        print("You are not at the Beach!")


def enter_cave(player):
    if player["location"] == "Jungle":
        player["energy"] -= 1
        player["location"] = "Cave"

        if "lantern" not in player["inventory"]:
            player["inventory"].append("lantern")
            print("You found a lantern!")

        show_location(player)
        print(f"Energy remaining: {player['energy']}")

    else:
        print("You must enter the Jungle before entering the Cave!")


def cross_bridge(player):
    if player["location"] == "Cave":
        if "rope" in player["inventory"]:
            player["energy"] -= 1
            player["location"] = "Old Bridge"

            show_location(player)
            print("You successfully crossed the bridge!")
            print(f"Energy remaining: {player['energy']}")

        else:
            print("You need a rope to cross the bridge!")

    else:
        print("You must enter the Cave before crossing the bridge!")


def enter_lighthouse(player):
    if player["location"] == "Old Bridge":
        if "lantern" in player["inventory"]:
            player["location"] = "Lighthouse"

            show_location(player)
            print("CONGRATULATIONS! YOU WON!")

            player["won"] = True
            player["game_over"] = True

        else:
            print("You need a lantern to light the lighthouse!")

    else:
        print("You must cross the Old Bridge before entering the Lighthouse!")


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
def main():
    while True:
        play_game()

        answer = input("\nWould you like to play again? (yes/no): ")

        if answer.lower() != "yes":
            print("\nThanks for playing Mystery Island!")
            break

if __name__ == "__main__":
    main()
                   
