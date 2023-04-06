import requests

def do_api_call(url):
    r = requests.get(url=url)
    response_data = r.json()
    return response_data

def parse_data(data):
    teams = []
    for team_data in data:
        teams.append(team_data['team_number'])
    return teams

def main():
    event_key = input("Enter event key: ")

    f = open("api_key.secret", "r")
    api_key = f.read()
    f.close

    base_url = "https://www.thebluealliance.com/api/v3"
    url = f"{base_url}/event/{event_key}/teams?X-TBA-Auth-Key={api_key}"
    response = do_api_call(url)
    
    teams = parse_data(response)
    
    f = open("event_teams.txt", "w")
    for team in teams:
        f.write(f"{team}\n")
    f.close()
    
    print("Data written")

if __name__ == "__main__":
    main()
