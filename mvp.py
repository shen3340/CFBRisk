import requests

# Function to fetch MVP player names
def get_mvp_players(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        mvp_players = [item["player"] for item in data if item.get("mvp")]
        return mvp_players
    else:
        print("Failed to fetch MVP data from the API")
        return []

# URL of the API for MVPs
mvp_url = "https://collegefootballrisk.com/api/team/players?season=4&day=3&team=Shark"

# Get MVP player names
mvp_players = get_mvp_players(mvp_url)

# Print the MVP players
if mvp_players:
    print("MVP Players:")
    for player in mvp_players:
        print(player)
else:
    print("No MVP players found")

# Now you can use mvp_players list to further process or analyze the MVPs