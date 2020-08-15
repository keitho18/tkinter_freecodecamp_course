from tkinter import *

root = Tk()
root.title("Simple Calculator")


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def btnAdd():
    return

def btnClick(num):
    #On delete and insert: Why is there a 0? Read and follow the link: https://stackoverflow.com/questions/50144388/python-tkinter-what-does-tkinter-end-do
    numCrt = e.get() 
    e.delete(0, END) #At position 0? the END constant refers to the position right after the last character the user entered, therefore deleting everything the user COULD have entered in the text field 
    e.insert(0, str(numCrt) + str(num)) #At line 0, position 0? Insert the number being sent from the buttons
    #Note: you're adding the strings togther in order, instead of having to add the numbers with respect to their decimal column (ones, tens, hundreds, etc.)
    
    return

def btnClear():
    e.delete(0,END)

    return

#Define buttons

btn_1 = Button(root, text=1, padx=40, pady=20, command=lambda: btnClick(1))
btn_2 = Button(root, text=2, padx=40, pady=20, command=lambda: btnClick(2))
btn_3 = Button(root, text=3, padx=40, pady=20, command=lambda: btnClick(3))
btn_4 = Button(root, text=4, padx=40, pady=20, command=lambda: btnClick(4))
btn_5 = Button(root, text=5, padx=40, pady=20, command=lambda: btnClick(5))
btn_6 = Button(root, text=6, padx=40, pady=20, command=lambda: btnClick(6))
btn_7 = Button(root, text=7, padx=40, pady=20, command=lambda: btnClick(7))
btn_8 = Button(root, text=8, padx=40, pady=20, command=lambda: btnClick(8))
btn_9 = Button(root, text=9, padx=40, pady=20, command=lambda: btnClick(9))
btn_0 = Button(root, text=0, padx=40, pady=20, command=lambda: btnClick(0))

btn_add = Button(root, text="+", padx=39, pady=20, command=lambda: btnClick(0))
btn_equal = Button(root, text="=", padx=87, pady=20, command=lambda: btnClick(0))
btn_clear = Button(root, text="Clear", padx=77, pady=20, command=btnClear)

#Display buttons

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)
btn_add.grid(row=5, column=0)
btn_equal.grid(row=4, column=1, columnspan=2)
btn_clear.grid(row=5, column=1, columnspan=2)

root.mainloop()

