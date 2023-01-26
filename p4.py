from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x200")
w = Label(root,text ='Demo of MessageBox',font ="80")
w.pack()
x=messagebox.showinfo("showinfo","Information")
print(x)
x=messagebox.showwarning("showwarning","warning")
print(x)
x=messagebox.showerror("showerror","error")
print(x)
x=messagebox.askquestion("showaskquestion","askquestion")
print(x)
x=messagebox.askokcancel("showaskokcancel","askokcancel")
print(x)





root.mainloop()
