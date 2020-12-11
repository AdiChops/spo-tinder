import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import time
import pandas as pd
import operator


window = tk.Tk()
window.title("Mood Playlist Generator")
window.geometry("900x500")
blacklistArtists_array = [""]

client_id = '3a5dd16e5d8c4367bc50f10853081107'
client_secret = '6174229408c24f3ea6696663273b2b97'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

mySongs = {}
blackListArtistsDict = {}
hashString = ""

def blackList():
    for i in range(0, len(blacklistArtists_array)):
        key = hash(blacklistArtists_array[i])
        blackListArtistsDict[key] = 1
        
    return(blackListArtistsDict)
    

def add_more():
    blacklistArtists_array.append(e1.get())
    #print(e1.get())   
    e1.delete(0, 'end')    

l = tk.Label(window, text = "Hi there! What's your mood today?") 
l.place(x=80, y=20)
 

v = tk.IntVar()
 
tk.Radiobutton(window, 
              text="Happy",
              variable=v, 
              value=1).place(x = 100, y = 50)
tk.Radiobutton(window, 
              text="Sad", 
              variable=v, 
              value=2).place(x = 100, y = 90)
tk.Radiobutton(window, 
              text="Party",
              variable=v, 
              value=3).place(x = 100, y = 130)
tk.Radiobutton(window, 
              text="Lonely",
              variable=v, 
              value=4).place(x = 100, y = 170)
tk.Radiobutton(window, 
              text="Old School Coool",
              variable=v, 
              value=5).place(x = 100, y = 210)
tk.Radiobutton(window, 
              text="Peace", 
              variable=v, 
              value=6).place(x = 100, y = 250)


l2 = tk.Label(window, text = "Would you like to blacklist any artists?") 
l2.place(x = 400, y = 20) 
e1 = tk.Entry(window)
e1.place(x = 440, y = 50)

    
button_add = tk.Button(window, text = 'Add', width = 15, command=add_more)
button_add.place(x = 580, y = 45)



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

array =[""]*1
array[0] = "6CdDDVPERRK6Q1o6Y7YOPo" # 90's
#array[1] = "2wjdNzVqTL0tDyIaWJQVqG" # 2000's
#array[2] = "1CFTvR6ix3w57I4xZCOekZ" # 2010's
#array[3] = "02sumE76DfbxZEfbqWqVNP" # 80's
#array[4] = "39JVQz5pR9Q4EUaPtNU9zZ" #70's
ids = getTrackIDs('Lomta', array)



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




def new_activity():
    blackList()
    mood = v.get()
    answ = []
    if mood == 1:
        # Happy - sort by energy (max to min)
        answ = sorted(tracks, key=operator.itemgetter(8), reverse = True)
    elif mood == 2:
        # Sad - sort by danceability (min to max)
        answ = sorted(tracks, key=operator.itemgetter(6))
    elif mood == 3:
        # Party - sort by danceability (max to min)
        answ = sorted(tracks, key=operator.itemgetter(6), reverse = True)    
    elif mood == 4:
        # Lonely - sort by energy(min to max)
        answ = sorted(tracks, key=operator.itemgetter(8))
    elif mood == 5:
        # Old School Cool - sort by release_date
        answ = sorted(tracks, key=operator.itemgetter(3))
    elif mood == 6:
        # Peace - sort by loudness (max to min because loudness is measured by negative numbers) 
        answ = sorted(tracks, key=operator.itemgetter(11), reverse = True)
    mood = v.get()
    song_cnt = 0
    window2 = tk.Toplevel(window)
    window2.title("Playlist")
    window2.geometry("500x500")
    for i in range(0, len(answ)):
        key = hash(answ[i][2])
        if not (key in blackListArtistsDict.keys()):
            Label1 = tk.Label(window2, text=answ[i][2]).grid(row=song_cnt, column = 0)
            Label2 = tk.Label(window2, text=answ[i][0]).grid(row=song_cnt, column = 1)
            song_cnt += 1
        if song_cnt == 20:
            break
    
button_finish = tk.Button(window, text = 'Generate playlist', command=new_activity)
button_finish.place(x = 350, y = 400)


window.mainloop()

