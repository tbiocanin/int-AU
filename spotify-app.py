import os 
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
print(sys.argv)
username = sys.argv[1]

scope = 'user-read-private user-read-playback-state user-modify-playback-state'

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

# Create Spotify object
spotifyObject = spotipy.Spotify(auth=token)

devices = spotifyObject.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']

# Get track information
track = spotifyObject.current_user_playing_track()
print(json.dumps(track, sort_keys=True, indent=4))
print()
artist = track['item']['artists'][0]['name']
track = track['item']['name']

if artist !="":
    print("Currently playing " + artist + " - " + track)

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
follower = user['followers']['total']

while True:

    print()
    print(">>> Welcome to Spotify " + displayName + " :)")
    print(">>> You have " + str(follower) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Enter your choice: ")

    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?: ")
        print()
    #get search result
    searchResult = spotifyObject.searh(searchQuery, 1, 0, "artist")

    trackSelectionList = []
    trackSelectionList.append(trackURIs[int(songSelection)])
    spotifyObject.start_playback(deviceID, None, trackSelectionList)

    if choice == "1":
        break