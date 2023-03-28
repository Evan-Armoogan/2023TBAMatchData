from match_data import *
import requests
import json

def do_api_call(url):
    r = requests.get(url=url)
    response_data = r.json()
    return response_data

def parse_data(data_dict):

    alliance_colours = ["blue", "red"]
    alliance_data = {"blue": 0, "red": 0}
    for alliance in alliance_colours:
        team_data = []
        auto_game_pieces = data_dict["score_breakdown"][alliance]["autoGamePieceCount"]
        tele_game_pieces = data_dict["score_breakdown"][alliance]["teleopGamePieceCount"]
        auto_engaged = data_dict["score_breakdown"][alliance]["autoBridgeState"] == "Level"
        endgame_engaged = data_dict["score_breakdown"][alliance]["endGameBridgeState"] == "Level"
        for i in range(3):
            team_number = data_dict["alliances"][alliance]["team_keys"][i][3:]
            robot_mobility = data_dict["score_breakdown"][alliance][f"mobilityRobot{i+1}"]
            robot_auto_charge_station = "None"
            if data_dict["score_breakdown"][alliance][f"autoChargeStationRobot{i+1}"] == "Docked":
                if auto_engaged:
                    robot_auto_charge_station = "Engaged"
                else:
                    robot_auto_charge_station = "Docked"
            robot_endgame_charge_station = "None"
            if data_dict["score_breakdown"][alliance][f"endGameChargeStationRobot{i+1}"] == "Docked":
                if endgame_engaged:
                    robot_endgame_charge_station = "Engaged"
                else:
                    robot_endgame_charge_station = "Docked"
            team_data.append(TeamData(team_number, robot_mobility, robot_auto_charge_station, robot_endgame_charge_station))

        alliance_data[alliance] = AllianceData(alliance, team_data, auto_game_pieces, tele_game_pieces)

    match_data = MatchData(data_dict["match_number"], alliance_data)
    return match_data


def get_match_data(event_key, match_key):
    key = f"{event_key}_{match_key}"

    #TODO: hide api_key in a .secret file
    f = open("api_key.secret", "r")
    api_key = f.read()

    base_url = "https://www.thebluealliance.com/api/v3"
    url = f"{base_url}/match/{key}?X-TBA-Auth-Key={api_key}"

    response_data = do_api_call(url)
    return parse_data(response_data)

def write_file(data):
    file = open("data.csv", "w")
    file.write("Match,Alliance,Team,Mobility,Auto Charge Station,Endgame Charge Station,Alliance Auto Pieces,Alliance Tele Pieces\n")
    for match in data:
        for colour in ['blue', 'red']:
            alliance = match.alliances[colour]
            for team in alliance.teams:
                line = f"{match.match_num},{alliance.alliance_colour},{team.team_number},{team.robot_mobility},{team.robot_auto_charge_station},{team.robot_endgame_charge_station},{alliance.auto_game_pieces},{alliance.tele_game_pieces}\n"
                file.write(line)


def main():
    print("Powered by The Blue Alliance. See thebluealliance.com")
    event_key = input("Enter event key: ")
    match_key = input("Enter match key prefix: ")
    start_match = input("Enter start match: ")
    end_match = input("Enter end match: ")

    data = []
    for i in range(int(start_match), int(end_match) + 1):
        current_match = match_key + str(i)
        data.append(get_match_data(event_key, current_match))

    write_file(data)

    print("Data written")

    # code used to validate the match object's attributes
    """
    for match in data:
        print(match.match_num)
        for colour in ['blue', 'red']:       
            alliance = match.alliances[colour]
            print(alliance.tele_game_pieces)
            for team in alliance.teams:
                print(team.robot_endgame_charge_station)
    """

if __name__ == "__main__":
    main()