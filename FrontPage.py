from tkinter import *
from PIL import Image,ImageTk
import os

root =Tk()

# root.configure(background="skyblue")
root.title("Automated Attendance System")
mainClr= "maroon"
burronClr="#0D47A1"
root.geometry("700x570")
# root.geometry('%dx%d+%d+%d' % (1000, 630, 100, 10))
image_path = "img/faceback.png"
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
        cv2.waitKey(1000)
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

def main():

#Creating lables
    Label(root,text="AUTOMATIC ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg=mainClr,height=2
          ).grid(row=0,rowspan=2,columnspan=4,sticky=N+S+E+W,padx=5,pady=5)
    Label(root,text="USER ENROLMENT",font=("Times new roman",20),fg="white",bg="red"
          ).grid(row=3,columnspan=4,sticky=N+S+E+W,padx=5,pady=5)
    #Buttons
    # 1
    Button(root, text="Create Database/Reset Data",font=("times new roman",20),fg="white",bg=burronClr,command=createTable
           ).grid(row=5,column=0,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    # 2
    Button(root, text="Capture Sample of New User",font=("times new roman",20),fg="white",bg=burronClr,command=captureSample
           ).grid(row=5,column=2,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    # 3
    Button(root, text="Delete Previous Samples",font=("times new roman",20),fg="white",bg=burronClr,command=deleteSamples
           ).grid(row=6,column=0,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    # 4
    Button(root, text="Train Model for new FACES",font=("times new roman",20),fg="white",bg=burronClr,command=trainModel
           ).grid(row=6,column=2,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    #Intermediate Lable
    Label(root,text="Recognize Person and Mark their Attendance",font=("times new roman",20),fg="white",bg="red"
          ).grid(row=7,columnspan=4,sticky=N+S+E+W,padx=5,pady=5)
    #Buttons
    # 5
    Button(root,text="Recognize Faces",font=("times new roman",20),fg="white",bg=burronClr,command=recognition
           ).grid(row=8,column=0,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    # 6
    Button(root,text="Mark Attendance",font=("times new roman",20),fg="white",bg=burronClr,command=markattendance
           ).grid(row=8,column=2,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    # 7
    Button(root,text="View Attendance in CSV",font=("times new roman",20),fg="white",bg=burronClr,command=viewAttendance
           ).grid(row=9,column=0,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    # 8
    Button(root,text="Generate Report",font=("times new roman",20),fg="white",bg=burronClr,command=report
           ).grid(row=9,column=2,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    # 9
    Button(root,text="Flowchart & Working Steps",font=("times new roman",20),fg="white",bg=burronClr,command=flowChart
           ).grid(row=10,column=0,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    # 10
    Button(root,text="About Us",font=("times new roman",20),fg="white",bg=burronClr,command=about
           ).grid(row=10,column=2,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
    # 11 for exit
    Button(root,text="Exit",font=("times new roman",20),fg="white",bg=mainClr,command=root.destroy
           ).grid(row=11,columnspan=4,sticky=N+S+E+W,padx=5,pady=5)

frontPage()
main()
root.mainloop()
