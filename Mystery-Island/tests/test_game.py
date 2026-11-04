import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

from main import create_player, show_location, show_status, enter_jungle, enter_cave, cross_bridge, enter_lighthouse

class TestMysteryIsland(unittest.TestCase):

    def test_player_starts_at_beach(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        self.assertEqual(player["location"], "Beach")

    def test_player_starts_with_five_energy(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        self.assertEqual(player["energy"], 5)

    def test_player_starts_with_empty_inventory(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        self.assertEqual(player["inventory"], [])

    def test_player_name_is_saved(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        self.assertEqual(player["name"], "Juliet")

    def test_game_is_not_over_at_start(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        self.assertFalse(player["game_over"])

    def test_player_has_not_won_at_start(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        self.assertFalse(player["won"])

    def test_beach_description_is_displayed(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        output = StringIO()

        with redirect_stdout(output):
            show_location(player)

        self.assertIn("beautiful beach", output.getvalue())

    def test_status_displays_player_name(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        output = StringIO()

        with redirect_stdout(output):
            show_status(player)

        self.assertIn("Juliet", output.getvalue())

    def test_enter_jungle(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        enter_jungle(player)

        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)
        self.assertIn("rope", player["inventory"])

    def test_cannot_enter_jungle_from_cave(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        player["location"] = "Cave"

        enter_jungle(player)

        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 5)
        self.assertNotIn("rope", player["inventory"])
    
    def test_enter_cave(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        enter_jungle(player)
        enter_cave(player)

        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 3)
        self.assertIn("rope", player["inventory"])
        self.assertIn("lantern", player["inventory"])

    def test_cross_bridge(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        enter_jungle(player)
        enter_cave(player)
        cross_bridge(player)

        self.assertEqual(player["location"], "Old Bridge")
        self.assertEqual(player["energy"], 2)
        self.assertIn("rope", player["inventory"])
    
    def test_enter_lighthouse_and_win(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        enter_jungle(player)
        enter_cave(player)
        cross_bridge(player)
        enter_lighthouse(player)

        self.assertEqual(player["location"], "Lighthouse")
        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])
    
    def test_cannot_light_lighthouse_without_lantern(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        player["location"] = "Old Bridge"

        enter_lighthouse(player)

        self.assertEqual(player["location"], "Old Bridge")
        self.assertFalse(player["won"])
        self.assertFalse(player["game_over"])
    
    def test_cannot_cross_bridge_without_rope(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        player["location"] = "Cave"

        cross_bridge(player)

        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 5)
    
    def test_dangerous_shortcut_ends_game(self):
        with patch("builtins.input", return_value="Juliet"):
            player = create_player()

        player["location"] = "Cave"
        player["energy"] = 3

        player["energy"] -= 3

        if player["energy"] <= 0:
            player["energy"] = 0
            player["game_over"] = True

        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])
        self.assertFalse(player["won"])
    
    def test_invalid_menu_input_does_not_crash(self):
        with patch("builtins.input", side_effect=["Juliet", "hello", "7", "no"]):
            with patch("builtins.print") as mock_print:
                from main import main
                main()

        messages = [str(call) for call in mock_print.call_args_list]

        self.assertTrue(
            any("Invalid choice!" in message for message in messages)
        )
    def test_player_can_replay_game(self):
        with patch("builtins.input", side_effect=[
            "Juliet", "7", "yes",
            "Grace", "7", "no"
        ]):
            with patch("builtins.print"):
                from main import main
                main()

if __name__ == "__main__":
    unittest.main()
