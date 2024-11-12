from tkinter import* from tkinter import ttk
from PIL import Image,ImageTk from tkinter import messagebox import mysql.connector
import cv2 import os
import numpy as np
 
class Help:

def _init_(self,root): self.root=root self.root.geometry("1530x800+0+0")
self.root.title("Face Recognition System")



# ===============title=====================

lbl_title=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue") lbl_title.place(x=0,y=0,width=1430,height=55)
# ==============Images===================

img_top=Image.open("images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg") img_top=img_top.resize((1290,620),Image.ANTIALIAS) self.photoimage_top=ImageTk.PhotoImage(img_top) lbl_img=Label(self.root,image=self.photoimage_top) lbl_img.place(x=0,y=55,width=1290,height=620)
dev_label=Label(lbl_img,text="Email:ngill7768@gmail.com",font=("times new roman",20,"bold"),fg="blue") dev_label.place(x=450,y=180)
if _name_ == '_main_':

root=Tk() obj=Help(root) root.mainloop()
