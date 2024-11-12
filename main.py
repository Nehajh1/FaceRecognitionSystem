from tkinter import* from tkinter import ttk
from PIL import Image,ImageTk import tkinter
import os

from student import Student

from attendance import Attendance from train import Train
from help import Help

from face_recognition import Face_Recognition class Face_Recognition_System:
def _init_(self,root):

self.root=root self.root.geometry("1530x800+0+0") self.root.title("Face Recognition System")
# ================ Image1 ===================

img=Image.open("images/BestFacialRecognition.jpg") img=img.resize((440,140),Image.ANTIALIAS) self.photoimage=ImageTk.PhotoImage(img) lbl_img=Label(self.root,image=self.photoimage) lbl_img.place(x=0,y=0,width=440,height=140) img1=Image.open("images/face_recognition.png") img1=img1.resize((440,140),Image.ANTIALIAS) self.photoimage1=ImageTk.PhotoImage(img1)
 
lbl_img=Label(self.root,image=self.photoimage1) lbl_img.place(x=440,y=0,width=440,height=140) img2=Image.open("images/images.jpg") img2=img2.resize((440,140),Image.ANTIALIAS) self.photoimage2=ImageTk.PhotoImage(img2) lbl_img=Label(self.root,image=self.photoimage2) lbl_img.place(x=880,y=0,width=440,height=140) # background image img3=Image.open("images/bg_image.jpg") img3=img3.resize((1330,610),Image.ANTIALIAS) self.photoimage3=ImageTk.PhotoImage(img3) bg_img=Label(self.root,image=self.photoimage3) bg_img.place(x=0,y=140,width=1330,height=610)
lbl_title=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")

lbl_title.place(x=0,y=140,width=1430,height=35)



# student button img4=Image.open("images/student.jpg") img4=img4.resize((160,160),Image.ANTIALIAS) self.photoimage4=ImageTk.PhotoImage(img4)
b1=Button(bg_img,image=self.photoimage4,command=self.student_details,cursor="hand2") b1.place(x=200,y=80,width=160,height=160)
b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")

b1_1.place(x=200,y=240,width=160,height=30) # detect face button img5=Image.open("images/face_detector1.jpg")
img5=img5.resize((160,160),Image.ANTIALIAS) self.photoimage5=ImageTk.PhotoImage(img5) b1=Button(bg_img,image=self.photoimage5,cursor="hand2",command=self.face_data) b1.place(x=450,y=80,width=160,height=160)
 
b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

b1_1.place(x=450,y=240,width=160,height=30) # attendance button img6=Image.open("images/report.jpg")
img6=img6.resize((160,160),Image.ANTIALIAS) self.photoimage6=ImageTk.PhotoImage(img6) b1=Button(bg_img,image=self.photoimage6,cursor="hand2",command=self.attendance_data) b1.place(x=700,y=80,width=160,height=160)
b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

b1_1.place(x=700,y=240,width=160,height=30) # help desk button img7=Image.open("images/help.jpg")
img7=img7.resize((160,160),Image.ANTIALIAS) self.photoimage7=ImageTk.PhotoImage(img7) b1=Button(bg_img,image=self.photoimage7,cursor="hand2",command=self.help_data) b1.place(x=950,y=80,width=160,height=160)
b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

b1_1.place(x=950,y=240,width=160,height=30) # train data button img8=Image.open("images/train.jpg")
img8=img8.resize((160,160),Image.ANTIALIAS) self.photoimage8=ImageTk.PhotoImage(img8) b1=Button(bg_img,image=self.photoimage8,cursor="hand2",command=self.train) b1.place(x=200,y=300,width=160,height=160)
b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

b1_1.place(x=200,y=460,width=160,height=30) # photos button img9=Image.open("images/data_train.jpg")
img9=img9.resize((160,160),Image.ANTIALIAS)
 
self.photoimage9=ImageTk.PhotoImage(img9) b1=Button(bg_img,image=self.photoimage9,cursor="hand2",command=self.open_img) b1.place(x=450,y=300,width=160,height=160)
b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

b1_1.place(x=450,y=460,width=160,height=30) # developer button img10=Image.open("images/team.jpg")
img10=img10.resize((160,160),Image.ANTIALIAS) self.photoimage10=ImageTk.PhotoImage(img10) b1=Button(bg_img,image=self.photoimage10,cursor="hand2") b1.place(x=700,y=300,width=160,height=160)
b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") b1_1.place(x=700,y=460,width=160,height=30)
# exit button img11=Image.open("images/exit.jpg")
img11=img11.resize((160,160),Image.ANTIALIAS) self.photoimage11=ImageTk.PhotoImage(img11) b1=Button(bg_img,image=self.photoimage11,cursor="hand2",command=self.Exit) b1.place(x=950,y=300,width=160,height=160)
b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.Exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white") b1_1.place(x=950,y=460,width=160,height=30)
# ====================function open image================ def open_img(self):
os.startfile("data") def Exit(self):
self.Exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root) if self.Exit>0:
self.root.destroy() else:
return

# ===========Function Buttons==================
 
def student_details(self): self.new_window=Toplevel(self.root) self.app=Student(self.new_window)
def train(self): self.new_window=Toplevel(self.root) self.app=Train(self.new_window)
def face_data(self): self.new_window=Toplevel(self.root) self.app=Face_Recognition(self.new_window)
def help_data(self): self.new_window=Toplevel(self.root) self.app=Help(self.new_window)
def attendance_data(self): self.new_window=Toplevel(self.root) self.app=Attendance(self.new_window)
if _name_ == '_main_': root=Tk()
obj=Face_Recognition_System(root)

 
root.mainloop()
