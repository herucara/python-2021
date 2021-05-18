from tkinter import *

from PIL import ImageTk, Image

root = Tk()
root.title('leer coderen bij Codemy.com')
root.iconbitmap('c:/gui/ ')

my_img1 = ImageTk.PhotoImage(Image.open("IMG_1136.png"))
my_img2 = ImageTk.PhotoImage(Image.open("IMG_2004.png"))

#image_list = [my_img1, my_img2]

#my_label = Label(image=my_img1)
#my_label.grid(row=0, column=0, columnspan=3) 
#my_label.pack()

button_back = Button(root, "<<")
button_exit = Button(root, text="exit program", command=root.quit)
button_forward = Button(root, text=">>")


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1) 
button_forward.grid(row=1, column=2) 



#button_quit = Button(root, text="exit program", command=root.quit)
#button_quit.pack()


root.mainloop()