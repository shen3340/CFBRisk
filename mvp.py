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

# Function to modify Discord usernames if needed
def modify_discord_username(username):
    # Define the mapping of usernames that need to be modified
    username_mapping = {
        "Shaller13": "shaller88", "32RH": "32rh", "bobsappisfat": "bobsappisfat1", "BrBuckeye1": "brbuckeye1", 
        "Janus67": "janus67", "Mavyn1": "mavyn1", "MochasAway": "mochasaway", "rax96": "rax96max",
        "doom_bagel":"uncle_bagel", "slappinDingers1":"slappindingers1"
        # Add more mappings as needed
    }
    # Check if the username needs to be modified
    if username in username_mapping:
        return username_mapping[username]
    else:
        return username

# URL of the API for MVPs
mvp_url = "https://collegefootballrisk.com/api/team/players?season=4&day=19&team=Shark"

# Get MVP player names
mvp_players = get_mvp_players(mvp_url)

# List of Reddit usernames
reddit_usernames = [
    "AbundantFailure", "bb06ta", "GoBucks513", "HonestDig1", 
    "madcel56", "SnooDogs365", "TopStuff513", "truetoatlanta17",
    "Vast_Field2374"
]

# Filter MVP players to include only Discord usernames not present in the list of Reddit usernames
discord_players = []
for player in mvp_players:
    # Check if the player is not in the list of Reddit usernames
    if player not in reddit_usernames:
        # Modify Discord usernames if needed and remove $0 suffix if present
        player = modify_discord_username(player)
        if player.endswith("$0"):
            player = player[:-2]  # Remove last two characters ($0)
        discord_players.append(player)

# Filter Reddit usernames to include only those who won MVP
mvp_reddit_usernames = [username for username in reddit_usernames if username in mvp_players]

# Sort the final lists alphabetically
discord_players.sort(key=lambda x: x.lower())
mvp_reddit_usernames.sort(key=lambda x: x.lower())

# Print the final lists
if discord_players:
    # Concatenate all Discord usernames with "@" prefix and separate them with a space
    discord_usernames_str = " ".join("@" + player for player in discord_players)
    print("Congratulations to the following Sharks who won MVP for last night's roll:", end=' ')
    print(discord_usernames_str, end=' ')  # Print Discord usernames on the same line

if mvp_reddit_usernames:
    # Concatenate all MVP Reddit usernames and separate them with a space
    mvp_reddit_usernames_str = " ".join(mvp_reddit_usernames)
    print(mvp_reddit_usernames_str)  # Print MVP Reddit usernames on the same line, after a space
