from tkinter import*

def singleleft(event):
    label.config(text="you click single time")
def rightclick(event):
    label.config(text="you right click single time")
def middleclick(event):
    label.config(text="you middle click  single time")
def motionleft(event):
    label.config(text="you mostonleft click single time")
def motionright(event):
    label.config(text="you motionright click single time")
def mousewheel(event):
    label.config(text="you mousewheel click single time")
def aclick(event):
    label.config(text="you click a key")
def doubleclickleft(event):
    label.config(text="double click left button")
def doubleclickright(event):
    label.config(text="double click right button")
def enter(event):
    label.config(text="you click enter button")
def leave(event):
    label.config(text="mouse is not on window")
def motion(event):
    label.config(text="you move the couser on window")
def keypress(event):
    label.config(text="press key")
def keyrelease(event):
    label.config(text="release key")
def right(event):
    label.config(text="press right arraw key")
def left(event):
    label.config(text="press left arraw key")
def up(event):
    label.config(text="press up arrow key")
def down(event):
    label.config(text="press down arrow key")


root=Tk()
root.geometry("500x350")
label=Label(root,text="Try all the click on thi button",fg="orange")
label.configure(font=('arial 15 bold'))

label.pack()

root.bind('<Button-1>',singleleft)
root.bind('<Button-3>',rightclick)
root.bind('<Button-2>',middleclick)
root.bind('<B1-Motion>',motionleft)
root.bind('<B3-Motion>',motionright)
root.bind('<MouseWheel>',mousewheel)
root.bind('<Double-Button-1>',doubleclickleft)
root.bind('<Double-Button-3>',doubleclickright)
root.bind('<Enter>',enter)
root.bind('<Leave>',leave)
root.bind('<Motion>',motion)
root.bind('<a>',aclick)
root.bind('<KeyPress>',keypress)
root.bind('<KeyRelease>',keyrelease)
root.bind('<Right>',right)
root.bind('<Left>',left)
root.bind('<Up>',up)
root.bind('<Down>',down)

mainloop()













    









    
