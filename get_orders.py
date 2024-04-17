import requests

# URL of the API
url = "https://collegefootballrisk.com/api/territories?day=16S&season=4"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()

    # Set to keep track of names already added to relevant data
    added_names = set()

    # List to store territories owned by "Shark"
    shark_territories = [item["name"] for item in data if item.get("owner") == "Shark"]

    # List to store territories neighboring Bermuda owned by "Shark"
    bermuda_neighbors_shark = [neighbor["name"] for territory in data if territory["name"] == "Bermuda" for neighbor in territory["neighbors"] if neighbor["name"] in shark_territories]

    # Filter the data where the owner is "Shark"
    relevant_data_shark = [item["name"] for item in data if item.get("owner") == "Shark" and not all(neighbor.get("owner") == "Shark" for neighbor in item.get("neighbors", []))]
    added_names.update(relevant_data_shark)

    # Filter the data where "Shark" appears at least once in the "neighbors" block but exclude items owned by "Shark"
    relevant_data_neighbors = []
    for item in data:
        if item.get("owner") != "Shark" and any(neighbor.get("owner") == "Shark" for neighbor in item.get("neighbors", [])):
            if item["name"] not in added_names and item["name"] != "Bermuda" and item["name"] not in bermuda_neighbors_shark:
                relevant_data_neighbors.append(item["name"])
                added_names.add(item["name"])

    # Sort the relevant data for better organization
    relevant_data_shark.sort()
    relevant_data_neighbors.sort()

    # Save the combined relevant data to a single .txt file
    with open("legal_moves_day_16.txt", "w") as file:
        # Write territories owned by Shark under "Defend" category
        file.write("Defend:\n")
        for name in relevant_data_shark:
            file.write(name + "\n")
        file.write("\n")
        # Write other territories under "Attack" category
        file.write("Attack:\n")
        for name in relevant_data_neighbors:
            file.write(name + "\n")
        print("Data saved to legal_moves_day_16.txt")
else:
    print("Failed to fetch data from the API")
