from tkinter import*
from tkinter import Tk
def left_click(event):
    x,y=event.x,event.y
    c.create_oval(10,10,80,80,outline="blue",fill="white",width=2)
    event.widget.configure(bg="green")
    c.create_oval(x,x,y,y,fill="red")
def motion(event):
    x,y=event.x,event.y
    c.create_oval(x,x,y,y,fill="yellow")
root=Tk()
c=Canvas(root,width=1100,height=800,bg="white")
c.pack()
c.bind("<Button-1>",left_click)
c.bind('<Motion>',motion)
root.mainloop()
    
