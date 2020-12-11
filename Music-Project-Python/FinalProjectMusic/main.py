import importlib
import tkinter as tk
import time
import operator

tracks = []
answ = []
modname = "readcsv"
funcname = "readData"

#write songs data in spotify.csv
modname2 = "writecsv"
module2 = importlib.import_module(modname2)

#save data in list (tracks) from csv file
module = importlib.import_module(modname)
func = getattr(module,funcname)
tracks = func('spotify.csv')


# GUI
window = tk.Tk()
window.title("Mood Playlist Generator")
window.geometry("900x500")

l = tk.Label(window, text = "Hi there! What's your mood today?") 
l.place(x=80, y=20)

# select mood buttons
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


song_cnt = 0
song_cnt_right = 0 # amount of right swipes

blacklistArtists_array = [""]

# blacklist artist - goes through the blacklisted artists list and deletes their songs from the main tracks list. 
def blackList():
    for i in range(0, len(blacklistArtists_array)):
        ind = 0
        while ind < len(tracks):
            if tracks[ind][2] == blacklistArtists_array[i]:
                tracks.pop(ind)
            else:
                ind += 1
    
#add more artists to blacklist - gets user input string
def add_more():
    blacklistArtists_array.append(e1.get())  
    e1.delete(0, 'end')    

button_add = tk.Button(window, text = 'Add', width = 15, command=add_more)
button_add.place(x = 580, y = 45)

# prints final list of right swipe songs    
def printAnsw():
    global answ
    global l3
    global l4
    global window2
    l3.after(100, l3.destroy)
    l4.after(100, l4.destroy)

    for i in range(0, song_cnt_right):
        Label1 = tk.Label(window2, text=answ[i][2]).grid(row=i, column = 0)
        Label2 = tk.Label(window2, text=answ[i][0]).grid(row=i, column = 1)   

      
def leftkey(event):
    global song_cnt 
    global window2
    global answ
    global l3
    global l4
    l3.after(100, l3.destroy)
    l4.after(100, l4.destroy)
    answ.pop(song_cnt)
    #song_cnt += 1
    l3 = tk.Label(window2, text = answ[song_cnt][0]) 
    l4 = tk.Label(window2, text = answ[song_cnt][2])
    l3.place(x = 340, y = 200) 
    l4.place(x = 340, y = 230)

def rightkey(event): 
    global song_cnt 
    global window2
    global answ
    global l3
    global l4
    global song_cnt_right
    l3.after(100, l3.destroy)
    l4.after(100, l4.destroy)
    song_cnt += 1
    song_cnt_right += 1
    l3 = tk.Label(window2, text = answ[song_cnt][0]) 
    l4 = tk.Label(window2, text = answ[song_cnt][2])
    l3.place(x = 340, y = 200) 
    l4.place(x = 340, y = 230)
    if song_cnt_right == 7:
        l3.after(100, l3.destroy)
        l4.after(100, l4.destroy)
        window2.unbind('<Left>')
        window2.unbind('<Right>')
        printAnsw()
        song_cnt_right = 0
    
    
def new_activity():
    blackList()
    global song_cnt_right
    song_cnt_right = 0
    mood = v.get()
    global answ
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
    global song_cnt
    song_cnt = 0
    global window2
    global l3
    global l4
    window2 = tk.Toplevel(window)
    window2.title("Playlist")
    window2.geometry("900x500")
    window2.bind('<Left>', leftkey)
    window2.bind('<Right>', rightkey)
    window2.after(1, lambda: window2.focus_force())
    l3 = tk.Label(window2, text = answ[song_cnt][0]) 
    l4 = tk.Label(window2, text = answ[song_cnt][2])
    l3.place(x = 340, y = 200) 
    l4.place(x = 340, y = 230)

    l5 = tk.Label(window2, text = "Press right arrow if you want the song to be added to your playlist, press left arrow if you don't")
    l5.place(x = 50, y = 20)
    l5.after(4000, l5.destroy)
    
    
button_finish = tk.Button(window, text = 'Generate playlist', command=new_activity)
button_finish.place(x = 350, y = 400)

window.mainloop()


 
