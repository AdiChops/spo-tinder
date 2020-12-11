import csv
import pandas as pd

tracks = []

'''
parameters in: file name(string)
returns: nested list with song info
'''
def readData(file_name):
    df = pd.read_csv(file_name)
    for i in range(0, len(df)):
        track = []
        track.append(df['name'][i])
        track.append(df['artist'][i])
        track.append(df['release_date'][i])
        track.append(df['length'][i])
        track.append(df['popularity'][i])
        track.append(df['danceability'][i])
        track.append(df['acousticness'][i])
        track.append(df['energy'][i])
        track.append(df['instrumentalness'][i])
        track.append(df['liveness'][i])
        track.append(df['loudness'][i])
        track.append(df['speechiness'][i])
        track.append(df['tempo'][i])
        track.append(df['time_signature'][i])
        tracks.append(track)
    return tracks
    
readData('spotify.csv')




