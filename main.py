#Import all the necessary libraries
from tkinter import *
from PIL import ImageTk, Image
import os

#Define the tkinter instance
# win= Toplevel()
win = Tk()
win.title("Start Page")
#Define the size of the tkinter frame
win.geometry("700x450")
win.geometry('%dx%d+%d+%d' % (860, 520, 60, 45))
img =Image.open('img/back.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(win, image=bg)
label.pack()
# label.place(x = 0,y = 0)
#Define the working of the button

#========Load Start page=================
def my_command():
   # text.config(text= "You have clicked Me...")
   win.destroy()
   os.system("python FrontPage.py")

click_btn= PhotoImage(file='img/start.png')
img_label= Label(image=click_btn)

btnUsingImg= Button(win, image=click_btn,command = my_command, borderwidth=0) #,highlightthickness=0, padx=0, pady=0
btnUsingImg.pack(pady=30)
btnUsingImg.place(x=600, y=150)

exitimg= PhotoImage(file="img/exit.png")
exitlable = Label(image=exitimg)

btn = Button(win, image=exitimg,command=win.destroy)
btn.place(x=589,y=400)


win.mainloop()