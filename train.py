from tkinter import*

from tkinter import ttk

from PIL import Image,ImageTk
 
from tkinter import messagebox

 import mysql.connector

i mport cv2

i mport os

i mport numpy as np

class Train:

    def _init_(self,root):

 	self.root=root

 	self.root.geometry("1530x800+0+0")

 	self.root.title("Face Recognition System")

 	# ===============title=====================

 	lbl_title=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="red")

 	lbl_title.place(x=0,y=0,width=1430,height=35)

 	# ==============Images===================

 	img_top=Image.open("images/face_recognition.png")

 	img_top=img_top.resize((1290,277),Image.ANTIALIAS)

 	self.photoimage_top=ImageTk.PhotoImage(img_top)

 	lbl_img=Label(self.root,image=self.photoimage_top)

 	lbl_img.place(x=0,y=40,width=1290,height=277)

 	# =====================button=====================

 	b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")

 	b1_1.place(x=0,y=318,width=1290,height=60)

 	img_bottom=Image.open("images/data_train.jpg")

 	img_bottom=img_bottom.resize((1290,277),Image.ANTIALIAS)

 	self.photoimage_bottom=ImageTk.PhotoImage(img_bottom)

 	lbl_img=Label(self.root,image=self.photoimage_bottom)

 	lbl_img.place(x=0,y=380,width=1290,height=277)

    def train_classifier(self):

 	data_dir=("data")

 	path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
 

 	faces=[]

 	ids=[]

 	for image in path:

 	img=Image.open(image).convert('L') #Gray scale image

 	imageNp=np.array(img,'uint8')

 	id=int(os.path.split(image)[1].split('.')[1])

 	faces.append(imageNp)

 	ids.append(id)

 	cv2.imshow("Training",imageNp)

 	cv2.waitKey(1)==13

 	ids=np.array(ids)

 	# =====================Train the classifier and save====================

 	clf=cv2.face.LBPHFaceRecognizer_create()

 	clf.train(faces,ids)

 	clf.write("classifier.xml")

 	cv2.destroyAllWindows()

 	messagebox.showinfo("Result","Training datasets completed!!")

 if _name_ == '_main_':

    root=Tk()

    obj=Train(root)

 
    root.mainloop()
 
