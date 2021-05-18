from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="kijk! ik klik op een knop!!")
	myLabel.pack()

myButton = Button(root, text="click me", command=myClick, fg="blue", bg="yellow")
myButton.pack()


root.mainloop()
