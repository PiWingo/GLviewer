import tkinter as tk
from tkinter import *

#definig constants
URL = 'http://pkinoko.web.fc2.com/ro/bb/'

#defining widgets
win = tk.Tk()
mapView = Canvas()


f = open('allMaps.txt')
allMaps = f.read().splitlines()

win.wm_attributes("-topmost", 1)
win.attributes('-alpha', 0.1)

win.title('GLviewer')




mapView.pack()
win.mainloop()
