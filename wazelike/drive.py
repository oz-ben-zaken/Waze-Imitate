from helpers import bgColor, make_Root, make_canvas, make_frame, Auto_Complete_Entry
from tkinter import Button, StringVar 
from PIL import ImageTk

def drive(wazelike):
    root=make_Root()
    bg=ImageTk.PhotoImage(wazelike.IMG_File)
    canvas=make_canvas(root,bg)
    radioBnVar = StringVar(None, "1")
    frame=make_frame(root,radioBnVar,wazelike)

    origin = Auto_Complete_Entry(frame,wazelike.getNames())
    destination = Auto_Complete_Entry(frame,wazelike.getNames())
    origin.entry.place(x=100, y=150)
    origin.entry.focus()
    destination.entry.place(x=100, y=200)

    startBtn=Button(frame,pady=10,padx=40, text="Start", bg=bgColor, fg='#ffffff',font= ('calibre',16,'bold'))
    startBtn['command']= lambda arg1=origin.entry_var, arg2=destination.entry_var, arg3=canvas, arg4=root: wazelike.navigate(wazelike.getNode(arg1.get()),wazelike.getNode(arg2.get()),arg3,arg4)
    startBtn.place(x=70, y=410)
        
    root.mainloop()