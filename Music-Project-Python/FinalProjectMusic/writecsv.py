import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import time
import pandas as pd

client_id = '3a5dd16e5d8c4367bc50f10853081107'
client_secret = '6174229408c24f3ea6696663273b2b97'


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

mySongs = {}
blackListArtistsDict = {}
hashString = ""

'''
 parameters in: user name(string), playlist ids (list)
 returns: ids of the songs in a playlist
'''

def getTrackIDs(user, playlist_id_array):
    ids = []
    for i in range(0, len(playlist_id_array)):
        playlist = sp.user_playlist(user, playlist_id_array[i])
        for item in playlist['tracks']['items']:
            hashString = item['track']['uri']
            key = hash(hashString)
            if not (key in mySongs.keys()):
                track = item['track']
                ids.append(track['id'])
                mySongs[key] = 1
    return ids


array =[""]*2
array[0] = "6CdDDVPERRK6Q1o6Y7YOPo" # 90's
array[1] = "2wjdNzVqTL0tDyIaWJQVqG" # 2000s's
#array[2] = "1CFTvR6ix3w57I4xZCOekZ" # 2010's
#array[3] = "02sumE76DfbxZEfbqWqVNP" # 80's
#array[4] = "39JVQz5pR9Q4EUaPtNU9zZ" #70's
ids = getTrackIDs('Lomta', array)


'''
parameters in: song id
returns: song info 
'''
def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  popularity = meta['popularity']

  # features
  acousticness = features[0]['acousticness'] # 0 - 1 ( 1 acoustic)
  danceability = features[0]['danceability'] # 0 - 1 
  energy = features[0]['energy'] # 0 - 1
  instrumentalness = features[0]['instrumentalness'] # max 1
  liveness = features[0]['liveness'] # > 0.8 == alive
  loudness = features[0]['loudness'] # -60 - 0
  speechiness = features[0]['speechiness'] # 0.33 - music 0.33 - 0. 66 - speech + music around 1 - speech
  tempo = features[0]['tempo'] # beats per minute
  time_signature = features[0]['time_signature'] #how many beats are in each bar

  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track
    
     
tracks = []
for i in range(len(ids)):
  track = getTrackFeatures(ids[i])
  tracks.append(track)

#creates csv file with song info
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("spotify.csv", sep = ',')
