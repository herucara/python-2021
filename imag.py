from tkinter import *

from PIL import ImageTk,Image

root = Tk()
root.title('leer coderen bij Codemy.com')
root.iconbitmap('c:/gui/')


button_quit = Button(root, text="exit program", command=root.quit)
button_quit.pack()

#my_img1 = ImageTk.PhotoImage(Image.open("IMG_1136.png"))
#my_img2 = ImageTk.PhotoImage(Image.open("IMG_3207.png"))
my_img = ImageTk.PhotoImage(Image.open("IMG_2004.png"))

#image_list = [my_img1, my_img2, my_img3]

my_label = Label(image=my_img)
my_label.pack()
#def forward(image_number):
#	global my_label
#	global button_forward
#	global button_back

#	my_label.grid_forget()
#	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 5:
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)






root.mainloop()