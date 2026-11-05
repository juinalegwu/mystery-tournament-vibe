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