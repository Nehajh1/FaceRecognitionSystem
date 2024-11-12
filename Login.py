from tkinter import*

from tkinter import ttk

from PIL import Image,ImageTk

from tkinter import messagebox

 import mysql.connector

i mport os

from student import Student

from train import Train

from help import Help

from attendance import Attendance

from face_recognition import Face_Recognition

from main import Face_Recognition_System

def main():

    win=Tk()

    app=Login_Window(win)

    win.mainloop()

class Login_Window:

    def _init_(self,root):

 	self.root=root

 	self.root.title("Login")

 	self.root.geometry("1530x800+0+0")

 	# ===========Background Image=========

 	self.bg=ImageTk.PhotoImage(file=r"C:\\Users\\user\\Downloads\\Billing System\\hotel images\\background.jpg")

 	bg_lbl=Label(self.root,image=self.bg)

 	bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

 	frame=Frame(root,bg="black")

 	frame.place(x=460,y=100,width=340,height=450)

 	img=Image.open("images/LoginIconAppl.png")

 	img=img.resize((100,100),Image.ANTIALIAS)
 
 	self.photoimage=ImageTk.PhotoImage(img)

 	lbl_img=Label(self.root,image=self.photoimage,bg="black",borderwidth=0)

 	lbl_img.place(x=590,y=100,width=100,height=100)

 	get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")

 	get_str.place(x=100,y=100)

 	# ============labels================

 	username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")

 	username.place(x=70,y=155)

 	self.txt_user=ttk.Entry(frame,font=("times new roman",20,"bold"))

 	self.txt_user.place(x=40,y=180,width=270)

 	password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")

 	password.place(x=70,y=225)

 	self.txt_pass=ttk.Entry(frame,font=("times new roman",20,"bold"))

 	self.txt_pass.place(x=40,y=250,width=270)

 	# ================Icon Images==================

 	img2=Image.open("images/LoginIconAppl.png")

 	img2=img2.resize((25,25),Image.ANTIALIAS)

 	self.photoimage2=ImageTk.PhotoImage(img2)

 	lbl_img=Label(self.root,image=self.photoimage2,bg="black",borderwidth=0)

 	lbl_img.place(x=500,y=255,width=25,height=25)

 	img3=Image.open("images/lock-512.png")

 	img3=img3.resize((25,25),Image.ANTIALIAS)

 	self.photoimage3=ImageTk.PhotoImage(img3)

 	lbl_img=Label(self.root,image=self.photoimage3,bg="black",borderwidth=0)

 	lbl_img.place(x=500,y=325,width=25,height=25)

 	# Login button

 	login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")

 	login_btn.place(x=110,y=300,width=120,height=35)

 	# Register button

 	register_btn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",14,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")

 	register_btn.place(x=20,y=350,width=160)
 
 	# Forget password

 	forget_btn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",14,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")

 	forget_btn.place(x=10,y=380,width=160)

    def register_window(self):

 	self.new_window=Toplevel(self.root)

 	self.app=Register(self.new_window)

    def login(self):

 	if self.txt_user.get=="" or self.txt_pass.get()=="":

 	messagebox.showerror("Error","All field required")

 	elif self.txt_user.get()=="neha" and self.txt_pass.get()=="gill":

 	messagebox.showinfo("Success","Welcome to Face Recognition System")

 	else:

 	conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition")

 	my_cursor=conn.cursor()

 	my_cursor.execute("select * from register where email=%s and password=%s",(

 	self.txt_user.get(),

 	self.txt_pass.get()

 	))

 	row=my_cursor.fetchone()

 	if row==None:

 	messagebox.showerror("Error","Invalid username & password")

 	else:

 	open_main=messagebox.askyesno("YesNo","Access only admin")

 	if open_main>0:

 	self.new_window=Toplevel(self.root)

 	self.app=Face_Recognition_System(self.new_window)

 	else:

 	if not open_main:

 	return

 	conn.commit()

 	conn.close()
 
    # ======================reset password=======================

    def reset_password(self):

 	if self.combo_security_Q.get()=="Select":

 	messagebox.showerror("Error","Select security question",parent=self.root2)

 	elif self.txt_security.get()=="":

 	messagebox.showerror("Error","Please enter the answer",parent=self.root2)

 	elif self.txt_new_password.get()=="":

 	messagebox.showerror("Error","Please enter the new password",parent=self.root2)

 	else:

 	conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition")

 	my_cursor=conn.cursor()

 	query=("select * from register where email=%s and securityQ=%s and securityA=%s")

 	value=(self.txt_user.get(),self.combo_security_Q.get(),self.txt_security.get())

 	my_cursor.execute(query,value)

 	row=my_cursor.fetchone()

 	if row==None:

 	messagebox.showerror("Error","Please enter correct answer",parent=self.root2)

 	else:

 	query=("update register set password=%s where email=%s")

 	value=(self.txt_new_password.get(),self.txt_user.get())

 	my_cursor.execute(query,value)

 	conn.commit()

 	conn.close()

 	messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)

 	self.root2.destroy()

    # ==================forgot password window=========================

    def forgot_password_window(self):

 	if self.txt_user.get()=="":

 	messagebox.showerror("Error","Please enter the Email address to reset password")

 	else:

 	conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition")

 	my_cursor=conn.cursor()
 
 	query=("select * from register where email=%s")

 	value=(self.txt_user.get(),)

 	my_cursor.execute(query,value)

 	row=my_cursor.fetchone()

 	if row==None:

 	messagebox.showerror("My Error","Please enter the valid username")

 	else:

 	conn.close()

 	self.root2=Toplevel()

 	self.root2.title("Forget Password")

 	self.root2.geometry("400x470+400+100")

 	l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")

 	l.place(x=0,y=10,relwidth=1)

 	# ====================row3=============

 	security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")

 	security_Q.place(x=40,y=80)

 	self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"))

 	self.combo_security_Q["values"]=("Select","Your Birth Place","Your Birth Year")

 	self.combo_security_Q.place(x=40,y=110,width=250)

 	self.combo_security_Q.current(0)

 	security_A=Label(self.root2,text="Select Answer",font=("times new roman",15,"bold"),bg="white",fg="black")

 	security_A.place(x=40,y=150)

 	self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))

 	self.txt_security.place(x=40,y=180,width=250)

 	new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")

 	new_password.place(x=40,y=220)

 	self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15))

 	self.txt_new_password.place(x=40,y=250,width=250)

 	btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15),fg="white",bg="green")

 	btn.place(x=140,y=290,width=120,height=35)

