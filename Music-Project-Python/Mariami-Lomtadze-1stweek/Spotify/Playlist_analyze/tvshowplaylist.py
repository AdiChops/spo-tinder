import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import time
import pandas as pd
from matplotlib import pyplot as plt 

client_id = '3a5dd16e5d8c4367bc50f10853081107'
client_secret = '6174229408c24f3ea6696663273b2b97'



client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

mySongs = {}
blackListArtistsDict = {}
hashString = ""

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        hashString = item['track']['uri']
        key = hash(hashString)
        if not (key in mySongs.keys()):
            track = item['track']
            ids.append(track['id'])
            mySongs[key] = 1
    return ids


array =[""]*10
array[0] = "1cjgdAcievcDPDLumpNne6" # How I met your mother
array[1] = "0YKfXGKGWa6WVloCH53ADz" # The office
array[2] = "3Qxh9fPAllYY6woPiitfxe" # Community
array[3] = "7sfsAupFz7Bw1aoLg9GB4h" # Friends
array[4] = "4hW8Ldn4q9VgSlvkCuqaMV" # Family guy
array[6] = "6hUPdr8D89Iac3hn6emtL7" # Scrubs
array[9] = "0tIh8uer62lqDvn6P1Z5gO" # Modern Family
array[8] = "5Xhl4Yg2bFglagDY5JhUU2" # Freaks and Geeks
array[7] = "4Z4veNVujTOrlO27YIIsrf" # brooklyn 99
array[5] = "7eDOlLhwXPVYdkhTJ9CJaM" # That 70's show

tvshow_names = [""]*10
tvshow_names[0] = "How I met your mother"
tvshow_names[1] = "The office"
tvshow_names[2] = "Community"
tvshow_names[3] = "Friends"
tvshow_names[4] = "Family guy"
tvshow_names[6] = "Scrubs"
tvshow_names[9] = "Modern Family"
tvshow_names[8] = "Freaks and Geeks"
tvshow_names[7] = "brooklyn 99"
tvshow_names[5] = "That 70's show"

    

def getTrackFeatures(id):
    global average
    global cnt
    meta = sp.track(id)
    features = sp.audio_features(id)

    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    if popularity != 0:
        average += popularity
        cnt += 1
    track = [name, album, artist, release_date, length, popularity]
    return track

average_array = [0]*10 

for x in range (0, 10):
    ids = getTrackIDs('Lomta', array[x])    
    average = 0
    cnt = 0
    tracks = []
    for i in range(len(ids)):
        track = getTrackFeatures(ids[i])
        tracks.append(track)
           
    average_array[x] = average/cnt
    
plt.plot(tvshow_names, average_array)
plt.show()    