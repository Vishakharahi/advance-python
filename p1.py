from tkinter import*
root=Tk()
root.geometry("400x400")

def bold1():
    label.configure(font="arial 10 bold")
def italic1():
    label.configure(font="arial 10 italic")
def underline1():
    label.configure(font="arial 10 underline")

bold=Button(root,text="Bold",command=bold1)
italic=Button(root,text="Italic",command=italic1)
underline=Button(root,text="Underline",command=underline)
bold.pack(pady=20)
italic.pack(pady=20)
underline.pack(pady=20)
label=Label(root,text="This Is Text")
label.pack(pady=30)
loop.mainloop()