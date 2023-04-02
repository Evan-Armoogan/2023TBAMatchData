import statbotics

# NOTE: Ontario district key is ONT

def main():
    year = int(input("Enter year: "))
    district = input("Enter district key: ")

    sb = statbotics.Statbotics()

    response = sb.get_teams(district=district, active=True)
    teams = []
    for team_info in response:
        teams.append(int(team_info['team']))
    stats_list = []
    for team in teams:
        try:
            stats_list.append(sb.get_team_year(year=year, team=team, fields=['team','epa_end']))
        except:
            'Hello World' # do nothing
    
    f = open('epa_data.csv', 'w')
    f.write('Team,EPA')
    for team_stat in stats_list:
        f.write(f"{team_stat['team']},{team_stat['epa_end']}\n")

    print("Data Written")

if __name__ == "__main__":
    main()