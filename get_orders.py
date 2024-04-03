import requests

# URL of the API
url = "https://collegefootballrisk.com/api/territories?day=3&season=4"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()

    # Set to keep track of names already added to relevant data
    added_names = set()

    # Filter the data where the owner is "Shark"
    relevant_data_shark = [item["name"] for item in data if item.get("owner") == "Shark" and not all(neighbor.get("owner") == "Shark" for neighbor in item.get("neighbors", []))]
    added_names.update(relevant_data_shark)

    # Filter the data where "Shark" appears at least once in the "neighbors" block but exclude items owned by "Shark"
    relevant_data_neighbors = []
    for item in data:
        if item.get("owner") != "Shark" and any(neighbor.get("owner") == "Shark" for neighbor in item.get("neighbors", [])):
            if item["name"] not in added_names:
                relevant_data_neighbors.append(item["name"])
                added_names.add(item["name"])

    # Combine relevant data from both filters
    combined_data = sorted(relevant_data_shark + relevant_data_neighbors)

    # Save the combined relevant data to a single .txt file
    with open("legal_moves_day_3.txt", "w") as file:
        for name in combined_data:
            file.write(name + "\n")
        print("Combined data saved to legal_moves_day_3.txt")
else:
    print("Failed to fetch data from the API")
