from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5) #can change bg and fg as well
e.pack()
e.insert(0, "Enter username...") #Inserts default text INSIDE the text field

def myClick():
    username = e.get()
    myLabel = Label(root, text=username) #This will take the string from the entry field
    myLabel.pack()

myBtn = Button(root, text="Enter", padx = 50, pady = 50, command=myClick)
myBtn.pack()

root.mainloop()

