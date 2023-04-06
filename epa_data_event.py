import epa_data
teams_file = "event_teams.txt"

def main():
    year = int(input("Enter year: "))

    teams = []
    f = open(teams_file, "r")
    while True:
        line = f.readline()
        if line == "":
            break
        teams.append(int(line[:-1]))
    
    epa_data.get_epa_data(teams, year)

if __name__ == "__main__":
    main()
