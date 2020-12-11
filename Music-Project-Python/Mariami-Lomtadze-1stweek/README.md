# Task
The task for the first week was to read the text file and find the largest song, we also could write other functions in addition to this.

# My approach to the problem
Our initial text file was formated like this: artist, song_name, length. I wanted to implement mood function too so I assigned a mood value to each song.
I decided to create a nested dictionary.
myDict = {0: {'artist': 'someone', 'song_name' : 'something', 'length' : 0, 'mood' : 0}} - where 0 is a song's number in my playlist, and others are pretty obvious to give it an explanation.

# def fillDictionary():
Going through the text file's lines I used split() function and saved it in a string's array(info[]). 0-th member of array is artist's name, 1-st member is song's name, 2-nd is the length of the song, and 3-rd is the mood value.
To make sure that songs do not repeat in my dictionary I used python's built in function hash() as the same strings has the same hash value. *Hash values are just integers that are used to compare dictionary keys during a dictionary lookup quickly.*
I decided to apply hash function to the string = info[0] + info[1] + info[2]. (I could also write only info[0] + info[1], but sometimes same artist has the different version of a song and the length we help us differentiate them- (e.g Radiohead - True Love Waits))
I check if I have already this hashstring key in my dictionary(mySongs{}), and if I don't then I create one. 

To print the song with the maximum length I sort my dictionary with it's length value from longest to shortest.

# def moodList(n):
For the moodList function, I ask a user to enter their mood today (on a scale of 1 to 10) and give this int value to the function. I use for loop to go through my dictionary, and save all the songs, which mood value are n +-2 (using module function abs), in the list called moodL. ( I could print these songs without saving them in a different list, but I use this list later for blacklisting the artist).

# def blackList(blackList_artists, destination):
I couldn't decide from which list/dictionary should I delete songs, so this function works for my original dictionary as well for the mood list. That's why I give the destination string to it. 
I ask a user to enter the artist's name to blacklist them, then I go through my data and check if the artist's name is equal to blackList_artists, and delete them if it is equal.

# def printOnNewLine(lists):
I use this function to print each element of my list/dictionary on the different lines. (it looks more beautiful this way imo).
