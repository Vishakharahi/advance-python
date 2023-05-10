from tkinter import *
import mysql.connector
root=Tk()
root.geometry("500x500")
try:
           def shownow():
               db=mysql.connector.connect(host="localhost",user="root",password="",db="studeta")
               cursor1=db.cursor()
               sql2="SELECT * FROM student WHERE email="+find.get()+";"
               print(sql2)
               cursor1.execute(sql2)
               
               
           def insert():
               db=mysql.connector.connect(host="localhost",user="root",password="",db="studeta")
               cursor=db.cursor()
               sql="INSERT INTO student values(%s,%s,%s,%s)"
               a=[firstname.get(),lastname.get(),email.get(),contact.get()]
               cursor.execute(sql,a)
               db.commit()
              
           def show():
               showi=Toplevel()
               showi.geometry("500x500")
               lablee=Label(showi,text="Enter Email")
               entEman=Entry(showi,textvariable=find)
               lablee.pack()
               entEman.pack()
               buttongfi=Button(showi,text="find" ,command=shownow)
               buttongfi.pack(pady=40)
               showi.mainloop()
           
           
           find=StringVar()
           firstname=StringVar()
           lablename=Label(root,text="First Name")
           entname=Entry(root,textvariable=firstname)
           lablename.pack()
           entname.pack()
           
           lastname=StringVar()
           lablelastname=Label(root,text="Last Name")
           entlastname=Entry(root,textvariable=lastname)
           lablelastname.pack()
           entlastname.pack()
           
           
           email=StringVar()
           lableemail=Label(root,text="Email")
           entemail=Entry(root,textvariable=email)
           lableemail.pack()
           entemail.pack()
           
           
           contact=StringVar()
           lablecontact=Label(root,text="Contact")
           entcontact=Entry(root,textvariable=contact)
           lablecontact.pack()
           entcontact.pack()
           
           butonsow=Button(root,text="Insert",command=insert)
           butonsow.pack(pady=40)
           
           butonshoe=Button(root,text="Show Record",command=show)
           butonshoe.pack(pady=40)
           
           root.mainloop() 
           
except(Exception):
    print("Not Working")
    