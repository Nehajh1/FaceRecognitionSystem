from tkinter import* from tkinter import ttk
from PIL import Image,ImageTk from tkinter import messagebox import mysql.connector
class Register:

def _init_(self,root):

self.root=root self.root.title("Register") self.root.geometry("1530x800+0+0")
# ================variables=======================

self.var_fname=StringVar() self.var_lname=StringVar() self.var_contact=StringVar() self.var_email=StringVar() self.var_security_Q=StringVar()
 
self.var_security_A=StringVar() self.var_password=StringVar() self.var_confirm_password=StringVar() self.var_ heck=IntVar()
# ===========Background Image=========== self.bg=ImageTk.PhotoImage(file=r"C:\\Users\\user\\Downloads\\Billing System\\hotel images\\background1.jpg") bg_lbl=Label(self.root,image=self.bg)
bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

# =============Main Frame================

frame=Frame(self.root,bg="white") frame.place(x=420,y=120,width=750,height=490)
register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white") register_lbl.place(x=20,y=20)
# ===========label and entry============== # ====================row1=============
fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black") fname.place(x=40,y=65)
fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold")) fname_entry.place(x=40,y=100,width=250)
l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black") l_name.place(x=370,y=65)
self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15)) self.txt_lname.place(x=370,y=100,width=250)
# ====================row2=============

contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black") contact.place(x=40,y=140) self.txt_contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold")) self.txt_contact_entry.place(x=40,y=180,width=250)
email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black") email.place(x=370,y=140) self.txt_contact=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15)) self.txt_contact.place(x=370,y=180,width=250)
 
# ====================row3=============

security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black") security_Q.place(x=40, y=220)


self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",15,"bold")) self.combo_security_Q["values"]=("Select","Your Birth Place","Your Birth Year") self.combo_security_Q.place(x=40,y=260,width=250)
self.combo_security_Q.current(0)

security_A=Label(frame,text="Select Answer",font=("times new roman",15,"bold"),bg="white",fg="black") security_A.place(x=370, y=220) self.txt_security=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",15)) self.txt_security.place(x=370,y=260,width=250)
# ====================row4=============

password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black") password.place(x=40,y=310) self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold")) self.txt_password.place(x=40,y=340,width=250)
confirm_password=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black") confirm_password.place(x=370,y=310) self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",15)) self.txt_confirm_password.place(x=370,y=340,width=250)
# =================check button==============

check_btn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold")) check_btn.place(x=40,y=380)
# ====================buttons===================

img=Image.open("images/register-now-button1.jpg") img=img.resize((200,50),Image.ANTIALIAS) self.photoimage=ImageTk.PhotoImage(img)
b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold")) b1.place(x=10,y=430,width=200)
img1=Image.open("images/loge.png") img1=img1.resize((200,50),Image.ANTIALIAS)
 
self.photoimage1=ImageTk.PhotoImage(img1) b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold")) b1.place(x=330,y=430,width=200)
# ===================Function Declaration===================

def register_data(self):

if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="Select": messagebox.showerror("Error","All fields are required")
elif self.var_password.get()!=self.var_confirm_password.get(): messagebox.showerror("Error","password & confirm password must be same")
elif self.var_check.get()==0:

messagebox.showerror("Error","Please agree our terms & conditions") else:
conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition") my_cursor=conn.cursor()
query=("select * from register where email=%s") value=(self.var_email.get(),) my_cursor.execute(query,value) row=my_cursor.fetchone()
if row!=None:

messagebox.showerror("Error","User already exist,please try another email") else:
my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",( self.var_fname.get(),
self.var_lname.get(), self.var_contact.get(), self.var_email.get(), self.var_security_Q.get(), self.var_security_A.get(), self.var_password.get()
))

conn.commit() conn.close()
 
messagebox.showinfo("Success","Register Successful") if _name_ == '_main_':
root=Tk() obj=Register(root) root.mainloop()
