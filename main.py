import os
from pathlib import Path
import re
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import messagebox

root = tk.Tk()
imgs = []
noDups = []
sortJPG = []
sortNEF = []
notSupported = []
seen = set()

def addImg():
    #removes previous entries
    for widget in frame.winfo_children():
        widget.destroy()

    #opens file explorer and appends img with the files opened
    filenames = filedialog.askopenfilenames(initialdir="/", title="Select Files", filetypes=(("image files", ".jpg .nef"),("JPEG files", "*.jpg"),("NEF files","*.nef")))
    for file in filenames:
        imgs.append(file)
    imgs.sort()

    #removes duplicate tuples from imgs and puts them in noDups
    for lst in imgs:
        current = tuple(lst)
        if current not in seen:
            noDups.append(lst)
            seen.add(current)
    noDups.sort()
    print(noDups)

    #output noDups to the gui
    for x in noDups:
        label = tk.Label(frame, text=x, bg="gray")
        label.pack()

def clear():
    #removes previous entries
    for widget in frame.winfo_children():
        widget.destroy()

    imgs = tuple()
    noDups = tuple()
    sortJPG = tuple()
    sortNEF = tuple()
    notSupported = tuple()

    for x in noDups:
        label = tk.Label(frame, text=x, bg="gray")
        label.pack()
    for x in imgs:
        label = tk.Label(frame, text=x, bg="gray")
        label.pack()


def namechange():
    #sorts files into .jpg and .nef
    for x in noDups:
        #current = tuple(x)
        if 'JPG' in str(x):
            sortJPG.append(x)
        elif 'NEF' in str(x):
            sortNEF.append(x)
        else:
            notSupported.append(x)

    #organisingg
    sortJPG.sort()
    sortNEF.sort()
    notSupported.sort()
    file = fileName.get()

    #actually changing name
    number = (0)
    for x in sortJPG:
        p = Path(x)
        print(p.parent)
        fTitle, fExt = os.path.splitext(x)
        print(fExt)
        number = str(number).zfill(4)
        finalName = ('{}\{}-{}{}'.format(p.parent, file, number, fExt))
        print(finalName)
        os.rename(x, finalName)
        number = int(number)
        number = number + 1
    number = (0)
    for x in sortNEF:
        p = Path(x)
        print(p.parent)
        fTitle, fExt = os.path.splitext(x)
        print(fExt)
        number = str(number).zfill(4)
        finalName = ('{}\{}-{}{}'.format(p.parent, file, number, fExt))
        print(finalName)
        os.rename(x, finalName)
        number = int(number)
        number = number + 1


#gui elements
canvas = tk.Canvas(root, height=700, width=700, bg="#cebfd6")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.7, relwidth=0.9, relx=0.05, rely=0.05)

openImg = tk.Button(root, text="Open Images", padx=10, pady=10, fg="white", bg="#cebfd6", command=addImg)
openImg.pack()

clear = tk.Button(root, text="Clear", padx=10, pady=10, fg="white", bg="#cebfd6", command=clear)
clear.pack()

header = tk.Label(root, text="Set image name to:")
header.pack()

fileName = tk.Entry(root, width = 50, bg="#cebfd6")
fileName.pack()

run = tk.Button(root, text="RUN", padx=10, pady=10, fg="white", bg="#cebfd6", command=namechange)
run.pack()
warning = tk.Label(frame, text="WARNING: If any special characters are inside of the 'Set image name' Field, please DO NOT run the program! ", bg="red")
warning.pack()

root.mainloop()
