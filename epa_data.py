import statbotics

# NOTE: Ontario district key is ONT

sb = statbotics.Statbotics()

def get_epa_data(teams, year):
    stats_list = []
    for team in teams:
        try:
            stats_list.append(sb.get_team_year(year=year, team=team, fields=['team','epa_end','auto_epa_end','teleop_epa_end','endgame_epa_end','rp_1_epa_end','rp_2_epa_end','winrate']))
        except:
            print("Team Grab Failure")
    
    f = open('epa_data.csv', 'w')
    f.write('Team,EPA,Auto EPA,Teleop EPA,Endgame EPA,Sustainability RP,Activation RP,Winrate\n')
    for team_stat in stats_list:
        f.write(f"{team_stat['team']},{team_stat['epa_end']},{team_stat['auto_epa_end']},{team_stat['teleop_epa_end']},{team_stat['endgame_epa_end']},{team_stat['rp_1_epa_end']},{team_stat['rp_2_epa_end']},{team_stat['winrate']}\n")

    print("Data Written")

def main():
    year = int(input("Enter year: "))
    district = input("Enter district key: ")

    response = sb.get_teams(district=district, active=True)
    teams = []
    for team_info in response:
        teams.append(int(team_info['team']))

    get_epa_data(teams, year)

if __name__ == "__main__":
    main()