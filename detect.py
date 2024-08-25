import cv2
import numpy as np 
import sqlite3
import os
conn = sqlite3.connect('AttendanceDB.db')
c = conn.cursor()
fname = "recognizer/trainingData.yml"
if not os.path.isfile(fname):
  print("Please train the data first")
  exit(0)
face_cascade = cv2.CascadeClassifier(r'C:\Users\hp\PycharmProjects\pythonProject\.venv\haarcascade_frontalface_default.xml')
# face_cascade1 = cv2.CascadeClassifier('haarcascade_upperbody.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(fname)
#--------------------
while True:
  ret, img = cap.read()
  # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    ids,conf = recognizer.predict(img[y:y+h,x:x+w])
    c.execute(f"select name from users1 where id = {ids};")

    result = c.fetchall()
    name = result[0][0]
    if conf < 72:
      # if ids == a:
      cv2.putText(img, name, (x+2,y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
      # else:
      #  cv2.putText(img, name, (x+2,y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
    else:
      cv2.putText(img, 'No Match', (x+2,y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
  cv2.imshow('Face Recognizer',img)
  #k = cv2.waitKey(30) & 0xff
  if(cv2.waitKey(1)==ord('q') or cv2.waitKey(1)==27):
      break;

cap.release()
cv2.destroyAllWindows()
