from tkinter import*
root=Tk()
root.geometry("300x200")
def chk1():
    print(checkbutton1.get())
v=Label(root,text='hello tkinter',font="50")
v.pack()
checkbutton1=IntVar()
Button1=Checkbutton(root,text="bold",variable=checkbutton1,onvalue=1,offvalue=0
                    ,height=2,command=chk1,width=10)
Button1.pack()
root.mainloop()

