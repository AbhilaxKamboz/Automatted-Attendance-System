#Import all the necessary libraries

from tkinter import *
from PIL import ImageTk, Image
import os

#Define the tkinter instance
# win= Toplevel()
win = Tk()
win.title("Start Page")
#Define the size of the tkinter frame
win.geometry("1500x720")
win.geometry('%dx%d+%d+%d' % (1000, 630, 100, 10))
img =Image.open('img/start/start.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(win, image=bg)
label.pack()
# label.place(x = 0,y = 0)
#Define the working of the button

#========Load Start page=================
def my_command():
   # text.config(text= "You have clicked Me...")
   win.destroy()
   os.system("python homepge.py")
def aboutfn():
   win.destroy()
   import cv2
   img = ['about.png', 'about1.png', 'about2.png']
   for i in img:
      img1 = cv2.imread("img/" + i)
      cv2.imshow("About", img1)
      cv2.waitKey(1500)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   os.system("Python main.py")

about = PhotoImage(file='img/start/about.png')
btn1 = Button(win, image=about,command=aboutfn)
btn1.place(x=655,y=227)

click_btn= PhotoImage(file='img/start/startbtn.png')
img_label= Label(image=click_btn)

btnUsingImg= Button(win, image=click_btn,command = my_command) #,highlightthickness=0, padx=0, pady=0
btnUsingImg.pack(pady=30)
btnUsingImg.place(x=651, y=363)

exitimg= PhotoImage(file="img/start/exit.png")
exitlable = Label(image=exitimg)

btn = Button(win, image=exitimg,command=win.destroy)
btn.place(x=655,y=522)


win.mainloop()