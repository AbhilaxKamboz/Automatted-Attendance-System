import cv2
import numpy as np 
import sqlite3
import os
import playsound
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('AttendanceDB.db')
c = conn.cursor()
if not os.path.exists('./dataset'):
  os.makedirs('./dataset')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# name feild
root = Tk()
root.configure(background="white")
# -------------------------------------------
def getInput1():
  global uname
  inputValue = textBox.get("1.0","end-1c")
  if inputValue != "":
    uname = inputValue
  else:
    print('Please enter the name. it is mandatory')
    root.withdraw()
    messagebox.showwarning("Warning", "Please enter the name. It is mandatory field...")
    exit()
  print(inputValue)
  root.destroy()

L1 = Label(root, text = 'Enter Your Name : ',font=("times new roman",12))
L1.pack()
textBox = Text(root, height=1, width = 20,font=("times new roman",12),bg="Pink",fg='Red')
textBox.pack()
textBox.focus()
buttonSave = Button(root, height = 1, width = 10,font=("times new roman",12), text = "Save", command = lambda:getInput1())
buttonSave.pack()
mainloop()

cap = cv2.VideoCapture(0)
str1 = f"INSERT INTO users1 (name) VALUES ('{uname}') "
print(str1)
c.execute(str1)
uid = c.lastrowid
sampleNum = 0
while True:
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    sampleNum = sampleNum+1
    cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.waitKey(100)
  cv2.imshow('img',img)
  cv2.waitKey(1);
  if sampleNum >= 20:
    break
print("\nSamples captured successfully...")
playsound.playsound('voice/sound.mp3')

cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()
messagebox.showinfo("Data","Samples captured successfully....")
