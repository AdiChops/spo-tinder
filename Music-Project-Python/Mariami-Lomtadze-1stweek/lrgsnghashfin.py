import operator
import copy
songdata = open('Blacklist.txt')

myDict = {0: {'artist': 'someone', 'song_name' : 'something', 'length' : 0, 'mood' : 0}}
blackListedDict = {0: {'artist': 'someone', 'song_name' : 'something', 'length' : 0, 'mood' : 0}}
mySongs = {}
moodL = []

def moodList(n):
    listLen = 0
    for i in range(1, len(myDict)):
        if abs(myDict[i]['mood'] - n) <= 2:
            moodL.append([])
            moodL[listLen] = myDict[i]
            listLen += 1
            
 
def blackList(blackList_artists, destination):
    if destination == "original":
        blackListedDict = copy.deepcopy(myDict)
        for i in range(1, len(blackListedDict)):
            if blackListedDict[i]['artist'] == blackList_artists:
                del(blackListedDict[i])
        return(blackListedDict)
    elif destination == "mood list":
        i = 0
        while i < len(moodL):
            if moodL[i]['artist'] == blackList_artists:
                moodL.remove(moodL[i])
            else:
                i += 1
        return(moodL)
        


def fillDictionary():
    songcnt = 0
    for line in songdata:
        hashstring = ""
        info = line.split(", ")
        info[len(info)-1] = info[len(info)-1].replace(",","");

        hashstring = info[0] + info[1] + info[2]
        key = hash(hashstring)
        if not (key in mySongs.keys()):
            songcnt += 1
            mySongs[key] = 1
            myDict[songcnt] = {}
            myDict[songcnt]['artist'] = info[1]
            myDict[songcnt]['song_name'] = info[0]
            myDict[songcnt]['length'] = float(info[2])
            myDict[songcnt]['mood'] = int(info[3])
   

def printOnNewLine(lists):
    for i in lists:
        print(i)
        
def main():
    fillDictionary()
    
    # Sort to get the largest song
    res = sorted(myDict.items(), key = lambda x: x[1]['length'], reverse = True)
    print(res[0][1])
    #print(myDict)
    
    # Mood Playlist
    mood = int(input("On a scale of 1(very sad) to 10 (very happy), what is your mood today? "))
    moodList(mood)
    printOnNewLine(moodL)

    
    # Blacklist playlist (delete from original playlist/ mood playlist)
    blackListArtists = input("Please enter the artist name to remove from the playlist: ") 
    printOnNewLine(blackList(blackListArtists, "mood list"))
    

             
main()