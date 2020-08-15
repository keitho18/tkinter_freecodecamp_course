from tkinter import *

root = Tk()

#Creating a label widget
myLabel = Label(root, text="Hello World")

#Putting the widget into the GUI
myLabel.pack()

#We need a continual loop
root.mainloop()