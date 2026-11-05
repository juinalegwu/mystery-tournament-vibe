from showlocation import show_location

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

