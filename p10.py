from tkinter import *
from tkinter import messagebox
def sel():
    selection=str(var.get())
    if selection=='yashvi':
        print("correct")
    if selection=='krupali':
        print("incorrect")
    if selection=='janki':
        print("incorrect")
    if selection=='jensi':
        print("incorrect")
    
    label.config(text=selection)
root = Tk()
root.geometry("300x200")
w = Label(root,text ='what is your name?',font ="20")
w.place(x=0,y=10)
var=StringVar()
R1=Radiobutton(root,text="yashvi",variable=var,value="yashvi",command=sel)
R1.place(x=10,y=40)
R2=Radiobutton(root,text="krupali",variable=var,value="krupali",command=sel)
R2.place(x=10,y=60)
R3=Radiobutton(root,text="janki",variable=var,value="janki",command=sel)
R3.place(x=10,y=80)
R3=Radiobutton(root,text="jensi",variable=var,value="jensi",command=sel)
R3.place(x=10,y=100)
label=Label(root)
label.place(x=10,y=120)


    


def sel():
    selection=str(var.get())
    if selection=='bca':
        print("correct")
    if selection=='bba':
        print("incorrect")
    if selection=='b.com':
        print("incorrect")
    if selection=='mca':
        print("incorrect")
    label1.config(text=selection)
a = Label(root,text ='what is your feild?',font ="20")
a.place(x=0,y=160)
var1=StringVar()
R1=Radiobutton(root,text="bca",variable=var,value="bca",command=sel)
R1.place(x=10,y=190)
R2=Radiobutton(root,text="bba",variable=var,value="bba",command=sel)
R2.place(x=10,y=210)
R3=Radiobutton(root,text="b.com",variable=var,value="b.com",command=sel)
R3.place(x=10,y=230)
R3=Radiobutton(root,text="mca",variable=var,value="mca",command=sel)
R3.place(x=10,y=250)
label1=Label(root)
label1.place(x=10,y=270)

def sel():
    selection=str(var.get())
    if selection=='junagadh':
        print("correct")
    if selection=='rajkot':
        print("incorrect")
    if selection=='surat':
        print("incorrect")
    if selection=='ahemdabad':
        print("incorrect")
    label2.config(text=selection)
b = Label(root,text ='what is your city?',font ="20")
b.place(x=0,y=310)
var2=StringVar()
R1=Radiobutton(root,text="junagadh",variable=var,value="junagadh",command=sel)
R1.place(x=10,y=340)
R2=Radiobutton(root,text="rajkot",variable=var,value="rajkot",command=sel)
R2.place(x=10,y=360)
R3=Radiobutton(root,text="surat",variable=var,value="surat",command=sel)
R3.place(x=10,y=380)
R3=Radiobutton(root,text="ahemdabad",variable=var,value="ahemdabad",command=sel)
R3.place(x=10,y=400)
label2=Label(root)
label2.place(x=10,y=420)

def sel():
    selection=str(var.get())
    if selection=='gujarat':
        print("correct")
    if selection=='maharastra':
        print("incorrect")
    if selection=='kasmir':
        print("incorrect")
    if selection=='abhu':
        print("incorrect")
    label3.config(text=selection)
c = Label(root,text ='what is your state?',font ="20")
c.place(x=0,y=460)
var3=StringVar()
R1=Radiobutton(root,text="gujarat",variable=var,value="gujarat",command=sel)
R1.place(x=10,y=490)
R2=Radiobutton(root,text="maharastra",variable=var,value="maharastra",command=sel)
R2.place(x=10,y=510)
R3=Radiobutton(root,text="kasmir",variable=var,value="kasmir",command=sel)
R3.place(x=10,y=530)
R3=Radiobutton(root,text="abhu",variable=var,value="abhu",command=sel)
R3.place(x=10,y=550)
label3=Label(root)
label3.place(x=10,y=570)

def sel():
    selection=str(var.get())
    if selection=='open':
        print("correct")
    if selection=='obc':
        print("incorrect")
    if selection=='st':
        print("incorrect")
    if selection=='sc':
        print("incorrect")
    label4.config(text=selection)
d = Label(root,text ='what is your cast?',font ="20")
d.place(x=0,y=610)
var4=StringVar()
R1=Radiobutton(root,text="open",variable=var,value="open",command=sel)
R1.place(x=10,y=640)
R2=Radiobutton(root,text="obc",variable=var,value="obc",command=sel)
R2.place(x=10,y=660)
R3=Radiobutton(root,text="st",variable=var,value="st",command=sel)
R3.place(x=10,y=680)
R3=Radiobutton(root,text="sc",variable=var,value="sc",command=sel)
R3.place(x=10,y=700)
label4=Label(root)
label4.place(x=10,y=720)

root.mainloop()




