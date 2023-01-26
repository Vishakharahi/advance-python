from tkinter import*

def sel(event):
    selection="Value="+str(var.get())
    label.config(text=selection)
    print(scale.get())
    button.config(width=str(var.get()))
root=Tk()
var=IntVar()
scale=Scale(root,variable=var,from_=50,to=100,tickinterval=1
            ,highlightbackground="BLUE",fg="RED",label="this is scale"
            ,length=500,orient="horizontal",resolution=0.5,sliderlength=100
            ,command=sel)
scale.pack(anchor=CENTER)
button=Button(root,text="Get Scale Value",command=sel)
button.pack(anchor=CENTER)
label=Label(root)
label.pack()
root.mainloop()