class Register:

    def _init_(self,root):
 
 	self.root=root

 	self.root.title("Register")

 	self.root.geometry("1530x800+0+0")

 	# ================variables=======================

 	self.var_fname=StringVar()

 	self.var_lname=StringVar()

 	self.var_contact=StringVar()

 	self.var_email=StringVar()

 	self.var_security_Q=StringVar()

 	self.var_security_A=StringVar()

 	self.var_password=StringVar()

 	self.var_confirm_password=StringVar()

 	self.var_check=IntVar()

 	# ===========Background Image===========

 	self.bg=ImageTk.PhotoImage(file=r"C:\\Users\\user\\Downloads\\Billing System\\hotel images\\background1.jpg")

 	bg_lbl=Label(self.root,image=self.bg)

 	bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

 	# =============Main Frame================

 	frame=Frame(self.root,bg="white")

 	frame.place(x=420,y=120,width=750,height=490)

 	register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")

 	register_lbl.place(x=20,y=20)

 	# ===========label and entry==============

 	# ====================row1=============

 	fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")

 	fname.place(x=40,y=65)

 	fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))

 	fname_entry.place(x=40,y=100,width=250)


 	l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")

 	l_name.place(x=370,y=65)

 	self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
 
 	self.txt_lname.place(x=370,y=100,width=250)

 	# ====================row2=============

 	contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")

 	contact.place(x=40,y=140)

 	self.txt_contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))

 	self.txt_contact_entry.place(x=40,y=180,width=250)

 	email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")

 	email.place(x=370,y=140)

 	self.txt_contact=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))

 	self.txt_contact.place(x=370,y=180,width=250)

 	# ====================row3=============

 	security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")

 	security Q.place(x=40,y=220)

 	self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",15,"bold"))

 	self.combo_security_Q["values"]=("Select","Your Birth Place","Your Birth Year")

 	self.combo_security_Q.place(x=40,y=260,width=250)

 	self.combo_security_Q.current(0)

 	security_A=Label(frame,text="Select Answer",font=("times new roman",15,"bold"),bg="white",fg="black")

 	security_A.place(x=370,y=220)

 	self.txt_security=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",15))

 	self.txt_security.place(x=370,y=260,width=250)

 	# ====================row4=============

 	password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")

 	password.place(x=40,y=310)

 	self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))

 	self.txt_password.place(x=40,y=340,width=250)

 	confirm_password=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")

 	confirm_password.place(x=370,y=310)

 	self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",15))

 	self.txt_confirm_password.place(x=370,y=340,width=250)

 	# =================check button==============

 	check_btn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"))
 
 	check_btn.place(x=40,y=380)

 	# ====================buttons===================

 	img=Image.open("images/register-now-button1.jpg")

 	img=img.resize((200,50),Image.ANTIALIAS)

 	self.photoimage=ImageTk.PhotoImage(img)

 	b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))

 	b1.place(x=10,y=430,width=200)

 	img1=Image.open("images/loge.png")

 	img1=img1.resize((200,50),Image.ANTIALIAS)

 	self.photoimage1=ImageTk.PhotoImage(img1)

 	b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))

 	b1.place(x=330,y=430,width=200)

    # ===================Function Declaration===================

    def register_data(self):

 	if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="Select":

 	messagebox.showerror("Error","All fields are required")

 	elif self.var_password.get()!=self.var_confirm_password.get():

 	messagebox.showerror("Error","password & confirm password must be same")

 	elif self.var_check.get()==0:

 	messagebox.showerror("Error","Please agree our terms & conditions")

 	else:

 	conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="management")

 	my_cursor=conn.cursor()

 	query=("select * from register where email=%s")

 	value=(self.var_email.get(),)

 	my_cursor.execute(query,value)

 	row=my_cursor.fetchone()

 	if row!=None:

 	messagebox.showerror("Error","User already exist,please try another email")

 	else:

 	my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
 
 	self.var_fname.get(),

 	self.var_lname.get(),

 	self.var_contact.get(),

 	self.var_email.get(),

 	self.var_security_Q.get(),

 	self.var_security_A.get(),

 	self.var_password.get()

 	))

 	conn.commit()

 	conn.close()

 	messagebox.showinfo("Success","Register Successful")

    def return_login(self):

 	self.root.destroy()

