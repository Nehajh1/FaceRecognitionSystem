from tkinter import* from tkinter import ttk
from PIL import Image,ImageTk from tkinter import messagebox import mysql.connector
import cv2 class Student:
def _init_(self,root): self.root=root
self.root.geometry("1530x800+0+0") self.root.title("Face Recognition System")
 
# ===============Variables==================

self.var_dep=StringVar() self.var_course=StringVar() self.var_year=StringVar() self.var_semester=StringVar() self.var_std_id=StringVar() self.var_std_name=StringVar() self.var_div=StringVar() self.var_roll=StringVar() self.var_gender=StringVar() self.var_dob=StringVar() self.var_email=StringVar() self.var_phone=StringVar() self.var_address=StringVar() self.var_teacher=StringVar()
# ================ Image1 ===================

img=Image.open("images/face-recognition.png") img=img.resize((440,140),Image.ANTIALIAS) self.photoimage=ImageTk.PhotoImage(img) lbl_img=Label(self.root,image=self.photoimage) lbl_img.place(x=0,y=0,width=440,height=140) img1=Image.open("images/smart-attendance.jpg") img1=img1.resize((440,140),Image.ANTIALIAS) self.photoimage1=ImageTk.PhotoImage(img1) lbl_img=Label(self.root,image=self.photoimage1) lbl_img.place(x=440,y=0,width=440,height=140) img2=Image.open("images/IMG_1183_augmented_reality_faces1.jpg") img2=img2.resize((440,140),Image.ANTIALIAS) self.photoimage2=ImageTk.PhotoImage(img2) lbl_img=Label(self.root,image=self.photoimage2) lbl_img.place(x=880,y=0,width=440,height=140)
# ============== background image ===================
 
img3=Image.open("images/bg_image.jpg") img3=img3.resize((1330,610),Image.ANTIALIAS) self.photoimage3=ImageTk.PhotoImage(img3) bg_img=Label(self.root,image=self.photoimage3) bg_img.place(x=0,y=140,width=1330,height=610)




lbl_title=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkgreen") lbl_title.place(x=0,y=140,width=1430,height=35)
main_frame=Frame(bg_img,bd=2) main_frame.place(x=10,y=36,width=1250,height=550) # left label frame
left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",13,"bold")) left_frame.place(x=10,y=10,width=590,height=460)
# current course label frame

current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current course information",font=("times new roman",13,"bold")) current_course_frame.place(x=5,y=0,width=580,height=110)
# Department

dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white") dep_label.grid(row=0,column=0,padx=10,sticky=W)
dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=16)

dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical") dep_combo.current(0) dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
#course

course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
course_label.grid(row=0,column=2,padx=10,sticky=W) course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new
roman",13,"bold"),state="readonly",width=16) course_combo["values"]=("Select Course","FE","SE","TE","BE") course_combo.current(0) course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
 
#year
year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
year_label.grid(row=1,column=0,padx=10,sticky=W) year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new
roman",13,"bold"),state="readonly",width=16)

year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24") year_combo.current(0) year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
# Semester

semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
semester_label.grid(row=1,column=2,padx=10,sticky=W) semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new
roman",13,"bold"),state="readonly",width=16)

semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4") semester_combo.current(0)
semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W) # Class Student label frame
class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class student information",font=("times new roman",13,"bold")) class_student_frame.place(x=5,y=120,width=580,height=298)
# student id

StudentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white") StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


StudentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=16,font=("times new roman",13,"bold")) StudentId_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)
# student name

StudentName_label=Label(class_student_frame,text="StudentName:",font=("times new roman",13,"bold"),bg="white") StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W) StudentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=16,font=("times new roman",13,"bold")) StudentName_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)
# class division

Class_div_label=Label(class_student_frame,text="Class:",font=("times new roman",13,"bold"),bg="white") Class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
 
div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=14) div_combo["values"]=("Select Division","A","B","C")
div_combo.current(0) div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W) # roll no
RollNo_label=Label(class_student_frame,text="Roll No.:",font=("times new roman",13,"bold"),bg="white") RollNo_label.grid(row=1,column=2,padx=10,pady=5,sticky=W) RollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=16,font=("times new roman",13,"bold")) RollNo_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)
# gender

Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white") Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=14)

gender_combo["values"]=("Male","Female","Other") gender_combo.current(0) gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W) # DOB
DOB_label=Label(class_student_frame,text="D.O.B:",font=("times new roman",13,"bold"),bg="white") DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W) DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=16,font=("times new roman",13,"bold")) DOB_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)
# Email

