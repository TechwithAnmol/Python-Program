 #simple program to determine type of events
from tkinter import *
mainwindow = Tk()

def leftclick(event):
    print("left")


def rightclick(event):
    print("right")

frame = Frame(mainwindow, width=300, height=250)
frame.bind("<Button-1>", leftclick)

frame.bind("<Button-3>", rightclick)
frame.pack()

mainwindow.mainloop()