class Face_Recognition_System:

    def _init_(self,root):

 	self.root=root

 	self.root.geometry("1530x800+0+0")

 	self.root.title("Face Recognition System")

 	# ================ Image1 ===================

 	img=Image.open("images/BestFacialRecognition.jpg")

 	img=img.resize((440,140),Image.ANTIALIAS)

 	self.photoimage=ImageTk.PhotoImage(img)

 	lbl_img=Label(self.root,image=self.photoimage)

 	lbl_img.place(x=0,y=0,width=440,height=140)

 	img1=Image.open("images/face_recognition.png")

 	img1=img1.resize((440,140),Image.ANTIALIAS)

 	self.photoimage1=ImageTk.PhotoImage(img1)

 	lbl_img=Label(self.root,image=self.photoimage1)

 	lbl_img.place(x=440,y=0,width=440,height=140)

 	img2=Image.open("images/images.jpg")

 	img2=img2.resize((440,140),Image.ANTIALIAS)

 	self.photoimage2=ImageTk.PhotoImage(img2)
 
 	lbl_img=Label(self.root,image=self.photoimage2)

 	lbl_img.place(x=880,y=0,width=440,height=140)

 	# background image

 	img3=Image.open("images/bg_image.jpg")

 	img3=img3.resize((1330,610),Image.ANTIALIAS)

 	self.photoimage3=ImageTk.PhotoImage(img3)

 	bg_img=Label(self.root,image=self.photoimage3)

 	bg_img.place(x=0,y=140,width=1330,height=610)


 	lbl_title=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")

 	lbl_title.place(x=0,y=140,width=1430,height=35)

 	# student button

 	img4=Image.open("images/student.jpg")

 	img4=img4.resize((160,160),Image.ANTIALIAS)

 	self.photoimage4=ImageTk.PhotoImage(img4)

 	b1=Button(bg_img,image=self.photoimage4,command=self.student_details,cursor="hand2")

 	b1.place(x=200,y=80,width=160,height=160)

 	b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")

 	b1_1.place(x=200,y=240,width=160,height=30)

 	# detect face button

 	img5=Image.open("images/face_detector1.jpg")

 	img5=img5.resize((160,160),Image.ANTIALIAS)

 	self.photoimage5=ImageTk.PhotoImage(img5)

 	b1=Button(bg_img,image=self.photoimage5,cursor="hand2",command=self.face_data)

 	b1.place(x=450,y=80,width=160,height=160)

 	b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

 	b1_1.place(x=450,y=240,width=160,height=30)

 	# attendance button

 	img6=Image.open("images/report.jpg")

 	img6=img6.resize((160,160),Image.ANTIALIAS)
 
 	self.photoimage6=ImageTk.PhotoImage(img6)

 	b1=Button(bg_img,image=self.photoimage6,cursor="hand2",command=self.attendance_data)

 	b1.place(x=700,y=80,width=160,height=160)

 	b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

 	b1_1.place(x=700,y=240,width=160,height=30)

 	# help desk button

 	img7=Image.open("images/help.jpg")

 	img7=img7.resize((160,160),Image.ANTIALIAS)

 	self.photoimage7=ImageTk.PhotoImage(img7)

 	b1=Button(bg_img,image=self.photoimage7,cursor="hand2",command=self.help_data)

 	b1.place(x=950,y=80,width=160,height=160)

 	b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

 	b1_1.place(x=950,y=240,width=160,height=30)

 	# train data button

 	img8=Image.open("images/train.jpg")

 	img8=img8.resize((160,160),Image.ANTIALIAS)

 	self.photoimage8=ImageTk.PhotoImage(img8)

 	b1=Button(bg_img,image=self.photoimage8,cursor="hand2",command=self.train)

 	b1.place(x=200,y=300,width=160,height=160)

 	b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

 	b1_1.place(x=200,y=460,width=160,height=30)

 	# photos button

 	img9=Image.open("images/data_train.jpg")

 	img9=img9.resize((160,160),Image.ANTIALIAS)

 	self.photoimage9=ImageTk.PhotoImage(img9)

 	b1=Button(bg_img,image=self.photoimage9,cursor="hand2",command=self.open_img)

 	b1.place(x=450,y=300,width=160,height=160)

 	b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

 	b1_1.place(x=450,y=460,width=160,height=30)
 
 	# developer button

 	img10=Image.open("images/team.jpg")

 	img10=img10.resize((160,160),Image.ANTIALIAS)

 	self.photoimage10=ImageTk.PhotoImage(img10)

 	b1=Button(bg_img,image=self.photoimage10,cursor="hand2")

 	b1.place(x=700,y=300,width=160,height=160)

 	b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")

 	b1_1.place(x=700,y=460,width=160,height=30)

 	# exit button

 	img11=Image.open("images/exit.jpg")

 	img11=img11.resize((160,160),Image.ANTIALIAS)

 	self.photoimage11=ImageTk.PhotoImage(img11)

 	b1=Button(bg_img,image=self.photoimage11,cursor="hand2",command=self.logout)

 	b1.place(x=950,y=300,width=160,height=160)

 	b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.logout,font=("times new roman",15,"bold"),bg="darkblue",fg="white")

 	b1_1.place(x=950,y=460,width=160,height=30)

    # ====================function open image================

    def open_img(self):

 	os.startfile("data")

    def Exit(self):

 	self.Exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)

 	if self.Exit>0:

 	self.root.destroy()

 	else:

 	return

# ===========Function Buttons==================

    def student_details(self):

 	self.new_window=Toplevel(self.root)

 	self.app=Student(self.new_window)

    def train(self):

 	self.new_window=Toplevel(self.root)

 	self.app=Train(self.new_window)
 
    def face_data(self):

 	self.new_window=Toplevel(self.root)

 	self.app=Face_Recognition(self.new_window)

    def help_data(self):

 	self.new_window=Toplevel(self.root)

 	self.app=Help(self.new_window)

    def attendance_data(self):

 	self.new_window=Toplevel(self.root)

 	self.app=Attendance(self.new_window)


    def logout(self):

 	self.root.destroy()

 if _name_ == '_main_':

 
    main()