Email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white") Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W) Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=16,font=("times new roman",13,"bold")) Email_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)
# phone no

PhoneNo_label=Label(class_student_frame,text="Phone No.:",font=("times new roman",13,"bold"),bg="white") PhoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky=W) PhoneNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=16,font=("times new roman",13,"bold")) PhoneNo_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)
 
# Address

Address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white") Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W) Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=16,font=("times new roman",13,"bold")) Address_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)
# Teacher name

TeacherName_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white") TeacherName_label.grid(row=4,column=2,padx=10,pady=5,sticky=W) TeacherName_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=16,font=("times new roman",13,"bold")) TeacherName_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)
# radio button self.var_radio1=StringVar()
Radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes") Radiobutton1.grid(row=6,column=0) Radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No") Radiobutton2.grid(row=6,column=1)
# button frame btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE) btn_frame.place(x=0,y=200,width=578,height=30)
save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white") save_btn.grid(row=0,column=0)


update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
update_btn.grid(row=0,column=1) delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new
roman",13,"bold"),bg="blue",fg="white")

delete_btn.grid(row=0,column=2)

reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white") reset_btn.grid(row=0,column=3)
# button frame1 btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE) btn_frame1.place(x=0,y=230,width=578,height=30)
 
take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=28,font=("times new roman",13,"bold"),bg="blue",fg="white")

take_photo_btn.grid(row=0,column=0)

update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=28,font=("times new roman",13,"bold"),bg="blue",fg="white") update_photo_btn.grid(row=0,column=1)
# right label frame

right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",13,"bold")) right_frame.place(x=610,y=10,width=625,height=460)
img_right=Image.open("images/student.jpg") img_right=img_right.resize((618,120),Image.ANTIALIAS) self.photoimage_right=ImageTk.PhotoImage(img_right) lbl_img=Label(right_frame,image=self.photoimage_right) lbl_img.place(x=5,y=0,width=618,height=120)
# Search System # search frame
search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",13,"bold")) search_frame.place(x=5,y=120,width=615,height=70)
search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white") search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W) search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="read only",width=12) search_combo['values']=('Select','Roll No','Phone No')
search_combo.current(0) search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) search_entry=ttk.Entry(search_frame,width=12,font=("times new roman",13,"bold")) search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)
search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white") search_btn.grid(row=0,column=3,padx=4)


showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white") showAll_btn.grid(row=0,column=4,padx=4)
# table frame table_frame=Frame(right_frame,bd=2,relief=RIDGE)
 
table_frame.place(x=5,y=195,width=615,height=230) scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","add ress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X) scroll_y.pack(side=RIGHT,fill=Y) scroll_x.config(command=self.student_table.xview) scroll_y.config(command=self.student_table.yview) self.student_table.heading("dep",text="Department") self.student_table.heading("course",text="Course") self.student_table.heading("year",text="Year") self.student_table.heading("sem",text="Semester") self.student_table.heading("id",text="StudentID") self.student_table.heading("name",text="Name") self.student_table.heading("roll",text="Roll No") self.student_table.heading("gender",text="Gender") self.student_table.heading("div",text="Division") self.student_table.heading("dob",text="DOB") self.student_table.heading("email",text="Email") self.student_table.heading("phone",text="Phone") self.student_table.heading("address",text="Address") self.student_table.heading("teacher",text="Teacher") self.student_table.heading("photo",text="PhotoSampleStatus") self.student_table["show"]="headings" self.student_table.column("dep",width=100) self.student_table.column("course",width=100) self.student_table.column("year",width=100) self.student_table.column("sem",width=100) self.student_table.column("id",width=100) self.student_table.column("name",width=100) self.student_table.column("roll",width=100)
 
self.student_table.column("gender",width=100) self.student_table.column("div",width=100) self.student_table.column("dob",width=100) self.student_table.column("email",width=100) self.student_table.column("phone",width=100) self.student_table.column("address",width=100) self.student_table.column("teacher",width=100) self.student_table.column("photo",width=100) self.student_table.pack(fill=BOTH,expand=1) self.student_table.bind("<ButtonRelease>",self.get_cursor) self.fetch_data()
# ====================Function Declaration=======================

def add_data(self):

if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="": messagebox.showerror("Error","All fields are required",parent=self.root)
else:

