In this file, I uploaded two python files.
spotifyapi.py - is a code for getting track information from the spotify's playllist using Spotipy (Python library for the Spotify Web API). Track information includes: name, album, artist, release_date, length, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature.
This code saves data in a list and also creates csv file and writes in it. 

GUI1.py - is a code for a mood playlist generator (with blacklisting function) using Tkinter (GUI framework).
For this code, I used spotifyapi.py but I don't create file to save info anymore. I work direcrly on the tracks list. For the blacklisting function I hash the artist's name use dictionary. While creating playlist I check if the hash(artist's_name) is a key in my dictionary, if yes, then I don't include the song in my playlist.



*To generate your own client_id and client_secret you have to make spotify's developer account.* 


GUI2.py - is an updated version of GUI1. I added 'tinder' elemnts(swipe left/right) to it as we discussed. Swiping happens by using left/right arrow keys (is it what those are called?). I added leftkey, rightkey, and printAnsw functions.

leftkey function will switch label text to the next song's name and artist's name. Also, will delete current song from the answ list, since it was swiped left.

rightkey function will switch label text to the next song's name and artist's name. Also, will raise the value of song_cnt_right by 1. The swiping will be possible before song_cnt_right becomes equal to 7. Which means our final list will contain 7 songs. (We can definetely change the amount of songs, it was just the first number that came to my mind).

printAnsw function will print the table of the songs that were swiped right and the artists names.
