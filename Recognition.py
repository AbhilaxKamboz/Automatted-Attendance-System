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

# face_cascade = cv2.CascadeClassifier(r'C:\Users\hp\PycharmProjects\pythonProject\.venv\haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(fname)

while True:
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.line(img, (x + 7, y - 9), (x + w - 10, y - 9), (0, 255, 0), 20)
    ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
    print(conf)
    c.execute(f"select name from users1 where id = {ids};")
    result = c.fetchall()
    name = result[0][0]
    if conf < 70:
      cv2.putText(img, name, (x + 30, y - 3), cv2.FONT_HERSHEY_DUPLEX, .6, (0, 0, 255),lineType=cv2.LINE_AA)
    else:
      cv2.putText(img, 'No Match', (x + 4, y - 3), cv2.FONT_HERSHEY_DUPLEX, .6, (255, 255, 255), lineType=cv2.LINE_AA)

  cv2.imshow('Face Recognizer',img)
  if(cv2.waitKey(1)==27):
      break;

cap.release()
cv2.destroyAllWindows()
