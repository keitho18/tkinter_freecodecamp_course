from tkinter import *

def myClick():
    myLabel = Label(root, text="Button clicked")
    myLabel.pack()

root = Tk()

#myBtn = Button(root, text="Click Me", state=DISABLED) -> This disables the button from being used
myBtn = Button(root, text="Click Me", padx = 50, pady = 50, command=myClick, fg="blue", bg="green")
#Note: it keeps ADDING the output of the function it calls. How can you erase these or refresh the root?
myBtn.pack()

root.mainloop()

