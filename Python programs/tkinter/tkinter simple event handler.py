#Usage of classes in tkinter

from tkinter import *

class butt:

    def __init__(self,master):#here master is call by value of the variable root
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame , text = "print it",command = self.printMessage)
        self.printButton.pack(side = LEFT)

    def printMessage(self):
        print("this actually works")


root = Tk()#main function 
b = butt(root)#object of the class
root.mainloop()
