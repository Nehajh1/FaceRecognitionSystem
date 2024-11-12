from tkinter import* from tkinter import ttk
from PIL import Image,ImageTk from tkinter import messagebox from time import strftime
from datetime import datetime import mysql.connector import cv2
 
import os

import numpy as np class Face_Recognition:
def _init_(self,root):

self.root=root self.root.geometry("1530x800+0+0") self.root.title("Face Recognition System")
# ===============title=====================

lbl_title=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="green") lbl_title.place(x=0,y=0,width=1430,height=35)


# ==============1st image===================

img_top=Image.open("images/face_detector1.jpg") img_top=img_top.resize((630,580),Image.ANTIALIAS) self.photoimage_top=ImageTk.PhotoImage(img_top) lbl_img=Label(self.root,image=self.photoimage_top) lbl_img.place(x=0,y=40,width=630,height=580)
# ==============2nd image===================

img_bottom=Image.open("images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3- 100740902-large.jpg")

img_bottom=img_bottom.resize((700,580),Image.ANTIALIAS) self.photoimage_bottom=ImageTk.PhotoImage(img_bottom) lbl_img=Label(self.root,image=self.photoimage_bottom) lbl_img.place(x=630,y=40,width=700,height=580)
# =====================button=====================

b1_1=Button(lbl_img,text="Face Recognition",command=self.face_rec,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")

b1_1.place(x=250,y=510,width=200,height=40) #================attendance=======================
def mark_attendance(self,i,r,n,d):

with open("attendance.csv","r+",newline="\n") as f: myDataList=f.readlines()
name_list=[]
 
for line in myDataList:

entry=line.split((",")) name_list.append(entry[0])
if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ): now=datetime.now()
d1=now.strftime("%d/%m/%Y") dtString=now.strftime("%H:%M:%S") f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
#=============face recognition=============== def face_rec(self):
def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf): gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors) coord=[]
for(x,y,w,h) in features:

cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) id,predict=clf.predict(gray_image[y:y+h,x:x+w]) confidence=int((100*(1-predict/300)))
conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition") my_cursor=conn.cursor()
my_cursor.execute("select Name from student where Student_id="+str(id)) n=my_cursor.fetchone()
n="+".join(n)

my_cursor.execute("select Roll from student where Student_id="+str(id)) r=my_cursor.fetchone()
r="+".join(r)

my_cursor.execute("select Dep from student where Student_id="+str(id)) d=my_cursor.fetchone()
d="+".join(d)

my_cursor.execute("select Student_id from student where Student_id="+str(id)) i=my_cursor.fetchone()
i="+".join(i)
 
if confidence>77:

cv2.putText(img,f"Student ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
self.mark_attendance(i,r,n,d) else:
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) coord=[x,y,w,h]
return coord

def recognize(img,clf,faceCascade): coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf) return img
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") clf=cv2.face.LBPHFaceRecognizer.create()
clf.read("classifier.xml") video_cap=cv2.VideoCapture(0) while True:
ret,img=video_cap.read() img=recognize(img,clf,faceCascade) cv2.imshow("Welcome to face Recognition",img) if cv2.waitKey(1000)==13:
cv2.destroyAllWindows() video_cap.release()
if _name_ == '_main_': root=Tk() obj=Face_Recognition(root) root.mainloop()
 
