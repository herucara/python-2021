from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
#e.insert(0, "schrijf je naam")


def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()

myButton = Button(root, text="schrijf je naam", command=myClick, fg="blue", bg="yellow")
myButton.pack()


root.mainloop()
