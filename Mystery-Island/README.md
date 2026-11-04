# Mystery Island — The Lost Lighthouse

## Project Description

Mystery Island is a Python command-line adventure game where players explore an island, collect useful items, manage their energy, and try to reach the lost lighthouse.

The goal is to reach the lighthouse safely using the rope and lantern.

## Requirements

- Python 3 installed.
- A terminal or command prompt.

## How to Run the Game

1. Open the project folder.
2. Run the following command:

```bash
python3 main.py
```

3. Enter your player name.
4. Follow the menu instructions to explore the island.

## Game Rules

- You start at the Beach with 5 energy.
- Entering the Jungle costs 1 energy.
- Entering the Cave costs 1 energy.
- Crossing the Old Bridge costs 1 energy.
- Collect the rope in the Jungle.
- Collect the lantern in the Cave.
- You need the rope to cross the bridge.
- You need the lantern to light the lighthouse.
- Taking the dangerous shortcut in the Cave costs 3 energy.
- If your energy reaches zero, you lose.
- Reach the Lighthouse safely to win.
- You can quit or replay the game.

## Game Locations

1. Beach
2. Jungle
3. Cave
4. Old Bridge
5. Lighthouse

## How to Run the Tests

Run this command from the project folder:

```bash
python3 -m unittest discover -s tests -v
```

The project currently has 18 automated tests.

## Project Structure

```text
Mystery-Island/
│
├── main.py
├── README.md
└── tests/
    └── test_game.py
```

## Technologies Used

- Python
- Python unittest module

## Known Limitations

- The game runs in the terminal.
- Player progress is not saved after the game ends.
- The game has a fixed set of locations and choices.
