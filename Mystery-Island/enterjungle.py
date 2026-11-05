from showlocation import show_location

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