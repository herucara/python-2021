from tkinter import *
window = Tk()
window.title('foto')
window = Canvas(window,width = 500, heigth = 500)
window.pack()
my_image = PhotoImage(file='D:\\Nieuwe map\\DCIM\\102APPLE.png')
window.create_image(0, 0, anchor = NW, image=my_image)

window.mainloop