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
