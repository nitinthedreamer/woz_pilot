from tkinter import *
from sys import exit
def popupError(s):
    popupRoot = Tk()
    popupRoot.after(2000, exit)
    popupButton = Button(popupRoot, text = s, font = ("Verdana", 12), bg = "yellow", command = exit)
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()

# popupError('Hello!')

from tkinter import *

def button_click():
    print(textbox.get())

root = Tk()

textbox = Entry(root, width=30)
textbox.pack()

button = Button(root, text="Click me!", command=button_click)
button.pack()

root.mainloop()
