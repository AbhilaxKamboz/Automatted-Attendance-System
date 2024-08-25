from tkinter import *
from PIL import Image,ImageTk
import os

root =Tk()

# root.configure(background="skyblue")
root.title("Automated Attendance System")
mainClr= "maroon"
burronClr="#0D47A1"
root.geometry("700x570")
root.geometry('%dx%d+%d+%d' % (1000, 630, 100, 10))
image_path = "img/homepage/back.png"
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)

# Create a label to hold the image and place it at the bottom layer
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Functions
def frontPage():
    import cv2
    # import playsound
    img = cv2.imread("img/homepage/homepage.jpg")
    cv2.imshow("Main Page",img)
    cv2.waitKey(1000)
    img1=cv2.imread("img/homepage/Homepage1.jpg")
    cv2.imshow("Main Page",img1)
    cv2.waitKey(1000)
    # playsound.playsound('voice/start.mp3')
    cv2.destroyAllWindows()
def createTable():
    os.system("python createDataBase.py")

def captureSample():
    os.system("python captureRecord.py")

def deleteSamples():
    import shutil
    shutil.rmtree("dataset/")
    print("Sampples Deleted Sucess...")

def trainModel():
    os.system("python training.py")

def recognition():
    os.system("python Recognition.py")

def markattendance():
    os.system("python Attendance.py")

def viewAttendance():
    os.system("Attendance.csv")

def report():
    os.system("20232028Synopsis.pdf")

def flowChart():
    import cv2
    img = ['flowChart1.png','flowChart2.png','flowChart3.png','flowChart4.png','flowChart5.png','flowChart6.png',
           'flowChart7.png','flowChart8.png','flowChart.png']
    for i in img:
        img1 = cv2.imread("img/"+i)
        cv2.imshow("Flowchart",img1)
        cv2.waitKey(500)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def about():
    import cv2
    img =['about.png','about1.png','about2.png']
    for i in img:
        img1= cv2.imread("img/"+i)
        cv2.imshow("About",img1)
        cv2.waitKey(1500)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Add Buttons
createDB = PhotoImage(file='img/homepage/createDB.png')
btn1 = Button(root, image=createDB,command=createTable)
btn1.place(x=61,y=80)

capture = PhotoImage(file='img/homepage/captureSample.png')
btn1 = Button(root, image=capture,command=captureSample)
btn1.place(x=350,y=80)

delete = PhotoImage(file='img/homepage/deleteSample.png')
btn1 = Button(root, image=delete,command=deleteSamples)
btn1.place(x=61,y=200)

train = PhotoImage(file='img/homepage/trainModel.png')
btn1 = Button(root, image=train,command=trainModel)
btn1.place(x=350,y=200)

recognise = PhotoImage(file='img/homepage/recognizeFace.png')
btn1 = Button(root, image=recognise,command=recognition)
btn1.place(x=61,y=400)

markattendance1 = PhotoImage(file='img/homepage/markAttendance.png')
btn1 = Button(root, image=markattendance1,command=markattendance)
btn1.place(x=350,y=400)

viewreport = PhotoImage(file='img/homepage/viewReport.png')
btn1 = Button(root, image=viewreport,command=report)
btn1.place(x=61,y=480)

viewAttendance1 = PhotoImage(file='img/homepage/vierAttendance.png')
btn1 = Button(root, image=viewAttendance1,command=viewAttendance)
btn1.place(x=350,y=480)

flow = PhotoImage(file='img/homepage/flowchart.png')
btn1 = Button(root, image=flow,command=flowChart)
btn1.place(x=185,y=550)

about1 = PhotoImage(file='img/homepage/about.png')
btn1 = Button(root, image=about1,command=about)
btn1.place(x=860,y=50)

exit1 = PhotoImage(file='img/homepage/exit.png')
btn1 = Button(root, image=exit1,command=root.destroy)
btn1.place(x=860,y=580)


frontPage()
root.mainloop()