from tkinter import*
def sel():
    selection=" "+str(var.get())
    label.config(text=selection)
root=Tk()
var=StringVar()
R1=Radiobutton(root,text="congress",variable=var,value="congress",command=sel)
R1.place(x=10,y=50)
R2=Radiobutton(root,text="bjp",variable=var,value="bjp",command=sel)
R2.place(x=10,y=100)
R3=Radiobutton(root,text="ap",variable=var,value="ap",command=sel)
R3.place(x=10,y=150)
label=Label(root)
label.place(x=10,y=200)
root.mainloop()

