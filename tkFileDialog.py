import os
from tkinter import *
from tkinter import filedialog

home_dir = 'D:/Study/Python/NetworkExplorer'

if os.path.isdir(home_dir):
    for path in os.listdir(home_dir):
        print(os.path.isdir(home_dir + '/' + path))

root = Tk().root.filename = filedialog.askopenfilename(initialdir = "D:/Study/Python/NetworkExplorer/images",
                                                       title = "choose your file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

