import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_player_exists(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")

    def test_search_player_does_not_exist(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        self.assertEqual(team_players[0].name, "Semenko")
        self.assertEqual(team_players[1].name, "Kurri")
        self.assertEqual(team_players[2].name, "Gretzky")

    def test_team_returns_empty_list_for_nonexistent_team(self):
        team_players = self.stats.team("XYZ")
        self.assertEqual(team_players, [])

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)  
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_returns_all_players_if_how_many_is_large(self):
        top_players = self.stats.top(10)
        self.assertEqual(len(top_players), 5)

if __name__ == "__main__":
    unittest.main()
