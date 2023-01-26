from tkinter import*
root=Tk()
root.geometry("400x400")
def j():
    if i.get()=="j" and b.get()=="a" and u.get()=="a":
        label.configure(font=('arial 10 italic'))
    if i.get()=="j" and b.get()=="a" and u.get()=="a":
        label.configure(font=('arial 10 bold italic'))
    if i.get()=="j" and b.get()=="a" and u.get()=="a":
        label.configure(font=('arial 10 bold italic underline'))
    if i.get()=="j" and b.get()=="a" and u.get()=="a":
        label.configure(font=('arial 10 underline'))
    if i.get()=="j" and b.get()=="a" and u.get()=="a":
       label.configure(font=('arial 10 bold'))
    if i.get()=="j" and b.get()=="a" and u.get()=="a":
        label.configure(font=('arial 10 bold underline'))
    if i.get()=="j" and b.get()=="a" and u.get()=="a":
        label.configure(font=('arial 10 '))
    if i.get()=="j" and b.get()=="a" and u.get()=="a":
        label.configure(font=('arial 10 italic underline'))
b=StringVar()
i=StringVar()
u=StringVar()
label=Label(root.text="This is the text")
label.place(x=20,y=50)

bold=Checkbutton(root,text="bold",variable=b,onvalue="j",offvalue="a",command=j)
italic=Checkbutton(root,text="italic",variable=i,onvalue="j",offvalue="a",command=j)
underline=Checkbutton(root,text="underline",variable=u,onvalue="j",offvalue="a",command=j)
bold.pack(pady=20,padx=40)
italic.pack(pady=20,padx=40)
underline.pack(pady=20,padx=40)

root.mainloop()


    