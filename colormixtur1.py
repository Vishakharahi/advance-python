def synthese(red,green,blue):
    win2 =()
    win2.title("ADDITIVE COLOR")
    win2.geometry("500x500")
    win2.resizable(0,0)

    hred = "#%02x%02x%02x" % (red, 0, 0) #RGB to Hexadecimal
    hgreen = "#%02x%02x%02x" % (0, green, 0)
    hblue = "#%02x%02x%02x" % (0, 0, blue)

    r = 50
    Width = 450
    Height = 450
    win3 = Canvas(win2, width = Width, height = Height, bg = 'white')
    win3.pack(padx=5,pady=5)
    win3.create_oval(10,150,300,440, outline=hred, fill=hred)
    win3.create_oval(150,150,440,440, outline=hblue, fill=hblue)
    win3.create_oval(75,10,375,300, outline=hgreen, fill=hgreen)

    win2.mainloop()