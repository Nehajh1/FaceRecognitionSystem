from tkinter import*

from tkinter import ttk

from PIL import Image,ImageTk

from tkinter import messagebox

 import mysql.connector

from time import strftime

from datetime import datetime

i mport cv2

i mport os

i mport csv

from tkinter import filedialog

myData=[]

class Attendance:

    def _init_(self,root):

 	self.root=root

 	self.root.geometry("1530x800+0+0")

 	self.root.title("Face Recognition System")

 	# ================= variables ====================

 	self.var_attendance_id=StringVar()

 	self.var_attendance_roll=StringVar()

 	self.var_attendance_name=StringVar()

 	self.var_attendance_dep=StringVar()

 	self.var_attendance_time=StringVar()

 	self.var_attendance_date=StringVar()

 	self.var_attendance_status=StringVar()

 	# ================ Image1 ===================

 	img=Image.open("images/smart-attendance.jpg")

 	img=img.resize((640,140),Image.ANTIALIAS)

 	self.photoimage=ImageTk.PhotoImage(img)

 	lbl_img=Label(self.root,image=self.photoimage)
 
 	lbl_img.place(x=0,y=0,width=640,height=140)

 	# =============== Image 2==================

 	img1=Image.open("images/clg.jpg")

 	img1=img1.resize((650,140),Image.ANTIALIAS)

 	self.photoimage1=ImageTk.PhotoImage(img1)

 	lbl_img=Label(self.root,image=self.photoimage1)

 	lbl_img.place(x=640,y=0,width=650,height=140)

 	# ================= Background image ================

 	img3=Image.open("images/bg_image.jpg")

 	img3=img3.resize((1330,610),Image.ANTIALIAS)

 	self.photoimage3=ImageTk.PhotoImage(img3)

 	bg_img=Label(self.root,image=self.photoimage3)

 	bg_img.place(x=0,y=140,width=1330,height=610)

 	# ================ title =========================

 	lbl_title=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")

 	lbl_title.place(x=0,y=140,width=1430,height=35)

 	# ================ main frame ================

 	main_frame=Frame(bg_img,bd=2,bg="white")

 	main_frame.place(x=10,y=36,width=1250,height=550)

 	# left label frame

 	left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",13,"bold"))

 	left_frame.place(x=10,y=10,width=590,height=460)

 	img_left=Image.open("images/face-recognition.png")

 	img_left=img_left.resize((580,130),Image.ANTIALIAS)

 	self.photo_img_left=ImageTk.PhotoImage(img_left)

 	bg_img=Label(left_frame,image=self.photo_img_left)

 	bg_img.place(x=5,y=0,width=580,height=130)

 	inside_left_frame=Frame(left_frame,relief=RIDGE,bd=2,bg="white")

 	inside_left_frame.place(x=0,y=135,width=580,height=290)

 	# Attendance id

 	AttendanceId_label=Label(inside_left_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
 
 	AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

 	AttendanceId_entry=ttk.Entry(inside_left_frame,width=13,textvariable=self.var_attendance_id,font=("times new roman",13,"bold"))

 	AttendanceId_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

 	# roll no

 	RollNo_label=Label(inside_left_frame,text="Roll No.:",font=("times new roman",13,"bold"),bg="white")

 	RollNo_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

 	RollNo_entry=ttk.Entry(inside_left_frame,width=13,textvariable=self.var_attendance_roll,font=("times new roman",13,"bold"))

 	RollNo_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

 	# name

 	Name_label=Label(inside_left_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")

 	Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

 	Name_entry=ttk.Entry(inside_left_frame,width=13,textvariable=self.var_attendance_name,font=("times new roman",13,"bold"))

 	Name_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

 	# Department

 	Department_label=Label(inside_left_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")

 	Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

 	Department_entry=ttk.Entry(inside_left_frame,width=13,textvariable=self.var_attendance_dep,font=("times new roman",13,"bold"))

 	Department_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

 	# Time

 	Time_label=Label(inside_left_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")

 	Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

 	Time_entry=ttk.Entry(inside_left_frame,width=13,textvariable=self.var_attendance_time,font=("times new roman",13,"bold"))

 	Time_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

 	# date

 	date_label=Label(inside_left_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")

 	date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

 	date_entry=ttk.Entry(inside_left_frame,width=13,textvariable=self.var_attendance_date,font=("times new roman",13,"bold"))

 	date_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

 	# attendance status

 	attendance_status_label=Label(inside_left_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")

 	attendance_status_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
 
 	attendance_status_combo=ttk.Combobox(inside_left_frame,textvariable=self.var_attendance_status,font=("times new roman",13,"bold"),state="readonly",width=13)

 	attendance_status_combo["values"]=("Status","Present","Absent")

 	attendance_status_combo.current(0)

 	attendance_status_combo.grid(row=3,column=1,padx=2,pady=5,sticky=W)


 	# button frame

 	btn_frame=Frame(inside_left_frame,bd=2,relief=RIDGE)

 	btn_frame.place(x=0,y=240,width=578,height=30)

 	import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")

 	import_btn.grid(row=0,column=0)

 	export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")

 	export_btn.grid(row=0,column=1)

 	update_btn=Button(btn_frame,text="Update",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")

 	update_btn.grid(row=0,column=2)

 	reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")

 	reset_btn.grid(row=0,column=3)

 	# right label frame

 	right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",13,"bold"))

 	right_frame.place(x=610,y=10,width=625,height=460)

 	# button frame

 	table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")

 	table_frame.place(x=5,y=5,width=610,height=419)

 	# ===================== scroll bar =====================

 	scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)

 	scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=s croll_x.set,yscrollcommand=scroll_y.set)

 	scroll_x.pack(side=BOTTOM,fill=X)

 	scroll_y.pack(side=RIGHT,fill=Y)

 	scroll_x.config(command=self.AttendanceReportTable.xview)
 
 	scroll_y.config(command=self.AttendanceReportTable.yview)

 	self.AttendanceReportTable.heading("id",text="Attendance ID")

 	self.AttendanceReportTable.heading("roll",text="Roll")

 	self.AttendanceReportTable.heading("name",text="Name")

 	self.AttendanceReportTable.heading("department",text="Department")

 	self.AttendanceReportTable.heading("time",text="Time")

 	self.AttendanceReportTable.heading("date",text="Date")

 	self.AttendanceReportTable.heading("attendance",text="Attendance")

 	self.AttendanceReportTable["show"]="headings"

 	self.AttendanceReportTable.column("id",width=100)

 	self.AttendanceReportTable.column("roll",width=100)

 	self.AttendanceReportTable.column("name",width=100)

 	self.AttendanceReportTable.column("department",width=100)

 	self.AttendanceReportTable.column("time",width=100)

 	self.AttendanceReportTable.column("date",width=100)

 	self.AttendanceReportTable.column("attendance",width=100)

 	self.AttendanceReportTable.pack(fill=BOTH,expand=1)

 	self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ================= fetch data =====================

    def fetchData(self,rows):

 	self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())

 	for i in rows:

 	self.AttendanceReportTable.insert("",END,values=i)

    # ============ import csv =============

    def importCsv(self):

 	global myData

 	myData.clear()

 	fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All file",".*")),parent=self.root)

 	with open(fln) as myfile:

 	csvread=csv.reader(myfile,delimiter=",")

 	for i in csvread:

 	myData.append(i)
 
 	self.fetchData(myData)

    # ============ export csv =============

    def exportCsv(self):

 	try:

 	if len(myData)<1:

 	messagebox.showerror("No Data","No data found to export",parent=self.root)

 	return False

 	fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All file",".*")),parent=self.root)

 	with open(fln,mode="w",newline="") as myfile:

 	exp_write=csv.writer(myfile,delimiter=",")

 	for i in myData:

 	exp_write.writerow(i)

 	messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+ "successfully")

 	except Exception as es:

 	messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    def get_cursor(self,event=""):

 	cursor_row=self.AttendanceReportTable.focus()

 	content=self.AttendanceReportTable.item(cursor_row)

 	rows=content['values']

 	self.var_attendance_id.set(rows[0])

 	self.var_attendance_roll.set(rows[1])

 	self.var_attendance_name.set(rows[2])

 	self.var_attendance_dep.set(rows[3])

 	self.var_attendance_time.set(rows[4])

 	self.var_attendance_date.set(rows[5])

 	self.var_attendance_status.set(rows[6])

    def reset_data(self):

 	self.var_attendance_id.set("")

 	self.var_attendance_roll.set("")

 	self.var_attendance_name.set("")
 
 	self.var_attendance_dep.set("")

 	self.var_attendance_time.set("")

 	self.var_attendance_date.set("")

 	self.var_attendance_status.set("")

 if _name_ == '_main_':

    root=Tk()

    obj=Attendance(root)

 
    root.mainloop()
