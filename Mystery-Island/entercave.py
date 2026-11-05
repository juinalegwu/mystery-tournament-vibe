from showlocation import show_location

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

