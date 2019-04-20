import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import urllib.request
import os


#rag map 130px/130px
#definig constants
URL = 'http://pkinoko.web.fc2.com/ro/bb/'
directory = os.path.dirname(os.path.realpath(__file__)) + '/MapImages/'
if not os.path.exists(directory):
    os.makedirs(directory)


#setting frames
win = tk.Tk()
mainFrame = Frame(win, width = 200, height = 200)
mainFrame.pack()
buttonFrame = Frame(win,  width = 200, height = 200)
buttonFrame.pack(side = BOTTOM)
listFrame = Frame(win)
listFrame.pack(side = BOTTOM)

def transparent(evt):
    if not var.get():
        win.attributes('-alpha', 0.3)
    else:
        win.attributes('-alpha', 1)



def mapGetter(evt):
    mapName = mapOptions.get(mapOptions.curselection()[0])
    fullURL = URL + mapName + '.gif'
    mapFilename = directory + mapName + '.png'
    print(fullURL)
    print(mapFilename)
    if not os.path.exists(mapFilename):
        try:
            urllib.request.urlretrieve(fullURL, mapFilename)
            print('successfully got map: ' + mapName)
        except:
            print('error getting map: ' + map)
            mapLabel("Map not found", "The selected map was not found")

    else:
        print('this map is already in the directory')

    mapDirectory = 'MapImages/' + mapName + '.png'
    map = Image.open(mapDirectory)
    map = map.resize((130, 130), Image.ANTIALIAS)
    mapImage = ImageTk.PhotoImage(map)
    mapLabel.configure(image = mapImage)
    mapLabel.image = mapImage


mapLabel = tkinter.Label(mainFrame)
logo = PhotoImage(file="Logo.png")
mapLabel.configure(image = logo)
mapLabel.image = logo
mapOptions = Listbox(listFrame, width=20, height=5)
scroll = Scrollbar(listFrame, orient="vertical")
mapOptions.config(yscrollcommand=scroll.set)
scroll.config(command=mapOptions.yview)

getMap = Button(buttonFrame, text = 'Select map')
getMap.bind('<ButtonRelease-1>', mapGetter)
var = tk.BooleanVar()
var.set(FALSE)
transparentCheck = Checkbutton(buttonFrame, text = 'transparent?', var = var)
transparentCheck.bind('<ButtonRelease-1>', transparent)


#loading all maps with gutter lines
f = open('MapImages/allMaps.txt')
allMaps = f.read().splitlines()

for map in allMaps:
    mapOptions.insert(END, map)

win.wm_attributes("-topmost", 1)
#win.attributes('-alpha', 0.3)

win.title('GLviewer')


scroll.pack(side="right", fill="y")
mapOptions.pack(side="left", fill="y")
mapLabel.pack()
getMap.pack()
transparentCheck.pack()
win.mainloop()
