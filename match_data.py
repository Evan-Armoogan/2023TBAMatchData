class MatchData:
    match_num = 0
    alliances = {}

    def __init__(self, match_num, alliances):
        self.match_num = match_num
        self.alliances = alliances

class AllianceData:
    alliance_colour = ""
    teams = []
    auto_game_pieces = 0
    tele_game_pieces = 0

    def __init__(self, colour, teams, auto_pieces, tele_pieces):
        self.alliance_colour = colour
        self.teams = teams
        self.auto_game_pieces = auto_pieces
        self.tele_game_pieces = tele_pieces

class TeamData:
    team_number = 0
    robot_mobility = 0
    robot_auto_charge_station = 0
    robot_endgame_charge_station = 0

    def __init__(self, team_number, mobility, auto_charge_station, endgame_charge_station):
        self.team_number = team_number
        self.robot_mobility = mobility
        self.robot_auto_charge_station = auto_charge_station
        self.robot_endgame_charge_station = endgame_charge_station