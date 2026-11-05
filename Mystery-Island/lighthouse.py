from showlocation import show_location

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