try:

conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition") my_cursor=conn.cursor()
my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_id.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
 
self.var_address.get(), self.var_teacher.get(), self.var_radio1.get()
))

conn.commit() self.fetch_data() conn.close()
messagebox.showinfo("Success","Student details has been added successfully",parent=self.root) except Exception as es:
messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) # ==============Fetch data====================
def fetch_data(self): conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition") my_cursor=conn.cursor()
my_cursor.execute("select * from student") data=my_cursor.fetchall()
if len(data)!=0: self.student_table.delete(*self.student_table.get_children()) for i in data:
self.student_table.insert("",END,values=i) conn.commit()
conn.close()

# ===============get cursor====================

def get_cursor(self,event=""): cursor_focus=self.student_table.focus() content=self.student_table.item(cursor_focus) data=content["values"] self.var_dep.set(data[0]), self.var_course.set(data[1]), self.var_year.set(data[2]), self.var_semester.set(data[3]), self.var_std_id.set(data[4]),
 
self.var_std_name.set(data[5]), self.var_div.set(data[6]), self.var_roll.set(data[7]), self.var_gender.set(data[8]), self.var_dob.set(data[9]), self.var_email.set(data[10]), self.var_phone.set(data[11]), self.var_address.set(data[12]), self.var_teacher.set(data[13]), self.var_radio1.set(data[14])
# ==============Update function====================

def update_data(self):

if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="": messagebox.showerror("Error","All fields are required",parent=self.root)
else:

try:

update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root) if update>0:
conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition") my_cursor=conn.cursor()
my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher
=%s,PhotoSample=%s where Student_id=%s",(

self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(),
 
self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get()
))

else:

if not Update:

return

messagebox.showinfo("Success","Student details successfully update completed",parent=self.root) conn.commit()
self.fetch_data() conn.close()
except Exception as es:

messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) # =================Delete function=====================
def delete_data(self):

if self.var_std_id.get()=="":

messagebox.showerror("Error","Student id must be required",parent=self.root) else:
try:

delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root) if delete>0:
conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition") my_cursor=conn.cursor()
sql="delete from student where Student_id=%s" val=(self.var_std_id.get(),) my_cursor.execute(sql,val)
else:

if not delete: return
conn.commit()
 
self.fetch_data() conn.close()
messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root) except Exception as es:
messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) # ==================Reset Function===================
def reset_data(self):

self.var_dep.set("Select Department") self.var_course.set("Select Course") self.var_year.set("Select Year") self.var_semester.set("Select Semester") self.var_std_id.set("") self.var_std_name.set("") self.var_div.set("Select Division") self.var_roll.set("") self.var_gender.set("Male") self.var_dob.set("") self.var_email.set("") self.var_phone.set("") self.var_address.set("") self.var_teacher.set("") self.var_radio1.set("")
# ================Generate data set or Take Photo Sample================== def generate_dataset(self):
if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="": messagebox.showerror("Error","All fields are required",parent=self.root)
else:

try:

conn=mysql.connector.connect(host="localhost",username="root",password="Nn1800**",database="face_recognition") my_cursor=conn.cursor()
my_cursor.execute("select * from student") my_result=my_cursor.fetchall()
 
id=0

for x in my_result:

id+=1

my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher
=%s,PhotoSample=%s where Student_id=%s",(

self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get()==id+1
))

conn.commit() self.fetch_data() self.reset_data() conn.close()
#================ Load predefined data on face frontals from open_cv=================== face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def face_cropped(img): gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) face=face_classifier.detectMultiScale(gray,1.3,5) #scaling factor = 1.3
#minimum Neighbour = 5
 
for(x,y,w,h) in face:

face_cropped=img[y:y+h,x:x+w] return face_cropped
cap=cv2.VideoCapture(0) img_id=0
while True:

ret,my_frame=cap.read()

if face_cropped(my_frame) is not None:

img_id+=1 face=cv2.resize(face_cropped(my_frame),(450,450)) face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg" cv2.imwrite(file_name_path,face)
cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) cv2.imshow("Cropped Face",face)
if cv2.waitKey(1)==13 or int(img_id)==100: break
cap.release() cv2.destroyAllWindows()
messagebox.showinfo("Result","Generating data sets completely!!!") except Exception as es:
messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) if _name_ == '_main_':
root=Tk() obj=Student(root) root.mainloop()
