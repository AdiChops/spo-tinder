import beautiful_soup

def get_artists():
    music = open('Music.txt', 'r')
    line = music.readline().strip()
    artists = []
    while line != '':
        song = line.split("~")
        # The second index is the artists
        artists.append(song[1])
        line = music.readline().strip()
    artists = list(dict.fromkeys(artists)) # removing duplicates
    return artists

print(get_artists())
