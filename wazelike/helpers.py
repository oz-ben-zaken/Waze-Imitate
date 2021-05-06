from tkinter import Tk,Label,Button,Frame, Canvas,Radiobutton, Entry,StringVar,INSERT ,END

bgColor='#0095fc'

def make_Root():
    """Create root from Tk() and return it"""
    root=Tk()
    root.title("WazeLike")
    root.geometry('600x816+400+200')
    root.configure(background='#555')
    return root

def make_canvas(root,bg):
    """Create canvas in root with bg image and return it"""
    canvas = Canvas(root, height = bg.height(), width = bg.width(),bg='black',highlightthickness=0)
    canvas.pack(expand = 'YES', fill = 'both')
    canvas.place(x = 0, y = 0)
    canvas.create_image(156, 408, image=bg, tag="img")
    canvas.configure(border=0)
    return canvas

def make_frame(root,radioBnVar,wazelike):
    """Create the right frame in root and create buttons and labele on it"""
    frame=Frame(root,width=288,height=500,bg='light green')
    frame.place(x=312,y=0)

    Radiobutton(frame, text = 'car',variable=radioBnVar,value=1, indicator = 0,font= ('calibre',11,'bold'),bg = "light blue",width=9,pady=6,command=lambda:wazelike.setSpeed('car')).place(x=4,y=350)
    Radiobutton(frame, text = 'bicycle',variable=radioBnVar,value=2, indicator = 0,font= ('calibre',11,'bold'),bg = "light blue",width=9,pady=6,command=lambda:wazelike.setSpeed('bicycle')).place(x=98,y=350)
    Radiobutton(frame, text = 'walk',variable=radioBnVar,value=3, indicator = 0,font= ('calibre',11,'bold'),bg = "light blue",width=9,pady=6,command=lambda:wazelike.setSpeed('walk')).place(x=192,y=350)
    
    listBtn=Button(frame,pady=10,padx=40, text="Open List of cities", bg=bgColor, fg='#ffffff',font= ('calibre',13,'bold'))
    listBtn['command']=lambda: wazelike.showNodeList(root)
    listBtn.place(x=30, y=260)
    
    headline = Label(frame, text = 'Welcome to WazeLike!\nHave a safe trip.', bg='light green', font = ('calibre',14,'bold'))
    headline.place(x=40, y=50)

    origin_label = Label(frame, text = 'Origin', bg='light green', font=('calibre',12, 'bold'))
    origin_label.place(x=10, y=150)
    destination_label = Label(frame, text = 'Destination', bg='light green', font=('calibre',12, 'bold'))
    destination_label.place(x=10, y=200)
    return frame

class Auto_Complete_Entry(object):
    """class thats create an entry widget on the frame and get a list of names.
    the class convert the entry to an auto complete entry that complete according to the list of name"""
    def __init__(self,frame,list_of_names):
        self.entry_var=StringVar()
        self.entry=Entry(frame,textvariable = self.entry_var, font=('calibre',12,'bold'))
        self.entry.bind('<KeyRelease>',lambda event: self.get_KeysTyped(event))
        self.entry.bind('<Key>', lambda event: self.detect_KeyPressed(event))
        self.detect_KeyPressed_filled = False
        self.names=list_of_names
    
    def match_string(self):
        hits = []
        got = self.entry_var.get()
        for name in self.names:
            if name.startswith(got.lower()):
                hits.append(name)
        return hits    

    def get_KeysTyped(self,event):
        if len(event.keysym) == 1:
            hits = self.match_string()
            self.show_hit(hits)

    def show_hit(self,lst):
        if len(lst) == 1:
            self.entry_var.set(lst[0])
            self.detect_KeyPressed_filled = True

    def detect_KeyPressed(self,event):    
        key = event.keysym
        if len(key) == 1 and self.detect_KeyPressed_filled is True:
            pos = self.entry.index(INSERT)
            self.entry.delete(pos, END)
