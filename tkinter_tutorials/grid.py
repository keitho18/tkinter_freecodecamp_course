from tkinter import *

root = Tk()

#Creating a label widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Keith")

#Putting the widgets into the GUI using the grid coordinates
#If there are empty grid cells, then the GUI will skip them when the GUI is displayed
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

#We need a continual loop to run the GUI
root.mainloop()

