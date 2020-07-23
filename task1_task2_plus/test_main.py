from main import QuakeLogParser


class TestParser:
    def test_total_kills_game2_15(self):
        quake_game = QuakeLogParser()

        dict_parser = quake_game.parser()

        assert dict_parser['game-2']['total_kills'] == 15

    def test_total_kills_game7_89(self):
        quake_game = QuakeLogParser()

        dict_parser = quake_game.parser()

        assert dict_parser['game-7']['total_kills'] == 89

    def test_length_games(self):
        quake_game = QuakeLogParser()

        dict_parser = quake_game.parser()

        assert len(dict_parser) == 20

    def test_ranking_kill_game11_26(self):
        quake_game = QuakeLogParser()

        dict_parser = quake_game.parser()
        game_11 = dict_parser['game-11']['kills']

        assert game_11[max(game_11, key=game_11.get)] == 26

    def test_ranking_kill_game18_name_zeh(self):
        quake_game = QuakeLogParser()

        dict_parser = quake_game.parser()
        game_18 = dict_parser['game-18']['kills']

        assert max(game_18, key = game_18.get) == 'Zeh'

    def test_ranking_means_of_death_game9_name_mod_telefrag(self):
        quake_game = QuakeLogParser()

        dict_parser = quake_game.means_of_death()
        game_9 = dict_parser['game-9']['kills_by_means']

        assert max(game_9, key = game_9.get) == 'MOD_TELEFRAG'

    def test_ranking_means_of_death_game20_60(self):
        quake_game = QuakeLogParser()

        dict_parser = quake_game.means_of_death()
        game_20 = dict_parser['game-20']['kills_by_means']

        assert game_20[max(game_20, key=game_20.get)] == 60

