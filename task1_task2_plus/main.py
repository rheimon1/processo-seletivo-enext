import json


class QuakeLogParser:
    path_game_log = ''

    def __init__(self):
        self.path_game_log = 'game.log'

    def open_log(self):
        with open(self.path_game_log) as file:
            return file.readlines()

    def parser(self):
        counter_kill, counter = 0, 0
        players = []
        game, kills, game_counter = dict(), dict(), dict()

        content_log = self.open_log()

        for line in content_log:
            data_line = line.split()
            if data_line[1] != "ShutdownGame:":
                if data_line[1] == "Kill:":
                    index = data_line.index("killed")
                    name = " ".join(data_line[5:index])
                    counter_kill += 1
                    if name == "<world>":
                        name = " ".join(data_line[7:-2])
                        if name in kills.keys():
                            kills[name] -= 1
                        elif name not in kills.keys():
                            kills[name] = -1
                    else:
                        if name not in kills.keys():
                            kills[name] = 1
                        elif name in kills.keys():
                            kills[name] += 1
                if data_line[1] == "ClientUserinfoChanged:":
                    length = len(data_line)
                    name = data_line[3:length]
                    name = " ".join(name)
                    name = name.split("\\")[1]
                    if name not in players:
                        players.append(name)
                    if name not in kills.keys():
                        kills[name] = 0
            elif data_line[1] == "ShutdownGame:":
                counter += 1
                game['id'] = counter
                game["total_kills"] = counter_kill
                game["players"] = players
                game["kills"] = kills
                name = "game-" + str(counter)
                game_counter[name] = game
                counter_kill = 0
                players = []
                game, kills = dict(), dict()
        return game_counter

    def print_report_parser(self):
        game_data = self.parser()
        json_game_data = json.dumps(game_data, indent=4)
        print(json_game_data)

    def general_ranking_kills_player(self):
        game_data = self.parser()
        players, rank = dict(), dict()

        for key, value in game_data.items():
            for key2, value2 in value.items():
                if type(value2) is list:
                    for player in value2:
                        if player in players.keys():
                            pass
                        else:
                            players[player] = 0

        for key, value in game_data.items():
            for key2, value2 in value.items():
                if type(value2) is dict:
                    for key3, value3 in value2.items():
                        if key3 in players.keys():
                            aux = players[key3]
                            players[key3] = aux + value3

        for item in sorted(players, key=players.get, reverse=True):
            print("{}: {}".format(item, players[item]))

    def means_of_death(self):
        means = [
            "MOD_UNKNOWN",
            "MOD_SHOTGUN",
            "MOD_GAUNTLET",
            "MOD_MACHINEGUN",
            "MOD_GRENADE",
            "MOD_GRENADE_SPLASH",
            "MOD_ROCKET",
            "MOD_ROCKET_SPLASH",
            "MOD_PLASMA",
            "MOD_RAILGUN",
            "MOD_LIGHTNING",
            "MOD_BFG",
            "MOD_BFG_SPLASH",
            "MOD_WATER",
            "MOD_SLIME",
            "MOD_LAVA",
            "MOD_CRUSH",
            "MOD_TELEFRAG",
            "MOD_FALLING",
            "MOD_SUICIDE",
            "MOD_TARGET_LASER",
            "MOD_TRIGGER_HURT",
            "MOD_NAIL",
            "MOD_CHAINGUN",
            "MOD_PROXIMITY_MINE",
            "MOD_KAMIKAZE",
            "MOD_JUICED",
            "MOD_GRAPPLE",
        ]
        content_log = self.open_log()
        game_counter, kills_by_means, game = dict(), dict(), dict()
        counter = 0

        for line in content_log:
            if line.split()[1] != "ShutdownGame:":
                if line.split()[1] == "Kill:":
                    mean = line.split()[-1]
                    if mean in means:
                        if mean in game.keys():
                            aux = game[mean]
                            game[mean] = aux + 1
                        else:
                            game[mean] = 1
            elif line.split()[1] == "ShutdownGame:":
                counter += 1
                kills_by_means["kills_by_means"] = game
                name = "game-" + str(counter)
                game_counter[name] = kills_by_means
                game, kills_by_means = dict(), dict()
        return game_counter

    def print_report_means_of_death(self):
        game_data = self.means_of_death()
        json_game_data = json.dumps(game_data, indent=4)
        print(json_game_data)

    def create_file_parser_json(self):
        game_data = self.parser()
        json_game_data = json.dumps(game_data, indent=4)

        json_file = open('parser.json', 'w+')
        json_file.write(json_game_data)
        json_file.close()