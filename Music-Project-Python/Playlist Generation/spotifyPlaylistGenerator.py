import requests
import json

# For now this code only creates playlists, adds and delete songs for a specific user that is hardcoded in
# Next steps will be to do user authentication from spotify and get permissions from them to modify playlists
# Once we get permission, we just set user_id and token to their information and use this code


# Keys needed to create/add songs to playlists
user_id = "" # Specific spotify ID
token = "" # For now you will need to generate token each time

# Authorization needed for any action with Spotify API
headers = {"Authorization": f"Bearer {token}",
            "Content-Type": "application/json"}

# Creating Playlist -----------------
url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
body = json.dumps({"name": "Spotify API 10",
        "public": False,
        "description": "Created using spotify API hellz ye"})

response = requests.post(url, data = body, headers = headers)

# -------------------------------------

# Adding songs to Playlist ---------------------

# Assumed that I will receive spotify playlist URIs
ids = ["spotify:track:0FE9t6xYkqWXU2ahLh6D8X", "spotify:track:12GEpg2XOPyqk03JZEZnJs", "spotify:track:09IStsImFySgyp0pIQdqAc", "spotify:track:54j7EaJPDmSZYcNYvLSJ78", "spotify:track:530J9GupahE2O4a1iVkQxB"]

playlist_id = response.json()["id"]

url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
uris = json.dumps({"uris": ids})

response = requests.post(url, headers = headers, data = uris)

# ---------------------------------------------

input()

# Deleting songs from Playlist --------------
url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

# Assumed I receive a list of spotify song URIs to delete
ids = ["spotify:track:0FE9t6xYkqWXU2ahLh6D8X", "spotify:track:12GEpg2XOPyqk03JZEZnJs"]

# Getting tracks to delete in correct format
tracks = {"tracks": []}
for i in ids:
    tracks["tracks"].append({"uri": i})

response = requests.delete(url, headers = headers, data = json.dumps(tracks))

# ----------------------------------