import requests
import json

users = input("Enter GitHub username: ")
url = f"https://api.github.com/users/{users}/repos"

# passing parameters in a GET request
data = {"type": "all", "sort": "full_name", "direction": "asc"}

# Making GET request with query parameters
output = requests.get(url, params=data)

# Convert response to JSON
output = output.json()

# Print repository names
for repo in output:
    print(repo["name"])
